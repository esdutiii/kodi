# -*- coding: utf-8 -*-
__all__ = [ 'ContextMenu' ]
if 82 - 82: Iii1i
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import re
import sys
import time
import datetime
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
import xbmc
import xbmcgui
import xbmcaddon
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
from libs . ioI1iII import P3Item , setInfoTag
from libs . ioiiiIIIiI import Tmdb
from libs . iooooooOoO0 import logger , dump_json , localize , KODI_VERSION , set_setting , ISESTUARYeduteamo , load_json , get_setting , CACHE , WINDOW
from libs . ioIIiII11 import Watched
from libs . ioOOO0oo import Resolver
if 98 - 98: I11iiIi11i1I % oOO
class i1ii1 ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , * args , ** kwargs ) :
  super ( i1ii1 , self ) . __init__ ( )
  self . listado = kwargs . get ( 'labels' , [ ] )
  self . result = - 1
  if 63 - 63: iI1iI11Ii111
 def onInit ( self ) :
  I11II1Ii = self . getControl ( 100000 )
  for iIi in self . listado :
   ii = xbmcgui . ListItem ( label = iIi )
   I11II1Ii . addItem ( ii )
  self . setFocus ( I11II1Ii )
  if 91 - 91: iI . I11iiIi11i1I . ooOOO / IIiIIiIi11I1 * oOO / OooOoo
 def show ( self ) :
  self . doModal ( )
  return self . result
  if 93 - 93: IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo . Ooo0Ooo
 def onClick ( self , controlId ) :
  if controlId == 100000 :
   I11II1Ii = self . getControl ( 100000 )
   self . result = I11II1Ii . getSelectedPosition ( )
   self . close ( )
   if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
   if 52 - 52: Oo + I1I / oOO / OooOoo - I1Ii1I1 - ooOOO
