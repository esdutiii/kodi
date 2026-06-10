# -*- coding: utf-8 -*-
import sys
import os
import re
import xbmc
import xbmcgui
import xbmcplugin
import xbmcvfs
import xbmcaddon
from datetime import datetime, timedelta
import threading

# Add libs to sys.path to resolve absolute imports inside the folder
addon_dir = os.path.dirname(os.path.abspath(__file__))
libs_dir = os.path.join(addon_dir, 'libs')
if libs_dir not in sys.path:
    sys.path.insert(0, libs_dir)

# Import local modules
from libs.ioiiI1II1 import getNameTempFile, getDateUpdate, MoriaDB, get_moria
from libs.iooooooOoO0 import logger, localize, KODI_VERSION, set_setting, get_setting, CACHE, DialogImage, WINDOW, ISESTUARYeduteamo
from libs.ioI1iII import P3Item, setInfoTag
from libs.ioIIiII11 import Watched, Trakt
from libs.ioiIIIiII import load_cookies
from libs.ioOooOO import ContextMenu

ADDON_NAME = "EduTeAmo"

def iii1i1iiIi1():
    # Background Trakt sync thread
    try:
        logger("Iniciando sincronización con Trakt.tv ...", "info")
        with Watched() as watcher:
            watcher.syncToTrakt()
        logger("... vistos sin cambios", "info")
    except Exception as e:
        logger(f"Error en sincronización Trakt: {e}", "error")

def I1ii1111IIi(url, video_path):
    # Background video downloader thread
    if WINDOW.getProperty("p3download_videoLock") != "true":
        WINDOW.setProperty("p3download_videoLock", "true")
        import requests
        try:
            logger("download video...")
            res = requests.get(url)
            res.raise_for_status()
            with open(video_path, 'wb') as f:
                f.write(res.content)
            set_setting("video_intro", url)
        except Exception as e:
            logger(f"download_video error: {str(e)}", "error")
        finally:
            WINDOW.clearProperty("p3download_videoLock")

def oOo0O00O0ooo():
    # Check and initialize Moria database
    db_path = "special://home/addons/plugin.video.eduteamo/moria.cm3"
    if not xbmcvfs.exists(db_path):
        logger("No existe la base de datos moria.cm3, descargando...", "info")
        get_moria()
        CACHE.clear("all")
        
    try:
        with MoriaDB() as db:
            res = db.executeSelect("SELECT version, mensaje_inicial, mensaje_update, notificacion_update, video_intro from version ORDER by version DESC")
            if not res:
                logger("No existe la base")
                return
            version, mensaje_inicial, mensaje_update, notificacion_update, video_intro = res[0]

            # Check for database version changes
            is_updated = False
            with Watched() as watcher:
                db_version_setting = get_setting("db_version")
                if db_version_setting != version:
                    CACHE.clear("all")
                    watcher.setShowUpdated()
                    set_setting("db_version", version)
                    is_updated = True
                    
                # Get count stats
                try:
                    series_count = len(db.executeSelect("select tmdb FROM enlaces_series group by tmdb,temporada,episodio;"))
                    movies_count = len(db.executeSelect("select * FROM pelis"))
                except Exception:
                    series_count = 0
                    movies_count = 0
        
                # Build notification message
                notif_msg = ""
                if is_updated and notificacion_update:
                    notif_msg = re.sub(r"\\n", os.linesep, notificacion_update)
                else:
                    localized_str = localize(30052)
                    if not localized_str:
                        localized_str = "BBDD cargada: %s - %s"
                    notif_msg = localized_str % (version, series_count + movies_count)
                    
                if notif_msg:
                    # Clean up any residual eduteamo / blogspot links from remote BBDD messages
                    notif_msg = re.sub(r'(?i)eduteamo(?:\.blogspot\S*)?', 'EduTeAmo', notif_msg)
                    notif_msg = re.sub(r'(?i)eduteamo', 'EduTeAmo', notif_msg)
                    xbmcgui.Dialog().notification(ADDON_NAME, notif_msg, xbmcgui.NOTIFICATION_INFO, 5000)
        
                # Popup warning messages (mensaje_inicial / mensaje_update)
                # We disable this completely as requested by the user
                # iiI1I11iiiiI = ""
                # if mensaje_inicial:
                #     iiI1I11iiiiI = re.sub(r"\\n", os.linesep, mensaje_inicial)
                # elif is_updated and mensaje_update:
                #     iiI1I11iiiiI = re.sub(r"\\n", os.linesep, mensaje_update)
                #
                # if iiI1I11iiiiI:
                #     DialogImage(ADDON_NAME, iiI1I11iiiiI)
                
                # Specials widgets setup
                try:
                    specials = db.executeSelect('SELECT label,action,sql from menus where sql like "%where coleccion like%" and menu_id > 0 and menu_id <= 100')
                    if specials:
                        label, action, sql = specials[0]
                        WINDOW.setProperty("p3especialesname", label)
                        p3_item = P3Item(label=label, action=action, sql=sql, isWidget=True, nameWidget="WidgetEspeciales", content="movies" if "v_pelis" in sql else "tvshows")
                        WINDOW.setProperty("p3especialespath", "plugin://plugin.video.eduteamo/?" + p3_item.tourl())
                        
                    specials2 = db.executeSelect('SELECT label,action,sql from menus where action = "listado_trakt" and menu_id > 0 and menu_id <= 100')
                    if len(specials2) > 1:
                        label, action, sql = specials2[1]
                        WINDOW.setProperty("p3especiales2name", label)
                        p3_item = P3Item(label=label, action=action, sql=sql, isWidget=True, nameWidget="WidgetEspeciales2", content="movies" if "v_pelis" in sql else "tvshows")
                        WINDOW.setProperty("p3especiales2path", "plugin://plugin.video.eduteamo/?" + p3_item.tourl())
                except Exception as e:
                    logger(f"Error loading specials widgets: {e}")
        
                # Intro video handling
                video_intro_path = xbmcvfs.translatePath("special://profile/addon_data/skin.estuary.eduteamo/video_especial.mp4")
                if not video_intro:
                    if os.path.exists(video_intro_path):
                        try:
                            os.remove(video_intro_path)
                        except Exception:
                            pass
                    set_setting("video_intro", "")
                else:
                    if get_setting("video_intro", "") != video_intro or not os.path.exists(video_intro_path):
                        downloader_thread = threading.Thread(target=I1ii1111IIi, args=(video_intro, video_intro_path))
                        downloader_thread.daemon = True
                        downloader_thread.start()
    except Exception as e:
        logger("No existe la base: {e}")
        return

