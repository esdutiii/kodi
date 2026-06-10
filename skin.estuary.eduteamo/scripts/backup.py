# -*- coding: utf-8 -*-

import os
import shutil
import sys
import zipfile
import datetime
import json

import xbmc
import xbmcaddon
import xbmcgui

from xbmcvfs import translatePath

def create_backup():
    dialog = xbmcgui.Dialog()
    info = dict()

    backup_folder = dialog.browse(3, "Seleccionar carpeta para guardar el backup", "")
    if not backup_folder:
        return

    current_date = datetime.datetime.now().strftime("%Y%m%d")
    zip_path = os.path.join(backup_folder,f"Backup_{current_date}.ep")
    try:
        with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
            for id in ["skin.estuary.palantir", "script.skinshortcuts", "plugin.video.palantir3"]:
                myAddon = xbmcaddon.Addon(id)
                info[id] = myAddon.getAddonInfo("version")
                myAddon_settings = translatePath(f"special://profile/addon_data/{id}")

                for root, folder, files in os.walk(myAddon_settings):
                    for fname in files:
                        if os.path.splitext(fname)[-1].lower() in ['.mp4', '.dat'] or fname in ['cache.db']:
                            # Extensiones excluidas
                            continue

                        if id == "skin.estuary.palantir" and fname == "settings.xml":
                            with open(os.path.join(root, fname), 'r') as file:
                                # Lee todo el contenido del archivo
                                settings_xml = file.read()
                                zf.writestr(os.path.join(id, fname),
                                    settings_xml.replace('<setting id="noprimeravez" type="bool">true</setting>',
                                                        '<setting id="noprimeravez" type="bool">false</setting>'))
                        else:
                            zf.write(os.path.join(root, fname), os.path.join(id, fname))

            zf.writestr("info.json", json.dumps(info, skipkeys=True, ensure_ascii=False, indent=4, sort_keys=True))
            message = f"Backup guardado en {zip_path}"
    except Exception as e:
        message = f"Error al crear el archivo zip: {e}"
        xbmc.log(message, level=xbmc.LOGERROR)

    dialog.ok("Estuary Palantir", message)


def restore_backup():
    dialog = xbmcgui.Dialog()
    listado_addons = [("skin.estuary.palantir","Skin Estuary Palantir"),
                      ("script.skinshortcuts","Skin ShortCuts"),
                      ("plugin.video.palantir3", "Palantir 3")]

    zip_path = dialog.browse(1, "Seleccionar archivo de restauración", "", "*.ep")
    if not zip_path:
        return

    restaurar = dialog.multiselect("Escoja que ajustes desea restaurar", list(name for id,name in listado_addons), preselect=[0, 1, 2])
    if not restaurar:
        return

    with zipfile.ZipFile(zip_path, 'r') as zf:
        info = json.loads(zf.read("info.json"))

        #xbmc.log(str(info), level=xbmc.LOGERROR)

        restaurados = list()
        for i, addon in enumerate(listado_addons):
            id, name = addon
            if i in restaurar:
                try:
                    if id == "script.skinshortcuts" and not xbmc.getCondVisibility(f"System.HasAddon({id})"):
                        xbmc.executebuiltin(f"InstallAddon({id})", True)
                        if not xbmc.getCondVisibility(f"System.HasAddon({id})"):
                            dialog.ok("Estuary Palantir", "Skin Shortcuts no instalado[CR]"
                                                          "No se pueden restaurar estos ajustes.")
                            continue

                    # comprobar versiones
                    myAddon = xbmcaddon.Addon(id)
                    myAddon_version = myAddon.getAddonInfo("version")
                    if info[id] != myAddon_version:
                        dialog.ok("Estuary Palantir", f"La versión instalada de {name} ({myAddon_version}) no coincide con la versión guardada ({info[id]})[CR]"
                                                      f"No se pueden restaurar estos ajustes.")
                        continue

                    # si llegas aqui es q el ID esta instalado asi q deszipear y remplazar del zip el directorio
                    myAddon_settings = translatePath(f"special://profile/addon_data/{id}")
                    shutil.rmtree(myAddon_settings, ignore_errors=True)
                    xbmc.sleep(500)

                    for file in zf.namelist():
                        if file.startswith(id):
                            zf.extract(file, translatePath("special://profile/addon_data/"))

                    restaurados.append(name)
                except Exception as e:
                    message = f"Error al restaurar {name}: {e}"
                    xbmc.log(message, level=xbmc.LOGERROR)
                    dialog.ok("Estuary Palantir", message)


        if restaurados:
            if len(restaurados) == len(restaurar):
                message = f"Backup {zip_path} restaurado con exito."
            elif len(restaurados) == 1:
                message = f"Solo hemos podido restaurar {restaurados[0]} con exito."
            else:
                message = f"Solo hemos podido restaurar {restaurados[0]} y {restaurados[1]} con exito."

            dialog.ok("Estuary Palantir", message)
            profile_name = xbmc.getInfoLabel("System.ProfileName")
            xbmc.executebuiltin(f"LoadProfile({profile_name})")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        action = sys.argv[1].lower()
        if action == "backup":
            create_backup()
        elif action == "restore":
            restore_backup()