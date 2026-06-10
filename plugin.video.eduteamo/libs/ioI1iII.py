# -*- coding: utf-8 -*-
__all__ = [ 'P3Item' , 'setInfoTag' ]
if 82 - 82: Iii1i
import re
import os
import time
import copy
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from libs . iooooooOoO0 import logger , dump_json , KODI_VERSION , load_json , get_setting , p3b64encode , p3b64decode
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
def setInfoTag ( listitem , item ) :
 if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
 iI111iiIi11i = None
 if not item . plot :
  item . plot = item . label or item . title
  if 77 - 77: iIiii1i - ooo0O0oO00 . o00o0OO00O
 if item . content in [ 'movies' , 'tvshows' , 'seasons' , 'episodes' ] :
  Ooo = item . content [ : - 1 ]
  listitem . setProperty ( 'P3Titulo' , item . tvshowtitle or item . title )
 elif item . content == 'album' and item . title :
  if 9 - 9: ii . Ii * i1
  Ooo = 'video'
  listitem . setProperty ( 'P3Titulo' , item . title )
 else :
  Ooo = 'video'
  if 9 - 9: i1iiIII111
 if item . trakt_list :
  listitem . setProperty ( 'trakt_list' , item . trakt_list )
  if 10 - 10: ooOOO / IIiIIiIi11I1 * ooo0O0oO00 / o00o0OO00O / o00o0OO00O
 if item . totalSeasons :
  listitem . setProperty ( 'TotalSeasons' , str ( item . totalSeasons ) )
 if item . p3TotalSeasons :
  listitem . setProperty ( 'P3TotalSeasons' , str ( item . p3TotalSeasons ) )
 if item . p3TotalEpisodes :
  listitem . setProperty ( 'P3TotalEpisodes' , str ( item . p3TotalEpisodes ) )
 if item . watchedEpisodes :
  listitem . setProperty ( 'WatchedEpisodes' , str ( item . watchedEpisodes ) )
 if item . totalEpisodes :
  listitem . setProperty ( 'TotalEpisodes' , str ( item . totalEpisodes ) )
  oOooo0OOO = 0
  if item . watchedEpisodes :
   oOooo0OOO = int ( 100 * ( item . watchedEpisodes / item . totalEpisodes ) )
  listitem . setProperty ( 'WatchedEpisodePercent' , str ( oOooo0OOO ) )
 if item . unWatchedEpisodes :
  listitem . setProperty ( 'UnWatchedEpisodes' , str ( item . unWatchedEpisodes ) )
 if item . newEpisodes :
  listitem . setProperty ( 'P3NewEpisodes' , 'True' )
  if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
 if item . categoria :
  listitem . setProperty ( 'P3Categoria' , item . categoria )
  if 14 - 14: I1I / ooo0O0oO00
 if item . sub_categoria :
  listitem . setProperty ( 'P3SubCategoria' , item . sub_categoria )
  if 58 - 58: I1Ii1I1 - ooOOO
 if item . specialSort :
  listitem . setProperty ( 'SpecialSort' , item . specialSort )
  if 60 - 60: iI1iII1I1I1i . ooo0O0oO00
 try :
  i1iiiiIIIiIi = re . sub ( r'\[/?COLOR.*?]' , '' , item . label )
  if item . content == 'movies' :
   II , OO0000 = re . findall ( r'.*?\(\d{4}\)\s?\[(.*?)]\s?\[(.*?)]' , i1iiiiIIIiIi ) [ 0 ]
   listitem . setProperty ( 'P3Calidad' , OO0000 )
  elif item . content == 'tvshows' :
   II = re . findall ( r'.*?\(\d{4}\)\s?\[(.*?)]' , i1iiiiIIIiIi ) [ 0 ]
   if 92 - 92: I1I / I1I + o00o0OO00O . ooo0O0oO00
  if II :
   Iio0 = II . replace ( ' ' , '' ) . split ( ',' )
   if len ( Iio0 ) == 1 and Iio0 [ 0 ] == 'Esp' :
    i1i = 'esp'
   elif len ( Iio0 ) == 1 and Iio0 [ 0 ] == 'Eng' :
    i1i = 'eng'
   elif len ( Iio0 ) == 2 and 'Eng' in Iio0 :
    i1i = 'esp_eng'
   else :
    i1i = 'multi'
    if 87 - 87: Oo - o00o0OO00O
   listitem . setProperty ( 'P3IdiomaStr' , II )
   listitem . setProperty ( 'P3IdiomaIco' , i1i )
 except :
  pass
  if 32 - 32: Ii % i1i1i1111I % o00o0OO00O - iIiii1i % i1iiIII111
  if 34 - 34: i1iiIII111 * i1
 if item . genre and isinstance ( item . genre , str ) :
  item . genre = item . genre . split ( '#' )
  if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
 ii1IiIiiII = item . label
 if not get_setting ( 'IdiomaCalidad' ) :
  if item . content == 'movies' :
   ii1IiIiiII = item . title
  elif item . content == 'tvshows' :
   ii1IiIiiII = item . tvshowtitle
 elif item . newEpisodes and item . content == 'tvshows' :
  import xbmc
  if xbmc . getSkinDir ( ) != 'skin.estuary.eduteamo' :
   if 21 - 21: oOo0O00 % iIiii1i % ooo0O0oO00 . oOo0O00
   ii1IiIiiII = '[COLOR red][B]* [/B][/COLOR]' + item . label
   if 85 - 85: OooOoo
   if 34 - 34: Oo
 listitem . setArt ( item . getart ( ) )
 if 96 - 96: ooOOO / ii + i1iiIII111 / ooOOO / iIiii1i
 if KODI_VERSION >= 20.0 :
  iI111iiIi11i = listitem . getVideoInfoTag ( )
  iI111iiIi11i . setMediaType ( Ooo )
  iI111iiIi11i . setPlot ( item . plot )
  if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
  iI111iiIi11i . setTitle ( ii1IiIiiII )
  if 6 - 6: i1iiIII111
  if item . content in [ 'tvshows' , 'seasons' , 'episodes' ] :
   iI111iiIi11i . setTvShowTitle ( item . tvshowtitle )
  if item . fecha :
   iI111iiIi11i . setYear ( int ( item . fecha . split ( '-' ) [ 0 ] ) )
   iI111iiIi11i . setPremiered ( item . fecha )
  if item . season != '' :
   iI111iiIi11i . setSeason ( item . season )
  if item . episode != '' :
   iI111iiIi11i . setEpisode ( item . episode )
  if item . tmdb :
   iI111iiIi11i . setUniqueIDs ( { 'tmdb' : str ( item . tmdb ) } , "tmdb" )
  if item . duration :
   iI111iiIi11i . setDuration ( item . duration )
  if item . mpaa :
   iI111iiIi11i . setMpaa ( item . mpaa )
  if item . genre :
   iI111iiIi11i . setGenres ( item . genre )
  if item . rating :
   try :
    I1I1 = item . rating . split ( '/' ) [ 1 ]
    iI111iiIi11i . setRating ( float ( I1I1 ) , type = "trakt" )
   except : pass
   try :
    oo0 = item . rating . split ( '/' ) [ 0 ]
    iI111iiIi11i . setRating ( float ( oo0 ) , type = "tmdb" , isdefault = True )
   except : pass
   if 20 - 20: IiIIii11Ii . ooo0O0oO00 % Ooo0Ooo / Ii / oOo0O00
  if item . trailer :
   iI111iiIi11i . setTrailer ( "plugin://plugin.video.youtube/play/?video_id={0}" . format ( item . trailer ) )
   if 47 - 47: IiIIii11Ii
 else :
  iiI1I11iiiiI = { 'title' : ii1IiIiiII ,
 'mediatype' : Ooo }
  for iII11iIi1iIiI in [ 'plot' , 'season' , 'episode' , 'duration' , 'mpaa' , 'genre' ] :
   iIIiii1iI = item . __dict__ . get ( iII11iIi1iIiI )
   if iIIiii1iI :
    iiI1I11iiiiI [ iII11iIi1iIiI ] = iIIiii1iI
    if 43 - 43: ooOOO . iIiii1i + ooo000
  if item . content in [ 'tvshows' , 'seasons' , 'episodes' ] :
   iiI1I11iiiiI [ 'TvShowTitle' ] = item . tvshowtitle
  if item . fecha :
   iiI1I11iiiiI [ 'year' ] = int ( item . fecha . split ( '-' ) [ 0 ] )
   iiI1I11iiiiI [ 'premiere' ] = item . fecha
  if item . trailer :
   iiI1I11iiiiI [ 'trailer' ] = "plugin://plugin.video.youtube/play/?video_id={0}" . format ( item . trailer )
  if item . tmdb :
   listitem . setUniqueIDs ( { 'tmdb' : str ( item . tmdb ) } , "tmdb" )
  if item . rating :
   oo0 , I1I1 = item . rating . split ( '/' )
   try :
    listitem . setRating ( "tmdb" , float ( oo0 ) )
   except : pass
   try :
    listitem . setRating ( "trakt" , float ( I1I1 ) , default = True )
   except :
    pass
    if 87 - 87: Iii1i + ooOOO . o00o0OO00O / Ii + Oo
  listitem . setInfo ( 'video' , iiI1I11iiiiI )
  if 77 - 77: i1iiIII111 + ii - Oo % ooo000
  if 74 - 74: Ii + Ooo0Ooo
 if item . isPlayable :
  listitem . setProperty ( 'IsPlayable' , 'true' )
  if 'icon' in item . __dict__ :
   item . pop ( 'icon' )
   if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  if item . percentPlayed and float ( item . percentPlayed ) > 0.0 and item . totalTime and int ( item . totalTime ) > 0 :
   item . pop ( 'playCount' )
   OOOO0O0ooO0O = ( int ( item . totalTime ) * float ( item . percentPlayed ) ) / 100
   if OOOO0O0ooO0O > 180 :
    if KODI_VERSION >= 20.0 :
     iI111iiIi11i . setResumePoint ( OOOO0O0ooO0O , item . totalTime )
    else :
     listitem . setProperty ( 'ResumeTime' , str ( OOOO0O0ooO0O ) )
     listitem . setProperty ( 'TotalTime' , str ( item . totalTime ) )
     if 87 - 87: ii / oOo0O00 % ooo0O0oO00 - oOo0O00 . I1I + Ooo0Ooo
 if item . playCount :
  if KODI_VERSION >= 20.0 :
   iI111iiIi11i . setPlaycount ( item . playCount )
  else :
   listitem . setInfo ( 'video' , { 'playCount' : item . playCount } )
   if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
   if 85 - 85: oOo0O00