def IIiI1i(p3Item):
    # Main menu list loader
    items_list = CACHE.get(p3Item.tourl())
    
    if not items_list:
        try:
            imported_mod = __import__("libs.ioiI1iIiiIi", fromlist=[p3Item.action])
            func = getattr(imported_mod, p3Item.action)
            items_list = func(p3Item)
        except Exception as e:
            logger(f"Error executing action {p3Item.action}: {e}", "error")
            return
            
        if p3Item.isWidget and items_list and p3Item.nameWidget != "WidgetRandom":
            tmdb_ids = ",".join([str(it.tmdb) for it in items_list if it.tmdb])
            expire = timedelta(days=3)
            CACHE.set(p3Item.nameWidget, items_list, pickle_data=True, sub_categoria=p3Item.content, expiration=expire, inWidget=tmdb_ids)
            
    if items_list:
        content_type = items_list[0].content if (hasattr(items_list[0], 'content') and items_list[0].content) else 'files'
        with Watched() as watcher:
            view_mode = watcher.getView(content_type)
            
        last_label = ""
        directory_items = []
        for item in items_list:
            if item.is_label():
                if view_mode not in (50, 51, 55):
                    last_label = item.label
                    continue
            
            if last_label:
                try:
                    matches = re.findall(r"\]([^\\[]+)", item.label)
                    if matches and matches[0].startswith(" "):
                        item.label = re.sub(r"\\n|\\r|\\t|\\s{2}|&nbsp;", "", last_label + item.label)
                    else:
                        last_label = ""
                except Exception:
                    last_label = ""
                    
            li_label = item.label if item.label else item.title
            li = xbmcgui.ListItem(li_label)
            
            if item.isPlayable:
                is_folder = False
            elif isinstance(item.isFolder, bool):
                is_folder = item.isFolder
            elif not item.action:
                is_folder = False
            else:
                is_folder = True
                
            setInfoTag(li, item)
            
            url = f"{sys.argv[0]}?{item.tourl()}"
            directory_items.append((url, li, is_folder))
            
        if directory_items:
            xbmcplugin.addDirectoryItems(int(sys.argv[1]), directory_items, len(directory_items))
            
        # Breadcrumbs title formatting
        if p3Item.label:
            clean_title = re.sub(r"\[[^\]]*]", "", p3Item.label)
            clean_title = f"[COLOR gold]{ADDON_NAME}[/COLOR] - " + re.sub(r"\s+", " ", clean_title).strip()
        else:
            clean_title = f"[COLOR gold]{ADDON_NAME}[/COLOR]"
            
        xbmcplugin.setProperty(int(sys.argv[1]), "breadcrumbs_label", clean_title)
        xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_NONE)
        xbmcplugin.setContent(int(sys.argv[1]), content_type)
        
        xbmcplugin.endOfDirectory(int(sys.argv[1]), True, p3Item.is_label(), cacheToDisc=True)
        
        if not ISESTUARYeduteamo:
            xbmc.sleep(100)
            xbmc.executebuiltin(f"Container.SetViewMode({view_mode})")