class ContextMenu ( object ) :
 def __init__ ( self , url = None ) :
  if url :
   self . IsEstuaryeduteamo = True
  else :
   self . IsEstuaryeduteamo = False
   try :
    I11I1ii1 = xbmc . getInfoLabel ( 'ListItem.FolderPath' ) or xbmc . getInfoLabel ( 'Container.ListItem().FolderPath' ) or xbmc . getInfoLabel ( 'ListItem.FileNameAndPath' )
    url = I11I1ii1 . split ( '?' ) [ 1 ]
   except : pass
   if 60 - 60: iI1iII1I1I1i . oOO
  if url :
   i1iiiiIIIiIi = P3Item ( ) . fromurl ( url )
   self . itemUrl = i1iiiiIIIiIi
   if 22 - 22: ooo000 . iI1iII1I1I1i + Ooo0Ooo + oOO
   oOoo0 = xbmcgui . ListItem ( i1iiiiIIIiIi . label or i1iiiiIIIiIi . title )
   setInfoTag ( oOoo0 , i1iiiiIIIiIi )
  else :
   self . itemUrl = None
   oOoo0 = sys . listitem
   if 95 - 95: i1iiIII111 . Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
  self . listItem = oOoo0
  ii1i = xbmc . getInfoLabel ( 'Container.Content' )
  I1i = True if ii1i == '' or ( self . itemUrl and self . itemUrl . isWidget ) else False
  if 75 - 75: iI . Ooo0Ooo . iI1iI11Ii111 * I11iiIi11i1I % i1iiIII111
  o0OoOOo00OOO = oOoo0 . getVideoInfoTag ( )
  if 97 - 97: Iii1i
  if ii1i != 'albums' :
   media_type = o0OoOOo00OOO . getMediaType ( )
   if media_type :
    ii1i = media_type
   if 59 - 59: Oo % oOO . I11iiIi11i1I / OooOoo + IiIIii11Ii
  if ii1i in [ 'movie' , 'tvshow' , 'season' , 'episode' ] :
   ii1i += 's'
   if 9 - 9: oOo0O00 + I1Ii1I1
   if 57 - 57: oOo0O00 * I11iiIi11i1I % oOO . Oo + OooOoo
  if self . itemUrl and ( not ii1i or ii1i not in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] ) :
   if self . itemUrl . content :
    ii1i = self . itemUrl . content
    if ii1i in [ 'movie' , 'tvshow' , 'season' , 'episode' ] :
     ii1i += 's'
  self . itemContext = {
 'content' : ii1i ,
 'containerId' : xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( ) ,
 'isWidget' : I1i
 }
  if 34 - 34: Oo
  if ii1i in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] :
   if KODI_VERSION < 20.0 :
    self . itemContext [ 'tmdb' ] = oOoo0 . getUniqueID ( 'tmdb' )
    I1i1Ii = float ( oOoo0 . getProperty ( 'resumeTime' ) )
    if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
   else :
    self . itemContext [ 'tmdb' ] = o0OoOOo00OOO . getUniqueID ( 'tmdb' )
    I1i1Ii = float ( o0OoOOo00OOO . getResumeTime ( ) )
    if 43 - 43: ooOOO * I1Ii1I1
    if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
   if not self . itemContext . get ( 'tmdb' ) and self . itemUrl and self . itemUrl . tmdb :
    self . itemContext [ 'tmdb' ] = str ( self . itemUrl . tmdb )
  if not self . itemContext . get ( 'tmdb' ) :
   self . itemContext [ 'content' ] = 'albums'
   if 70 - 70: IiIIii11Ii
  if self . itemContext [ 'content' ] in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] :
   self . itemContext [ 'plot' ] = o0OoOOo00OOO . getPlot ( )
   self . itemContext [ 'playCount' ] = o0OoOOo00OOO . getPlayCount ( )
   self . itemContext [ 'poster' ] = oOoo0 . getArt ( 'poster' )
   self . itemContext [ 'fanart' ] = oOoo0 . getArt ( 'fanart' )
   self . itemContext [ 'title' ] = oOoo0 . getProperty ( 'P3Titulo' )
   if self . itemUrl :
    if not self . itemContext . get ( 'plot' ) and self . itemUrl . plot :
     self . itemContext [ 'plot' ] = self . itemUrl . plot
    if not self . itemContext . get ( 'poster' ) and self . itemUrl . poster :
     self . itemContext [ 'poster' ] = self . itemUrl . poster
    if not self . itemContext . get ( 'fanart' ) and self . itemUrl . fanart :
     self . itemContext [ 'fanart' ] = self . itemUrl . fanart
    if not self . itemContext . get ( 'title' ) :
     self . itemContext [ 'title' ] = self . itemUrl . tvshowtitle or self . itemUrl . title or self . itemUrl . label
   if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
   if oOoo0 . getProperty ( 'IsPlayable' ) :
    if I1i1Ii > 0.0 :
     self . itemContext [ 'resumeTime' ] = I1i1Ii
     if 88 - 88: Oo * IiIIii11Ii
     if 100 - 100: iI - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  if oOoo0 . getProperty ( 'trakt_list' ) :
   self . itemContext [ 'trakt_list' ] = oOoo0 . getProperty ( 'trakt_list' )
   if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
  if self . itemContext [ 'content' ] == 'seasons' :
   self . itemContext [ 'season' ] = o0OoOOo00OOO . getSeason ( )
   if 29 - 29: IiIIii11Ii - oOo0O00
  elif self . itemContext [ 'content' ] == 'episodes' :
   self . itemContext [ 'season' ] = o0OoOOo00OOO . getSeason ( )
   self . itemContext [ 'episode' ] = o0OoOOo00OOO . getEpisode ( )
   self . itemContext [ 'P3SubCategoria' ] = 'tvshows'
   if 30 - 30: I1I . ooo000
  if oOoo0 . getProperty ( 'P3SubCategoria' ) :
   self . itemContext [ 'P3SubCategoria' ] = oOoo0 . getProperty ( 'P3SubCategoria' )
   if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
   if 87 - 87: Iii1i + ooOOO . iI1iI11Ii111 / Ii + Oo
   if 77 - 77: i1iiIII111 + iI - Oo % ooo000
   if 74 - 74: Ii + Ooo0Ooo
 def _generate_menu ( self ) :
  iIi1I1I = list ( )
  if 85 - 85: oOo0O00
  if 65 - 65: Ooo0Ooo * ooo000 + oOo0O00
  i1I11i11 = re . match ( r'(\d+)-(\d+)-(\d+)' , get_setting ( 'PalCO' , '' ) )
  if i1I11i11 :
   iIi1I1I . append ( ( localize ( 30145 ) , 'notification' ) )
   if 39 - 39: Iii1i % oOo0O00 + Ooo0Ooo / iI1iI11Ii111
  if self . itemContext [ 'content' ] in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] :
   if 78 - 78: iI1iII1I1I1i + iI1iII1I1I1i - I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
   if self . IsEstuaryeduteamo :
    iIi1I1I . insert ( 0 , ( xbmc . getLocalizedString ( 22081 ) , 'info' ) )
    if 37 - 37: iI * i1i1i1111I + oOo0O00 / I1I / OooOoo
    if 4 - 4: i1
   iIi1I1I . append ( ( 'Embuary Info' , 'embuaryInfo' ) )
   if 61 - 61: iI1iII1I1I1i . iI1iI11Ii111 - ooo000 / ooo000 - i1
   if 19 - 19: Iii1i * Ooo0Ooo . I1Ii1I1 / I11iiIi11i1I * Ii - oOO
  if self . itemContext [ 'content' ] in [ 'movies' , 'tvshows' ] :
   if self . itemUrl and self . itemUrl . trailer :
    iIi1I1I . insert ( 0 , ( localize ( 30067 ) , 'trailer' ) )
   else :
    iIi1I1I . append ( ( localize ( 30065 ) , 'trailer' ) )
    if 32 - 32: iI1iII1I1I1i
    if 18 - 18: I11iiIi11i1I * iI % iI1iII1I1I1i + iI
  if get_setting ( 'parental_enabled' ) :
   iIi1I1I . append ( ( localize ( 30508 ) , 'subParental' ) )
  else :
   iIi1I1I . append ( ( localize ( 30520 ) , 'parentalEnabled' ) )
   if 93 - 93: oOO - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
  if not self . itemContext . get ( 'trakt_list' ) :
   with Watched ( ) as OoOOo0OoOOO0 :
    if self . itemContext [ 'content' ] == 'tvshows' and OoOOo0OoOOO0 . getLiTraktUser ( 'show' ) :
     if 11 - 11: i1 / ooo000
     iIi1I1I . append ( ( localize ( 30533 ) , 'add2Trak' ) )
     if 89 - 89: I1I * i1i1i1111I
    elif self . itemContext [ 'content' ] == 'movies' and OoOOo0OoOOO0 . getLiTraktUser ( 'movie' ) :
     if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
     iIi1I1I . append ( ( localize ( 30533 ) , 'add2Trak' ) )
     if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
  elif self . itemContext [ 'content' ] not in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] :
   if 54 - 54: oOO * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
   if not '|-1|' in self . itemContext . get ( 'trakt_list' ) :
    if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - iI
    iIi1I1I . append ( ( localize ( 30521 ) , 'delTraktList' ) )
    if 69 - 69: ooo000
    if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
   iIi1I1I . append ( ( "Ordenar lista" , 'sortTraktList' ) )
   if 49 - 49: iI1iII1I1I1i / i1iiIII111 + ooo000
  if self . itemContext [ 'content' ] in [ 'movies' , 'episodes' ] and self . itemContext . get ( 'P3SubCategoria' ) :
   if self . IsEstuaryeduteamo :
    if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
    iIi1I1I . insert ( 0 , ( xbmc . getLocalizedString ( 12021 ) , 'play' ) )
    if 45 - 45: i1i1i1111I * Ii
   if self . itemContext . get ( 'playCount' ) :
    if 97 - 97: i1
    iIi1I1I . append ( ( xbmc . getLocalizedString ( 16104 ) , 'markAsUnwatched' ) )
   else :
    if 26 - 26: iI
    iIi1I1I . append ( ( xbmc . getLocalizedString ( 16103 ) , 'markAsWatched' ) )
    if 20 - 20: IIiIIiIi11I1 / Oo
   if self . itemContext . get ( 'resumeTime' ) :
    if 73 - 73: ooOOO - IiIIii11Ii
    iIi1I1I . append ( ( xbmc . getLocalizedString ( 38209 ) , 'resetResumeTime' ) )
    if self . IsEstuaryeduteamo :
     if 22 - 22: Oo % oOo0O00 / iI1iI11Ii111 . oOo0O00 . iI1iI11Ii111
     I1i1Ii = '0' + str ( datetime . timedelta ( seconds = self . itemContext . get ( 'resumeTime' ) ) ) . split ( '.' ) [ 0 ]
     if 87 - 87: I1I - iI1iI11Ii111 . i1 * Oo
     iIi1I1I . insert ( 0 , ( xbmc . getLocalizedString ( 12022 ) . format ( I1i1Ii ) , 'playResume' ) )
     if 90 - 90: iI * iI1iI11Ii111 . Ii
  if self . itemContext [ 'content' ] == 'movies' :
   self . itemContext [ 'type' ] = 'movie'
   if not self . itemContext [ 'isWidget' ] and not ISESTUARYeduteamo :
    if 45 - 45: IiIIii11Ii - I11iiIi11i1I . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
    iIi1I1I . append ( ( localize ( 30147 ) , 'set_view' ) )
    if 14 - 14: iI1iII1I1I1i + OooOoo * I1Ii1I1 - I11iiIi11i1I
    if 84 - 84: oOO % iI1iII1I1I1i - Ooo0Ooo
   if get_setting ( 'trakt_enabled' ) :
    iIi1I1I . append ( ( localize ( 30035 ) , 'addRatings' ) )
    if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / iI1iI11Ii111
    if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
   Oo0ooo0OO0 = False
   if WINDOW . getProperty ( 'p3PelisFavoritasPath' ) :
    try :
     I1IIiiIiI1iI = P3Item ( ) . fromurl ( WINDOW . getProperty ( 'p3PelisFavoritasPath' ) . split ( '?' ) [ 1 ] )
     O0OO00OO0O = re . findall ( r'\(([^)]+)\)$' , I1IIiiIiI1iI . sql ) [ 0 ] . split ( ',' )
    except : Oo0ooo0OO0 = True
   else :
    Oo0ooo0OO0 = True
    if 35 - 35: i1 + I1I . i1iiIII111
   if Oo0ooo0OO0 :
    with Watched ( ) as OoOOo0OoOOO0 :
     O0OO00OO0O = OoOOo0OoOOO0 . getFavoritos ( 'movies' )
     if 16 - 16: I1Ii1I1 % I1I / IIiIIiIi11I1 * iI1iI11Ii111 + iI % oOo0O00
   if str ( self . itemContext [ 'tmdb' ] ) in O0OO00OO0O :
    iIi1I1I . append ( ( localize ( 30039 ) , 'delFavorito' ) )
   else :
    iIi1I1I . append ( ( localize ( 30041 ) , 'addFavorito' ) )
    if 13 - 13: i1 + IiIIii11Ii
  elif self . itemContext [ 'content' ] == 'tvshows' :
   self . itemContext [ 'type' ] = 'tv'
   if not self . itemContext [ 'isWidget' ] and not ISESTUARYeduteamo :
    if 23 - 23: oOO . ooOOO / Ii
    iIi1I1I . append ( ( localize ( 30148 ) , 'set_view' ) )
    if 7 - 7: OooOoo + IIiIIiIi11I1 * Iii1i . oOo0O00 % IIiIIiIi11I1
    if 62 - 62: I1Ii1I1 + ooOOO . Oo - i1i1i1111I
   if get_setting ( 'trakt_enabled' ) :
    iIi1I1I . append ( ( localize ( 30035 ) , 'addRatings' ) )
    if 52 - 52: iI1iI11Ii111 . Ii * OooOoo / iI1iI11Ii111
    if 39 - 39: i1
   Oo0ooo0OO0 = False
   if WINDOW . getProperty ( 'p3SeriesFavoritasPath' ) :
    try :
     I1IIiiIiI1iI = P3Item ( ) . fromurl ( WINDOW . getProperty ( 'p3SeriesFavoritasPath' ) . split ( '?' ) [ 1 ] )
     O0OO00OO0O = re . findall ( r'\(([^)]+)\)$' , I1IIiiIiI1iI . sql ) [ 0 ] . split ( ',' )
    except : Oo0ooo0OO0 = True
   else :
    Oo0ooo0OO0 = True
    if 16 - 16: iI - iI % I11iiIi11i1I / iI1iII1I1I1i - iI1iII1I1I1i
   if Oo0ooo0OO0 :
    with Watched ( ) as OoOOo0OoOOO0 :
     O0OO00OO0O = OoOOo0OoOOO0 . getFavoritos ( 'tvshows' )
     if 39 - 39: oOo0O00 - iI % iI . Oo * I1I
   if str ( self . itemContext [ 'tmdb' ] ) in O0OO00OO0O :
    iIi1I1I . append ( ( localize ( 30039 ) , 'delFavorito' ) )
   else :
    iIi1I1I . append ( ( localize ( 30041 ) , 'addFavorito' ) )
    if 81 - 81: i1i1i1111I + I1Ii1I1
    if 31 - 31: i1i1i1111I % I1Ii1I1
    if 1 - 1: iI - oOo0O00 - i1 . oOo0O00
   if self . itemUrl and self . itemUrl . action == 'play_mis_serieS' :
    iIi1I1I . append ( ( localize ( 30068 ) , 'showSeasons' ) )
    iIi1I1I . append ( ( localize ( 30091 ) , 'SubNoSeguir' ) )
    if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
    if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
   if self . itemContext . get ( 'playCount' ) :
    if 19 - 19: Ii
    iIi1I1I . append ( ( localize ( 30079 ) , 'markAsUnwatched' ) )
   else :
    if 22 - 22: iI1iI11Ii111 % iI1iII1I1I1i + Oo
    iIi1I1I . append ( ( localize ( 30080 ) , 'markAsWatched' ) )
    if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
  elif self . itemContext [ 'content' ] == 'seasons' :
   if not self . itemContext [ 'isWidget' ] and not ISESTUARYeduteamo :
    if 95 - 95: ooOOO % i1i1i1111I . i1
    iIi1I1I . append ( ( localize ( 30149 ) , 'set_view' ) )
    if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
   if self . itemContext . get ( 'playCount' ) :
    if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
    iIi1I1I . append ( ( localize ( 30081 ) , 'markAsUnwatched' ) )
   else :
    if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
    iIi1I1I . append ( ( localize ( 30082 ) , 'markAsWatched' ) )
    if 43 - 43: IIiIIiIi11I1 * ooo000 + Ii % iI1iII1I1I1i
  elif self . itemContext [ 'content' ] == 'episodes' :
   if not self . itemContext [ 'isWidget' ] and not ISESTUARYeduteamo :
    if 12 - 12: i1iiIII111 + ooo000 . I11iiIi11i1I
    iIi1I1I . append ( ( localize ( 30150 ) , 'set_view' ) )
    if 1 - 1: iI1iII1I1I1i % Ii - I11iiIi11i1I / iI + iI1iII1I1I1i - Ii
  elif not self . itemContext [ 'isWidget' ] and not ISESTUARYeduteamo :
   if 27 - 27: OooOoo % iI1iII1I1I1i + IIiIIiIi11I1
   iIi1I1I . append ( ( localize ( 30151 ) , 'set_view' ) )
   if 16 - 16: iI
  return iIi1I1I
  if 31 - 31: oOo0O00 / Iii1i % Ooo0Ooo % i1 . iI1iII1I1I1i . Oo
  if 83 - 83: oOo0O00 - I11iiIi11i1I
 def show ( self , menu = None ) :
  if menu :
   self . labelActionlist = menu
  else :
   self . labelActionlist = self . _generate_menu ( )
   if 91 - 91: IIiIIiIi11I1 - i1 - iI1iII1I1I1i
  if len ( self . labelActionlist ) > 0 :
   if not menu :
    I111i = - 1
    for II1IiI1I , o0OOO00OO in enumerate ( self . labelActionlist ) :
     if o0OOO00OO [ 0 ] == localize ( 30145 ) :
      I111i = II1IiI1I
      break
      if 42 - 42: i1 * iI1iI11Ii111
    if I111i > - 1 :
     ooO0O0OO = self . labelActionlist [ : I111i + 1 ]
     Iioo0Oo0oO0 = self . labelActionlist [ I111i + 1 : ]
     Iioo0Oo0oO0 . sort ( key = lambda iII11I1iI : iII11I1iI [ 0 ] )
     self . labelActionlist = ooO0O0OO + Iioo0Oo0oO0
    else :
     self . labelActionlist . sort ( key = lambda iII11I1iI : iII11I1iI [ 0 ] )
     if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
   ooOo00oOo0Ooo = list ( map ( lambda iII11I1iI : iII11I1iI [ 0 ] , self . labelActionlist ) )
   if 42 - 42: oOo0O00
   if self . IsEstuaryeduteamo :
    Ooo0O00o = i1ii1 ( 'Custom_1193_Context.xml' , "special://skin" , '' , 'xml' , labels = ooOo00oOo0Ooo ) . show ( )
   else :
    Ooo0O00o = xbmcgui . Dialog ( ) . contextmenu ( ooOo00oOo0Ooo )
    if 22 - 22: iI . ooo000
   if Ooo0O00o > - 1 :
    self . _exec ( self . labelActionlist [ Ooo0O00o ] )
    if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
    if 60 - 60: oOO * i1i1i1111I / iI1iII1I1I1i
 def _exec ( self , labelAction ) :
  iIi , OO0OOOoOOooO = labelAction
  if 74 - 74: oOo0O00 % oOo0O00 * Iii1i
  O0 = None
  Ii1Ii1 = 5000
  I111i1i11iII = 'special://home/addons/plugin.video.eduteamo/icon.png'
  if 5 - 5: OooOoo + oOo0O00 . Ooo0Ooo + I1I / OooOoo
  if OO0OOOoOOooO == 'set_view' :
   if 70 - 70: I11iiIi11i1I % I1Ii1I1 + ooOOO
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . setView ( self . itemContext [ 'content' ] )
   xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' , iIi )
   if 62 - 62: i1iiIII111 * iI1iII1I1I1i . i1i1i1111I
  elif OO0OOOoOOooO == 'playResume' and self . itemUrl :
   i11I1IiIiI1i = self . itemUrl
   i11I1IiIiI1i . playContext = True
   xbmc . executebuiltin ( "RunPlugin(plugin://plugin.video.eduteamo/?%s)" % i11I1IiIiI1i . tourl ( ) )
   if 59 - 59: ooOOO * ooo000 % IiIIii11Ii
  elif OO0OOOoOOooO == 'play' and self . itemUrl :
   i11I1IiIiI1i = self . itemUrl
   i11I1IiIiI1i . playContext = True
   i11I1IiIiI1i . pop ( 'percentPlayed' )
   xbmc . executebuiltin ( "RunPlugin(plugin://plugin.video.eduteamo/?%s)" % i11I1IiIiI1i . tourl ( ) )
   if 14 - 14: IIiIIiIi11I1 / iI . i1iiIII111 % i1 % i1i1i1111I * iI1iII1I1I1i
  elif OO0OOOoOOooO == 'info' :
   time . sleep ( 0.4 )
   xbmc . executebuiltin ( 'Action(info)' )
   if 90 - 90: Ooo0Ooo * OooOoo . Ii
  elif OO0OOOoOOooO == 'notification' :
   if 5 - 5: Oo - i1 . oOO
   i1I11i11 = re . match ( r'(\d+)-(\d+)-(\d+)' , get_setting ( 'PalCO' , '' ) )
   O0 = '%s %s' % ( localize ( 30146 ) , '-' . join ( list ( i1I11i11 . groups ( ) ) [ : : - 1 ] ) )
   try :
    if get_setting ( 'Alldebrid_enabled' ) or get_setting ( 'Realdebrid_enabled' ) :
     II1111I11 = Resolver ( { 'servidor' : '1fichier' } )
     if II1111I11 . subresolver in [ "Alldebrid" , "Realdebrid" ] :
      IiI1IIi1IiII = II1111I11 . getExpiration ( )
      if IiI1IIi1IiII :
       O0 += '[CR]{0} caduca el {1}' . format ( II1111I11 . subresolver , IiI1IIi1IiII . strftime ( "%d-%m-%Y" ) )
     del II1111I11
    else :
     O0 += '[CR]Sin cuenta premium'
   except : pass
   Ii1Ii1 = 8000
   if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
  elif OO0OOOoOOooO == 'trailer' :
   if self . itemUrl and self . itemUrl . trailer :
    xbmc . executebuiltin ( 'PlayMedia(plugin://plugin.video.youtube/play/?video_id=%s)' % self . itemUrl . trailer )
   else :
    try :
     OoOo0 = Tmdb ( ) . buscarTrailer ( self . itemContext [ 'tmdb' ] , self . itemContext [ 'type' ] )
     if OoOo0 :
      if 28 - 28: iI * Ii . i1 + iI1iI11Ii111 / i1i1i1111I / oOO
      ooOo00oOo0Ooo = list ( )
      for I111i in OoOo0 :
       ooOo00oOo0Ooo . append ( I111i [ 0 ] )
      iIi1i = 0
      if len ( ooOo00oOo0Ooo ) > 1 :
       iIi1i = xbmcgui . Dialog ( ) . select ( '%s %s' % ( localize ( 30065 ) , self . itemContext [ 'title' ] ) , ooOo00oOo0Ooo )
       if 36 - 36: oOO / ooOOO
      if iIi1i > - 1 :
       xbmc . executebuiltin ( 'PlayMedia(%s)' % OoOo0 [ iIi1i ] [ 1 ] )
       return
     else :
      from libs . ioiIi11II1 import searchYou
      if searchYou ( self . itemContext [ 'title' ] + ' Trailer EspaÃƒÂ±ol' ) :
       return
    except :
     pass
     if 23 - 23: Iii1i
    xbmcgui . Dialog ( ) . ok ( 'EduTeAmo %s' % ( localize ( 30065 ) ) , localize ( 30066 ) % self . itemContext [ 'title' ] )
    if 17 - 17: IiIIii11Ii
  elif OO0OOOoOOooO == 'markAsWatched' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . markAsWatched ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] ,
 self . itemContext . get ( 'season' ) , self . itemContext . get ( 'episode' ) )
    if 31 - 31: Iii1i + ooOOO / OooOoo . Ooo0Ooo * I11iiIi11i1I
   CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
   if not self . itemContext [ 'isWidget' ] :
    xbmc . executebuiltin ( 'Container.Refresh' )
   if ISESTUARYeduteamo :
    CACHE . actualizarWidgetsByTmdb ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] )
    if 15 - 15: IIiIIiIi11I1 . IiIIii11Ii - iI1iI11Ii111 % iI1iII1I1I1i . i1 % iI
  elif OO0OOOoOOooO == 'markAsUnwatched' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . markAsUnwatched ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] ,
 self . itemContext . get ( 'season' ) , self . itemContext . get ( 'episode' ) )
    if 6 - 6: I11iiIi11i1I * iI1iII1I1I1i + Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
   CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
   if not self . itemContext [ 'isWidget' ] :
    xbmc . executebuiltin ( 'Container.Refresh' )
   if ISESTUARYeduteamo :
    CACHE . actualizarWidgetsByTmdb ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] )
    if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . iI + iI1iI11Ii111
  elif OO0OOOoOOooO == 'SubNoSeguir' :
   iIi1I1I = list ( )
   iIi1I1I . append ( ( localize ( 30083 ) , 'NoSeguirAqui' ) )
   iIi1I1I . append ( ( localize ( 30097 ) , 'NoSeguir' ) )
   self . show ( iIi1I1I )
   if 71 - 71: ooo000 + I11iiIi11i1I % iI1iII1I1I1i + iI % Oo - Oo
  elif OO0OOOoOOooO == 'NoSeguir' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . markAsUnwatched ( 'tvshows' , self . itemContext [ 'tmdb' ] )
   CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
   if not self . itemContext [ 'isWidget' ] :
    xbmc . executebuiltin ( 'Container.Refresh' )
   if ISESTUARYeduteamo :
    CACHE . actualizarWidgetsByTmdb ( 'tvshows' , self . itemContext [ 'tmdb' ] )
    if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
  elif OO0OOOoOOooO == 'NoSeguirAqui' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . setShowHide ( self . itemContext [ 'tmdb' ] )
   CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
   if not self . itemContext [ 'isWidget' ] :
    xbmc . executebuiltin ( 'Container.Refresh' )
   if ISESTUARYeduteamo :
    CACHE . actualizarWidgetsByTmdb ( 'tvshows' , self . itemContext [ 'tmdb' ] )
    if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
  elif OO0OOOoOOooO == 'resetResumeTime' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . resetResumeTime ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] ,
 self . itemContext . get ( 'season' ) , self . itemContext . get ( 'episode' ) )
   CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
   if not self . itemContext [ 'isWidget' ] :
    xbmc . executebuiltin ( 'Container.Refresh' )
    if 12 - 12: i1i1i1111I
   if ISESTUARYeduteamo :
    CACHE . actualizarWidgetsByTmdb ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] )
    if 56 - 56: IiIIii11Ii
  elif OO0OOOoOOooO == 'showSeasons' :
   i11I1IiIiI1i = P3Item ( action = 'listado_temporadaS' ,
 tmdb = self . itemContext . get ( 'tmdb' ) ,
 plot = self . itemContext . get ( 'plot' ) ,
 poster = self . itemContext . get ( 'poster' ) ,
 fanart = self . itemContext . get ( 'fanart' ) )
   if 17 - 17: iI1iI11Ii111 . oOO % Oo + IiIIii11Ii - Ooo0Ooo
   IIIi11ii1Ii = 'plugin://plugin.video.eduteamo/?%s' % i11I1IiIiI1i . tourl ( )
   xbmc . executebuiltin ( 'ActivateWindow(videos, %s ,return)' % IIIi11ii1Ii )
   if 14 - 14: IiIIii11Ii % ooOOO . iI1iI11Ii111
  elif OO0OOOoOOooO == 'addFavorito' :
   try :
    with Watched ( ) as OoOOo0OoOOO0 :
     OoOOo0OoOOO0 . addFavorito ( P3Item ( ) . fromjson ( self . itemContext ) )
    self . _add_kodi_favorite ( )
    O0 = localize ( 30044 ) % self . itemContext [ 'title' ]
    if 29 - 29: iI % oOO % iI . ooOOO
   except : O0 = localize ( 30047 )
   if 4 - 4: oOo0O00 + i1iiIII111
  elif OO0OOOoOOooO == 'delFavorito' :
   try :
    with Watched ( ) as OoOOo0OoOOO0 :
     OoOOo0OoOOO0 . delFavorito ( P3Item ( ) . fromjson ( self . itemContext ) )
    self . _del_kodi_favorite ( )
    O0 = localize ( 30048 ) % self . itemContext [ 'title' ]
   except :
    O0 = localize ( 30050 )
   else :
    if not self . itemContext [ 'isWidget' ] :
     CACHE . clear ( self . itemContext . get ( 'P3SubCategoria' ) )
     oo00 = xbmc . getInfoLabel ( 'Container.FolderPath' )
     if oo00 and '?' in oo00 :
      try :
       o00o = P3Item ( ) . fromurl ( oo00 . split ( '?' ) [ 1 ] )
       iIIIiII1 = "{0},|,{1}|{2}" . format ( str ( self . itemContext [ 'tmdb' ] ) , str ( self . itemContext [ 'tmdb' ] ) , str ( self . itemContext [ 'tmdb' ] ) )
       o00o . sql = re . sub ( iIIIiII1 , '' , o00o . sql , re . MULTILINE )
       if o00o . sql . endswith ( '()' ) :
        xbmc . executebuiltin ( 'Action(back)' )
       else :
        oo00 = 'plugin://plugin.video.eduteamo/?%s' % o00o . tourl ( )
        xbmc . executebuiltin ( 'Container.Update(%s, replace)' % oo00 )
      except Exception as e :
       logger ( f"Error updating container on delFavorito: {e}" , "error" )
  elif OO0OOOoOOooO == 'subParental' :
   iIi1I1I = list ( )
   if 15 - 15: iI1iI11Ii111 * I11iiIi11i1I - oOo0O00
   i1iiiIii = xbmcgui . Dialog ( ) . input ( localize ( 30509 ) ,
 defaultt = get_setting ( 'parental_passw' ) ,
   option = xbmcgui . PASSWORD_VERIFY ,
 type = xbmcgui . INPUT_PASSWORD )
   if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
   if i1iiiIii :
    iIi1I1I . append ( ( localize ( 30522 ) , 'parentalDisabled' ) )
    iIi1I1I . append ( ( localize ( 30523 ) , 'parentalChange' ) )
    self . show ( iIi1I1I )
   else :
    if 96 - 96: OooOoo / oOO - i1 * I11iiIi11i1I
    xbmcgui . Dialog ( ) . ok ( 'EduTeAmo' , localize ( 30524 ) )
    if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - iI1iI11Ii111 + Ooo0Ooo
  elif OO0OOOoOOooO == 'parentalDisabled' :
   set_setting ( 'parental_enabled' , 'false' )
   O0 = localize ( 30525 )
   if 74 - 74: Ooo0Ooo * Oo + Iii1i - i1iiIII111
  elif OO0OOOoOOooO == 'parentalEnabled' :
   i1iiiIii = xbmcgui . Dialog ( ) . input ( localize ( 30510 ) , type = xbmcgui . INPUT_PASSWORD )
   if i1iiiIii :
    set_setting ( 'parental_passw' , i1iiiIii )
    set_setting ( 'parental_enabled' , 'true' )
    O0 = localize ( 30526 )
    if 22 - 22: IiIIii11Ii - Ooo0Ooo . i1 . iI1iI11Ii111 - ooo000
  elif OO0OOOoOOooO == 'parentalChange' :
   i1iiiIii = xbmcgui . Dialog ( ) . input ( localize ( 30511 ) , type = xbmcgui . INPUT_PASSWORD )
   if i1iiiIii :
    set_setting ( 'parental_passw' , i1iiiIii )
    O0 = localize ( 30527 )
    if 68 - 68: ooo000
    if 40 - 40: i1 + I1Ii1I1 + I11iiIi11i1I . Oo * I11iiIi11i1I % I1I
  elif OO0OOOoOOooO == 'delTraktList' :
   if xbmcgui . Dialog ( ) . yesno ( 'EduTeAmo' , localize ( 30535 ) ) :
    with Watched ( ) as OoOOo0OoOOO0 :
     OoOOo0OoOOO0 . delLiTrakt ( self . itemContext [ 'trakt_list' ] )
    xbmc . executebuiltin ( 'Container.Refresh' )
    if 100 - 100: OooOoo + Oo / OooOoo
  elif OO0OOOoOOooO == 'sortTraktList' :
   with Watched ( ) as OoOOo0OoOOO0 :
    OoOOo0OoOOO0 . setSortLiTrakt ( self . itemContext [ 'trakt_list' ] )
   xbmc . executebuiltin ( 'Container.Refresh' )
   if 33 - 33: iI / OooOoo
  elif OO0OOOoOOooO == 'add2Trak' :
   with Watched ( ) as OoOOo0OoOOO0 :
    iII11I11111I = OoOOo0OoOOO0 . getLiTraktUser ( self . itemContext [ 'content' ] )
    iII11I11111I . sort ( key = lambda iII11I1iI : iII11I1iI [ 0 ] )
    iII11I11111I . insert ( 0 , ( '[COLOR gold]%s[/COLOR]' % localize ( 30534 ) , None ) )
    if 81 - 81: iI1iII1I1I1i / IIiIIiIi11I1 . iI1iII1I1I1i
   iIi1I1I = list ( )
   for I111i , iII11I1iI in enumerate ( iII11I11111I ) :
    iIi1I1I . append ( ( iII11I1iI [ 0 ] , 'add2Trak|{0}' . format ( I111i ) ) )
   self . show ( iIi1I1I )
   if 81 - 81: iI1iI11Ii111 + IiIIii11Ii . I11iiIi11i1I
  elif OO0OOOoOOooO . startswith ( 'add2Trak|' ) :
   with Watched ( ) as OoOOo0OoOOO0 :
    iII11I11111I = OoOOo0OoOOO0 . getLiTraktUser ( self . itemContext [ 'content' ] )
    iII11I11111I . sort ( key = lambda iII11I1iI : iII11I1iI [ 0 ] )
    iII11I11111I . insert ( 0 , ( '[COLOR gold]%s[/COLOR]' % localize ( 30534 ) , None ) )
    if 10 - 10: iI1iII1I1I1i - Ii . IiIIii11Ii
   Ooo0O00o = int ( OO0OOOoOOooO . split ( '|' ) [ 1 ] )
   if 37 - 37: i1i1i1111I
   if Ooo0O00o > 0 :
    with Watched ( ) as OoOOo0OoOOO0 :
     O00oO00oO0O = OoOOo0OoOOO0 . addItem2Trakt ( self . itemContext [ 'content' ] , self . itemContext [ 'tmdb' ] , iII11I11111I [ Ooo0O00o ] [ 1 ] )
     if 65 - 65: iI1iII1I1I1i . Oo
    if O00oO00oO0O > 0 :
     if 44 - 44: I11iiIi11i1I . I1Ii1I1 * i1 . iI1iII1I1I1i * I11iiIi11i1I - I11iiIi11i1I
     O0 = localize ( 30530 ) % ( self . itemContext [ 'title' ] , iII11I11111I [ Ooo0O00o ] [ 0 ] )
    elif O00oO00oO0O < 0 :
     if 79 - 79: IiIIii11Ii + oOo0O00
     O0 = localize ( 30531 ) % ( self . itemContext [ 'title' ] , iII11I11111I [ Ooo0O00o ] [ 0 ] )
     I111i1i11iII = xbmcgui . NOTIFICATION_WARNING
    else :
     if 50 - 50: iI + i1iiIII111 . i1iiIII111 . Oo
     O0 = localize ( 30532 ) % ( self . itemContext [ 'title' ] , iII11I11111I [ Ooo0O00o ] [ 0 ] )
     I111i1i11iII = xbmcgui . NOTIFICATION_INFO
     if 72 - 72: oOo0O00 - iI + i1iiIII111 / iI1iI11Ii111 . OooOoo * IiIIii11Ii
  elif OO0OOOoOOooO == 'addRatings' :
   from libs . ioIIiII11 import Trakt
   Trakt ( ) . addRatings ( self . itemContext [ 'content' ] , self . itemContext [ 'title' ] , self . itemContext [ 'tmdb' ] , forzado = True )
   if 40 - 40: ooo000 * iI / i1i1i1111I * oOO + i1iiIII111 - OooOoo
  elif OO0OOOoOOooO == 'embuaryInfo' :
   if 86 - 86: I11iiIi11i1I * Ooo0Ooo . IiIIii11Ii % IiIIii11Ii . I1Ii1I1 + I1I
   if not xbmc . getCondVisibility ( 'System.HasAddon(script.embuary.info)' ) :
    xbmc . executebuiltin ( "InstallAddon(script.embuary.info)" )
   elif not xbmc . getCondVisibility ( 'System.AddonIsEnabled(script.embuary.info)' ) :
    xbmc . executebuiltin ( "EnableAddon(script.embuary.info)" )
    if 44 - 44: i1 / OooOoo / oOo0O00 . Oo
   Ii1Iiii11i1 = 0.0
   while not xbmc . getCondVisibility ( 'System.AddonIsEnabled(script.embuary.info)' ) or Ii1Iiii11i1 >= 120 :
    xbmc . sleep ( 500 )
    Ii1Iiii11i1 += 0.5
    if 57 - 57: Ooo0Ooo
   if Ii1Iiii11i1 < 120 :
    o0O0Oo0oO = None
    if self . itemContext [ 'content' ] == 'movies' :
     o0O0Oo0oO = 'RunScript(script.embuary.info,call=movie,tmdb_id=%s)' % self . itemContext [ 'tmdb' ]
    elif self . itemContext [ 'content' ] == 'tvshows' :
     o0O0Oo0oO = 'RunScript(script.embuary.info,call=tv,tmdb_id=%s)' % self . itemContext [ 'tmdb' ]
    elif self . itemContext [ 'content' ] == 'seasons' :
     o0O0Oo0oO = 'RunScript(script.embuary.info,call=tv,tmdb_id=%s,season=%s)' % (
 self . itemContext [ 'tmdb' ] , self . itemContext [ 'season' ] )
    elif self . itemContext [ 'content' ] == 'episodes' :
     o0O0Oo0oO = 'RunScript(script.embuary.info,call=tv,tmdb_id=%s,season=%s, episode=%s)' % (
 self . itemContext [ 'tmdb' ] , self . itemContext [ 'season' ] , self . itemContext [ 'episode' ] )
    if o0O0Oo0oO :
     xbmc . executebuiltin ( o0O0Oo0oO )
     if 61 - 61: iI1iI11Ii111 + iI1iII1I1I1i
  else :
   xbmc . executebuiltin ( OO0OOOoOOooO )
   if 60 - 60: I11iiIi11i1I - Ooo0Ooo % I1Ii1I1
  if O0 :
   logger ( O0 )
   ii1II1 = "EduTeAmo %s" % xbmcaddon . Addon ( ) . getAddonInfo ( 'version' )
   xbmcgui . Dialog ( ) . notification ( ii1II1 , O0 , I111i1i11iII , Ii1Ii1 )
   if 14 - 14: Oo % i1i1i1111I + ooOOO / I11iiIi11i1I - Ooo0Ooo / i1i1i1111I
 def _add_kodi_favorite ( self ) :
  try :
   import xbmcvfs
   import os
   import xml.etree.ElementTree as ET
   path = ""
   if self . itemUrl :
    path = 'plugin://plugin.video.eduteamo/?' + self . itemUrl . tourl ( )
   else :
    path = xbmc . getInfoLabel ( 'ListItem.FolderPath' ) or xbmc . getInfoLabel ( 'Container.ListItem().FolderPath' ) or xbmc . getInfoLabel ( 'ListItem.FileNameAndPath' )
   if not path :
    return
   is_folder = True if self . itemContext . get ( 'content' ) == 'tvshows' else False
   if is_folder :
    cmd = f'ActivateWindow(10025,"{path}",return)'
   else :
    cmd = f'PlayMedia("{path}")'
   name = ""
   if self . listItem :
    try :
     name = self . listItem . getLabel ( )
    except : pass
   if not name :
    name = self . itemContext . get ( 'title' ) or 'EduTeAmo Favorite'
   thumb = self . itemContext . get ( 'poster' ) or self . itemContext . get ( 'fanart' ) or ''
   fav_xml = xbmcvfs . translatePath ( 'special://profile/favourites.xml' )
   content = '<favourites>\n</favourites>'
   if os . path . exists ( fav_xml ) :
    try :
     with open ( fav_xml , 'r' , encoding = 'utf-8' , errors = 'ignore' ) as f :
      content = f . read ( )
    except Exception as e :
     logger ( f"Error reading favourites.xml: {e}" , "error" )
   try :
    root = ET . fromstring ( content )
   except Exception :
    root = ET . Element ( 'favourites' )
   exists = False
   for child in list ( root ) :
    if child . text == cmd :
     exists = True
     break
   if not exists :
    fav_elem = ET . SubElement ( root , 'favourite' )
    fav_elem . set ( 'name' , name )
    if thumb :
     fav_elem . set ( 'thumb' , thumb )
    fav_elem . text = cmd
    try :
     from xml . dom import minidom
     raw_xml = ET . tostring ( root , encoding = 'utf-8' )
     parsed = minidom . parseString ( raw_xml )
     pretty_xml = parsed . toprettyxml ( indent = "    " )
     lines = pretty_xml . split ( '\n' )
     if lines and lines [ 0 ] . startswith ( '<?xml' ) :
      lines = lines [ 1 : ]
     pretty_xml = '\n' . join ( lines )
     with open ( fav_xml , 'w' , encoding = 'utf-8' ) as f :
      f . write ( pretty_xml )
    except Exception as e :
     logger ( f"Error writing favourites.xml: {e}" , "error" )
  except Exception as e :
   logger ( f"Error in _add_kodi_favorite: {e}" , "error" )
 def _del_kodi_favorite ( self ) :
  try :
   import xbmcvfs
   import os
   import xml.etree.ElementTree as ET
   path = ""
   if self . itemUrl :
    path = 'plugin://plugin.video.eduteamo/?' + self . itemUrl . tourl ( )
   else :
    path = xbmc . getInfoLabel ( 'ListItem.FolderPath' ) or xbmc . getInfoLabel ( 'Container.ListItem().FolderPath' ) or xbmc . getInfoLabel ( 'ListItem.FileNameAndPath' )
   if not path :
    return
   fav_xml = xbmcvfs . translatePath ( 'special://profile/favourites.xml' )
   if not os . path . exists ( fav_xml ) :
    return
   try :
    with open ( fav_xml , 'r' , encoding = 'utf-8' , errors = 'ignore' ) as f :
     content = f . read ( )
    root = ET . fromstring ( content )
   except Exception as e :
    logger ( f"Error parsing favourites.xml on delete: {e}" , "error" )
    return
   changed = False
   for child in list ( root ) :
    if path in ( child . text or '' ) :
     root . remove ( child )
     changed = True
   if changed :
    try :
     from xml . dom import minidom
     raw_xml = ET . tostring ( root , encoding = 'utf-8' )
     parsed = minidom . parseString ( raw_xml )
     pretty_xml = parsed . toprettyxml ( indent = "    " )
     lines = pretty_xml . split ( '\n' )
     if lines and lines [ 0 ] . startswith ( '<?xml' ) :
      lines = lines [ 1 : ]
     pretty_xml = '\n' . join ( lines )
     with open ( fav_xml , 'w' , encoding = 'utf-8' ) as f :
      f . write ( pretty_xml )
    except Exception as e :
     logger ( f"Error writing favourites.xml on delete: {e}" , "error" )
  except Exception as e :
   logger ( f"Error in _del_kodi_favorite: {e}" , "error" )
if __name__ == '__main__' :
 ContextMenu ( ) . show ( )
 if 29 - 29: Iii1i + Ii - I11iiIi11i1I - IiIIii11Ii