class P3Item ( object ) :
 defaults = { }
 if 66 - 66: ii * i1i1i1111I + oOo0O00 / I1I / Iii1i / Ii
 def __init__ ( self , ** kwargs ) :
  for iII11iIi1iIiI , iIIiii1iI in kwargs . items ( ) :
   setattr ( self , iII11iIi1iIiI , iIIiii1iI )
   if 32 - 32: i1i1i1111I % Ooo0Ooo - o00o0OO00O * I1I
 def __contains__ ( self , item ) :
  return item in self . __dict__
  if 92 - 92: IIiIIiIi11I1 - i1 - Iii1i / Ooo0Ooo . I1Ii1I1 / iIiii1i
 def __setattr__ ( self , key , value ) :
  if key == 'isPlayable' and value == True :
   if 60 - 60: ooo0O0oO00
   object . __setattr__ ( self , 'time' , time . time ( ) )
  object . __setattr__ ( self , key , value )
  if 32 - 32: iI1iII1I1I1i
 def __getattribute__ ( self , item ) :
  return object . __getattribute__ ( self , item )
  if 18 - 18: iIiii1i * ii % iI1iII1I1I1i + ii
 def __getattr__ ( self , item ) :
  if item . startswith ( '__' ) :
   return object . __getattribute__ ( self , item )
  else :
   return self . defaults . get ( item , '' )
   if 93 - 93: ooo0O0oO00 - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
 def __eq__ ( self , other ) :
  return isinstance ( other , P3Item ) and self . action == other . action and self . content == other . content and self . tmdb == other . tmdb and self . season == other . season and self . episode == other . episode
  if 82 - 82: IIiIIiIi11I1 % i1 * ooOOO
  if 57 - 57: oOo0O00
 def __str__ ( self ) :
  return '{%s}' % ( ', ' . join (
 [ '%s%s%s: %s' % ( chr ( 34 ) , k , chr ( 34 ) , repr ( self . __dict__ [ k ] ) ) for k in sorted ( self . __dict__ . keys ( ) ) ] ) )
  if 31 - 31: i1iiIII111 + i1i1i1111I % OooOoo
 def pop ( self , attr ) :
  return self . __dict__ . pop ( attr , None )
  if 20 - 20: OooOoo - I1I
 def getart ( self ) :
  II1IIiiI = "https://image.tmdb.org/t/p/"
  oOOoOOOO000 = [ 'w500' , 'w300' , 'w1280' , 'w300' , 'w500' , 'w500' , 'w500' ]
  if 70 - 70: IIiIIiIi11I1 / ooOOO / IIiIIiIi11I1 - ooo000 . i1iiIII111
  if 'fanart' not in self . __dict__ :
   self . __dict__ [ 'fanart' ] = 'special://home/addons/plugin.video.eduteamo/fanart.gif'
   if 86 - 86: I1Ii1I1 - OooOoo - ooo0O0oO00 % ooo000 . o00o0OO00O % Iii1i
   if 11 - 11: OooOoo - I1Ii1I1 - ooOOO . i1iiIII111 - iI1iII1I1I1i / i1iiIII111
  OOOoOo = dict ( )
  for I1i1i , iII11iIi1iIiI in enumerate ( [ 'poster' , 'icon' , 'fanart' , 'thumb' , 'clearlogo' , 'season_poster' , 'still' ] ) :
   if iII11iIi1iIiI in self . __dict__ :
    iIIiii1iI = self . __dict__ . get ( iII11iIi1iIiI )
    if iIIiii1iI :
     if not ( iIIiii1iI . lower ( ) . startswith ( 'http' ) or iIIiii1iI . startswith ( 'special://home/addons/plugin.video.eduteamo' ) ) :
      iIIiii1iI = II1IIiiI + oOOoOOOO000 [ I1i1i ] + ( iIIiii1iI if iIIiii1iI . startswith ( '/' ) else '/%s' % iIIiii1iI )
      if 97 - 97: i1
     OOOoOo [ iII11iIi1iIiI . replace ( '_' , '.' ) ] = iIIiii1iI
     if 26 - 26: ii
  if OOOoOo . get ( 'still' ) and not OOOoOo . get ( 'poster' ) :
   OOOoOo [ 'poster' ] = OOOoOo . get ( 'still' )
  if not OOOoOo . get ( 'thumb' ) :
   OOOoOo [ 'thumb' ] = OOOoOo . get ( 'poster' ) or OOOoOo . get ( 'icon' )
  if not OOOoOo . get ( 'icon' ) :
   OOOoOo [ 'icon' ] = OOOoOo . get ( 'poster' , '' )
   if 20 - 20: IIiIIiIi11I1 / Oo
  return OOOoOo
  if 73 - 73: ooOOO - IiIIii11Ii
 def tourl ( self ) :
  return p3b64encode ( self . __str__ ( ) )
  if 22 - 22: Oo % oOo0O00 / o00o0OO00O . oOo0O00 . o00o0OO00O
 def fromurl ( self , url ) :
  try :
   decoded = p3b64decode ( url )
   if decoded :
    self . __dict__ . update ( eval ( decoded ) )
  except Exception as e :
   logger ( f"Error parsing url: {url} -> {e}" , "error" )
  return self
  if 87 - 87: I1I - o00o0OO00O . i1 * Oo
 def tojson ( self , path = "" ) :
  if path :
   open ( path , "wb" ) . write ( str ( dump_json ( self . __dict__ ) ) . encode ( ) )
  else :
   return dump_json ( self . __dict__ )
   if 90 - 90: ii * o00o0OO00O . Ii
 def fromjson ( self , json_item = None , path = "" ) :
  if path :
   json_item = str ( open ( path , "rb" ) . read ( ) , "utf8" )
   if 45 - 45: IiIIii11Ii - iIiii1i . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
  if isinstance ( json_item , dict ) :
   I1I1iIi = json_item
  else :
   I1I1iIi = load_json ( json_item )
  self . __dict__ . update ( I1I1iIi )
  return self
  if 94 - 94: ooOOO * ooo0O0oO00 % iI1iII1I1I1i - o00o0OO00O - ooOOO
 def is_label ( self ) :
  return not self . __dict__ . get ( 'action' ) and not self . __dict__ . get ( 'sql' )
  if 42 - 42: ooOOO . iI1iII1I1I1i
 def clone ( self , ** kwargs ) :
  I11IIiIIiIi = copy . deepcopy ( self )
  for iII11iIi1iIiI in [ 'label' , 'sql' , 'contextMenu' , 'playCount' , 'isWidget' , 'nameWidget' ] :
   if iII11iIi1iIiI in I11IIiIIiIi . __dict__ :
    I11IIiIIiIi . __dict__ . pop ( iII11iIi1iIiI )
    if 46 - 46: ooOOO + ooOOO % ooo0O0oO00
  for iII11iIi1iIiI , iIIiii1iI in kwargs . items ( ) :
   setattr ( I11IIiIIiIi , iII11iIi1iIiI , iIIiii1iI )
  return I11IIiIIiIi
