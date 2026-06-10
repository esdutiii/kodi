#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script para compilar y generar un repositorio de Kodi completo y limpio para EduTeAmo.
"""

import os
import shutil
import hashlib
import zipfile
import xml.etree.ElementTree as ET

# Directorios de origen (en la raíz del espacio de trabajo)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ADDON_SRC = os.path.join(BASE_DIR, 'plugin.video.eduteamo')
SKIN_SRC = os.path.join(BASE_DIR, 'skin.estuary.eduteamo')
REPO_SRC = os.path.join(BASE_DIR, 'repo_eduteamo', 'repository.eduteamo')

# Directorio de destino del repositorio
REPO_OUT_DIR = os.path.join(BASE_DIR, 'repo_eduteamo')
ZIPS_DIR = os.path.join(REPO_OUT_DIR, 'zips')

def clean_and_create_dir(path):
    if os.path.exists(path):
        # Intentamos vaciar pero mantener el directorio
        try:
            shutil.rmtree(path)
        except Exception:
            pass
    os.makedirs(path, exist_ok=True)

def get_addon_info(addon_dir):
    addon_xml_path = os.path.join(addon_dir, 'addon.xml')
    if not os.path.exists(addon_xml_path):
        return None, None, None
    try:
        tree = ET.parse(addon_xml_path)
        root = tree.getroot()
        addon_id = root.get('id')
        version = root.get('version')
        return addon_id, version, addon_xml_path
    except Exception as e:
        print(f"Error al analizar {addon_xml_path}: {e}")
        return None, None, None

def make_zip(addon_id, src_dir, dest_zip_path):
    print(f"  Creando ZIP para {addon_id}...")
    with zipfile.ZipFile(dest_zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(src_dir):
            # Excluir carpetas temporales, de caché y zips anteriores
            dirs[:] = [d for d in dirs if d not in ('__pycache__', '.git', '.github', '.vscode')]
            for file in files:
                if file.endswith('.pyc') or file.endswith('.zip') or file.endswith('.pyo'):
                    continue
                file_path = os.path.join(root, file)
                # El relativo debe empezar con la carpeta del addon_id (ej. plugin.video.eduteamo/addon.xml)
                rel_path = os.path.relpath(file_path, src_dir)
                arcname = os.path.join(addon_id, rel_path).replace('\\', '/')
                zf.write(file_path, arcname)
    print(f"  [OK] Creado: {os.path.basename(dest_zip_path)}")

def process_addon(src_dir):
    addon_id, version, xml_path = get_addon_info(src_dir)
    if not addon_id:
        print(f"[!] No se pudo leer la informacion de: {src_dir}")
        return None

    print(f"\nProcesando addon: {addon_id} (version {version})...")
    
    # Crear carpeta del addon en zips/
    addon_dest_dir = os.path.join(ZIPS_DIR, addon_id)
    if os.path.exists(addon_dest_dir):
        try:
            shutil.rmtree(addon_dest_dir)
        except Exception as e:
            print(f"  [!] No se pudo limpiar la carpeta {addon_dest_dir}: {e}")
    os.makedirs(addon_dest_dir, exist_ok=True)

    # Copiar addon.xml
    shutil.copy2(xml_path, os.path.join(addon_dest_dir, 'addon.xml'))

    # Intentar copiar icon.png y fanart.jpg/gif de sus ubicaciones declaradas en addon.xml
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        metadata = root.find('extension[@point="xbmc.addon.metadata"]')
        if metadata is not None:
            assets = metadata.find('assets')
            if assets is not None:
                for asset in assets:
                    asset_type = asset.tag  # 'icon', 'fanart', etc.
                    asset_rel_path = asset.text
                    if asset_rel_path:
                        src_asset_path = os.path.join(src_dir, asset_rel_path)
                        if os.path.exists(src_asset_path):
                            # Copiar a la raíz del directorio zips/addon_id con el nombre base
                            dest_asset_path = os.path.join(addon_dest_dir, os.path.basename(asset_rel_path))
                            shutil.copy2(src_asset_path, dest_asset_path)
                            print(f"  [OK] Copiado asset: {asset_type} ({os.path.basename(asset_rel_path)})")
    except Exception as e:
        print(f"  [!] Error al buscar assets en addon.xml: {e}")

    # Si no tiene assets copiados, buscamos icon.png / fanart.jpg en la raíz
    for fallback in ('icon.png', 'fanart.jpg', 'fanart.gif'):
        fb_src = os.path.join(src_dir, fallback)
        fb_dst = os.path.join(addon_dest_dir, fallback)
        if os.path.exists(fb_src) and not os.path.exists(fb_dst):
            shutil.copy2(fb_src, fb_dst)
            print(f"  [OK] Copiado asset fallback: {fallback}")

    # Crear el archivo zip en zips/addon_id/addon_id-version.zip
    zip_name = f"{addon_id}-{version}.zip"
    dest_zip_path = os.path.join(addon_dest_dir, zip_name)
    make_zip(addon_id, src_dir, dest_zip_path)

    return addon_id

def main():
    print("=" * 60)
    print("  KODI REPOSITORY BUILDER - EduTeAmo")
    print("=" * 60)

    # Crear directorios limpios
    os.makedirs(REPO_OUT_DIR, exist_ok=True)
    # No vaciar totalmente zips si tiene otras cosas, pero lo mantendremos limpio
    os.makedirs(ZIPS_DIR, exist_ok=True)

    addons_to_process = [REPO_SRC, ADDON_SRC, SKIN_SRC]
    processed_ids = []

    for src in addons_to_process:
        if os.path.exists(src):
            addon_id = process_addon(src)
            if addon_id:
                processed_ids.append(addon_id)
        else:
            print(f"[!] Directorio no encontrado: {src}")

    # Generar addons.xml y addons.xml.md5
    print("\nGenerando addons.xml y addons.xml.md5...")
    
    addons_xml_path = os.path.join(REPO_OUT_DIR, 'addons.xml')
    addons_md5_path = os.path.join(REPO_OUT_DIR, 'addons.xml.md5')

    addons_xml_header = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
    addons_xml_footer = '</addons>\n'

    addons_content = []
    for addon_id in processed_ids:
        xml_file = os.path.join(ZIPS_DIR, addon_id, 'addon.xml')
        if os.path.exists(xml_file):
            with open(xml_file, 'r', encoding='utf-8') as f:
                content = f.read().strip()
            # Eliminar la declaración XML inicial si existe
            lines = content.split('\n')
            clean_lines = [l for l in lines if not l.strip().startswith('<?xml')]
            clean_content = '\n'.join(clean_lines).strip()
            addons_content.append(clean_content)

    with open(addons_xml_path, 'w', encoding='utf-8') as f:
        f.write(addons_xml_header)
        for content in addons_content:
            # Indentar el contenido
            indented = '\n'.join('  ' + line for line in content.split('\n'))
            f.write(indented + '\n\n')
        f.write(addons_xml_footer)

    print("  [OK] addons.xml generado.")

    # Generar MD5
    with open(addons_xml_path, 'rb') as f:
        data = f.read()
    md5_hash = hashlib.md5(data).hexdigest()
    with open(addons_md5_path, 'w', encoding='utf-8') as f:
        f.write(md5_hash)
    
    print(f"  [OK] addons.xml.md5 generado: {md5_hash}")

    # Crear el zip de la instalación del repositorio en sí
    # Este se instala en Kodi, ej: repository.eduteamo.zip
    print("\nCreando el archivo ZIP instalable para Kodi...")
    repo_zip_name = "repository.eduteamo.zip"
    repo_zip_path = os.path.join(BASE_DIR, repo_zip_name)
    if os.path.exists(repo_zip_path):
        os.remove(repo_zip_path)
    
    make_zip('repository.eduteamo', REPO_SRC, repo_zip_path)
    
    # También colocar una copia del zip del repositorio en la raíz de repo_eduteamo
    shutil.copy2(repo_zip_path, os.path.join(REPO_OUT_DIR, repo_zip_name))

    print("\n" + "=" * 60)
    print("  ¡REPOSITORIO Y COMPLEMENTOS COMPILADOS CON EXITO!")
    print("=" * 60)
    print(f"  El archivo ZIP para instalar en Kodi es:")
    print(f"    -> {repo_zip_name}")
    print(f"  La carpeta del repositorio para subir a GitHub/Hosting es:")
    print(f"    -> repo_eduteamo")
    print("=" * 60)

if __name__ == '__main__':
    main()
