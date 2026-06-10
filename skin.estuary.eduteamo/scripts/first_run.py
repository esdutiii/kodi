# -*- coding: utf-8 -*-

import subprocess
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import os

def es_tactil():
    xbmc.log("[Skin.Estuary.Palantir] Ejecutando es_tactil()", level=xbmc.LOGINFO)
    ret = False
    try:
        # Verificar si el sistema operativo es Android
        if xbmc.getCondVisibility('system.platform.android'):
            # Ejecutar el comando getprop para Android
            result = subprocess.check_output(["getprop", 'ro.build.characteristics'], text=True)
            if "phone" in result  or "tablet" in result:
                #xbmc.log("La caracteristica define {result}.", level=xbmc.LOGINFO)
                ret = True
            else:
                result = subprocess.check_output(["getprop"], text=True)
                if "set_touch_timer_ms" in result:
                    #xbmc.log("Existe el ajuste set_touch_timer.", level=xbmc.LOGINFO)
                    ret = True
                else:
                    xbmc.log(f"No se puede determinar es_touch: {result}.", level=xbmc.LOGINFO)

    except Exception as e:
        xbmc.log(f"Error en es_tactil: {e}", level=xbmc.LOGERROR)

    if ret:
        xbmc.executebuiltin("Skin.SetBool(touchmode)")


def inicializar_valores_por_defecto():
    xbmc.log("[Skin.Estuary.Eduteamo] Inicializando valores por defecto de la skin", level=xbmc.LOGINFO)
    # Ajustar ajustes booleanos (activar los que estan a True en tu configuracion)
    bool_settings = [
        "hidespotlightpelis_anime",
        "hidespotlightseries_anime",
        "hidespotlightseries_documental",
        "hidespotlightpelis_documental",
        "hidespotlightpelis_dibujo",
        "hidespotlightseries_dibujo",
        "hidespotlightseries_novela",
        "hidespotlightpelis_musica",
        "hidespotlightseries_general",
        "hidespotlightseries_retro",
        "SkinShortcuts-FullMenu",
        "skinshortcuts-widget-WidgetPelis",
        "skinshortcuts-widget-PersonalWidgetList",
        "skinshortcuts-widget-WidgetRandom",
        "skinshortcuts-widget-addons",
        "skinshortcuts-widget-EduteamoSpotlight",
        "skinshortcuts-background-special://skin/extras/home-images/addons.jpg",
        "skinshortcuts-widget-WidgetSeries",
        "skinshortcuts-sharedmenu"
    ]
    for s in bool_settings:
        xbmc.executebuiltin(f"Skin.SetBool({s})")

    # Ajustar valores string
    string_settings = {
        "skinshortcuts-widget-6": "addons",
        "skinshortcuts-widget-7": "addons",
        "skinshortcuts-widget-4": "WidgetSeries",
        "skinshortcuts-widget-5": "PersonalWidgetList",
        "skinshortcuts-widget-1": "",
        "skinshortcuts-widget-2": "WidgetPelis",
        "skinshortcuts-widget-3": "PersonalWidgetList",
        "background_overlay": "1"
    }
    for k, v in string_settings.items():
        xbmc.executebuiltin(f'Skin.SetString({k},"{v}")')

if __name__ == "__main__":
    #xbmc.log("[Skin.Estuary.Palantir] Ejecutando script inicial", level=xbmc.LOGINFO)
    if xbmcvfs.exists("special://profile/addon_data/skin.estuary.palantir/video_especial.mp4"):
        xbmcgui.Window(12999).setProperty('video_exists', 'true')

    if not xbmc.getCondVisibility("Skin.HasSetting(noPrimeraVez)"):
        es_tactil()
        inicializar_valores_por_defecto()
        xbmc.executebuiltin("Skin.SetBool(noPrimeraVez)")





