#!/usr/bin/env python3
"""Script rápido para crear los zips de los addons"""
import zipfile
import os

BASE = os.path.dirname(os.path.abspath(__file__))
ZIPS = os.path.join(BASE, 'zips')

def make_zip(addon_id, addon_dir, version):
    dst = os.path.join(ZIPS, addon_id, f"{addon_id}-{version}.zip")
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    
    # Eliminar zip previo si existe
    if os.path.exists(dst):
        os.remove(dst)
    
    count = 0
    with zipfile.ZipFile(dst, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(addon_dir):
            dirs[:] = [d for d in dirs if d != '__pycache__']
            for f in files:
                fp = os.path.join(root, f)
                arc = os.path.relpath(fp, addon_dir)
                zf.write(fp, arc)
                count += 1
    print(f"Creado: {os.path.basename(dst)} ({count} archivos)")

# plugin.video.eduteamo
p1 = os.path.join(ZIPS, 'plugin.video.eduteamo')
make_zip('plugin.video.eduteamo', p1, '3.3.9')

# skin.estuary.eduteamo
s1 = os.path.join(ZIPS, 'skin.estuary.eduteamo')
make_zip('skin.estuary.eduteamo', s1, '1.4.1')

print("\n¡Zips creados!")