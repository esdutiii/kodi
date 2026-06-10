# -*- coding: utf-8 -*-
__all__ = [ 'P3Player' , 'info_nextEpisode' , 'get_nextEpisode' ]
if 82 - 82: Iii1i
import re
import sys
import os
import glob
import sqlite3
import queue
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import xbmc
import xbmcvfs
import xbmcplugin
import xbmcgui
import xbmcaddon
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from threading import Thread
from libs . ioiIIIiII import downloadpage
from libs . ioIIiII11 import Watched , Trakt
from libs . ioiiiIIIiI import Tmdb
from libs . ioiiI1II1 import MoriaDB
from libs . iooooooOoO0 import logger , compare_versions , KODI_VERSION , ISESTUARYeduteamo , get_setting , CACHE , localize
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
class iI111iiIi11i ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , p3Item , duration ) :
  self . p3Item = p3Item
  self . duration = int ( duration )
  self . ret = 0
  self . doModal ( )
  if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
 def __new__ ( cls , p3Item , duration ) :
  return super ( iI111iiIi11i , cls ) . __new__ ( cls , "Custom_1111_Overlay.xml" , 'special://home/addons/skin.estuary.eduteamo' )
  if 57 - 57: iiIi1 - i1 % i1 % i1i1i1111I . Ii
 def onInit ( self ) :
  if 30 - 30: Ii
  self . getControl ( 200001 ) . setLabel ( self . p3Item . tvshowtitle )
  if 43 - 43: iIiii1i
  IIi1i111IiII = self . p3Item . label2
  if self . p3Item . duration :
   IIi1i111IiII += " ({0} min)" . format ( int ( self . p3Item . duration / 60 ) )
  self . getControl ( 200002 ) . setLabel ( IIi1i111IiII )
  i1I = self . p3Item . totalEpisodes - self . p3Item . episode + 1
  if i1I > 1 :
   IIi1i111IiII = "Quedan {0} episodios para terminar la temporada {1}" . format ( i1I , self . p3Item . season )
  else :
   IIi1i111IiII = "Ultimo episodio de la temporada {0}" . format ( self . p3Item . season )
  self . getControl ( 200003 ) . setLabel ( IIi1i111IiII . encode ( 'utf-8' ) )
  if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
  if 52 - 52: Oo + I1I / ooo0O0oO00 / OooOoo - I1Ii1I1 - ooOOO
  self . getControl ( 200005 ) . controlLeft ( self . getControl ( 200006 ) )
  self . getControl ( 200006 ) . controlRight ( self . getControl ( 200005 ) )
  if 60 - 60: iI1iII1I1I1i . ooo0O0oO00
  if 13 - 13: ooo0O0oO00
  try :
   iiIII = self . p3Item . getart ( )
   if self . p3Item . still :
    IioOOOO000 = iiIII [ 'still' ]
   elif self . p3Item . season_poster :
    IioOOOO000 = iiIII [ 'season.poster' ]
   else :
    IioOOOO000 = iiIII [ 'thumb' ]
   self . getControl ( 200000 ) . setImage ( IioOOOO000 )
  except :
   self . getControl ( 200000 ) . setImage ( 'special://home/addons/plugin.video.eduteamo/icon.png' )
   if 85 - 85: OooOoo - oOo0O00 / Ii / ooo0O0oO00 % i1iiIII111 . Ii
  self . start ( )
  self . close ( )
  if self . ret > 0 :
   xbmc . Player ( ) . stop ( )
   if 7 - 7: iIiii1i - I1Ii1I1 % iIiii1i . I1Ii1I1 . i1i1i1111I
   if 77 - 77: i1
 def onClick ( self , controlId ) :
  if controlId == 200005 :
   self . ret = - 1
   if 52 - 52: o00o0OO00O
  elif controlId == 200006 :
   self . ret = 1
   if 32 - 32: Ii % i1i1i1111I % o00o0OO00O - iIiii1i % i1iiIII111
   if 34 - 34: i1iiIII111 * i1
 def start ( self ) :
  O00O = self . getControl ( 200007 )
  for OoO in range ( self . duration * 2 , 0 , - 1 ) :
   if not xbmc . getCondVisibility ( 'System.HasVisibleModalDialog' ) :
    self . ret = - 1
   if self . ret != 0 :
    return
   ii1IiIiiII = int ( 100 - ( OoO / 2 * 100 / self . duration ) )
   I1I111i11I = OoO // 2
   if I1I111i11I > 59 :
    self . getControl ( 200006 ) . setLabel ( "Reproducir en {0:02}:{1:02}" . format ( I1I111i11I // 60 , I1I111i11I % 60 ) )
   else :
    self . getControl ( 200006 ) . setLabel ( "Reproducir en {0:02} segundos" . format ( I1I111i11I % 60 ) )
   O00O . setPercent ( ii1IiIiiII )
   self . getControl ( 200017 ) . setLabel ( str ( self . duration - I1I111i11I ) )
   xbmc . sleep ( 500 )
   if 85 - 85: OooOoo
  self . ret = 2
  if 34 - 34: Oo
  if 96 - 96: ooOOO / iiIi1 + i1iiIII111 / ooOOO / iIiii1i
class P3Player ( xbmc . Player ) :
 def __init__ ( self ) :
  if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
  self . total_Time = 0
  self . db_myvideos = sorted ( glob . glob ( os . path . join ( xbmcvfs . translatePath ( 'special://database/' ) , 'MyVideos*.db' ) ) ,
 reverse = True ) [ 0 ]
  if 6 - 6: i1iiIII111
  I1I1 = sqlite3 . connect ( self . db_myvideos )
  oo0 = I1I1 . cursor ( )
  oo0 . execute ( 'select max(idPath) from path' )
  self . db_last_idPath = 0
  i11iIii = oo0 . fetchone ( )
  if i11iIii [ 0 ] :
   self . db_last_idPath = i11iIii [ 0 ]
   if 40 - 40: IiIIii11Ii . i1 / Oo
  oo0 . execute ( 'select max(idFile) from files' )
  self . db_last_idFile = 0
  O0ooooOoo0O = oo0 . fetchone ( )
  if O0ooooOoo0O [ 0 ] :
   self . db_last_idFile = O0ooooOoo0O [ 0 ]
  I1I1 . close ( )
  if 53 - 53: i1 * I1Ii1I1 + Oo * Ii - i1 - I1I
 def _del_myvideos ( self ) :
  I1I1 = sqlite3 . connect ( self . db_myvideos )
  oo0 = I1I1 . cursor ( )
  if 59 - 59: i1 + Iii1i / I1I
  oo0 . execute ( 'select max(idPath) from path' )
  OoOO00 = oo0 . fetchone ( )
  if OoOO00 [ 0 ] :
   if OoOO00 [ 0 ] > self . db_last_idPath :
    if 52 - 52: i1iiIII111 % Oo . I1Ii1I1 + ooOOO % Oo . iiIi1
    OOO00oO0oOo0O = 'DELETE FROM path WHERE idPath > {0}' . format ( self . db_last_idPath )
    oo0 . execute ( OOO00oO0oOo0O )
    OOO00oO0oOo0O = 'DELETE FROM files WHERE idPath not in (select idPath from path)'
    oo0 . execute ( OOO00oO0oOo0O )
    I1I1 . commit ( )
    if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
   oo0 . execute ( 'select max(idFile) from files' )
   OOOO0O0ooO0O = oo0 . fetchone ( )
   if OOOO0O0ooO0O [ 0 ] and OOOO0O0ooO0O [ 0 ] > self . db_last_idFile :
    if 87 - 87: iiIi1 / oOo0O00 % ooo0O0oO00 - oOo0O00 . I1I + Ooo0Ooo
    OOO00oO0oOo0O = 'DELETE FROM files WHERE idFile > {0}' . format ( self . db_last_idFile )
    oo0 . execute ( OOO00oO0oOo0O )
    I1I1 . commit ( )
    if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
  I1I1 . close ( )
  if 85 - 85: oOo0O00
  if 66 - 66: iiIi1 * i1i1i1111I + oOo0O00 / I1I / Iii1i / Ii
 def playStream ( self , p3Item , videoUrl , listitem , enlace = None ) :
  if 32 - 32: i1i1i1111I % Ooo0Ooo - o00o0OO00O * I1I
  if 92 - 92: IIiIIiIi11I1 - i1 - Iii1i / Ooo0Ooo . I1Ii1I1 / iIiii1i
  self . p3Item = p3Item
  self . AVStarted = False
  self . is_active = True
  self . is_pause = False
  if 60 - 60: ooo0O0oO00
  self . label = enlace [ 'label' ]
  self . servidor = enlace [ 'servidor' ]
  self . videoUrl = videoUrl
  self . current_time = 0
  if 32 - 32: iI1iII1I1I1i
  if 18 - 18: iIiii1i * iiIi1 % iI1iII1I1I1i + iiIi1
  if ISESTUARYeduteamo and self . p3Item . content == 'episodes' :
   if 93 - 93: ooo0O0oO00 - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
   for OoOOo0OoOOO0 in [ "totalEpisodes" ,
   "p3TotalEpisodes" ,
   "totalSeasons" ,
   "p3TotalSeasons" ] :
    if 11 - 11: i1 / ooo000
    if OoOOo0OoOOO0 in p3Item :
     xbmcgui . Window ( 10000 ) . setProperty ( 'p3Info_%s' % OoOOo0OoOOO0 , str ( self . p3Item . __dict__ . get ( OoOOo0OoOOO0 ) ) )
     if 89 - 89: I1I * i1i1i1111I
     if 54 - 54: ooo0O0oO00 + Ooo0Ooo - I1I . Ooo0Ooo
   IIi1i111IiII = ''
   try :
    if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
    i1I = self . p3Item . totalEpisodes - self . p3Item . episode
    if i1I > 0 :
     IIi1i111IiII = "Quedan {0} episodios para terminar la temporada {1}" . format ( i1I , self . p3Item . season )
    else :
     IIi1i111IiII = "Ultimo episodio de la temporada {0}" . format ( self . p3Item . season )
   except : pass
   try :
    if 54 - 54: ooo0O0oO00 * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
    if self . p3Item . season == self . p3Item . totalSeasons or self . p3Item . season + 1 not in self . p3Item . p3Seasons :
     IIi1i111IiII += '[CR]Esta es la ultima temporada disponible'
    else :
     IIi1i111IiII += '[CR]Temporada {0} de ' . format ( self . p3Item . season )
     if self . p3Item . totalSeasons == self . p3Item . p3TotalSeasons :
      IIi1i111IiII += '{0}' . format ( self . p3Item . totalSeasons )
     else :
      IIi1i111IiII += '{0} disponibles' . format ( self . p3Item . p3TotalSeasons )
   except : pass
   if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - iiIi1
   if IIi1i111IiII :
    xbmcgui . Window ( 10000 ) . setProperty ( 'p3Info_extraET' , IIi1i111IiII )
    if 69 - 69: ooo000
    if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
    if 49 - 49: iI1iII1I1I1i / i1iiIII111 + ooo000
  OoOo00 = True
  I1i1i = 0
  ii1ii = { 'status' : 'failed' ,
 'respuesta_dialog_nextPlay' : 0 ,
 'nextEpisode' : None }
  if 17 - 17: Oo * I1I % ooOOO - IiIIii11Ii
  iIi1 = xbmc . Monitor ( )
  if 'verifypeer=' in self . videoUrl . url :
   OoOo00 = re . findall ( r'verifypeer=(true|false)' , self . videoUrl . url ) [ 0 ] == 'true'
  else :
   with Watched ( ) as I1II1ii111i :
    OoOo00 , I1i1i = I1II1ii111i . getVerifypeer2Certificate ( self . servidor )
    if 14 - 14: iiIi1 + o00o0OO00O . IiIIii11Ii . Ooo0Ooo % IiIIii11Ii * i1i1i1111I
  for oOoOO0O0 in [ 1 , 2 ] :
   if self . videoUrl . is_InputStream :
    if oOoOO0O0 == 1 : continue
    xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , listitem )
    if 20 - 20: iIiii1i / ooOOO * ooo0O0oO00 % IIiIIiIi11I1
   else :
    if 'verifypeer=' in self . videoUrl . url :
     self . videoUrl . url = re . sub ( r'verifypeer=(true|false)' , 'verifypeer=%s' % ( str ( OoOo00 ) . lower ( ) ) ,
 self . videoUrl . url )
    elif 'verifypeer=' not in self . videoUrl . url and not OoOo00 :
     if '|' not in self . videoUrl . url :
      self . videoUrl . url += '|verifypeer=false'
     else :
      self . videoUrl . url += '&verifypeer=false'
      if 60 - 60: o00o0OO00O * i1iiIII111 + i1i1i1111I / ooOOO
    if oOoOO0O0 == 2 or self . p3Item . nextEpisode or self . p3Item . playContext :
     if 58 - 58: o00o0OO00O - iiIi1
     if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
     self . play ( self . videoUrl . url , listitem )
     xbmcplugin . endOfDirectory ( handle = int ( sys . argv [ 1 ] ) , succeeded = False )
    else :
     if 46 - 46: ooOOO + ooOOO % ooo0O0oO00
     if 2 - 2: i1i1i1111I / Ooo0Ooo / ooo0O0oO00 - IIiIIiIi11I1 / IIiIIiIi11I1
     listitem . setPath ( self . videoUrl . url )
     xbmcplugin . setResolvedUrl ( int ( sys . argv [ 1 ] ) , True , listitem )
     if 58 - 58: i1i1i1111I
   o0oO00OO = O0OO0OOOOoo0o = False
   o00ooo0OO0000 = None
   oOoOo = False
   o0oOoo0O0o0Oo = get_setting ( 'NextEpisode' ) if self . p3Item . content == 'episodes' else False
   if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
   if o0oOoo0O0o0Oo and ( xbmc . getSkinDir ( ) == 'skin.estuary.eduteamo' ) and ( compare_versions ( xbmcaddon . Addon ( 'skin.estuary.eduteamo' ) . getAddonInfo ( 'version' ) , '1.3.0' ) >= 0 ) :
    if 15 - 15: ooo000
    if 63 - 63: o00o0OO00O
    with open ( xbmcvfs . translatePath ( 'special://profile/addon_data/skin.estuary.eduteamo/settings.xml' ) , 'r' ,
 encoding = 'utf-8' ) as i1Ii :
     iI111i1III = i1Ii . read ( )
     O00o00 = re . findall ( r'<setting id="UpNext" type="string">([^<]+)</setting>' , iI111i1III , re . IGNORECASE )
     if 13 - 13: I1I * ooOOO
     if not O00o00 or O00o00 [ 0 ] != 'Desactivado' :
      oOoOo = True
      if 85 - 85: I1Ii1I1
   iiiiII11II = queue . Queue ( )
   if 5 - 5: oOo0O00 + iI1iII1I1I1i
   while self . is_active and not iIi1 . abortRequested ( ) :
    try :
     self . current_time = self . getTime ( )
     if self . current_time > 180 :
      if not o0oO00OO :
       with Watched ( ) as I1II1ii111i :
        I1II1ii111i . scrobble ( 'start' , self . p3Item , self . current_time , self . total_Time )
       o0oO00OO = True
      elif oOoOo and not xbmc . getCondVisibility ( 'Window.IsActive(videoOSD)' ) :
       if not O0OO0OOOOoo0o and self . current_time >= 0.5 * self . total_Time :
        if 10 - 10: ooOOO / o00o0OO00O * I1I * Oo - i1 % OooOoo
        ooo = Thread ( target = OoO0O0OO0 , args = ( p3Item , iiiiII11II , ) )
        ooo . start ( )
        O0OO0OOOOoo0o = True
        if 70 - 70: i1i1i1111I - Ii % i1iiIII111 - iiIi1
       elif not o00ooo0OO0000 and self . current_time >= 0.9 * self . total_Time and not self . is_pause and not ooo . is_alive ( ) :
        oo0IiiI11IIi1I = ( self . total_Time - self . current_time )
        if 82 - 82: IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
        if 21 - 21: IIiIIiIi11I1 - ooo000 + ooo0O0oO00
        if not iiiiII11II . empty ( ) :
         if 5 - 5: i1iiIII111 . i1iiIII111 + ooo000 . iIiii1i
         if int ( xbmc . getInfoLabel ( 'Player.ChapterCount' ) ) :
          if 1 - 1: iI1iII1I1I1i % Ii - iIiii1i / iiIi1 + iI1iII1I1I1i - Ii
          if 27 - 27: OooOoo % iI1iII1I1I1i + IIiIIiIi11I1
          if xbmc . getInfoLabel ( 'Player.ChapterCount' ) == xbmc . getInfoLabel ( 'Player.Chapter' ) :
           if 16 - 16: iiIi1
           o00ooo0OO0000 = iI111iiIi11i ( iiiiII11II . get ( ) , oo0IiiI11IIi1I )
         elif self . current_time >= self . total_Time - 240.0 :
          if 31 - 31: oOo0O00 / Iii1i % Ooo0Ooo % i1 . iI1iII1I1I1i . Oo
          o00ooo0OO0000 = iI111iiIi11i ( iiiiII11II . get ( ) , oo0IiiI11IIi1I )
    except : pass
    iIi1 . waitForAbort ( 1 )
    if 83 - 83: oOo0O00 - iIiii1i
   if self . AVStarted :
    self . _del_myvideos ( )
    if 91 - 91: IIiIIiIi11I1 - i1 - iI1iII1I1I1i
    if self . current_time >= 0.8 * self . total_Time :
     ii1ii [ 'status' ] = 'finished'
     if o00ooo0OO0000 :
      ii1ii [ 'respuesta_dialog_nextPlay' ] = o00ooo0OO0000 . ret
      del o00ooo0OO0000
    else :
     ii1ii [ 'status' ] = 'stopped'
     ii1ii [ 'current_time' ] = self . current_time
     if 71 - 71: I1I - iiIi1
    if self . current_time > 180 :
     with Watched ( ) as I1II1ii111i :
      I1II1ii111i . setCertificate ( self . servidor , OoOo00 , I1i1i )
      if 66 - 66: i1i1i1111I / Ooo0Ooo + iIiii1i + Iii1i + oOo0O00 + o00o0OO00O
    break
    if 75 - 75: OooOoo - ooo0O0oO00 - IiIIii11Ii - ooo0O0oO00 + ooo000 % iI1iII1I1I1i
   else :
    OoOo00 = not OoOo00
    if 42 - 42: i1 * o00o0OO00O
  del iIi1
  return ii1ii
  if 50 - 50: Ii - i1iiIII111
 def onAVStarted ( self ) :
  if 96 - 96: ooo000 * OooOoo - Ii - OooOoo
  self . AVStarted = True
  self . total_Time = self . getTotalTime ( )
  if 65 - 65: Oo + Oo - iI1iII1I1I1i % OooOoo . Ooo0Ooo
  if self . p3Item . percentPlayed :
   if 84 - 84: IIiIIiIi11I1 . ooOOO
   self . seekTime ( ( float ( self . p3Item . percentPlayed ) * self . total_Time ) / 100 )
   if 44 - 44: ooo000 * i1i1i1111I * ooo0O0oO00 + i1iiIII111 - IIiIIiIi11I1
   if 70 - 70: iiIi1
  if 'Realdebrid' in self . label :
   try :
    downloadpage (
 "https://api.real-debrid.com/rest/1.0/downloads/delete/%s" % self . videoUrl . url . split ( '/' ) [ 4 ] ,
 method = 'DELETE' , headers = { 'Authorization' : 'Bearer %s' % get_setting ( 'Realdebrid_token' ) } )
   except : pass
  elif 'Alldebrid' in self . label :
   try :
    downloadpage (
 url = 'https://api.alldebrid.com/v4/user/history/delete?agent=EduTeAmo&apikey=%s' % get_setting (
 'Alldebrid_apikey' ) )
   except : pass
   if 9 - 9: oOo0O00 * i1
 def __onPlayBackStopEnd ( self ) :
  self . is_active = False
  with Watched ( ) as I1II1ii111i :
   I1II1ii111i . scrobble ( 'stop' , self . p3Item , self . current_time , self . total_Time )
   if 96 - 96: Ooo0Ooo
  if self . p3Item . sub_categoria :
   CACHE . clear ( self . p3Item . sub_categoria )
  if ISESTUARYeduteamo :
   CACHE . actualizarWidgetsByIds ( 'WidgetRandom' )
   CACHE . actualizarWidgetsByTmdb ( self . p3Item . content , self . p3Item . tmdb )
   Tmdb ( ) . clearInfoExtra ( )
   if self . current_time < 0.8 * self . total_Time :
    if self . p3Item . content == 'movies' :
     CACHE . actualizarWidgetsByIds ( 'WidgetPeliculasNoFinalizadas' )
   if self . current_time > 180 and self . p3Item . content == 'episodes' :
    CACHE . actualizarWidgetsByIds ( 'WidgetSeriesSeguimiento' )
    if 13 - 13: Oo * I1Ii1I1 - oOo0O00 * Ii . Ii + oOo0O00
 def onPlayBackEnded ( self ) :
  if 46 - 46: OooOoo - iIiii1i / Ooo0Ooo
  self . __onPlayBackStopEnd ( )
  if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % o00o0OO00O - OooOoo
 def onPlayBackStopped ( self ) :
  if 30 - 30: ooOOO * ooOOO - Iii1i * iI1iII1I1I1i
  self . __onPlayBackStopEnd ( )
  if 37 - 37: I1Ii1I1 % iI1iII1I1I1i . o00o0OO00O + Ooo0Ooo + ooOOO * iI1iII1I1I1i
 def onPlayBackError ( self ) :
  if 39 - 39: IIiIIiIi11I1 - Oo
  self . is_active = False
  if ISESTUARYeduteamo :
   Tmdb ( ) . clearInfoExtra ( )
   if 31 - 31: IiIIii11Ii % oOo0O00 % oOo0O00 * Iii1i
 def onPlayBackPaused ( self ) :
  if 85 - 85: Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
  self . is_pause = True
  with Watched ( ) as I1II1ii111i :
   I1II1ii111i . scrobble ( 'pause' , self . p3Item , self . current_time , self . total_Time )
   if 100 - 100: IiIIii11Ii % i1
  I111i1i11iII = ( self . current_time / self . total_Time ) * 100
  if 5 - 5: OooOoo + oOo0O00 . Ooo0Ooo + I1I / OooOoo
  if 70 - 70: iIiii1i % I1Ii1I1 + ooOOO
  if 62 - 62: i1iiIII111 * iI1iII1I1I1i . i1i1i1111I
 def onPlayBackResumed ( self ) :
  if 19 - 19: ooo000 * ooo0O0oO00
  self . is_pause = False
  with Watched ( ) as I1II1ii111i :
   I1II1ii111i . scrobble ( 'start' , self . p3Item , self . current_time , self . total_Time )
   if 47 - 47: ooo000
   if 2 - 2: Oo % IiIIii11Ii - ooOOO
 def onPlayBackSeek ( self , time , seekOffset ) :
  if 75 - 75: IiIIii11Ii * i1 . Iii1i - iiIi1
  pass
  if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
  if 90 - 90: Ooo0Ooo * OooOoo . Ii
def get_nextEpisode ( p3Item ) :
 if 5 - 5: Oo - i1 . ooo0O0oO00
 II1111I11 = p3Item . clone ( )
 if 94 - 94: Oo - IIiIIiIi11I1
 if not II1111I11 . season or not II1111I11 . episode :
  try :
   with Watched ( ) as I1II1ii111i :
    II1111I11 . season , II1111I11 . episode , II1111I11 . percentPlayed = I1II1ii111i . getMisSeries ( ) . get ( II1111I11 . tmdb ) . get ( 'ultimo_episodio' )
  except :
   return None
 else :
  II1111I11 . percentPlayed = 0.0
  if 79 - 79: Ii + IiIIii11Ii * iI1iII1I1I1i / iI1iII1I1I1i
 if II1111I11 . season == 0 :
  if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
  return None
  if 51 - 51: Oo / i1i1i1111I - I1I
  if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % ooo0O0oO00 . I1I
  if 76 - 76: i1iiIII111 / OooOoo
 Ii1I = Tmdb ( ) . getSeasons ( II1111I11 . tmdb )
 if 23 - 23: Iii1i
 if not II1111I11 . tvshowtitle :
  II1111I11 . tvshowtitle = Ii1I . get ( 'tvshowtitle' , '' )
  if 17 - 17: IiIIii11Ii
 if II1111I11 . percentPlayed == 0.0 :
  II1111I11 . episode += 1
  if II1111I11 . episode > Ii1I [ II1111I11 . season ] [ 'num_episodios' ] :
   if Ii1I . get ( II1111I11 . season + 1 ) :
    if 31 - 31: Iii1i + ooOOO / OooOoo . Ooo0Ooo * iIiii1i
    II1111I11 . episode = 1
    II1111I11 . season += 1
   else :
    if 15 - 15: IIiIIiIi11I1 . IiIIii11Ii - o00o0OO00O % iI1iII1I1I1i . i1 % iiIi1
    return localize ( 30502 )
    if 6 - 6: iIiii1i * iI1iII1I1I1i + Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
 II1111I11 . totalEpisodes = Ii1I [ II1111I11 . season ] . get ( 'num_episodios' )
 II1111I11 . totalSeasons = Ii1I . get ( 'num_total_seasons' , '' )
 if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . iiIi1 + o00o0OO00O
 return II1111I11
 if 71 - 71: ooo000 + iIiii1i % iI1iII1I1I1i + iiIi1 % Oo - Oo
def info_nextEpisode ( p3Item ) :
 if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
 O0OOo0O = Tmdb ( ) . getEpisodes ( p3Item . tmdb , p3Item . season ) . get ( p3Item . episode , { } )
 if 9 - 9: i1i1i1111I
 I11 = p3Item . clone (
 nextEpisode = True ,
 content = 'episodes'
 )
 if 48 - 48: Ii % o00o0OO00O
 I11 . label = '%dx%02d %s' % (
 int ( p3Item . season ) , int ( p3Item . episode ) , O0OOo0O . get ( 'titulo' , 'Episodio %s' % p3Item . episode ) )
 if 72 - 72: Oo + IiIIii11Ii - Ooo0Ooo * Ii * oOo0O00
 if ISESTUARYeduteamo :
  I11 . label2 = I11 . label
  I11 . label = O0OOo0O . get ( 'titulo' , 'Episodio %s' % p3Item . episode )
  if 77 - 77: Oo + iIiii1i % I1I
  if 20 - 20: i1 - IiIIii11Ii . IiIIii11Ii % ooOOO . i1 % Ooo0Ooo
 if O0OOo0O . get ( 'plot' ) : I11 . plot = O0OOo0O . get ( 'plot' )
 if O0OOo0O . get ( 'still' ) : I11 . still = O0OOo0O . get ( 'still' )
 if not I11 . season_poster : I11 . season_poster = I11 . pop ( 'poster' )
 if O0OOo0O . get ( 'duration' ) : I11 . duration = int ( O0OOo0O . get ( 'duration' ) * 60 )
 if O0OOo0O . get ( 'air_date' ) : I11 . fecha = O0OOo0O . get ( 'air_date' )
 if O0OOo0O . get ( 'rating' ) :
  I11 . rating = str ( O0OOo0O . get ( 'rating' ) )
  if p3Item . rating and '/' in p3Item . rating :
   if 72 - 72: ooo0O0oO00 % iiIi1 . ooOOO * I1Ii1I1 . ooOOO
   I11 . rating += '/%s' % p3Item . rating . split ( '/' ) [ 1 ]
   if 90 - 90: IiIIii11Ii + I1Ii1I1 . OooOoo
 if not I11 . percentPlayed :
  I11 . pop ( 'percentPlayed' )
  if 73 - 73: i1i1i1111I - Iii1i / iIiii1i . ooo000 / iI1iII1I1I1i - i1iiIII111
 return I11
 if 21 - 21: i1iiIII111 + iiIi1 % i1i1i1111I
def OoO0O0OO0 ( p3Item , result_queue ) :
 i1i1 = get_nextEpisode ( p3Item )
 if 11 - 11: Ooo0Ooo - iiIi1 - iI1iII1I1I1i
 if i1i1 and not isinstance ( i1i1 , str ) :
  if 54 - 54: iIiii1i / IiIIii11Ii . Ooo0Ooo
  OOO00oO0oOo0O = 'select * from enlaces_series where tmdb = %s and temporada = %s and episodio = %s' % (
 i1i1 . tmdb , i1i1 . season , i1i1 . episode )
  with MoriaDB ( ) as I11I11IiiI1i :
   iiiIII = I11I11IiiI1i . executeSelect ( OOO00oO0oOo0O )
   if 16 - 16: IIiIIiIi11I1
  if iiiIII :
   oO00 = info_nextEpisode ( i1i1 )
   if 30 - 30: IiIIii11Ii % ooo000 . Ii * Iii1i - iI1iII1I1I1i
   result_queue . put ( oO00 )
   if 10 - 10: Ooo0Ooo % ooo000 % Ooo0Ooo
