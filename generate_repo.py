#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generador de repositorio Kodi para EduTeAmo
Crea addons.xml, addons.xml.md5 y zips de todos los addons
"""

import os
import sys
import hashlib
import zipfile
import xml.etree.ElementTree as ET

# Configuración
REPO_DIR = os.path.dirname(os.path.abspath(__file__))
ZIPS_DIR = os.path.join(REPO_DIR, 'zips')
ADDONS_XML = os.path.join(REPO_DIR, 'addons.xml')
ADDONS_MD5 = os.path.join(REPO_DIR, 'addons.xml.md5')

# Orden de carpetas a incluir (excluir el repo en sí y el script)
EXCLUDE = ('repository.eduteamo', 'generate_repo.py', 'addons.xml', 'addons.xml.md5')


def create_zip(addon_id, addon_dir, version):
    """Crea un zip del addon en la carpeta zips/id/"""
    dest_dir = os.path.join(ZIPS_DIR, addon_id)
    os.makedirs(dest_dir, exist_ok=True)
    
    zip_filename = f"{addon_id}-{version}.zip"
    zip_path = os.path.join(dest_dir, zip_filename)
    
    # Si ya existe y está actualizado, no recrear
    if os.path.exists(zip_path):
        os.remove(zip_path)  # Forzar recreación
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(addon_dir):
            # Excluir __pycache__
            dirs[:] = [d for d in dirs if d != '__pycache__' and not d.endswith('.pyc')]
            for file in files:
                if file.endswith('.pyc'):
                    continue
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, addon_dir)
                zf.write(file_path, arcname)
    
    print(f"  ✓ Zip creado: {zip_filename}")
    return zip_filename


def get_addon_info(addon_dir):
    """Lee addon.xml y extrae id y versión"""
    addon_xml_path = os.path.join(addon_dir, 'addon.xml')
    if not os.path.exists(addon_xml_path):
        return None, None
    
    tree = ET.parse(addon_xml_path)
    root = tree.getroot()
    addon_id = root.get('id')
    version = root.get('version')
    return addon_id, version


def get_addon_xml_content(addon_dir):
    """Lee y retorna el contenido de addon.xml"""
    addon_xml_path = os.path.join(addon_dir, 'addon.xml')
    if not os.path.exists(addon_xml_path):
        return None
    
    with open(addon_xml_path, 'r', encoding='utf-8') as f:
        return f.read()


def build_addons_xml():
    """Construye addons.xml agregando los addon.xml de cada addon"""
    addons_xml_header = '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>\n<addons>\n'
    addons_xml_footer = '</addons>\n'
    
    addons_content = []
    total_addons = 0
    
    # Recorrer las carpetas dentro de zips (cada una es un addon)
    for item in sorted(os.listdir(ZIPS_DIR)):
        item_path = os.path.join(ZIPS_DIR, item)
        if not os.path.isdir(item_path):
            continue
        
        addon_xml_path = os.path.join(item_path, 'addon.xml')
        if not os.path.exists(addon_xml_path):
            continue
        
        with open(addon_xml_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extraer solo el contenido del addon dentro del tag <addon>
        # Mantener el XML completo pero sin el <?xml?> header
        lines = content.split('\n')
        clean_lines = [l for l in lines if not l.strip().startswith('<?xml')]
        clean_content = '\n'.join(clean_lines).strip()
        
        addons_content.append(clean_content)
        total_addons += 1
        print(f"  ✓ Añadido: {item}")
    
    # Escribir addons.xml
    with open(ADDONS_XML, 'w', encoding='utf-8') as f:
        f.write(addons_xml_header)
        for content in addons_content:
            f.write('  ' + content + '\n')
        f.write(addons_xml_footer)
    
    print(f"\n  Total addons en addons.xml: {total_addons}")
    return total_addons


def generate_md5():
    """Genera addons.xml.md5 con el hash MD5 de addons.xml"""
    if not os.path.exists(ADDONS_XML):
        print("  ✗ Error: addons.xml no encontrado")
        return False
    
    with open(ADDONS_XML, 'r', encoding='utf-8') as f:
        content = f.read()
    
    md5_hash = hashlib.md5(content.encode('utf-8')).hexdigest()
    
    with open(ADDONS_MD5, 'w', encoding='utf-8') as f:
        f.write(md5_hash)
    
    print(f"  ✓ MD5: {md5_hash}")
    return True


def main():
    print("=" * 60)
    print("  GENERADOR DE REPOSITORIO KODI - EduTeAmo")
    print("=" * 60)
    
    # Asegurar que el directorio zips existe
    if not os.path.exists(ZIPS_DIR):
        print("\n  ✗ Error: Directorio 'zips/' no encontrado")
        sys.exit(1)
    
    # Paso 1: Crear zips de cada addon
    print("\n[1/3] Creando zips de addons...")
    print("-" * 40)
    
    zips_created = []
    for item in sorted(os.listdir(ZIPS_DIR)):
        item_path = os.path.join(ZIPS_DIR, item)
        if not os.path.isdir(item_path):
            continue
        if item in EXCLUDE:
            continue
        
        addon_id, version = get_addon_info(item_path)
        if addon_id and version:
            zip_name = create_zip(addon_id, item_path, version)
            zips_created.append(zip_name)
    
    if not zips_created:
        print("\n  ⚠ No se encontraron addons para empaquetar")
    
    # Paso 2: Generar addons.xml
    print("\n[2/3] Generando addons.xml...")
    print("-" * 40)
    total = build_addons_xml()
    
    # Paso 3: Generar addons.xml.md5
    print("\n[3/3] Generando addons.xml.md5...")
    print("-" * 40)
    generate_md5()
    
    print("\n" + "=" * 60)
    print("  ¡REPOSITORIO GENERADO CON ÉXITO!")
    print("=" * 60)
    print(f"\n  Archivos generados:")
    print(f"    • {ADDONS_XML}")
    print(f"    • {ADDONS_MD5}")
    print(f"\n  Zips creados en: {ZIPS_DIR}")
    for z in zips_created:
        print(f"    • {z}")
    print("\n  ¡Listo para subir a GitHub/GitLab!")


if __name__ == '__main__':
    main()