if __name__ == "__main__":
    is_resumable = False
    limit_item_list = None
    
    # Clear lock on startup to prevent infinite hangs
    WINDOW.clearProperty("p3WatchedLock")
    
    # Check Kodi version compatibility
    if KODI_VERSION < 19.0:
        xbmcgui.Dialog().ok(ADDON_NAME, localize(30057))
        exit(0)
        
    if WINDOW.getProperty("p3UpdateLock") == "true":
        exit(0)
        
    # Parameter routing
    if len(sys.argv) > 2 and sys.argv[2] and not sys.argv[2].startswith("?reload="):
        query = sys.argv[2]
        main_param = query.split('&')[0]
        sys.argv[2] = main_param
        
        params = {}
        for part in query.split('&')[1:]:
            if '=' in part:
                k, v = part.split('=', 1)
                params[k] = v
                
        # Handle resets and custom actions
        if "debrid_pin" in params:
            xbmc.executebuiltin("SendClick(10140,28)")
        elif "trakt_pin" in params:
            xbmc.executebuiltin("SendClick(10140,28)")
            try:
                Trakt().auth()
            except Exception as e:
                logger(f"Error Trakt auth: {e}", "error")
        elif "reset_cache" in params:
            CACHE.clear("all")
            xbmcgui.Dialog().notification(ADDON_NAME, "Cache reiniciada", xbmcgui.NOTIFICATION_INFO, 2000)
            exit(0)
        elif "reset_watched" in params:
            try:
                with Watched() as watcher:
                    watcher.clear()
            except Exception:
                db_file = xbmcvfs.translatePath("special://profile/addon_data/plugin.video.eduteamo/watched.db")
                if os.path.exists(db_file):
                    try:
                        os.remove(db_file)
                    except Exception:
                        exit(0)
            xbmcgui.Dialog().notification(ADDON_NAME, "Reiniciando la sincronizaciÃ³n con trakt.tv", xbmcgui.NOTIFICATION_INFO, 2000)
            sync_thread = threading.Thread(target=iii1i1iiIi1)
            sync_thread.daemon = True
            sync_thread.start()
            exit(0)
        elif "contextMenu" in params:
            url = params["contextMenu"].replace("plugin://plugin.video.eduteamo/?", "")
            ContextMenu(url).show()
            exit(0)
            
        if "resumable" in params and params["resumable"] == "true":
            is_resumable = True
        if "limit" in params:
            try:
                limit_item_list = int(params["limit"])
            except Exception:
                pass
        if "update" in params:
            if WINDOW.getProperty("p3UpdateLock") != "true":
                try:
                    WINDOW.setProperty("p3UpdateLock", "true")
                    oOo0O00O0ooo()
                    iii1i1iiIi1()
                    xbmcgui.Window(12999).setProperty("P3Updated", "true")
                finally:
                    WINDOW.clearProperty("p3UpdateLock")
            exit(0)
            
        if "searchYou" in params:
            from libs.ioiIi11II1 import searchYou
            searchYou()
            exit(0)
            
        if "infoExtra" in params:
            from libs.ioiiiIIIiI import Tmdb
            action = params["infoExtra"]
            if action == "clear":
                Tmdb().clearInfoExtra()
            exit(0)
            
        # Parse P3Item and handle context menus
        p3Item = P3Item().fromurl(sys.argv[2])
        if not p3Item.action:
            logger(f"Acción o parámetro URL no válido: {sys.argv[2]}", "error")
            exit(0)
        if limit_item_list is not None:
            p3Item.limitItemList = limit_item_list
            
        if p3Item.action == "addRating":
            pass
        elif p3Item.action == "findByActor":
            pass
        else:
            IIiI1i(p3Item)
            
    else:
        # Standard launch (addon clicked)
        load_cookies()
        if WINDOW.getProperty("p3initialized") != "true":
            if WINDOW.getProperty("p3UpdateLock") != "true":
                try:
                    WINDOW.setProperty("p3UpdateLock", "true")
                    oOo0O00O0ooo()
                    sync_thread = threading.Thread(target=iii1i1iiIi1)
                    sync_thread.daemon = True
                    sync_thread.start()
                finally:
                    WINDOW.clearProperty("p3UpdateLock")
            WINDOW.setProperty("p3initialized", "true")
                
        # Show main menu
        sql = 'select label,action,icon,sql,fanart from menus where menu_id = 10 ORDER by item_id asc'
        p3Item = P3Item(
            label=ADDON_NAME,
            action="menu",
            sql=sql,
            icon="special://home/addons/plugin.video.eduteamo/icon.png",
            fanart="special://home/addons/plugin.video.eduteamo/fanart.gif"
        )
        IIiI1i(p3Item)
