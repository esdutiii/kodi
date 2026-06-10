# -*- coding: utf-8 -*-
__all__ = [ 'Tmdb' ]
if 82 - 82: Iii1i
import requests
import xbmcgui
import xbmcvfs
import datetime
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from urllib . parse import urlencode
from libs . iooooooOoO0 import logger , load_json_file , CACHE
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
OOoOoo000O00 = True
if 55 - 55: o0Oo - ii1I1iII1I1I . i1I1IiIIiIi1 % oo0O000ooO * iIIiiIIiii1
iIi1ii1I1iI11 = datetime . timedelta ( hours = 24 )
if 55 - 55: I11II1Ii % iIi
class Tmdb ( object ) :
 base_url = "https://api.themoviedb.org/3"
 if 76 - 76: i11 / i1 . Ii . i1i1i1111I + iIIiiIIiii1
 def __init__ ( self ) :
  self . params = {
 "api_key" : "a79d70765e78bc6b322fb6f81bb6659d" ,
 "language" : "es-ES"
 }
  if 31 - 31: oo0O000ooO * I11II1Ii / OooOoo
 def request ( self , actions , id , params = None ) :
  if params :
   self . params . update ( params )
   if 93 - 93: oo0O000ooO % oo0O000ooO / I1I - Oo . ii1I1iII1I1I
  OO0o000o = "/" . join ( [ self . base_url , actions , str ( id ) ] ) + "?" + urlencode ( self . params )
  IIiiii1IiIiII = requests . get ( OO0o000o ) . json ( )
  if 32 - 32: i1I1IiIIiIi1
  if 71 - 71: Ii
  if 84 - 84: i1i1i1111I . I1Ii1I1 / oo0O000ooO - I1I - o0Oo
  if 8 - 8: Iii1i - o0Oo
  if 34 - 34: ii1I1iII1I1I + I11II1Ii * oo0O000ooO * OooOoo
  if 25 - 25: Ii / I11II1Ii % Ii
  if 96 - 96: Ii . oo0O000ooO % iIIiiIIiii1
  if IIiiii1IiIiII . get ( 'status_code' ) :
   IIiiii1IiIiII = dict ( )
   if 68 - 68: iIIiiIIiii1 . i1i1i1111I
  return IIiiii1IiIiII
  if 24 - 24: i11
  if 9 - 9: o0Oo / iIi . iIi / Ii % i1i1i1111I % ii1I1iII1I1I
 def getSeasons ( self , tmdb ) :
  O00Oo = dict ( )
  O00O = 'getSeasons{0}' . format ( tmdb )
  if 59 - 59: Iii1i . i11 - iIi
  if OOoOoo000O00 :
   try :
    ii1IiIiiII = CACHE . get ( O00O )
    if ii1IiIiiII :
     if 21 - 21: oOo0O00 % iIIiiIIiii1 % I11II1Ii . oOo0O00
     return ii1IiIiiII
   except : pass
   if 85 - 85: OooOoo
  IIiiii1IiIiII = self . request ( 'tv' , tmdb , { 'append_to_response' : 'aggregate_credits' } )
  O00Oo [ 'num_total_episodios' ] = 0
  O00Oo [ 'num_total_seasons' ] = 0
  O00Oo [ 'tvshowtitle' ] = IIiiii1IiIiII . get ( 'name' )
  if 34 - 34: Oo
  for I1i1Ii in IIiiii1IiIiII . get ( 'seasons' , [ ] ) :
   if I1i1Ii [ 'season_number' ] > 0 and I1i1Ii [ 'air_date' ] and datetime . date . fromisoformat ( I1i1Ii [ 'air_date' ] ) <= datetime . date . today ( ) :
    O00Oo [ 'num_total_seasons' ] += 1
    O00Oo [ 'num_total_episodios' ] += I1i1Ii [ 'episode_count' ]
    O00Oo [ I1i1Ii [ 'season_number' ] ] = { 'titulo' : I1i1Ii [ 'name' ] ,
 'plot' : I1i1Ii [ 'overview' ] if I1i1Ii [ 'overview' ] else '' ,
 'num_episodios' : I1i1Ii [ 'episode_count' ] ,
 'air_date' : I1i1Ii [ 'air_date' ] ,
 'rating' : I1i1Ii [ 'vote_average' ] ,
 'poster' : I1i1Ii [ 'poster_path' ]
 }
    if 88 - 88: iIIiiIIiii1 + ooOOO - i1i1i1111I . ii1I1iII1I1I * Ii + Iii1i
    if 43 - 43: ooOOO * I1Ii1I1
  if OOoOoo000O00 :
   try :
    CACHE . set ( O00O , O00Oo , expiration = iIi1ii1I1iI11 )
   except :
    pass
  return O00Oo
  if 95 - 95: ii1I1iII1I1I % Iii1i % i1i1i1111I . OooOoo
  if 70 - 70: IiIIii11Ii
 def getEpisodes ( self , tmdb , numSeason ) :
  O00Oo = dict ( )
  O00O = 'getEpisodes{0}_{1}' . format ( tmdb , numSeason )
  if 75 - 75: ii1I1iII1I1I / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  if OOoOoo000O00 :
   try :
    ii1IiIiiII = CACHE . get ( O00O )
    if ii1IiIiiII :
     if 88 - 88: Oo * IiIIii11Ii
     return ii1IiIiiII
   except : pass
   if 100 - 100: i11 - OooOoo * I1Ii1I1 / ii1I1iII1I1I / Iii1i
  IIiiii1IiIiII = self . request ( 'tv/%s/season' % tmdb , numSeason )
  if 23 - 23: ii1I1iII1I1I + i1 * I1Ii1I1 + Oo * Ii - oo0O000ooO
  for iIIiii1iI in IIiiii1IiIiII . get ( 'episodes' , [ ] ) :
   O00Oo [ iIIiii1iI [ 'episode_number' ] ] = { 'titulo' : iIIiii1iI [ 'name' ] ,
 'plot' : iIIiii1iI [ 'overview' ] if iIIiii1iI [ 'overview' ] else '' ,
 'duration' : iIIiii1iI [ 'runtime' ] ,
 'air_date' : iIIiii1iI [ 'air_date' ] ,
 'rating' : iIIiii1iI [ 'vote_average' ] ,
 'still' : iIIiii1iI [ 'still_path' ] }
   if 43 - 43: ooOOO . iIIiiIIiii1 + o0Oo
  if OOoOoo000O00 :
   try :
    CACHE . set ( O00O , O00Oo , expiration = iIi1ii1I1iI11 )
   except :
    pass
  return O00Oo
  if 87 - 87: Iii1i + ooOOO . iIi / Ii + Oo
  if 77 - 77: i1iiIII111 + i11 - Oo % o0Oo
 def getVideos ( self , tmdb , type ) :
  O00Oo = list ( )
  O00O = 'getVideos{0}_{1}' . format ( tmdb , type )
  if 74 - 74: Ii + ii1I1iII1I1I
  if OOoOoo000O00 :
   try :
    ii1IiIiiII = CACHE . get ( O00O )
    if ii1IiIiiII :
     if 1 - 1: I1I % ii1I1iII1I1I + i1iiIII111 . i1iiIII111 % Oo
     return ii1IiIiiII
   except : pass
   if 93 - 93: oOo0O00 % ii1I1iII1I1I * i1iiIII111
  OooO0O00o0 = self . params
  OoOOoO000O = { 'es' : 0 , 'en' : 1 }
  for O0o0O0o0o in OoOOoO000O . keys ( ) :
   OooO0O00o0 [ 'language' ] = O0o0O0o0o
   OO0o000o = 'https://api.themoviedb.org/3/%s/%s/videos?%s' % ( type , tmdb , urlencode ( OooO0O00o0 ) )
   Oo0 = requests . get ( OO0o000o )
   if Oo0 . ok :
    O00Oo . extend ( Oo0 . json ( ) . get ( 'results' , [ ] ) )
    if 40 - 40: OooOoo / Iii1i
  O00Oo = list ( filter ( lambda i1iII11i1 : i1iII11i1 . get ( 'site' ) == 'YouTube' , O00Oo ) )
  Ooo00ooO = { 'Teaser' : 1 , 'Trailer' : 0 , 'Opening Credits' : 2 }
  O00Oo = sorted ( O00Oo , key = lambda i1iII11i1 : ( OoOOoO000O . get ( i1iII11i1 [ 'iso_639_1' ] , 100 ) ,
 Ooo00ooO . get ( i1iII11i1 [ 'type' ] , 100 ) ,
 - int ( i1iII11i1 [ 'size' ] ) ) )
  if OOoOoo000O00 :
   try :
    CACHE . set ( O00O , O00Oo , expiration = iIi1ii1I1iI11 )
   except :
    pass
  return O00Oo
  if 29 - 29: iIIiiIIiii1 * i1I1IiIIiIi1
  if 7 - 7: Oo / OooOoo - iIIiiIIiii1 - i11 % i1iiIII111
 def buscarTrailer ( self , tmdb , type ) :
  O00Oo = list ( )
  OOo0OOOo0O = self . getVideos ( tmdb , type )
  if 99 - 99: i1 - i1I1IiIIiIi1 + oOo0O00 . ooOOO / i1iiIII111
  for oooO in OOo0OOOo0O :
   iII = '%s - %s (%s) [%sp]' % ( oooO [ 'name' ] , oooO [ 'type' ] , oooO [ 'iso_639_1' ] , oooO [ 'size' ] )
   O00Oo . append ( ( iII , "plugin://plugin.video.youtube/play/?video_id=%s" % oooO [ 'key' ] ) )
   if 43 - 43: ii1I1iII1I1I - I1I . o0Oo - Iii1i % iIi
  return O00Oo
  if 49 - 49: IiIIii11Ii . o0Oo + I11II1Ii - I11II1Ii
  if 78 - 78: i1 - ooOOO
 def clearInfoExtra ( self ) :
  OO = [ 'tagline' , 'production_countries' , 'productora_logo' ,
 'resume_time' , 'productora_name' , 'created_by' , 'status' , 'budget' ,
 'revenue' , 'director' , 'pausa' , 'tvshow_poster' ]
  OoOo00oO000oo = [ "p3Info_extraET" , "p3TotalEpisodes" , "totalEpisodes" , "totalSeasons" , "p3TotalSeasons" ]
  if 83 - 83: i1I1IiIIiIi1 / Ii / o0Oo + i1iiIII111
  for IIIIIIi in OO + OoOo00oO000oo :
   xbmcgui . Window ( 10000 ) . clearProperty ( 'p3Info_%s' % IIIIIIi )
   if 61 - 61: I11II1Ii
   if 7 - 7: i1i1i1111I / Ii * Iii1i
 def getInfoExtra ( self , tmdb , type , resume_time = None ) :
  import sys
  import xbmcplugin
  if 32 - 32: i11 . OooOoo
  if 31 - 31: Oo - iIi
  IIIi1111iiIi1 = "https://image.tmdb.org/t/p/"
  O00Oo = dict ( )
  O00O = 'getInfoExtra{0}_{1}' . format ( tmdb , type )
  if 4 - 4: o0Oo % I1I - i1i1i1111I
  if OOoOoo000O00 :
   try :
    ii1IiIiiII = CACHE . get ( O00O )
    if ii1IiIiiII :
     if 76 - 76: i1 * oOo0O00 . i11 * iIi . IiIIii11Ii . I11II1Ii
     O00Oo = ii1IiIiiII
   except :
    pass
    if 55 - 55: i1i1i1111I + i1iiIII111 % ii1I1iII1I1I . Oo - IiIIii11Ii - i1I1IiIIiIi1
  if not O00Oo :
   if type == 'tv' :
    credits = 'aggregate_credits'
   else :
    credits = 'credits'
    if 91 - 91: I1Ii1I1 - iIIiiIIiii1
   IIiiii1IiIiII = self . request ( type , tmdb , { 'append_to_response' : credits } )
   if 84 - 84: I11II1Ii % i1I1IiIIiIi1 - ii1I1iII1I1I
   O00Oo = {
 'pausa' : 'true' ,
 'tagline' : IIiiii1IiIiII . get ( 'tagline' )
 }
   if 94 - 94: i1iiIII111 + i1i1i1111I / i1I1IiIIiIi1 + i1I1IiIIiIi1 / iIi
   if 79 - 79: i1iiIII111 - oo0O000ooO . I1Ii1I1 + I1I - ooOOO + i1iiIII111
   if 36 - 36: ooOOO * Iii1i % I1I % i1 . ii1I1iII1I1I
   try :
    oO00OOooOoO0o = load_json_file ( xbmcvfs . translatePath ( 'special://home/addons/plugin.video.palantir3/resources/iso3166.json' ) )
    O00OO00OO = IIiiii1IiIiII . get ( 'production_countries' , [ ] )
    OOoo0o = ""
    for oooO in range ( 0 , 3 if len ( O00OO00OO ) >= 3 else len ( O00OO00OO ) ) :
     o00ooo0OO0000 = O00OO00OO [ oooO ] . get ( 'iso_3166_1' )
     oOoOo = oO00OOooOoO0o . get ( o00ooo0OO0000 )
     if not oOoOo :
      oOoOo = O00OO00OO [ oooO ] . get ( 'name' , '' )
     if oOoOo :
      OOoo0o += oOoOo + ', '
    if OOoo0o :
     O00Oo [ 'production_countries' ] = OOoo0o [ : - 2 ]
   except : pass
   if 39 - 39: I11II1Ii
   if 17 - 17: Ii . oOo0O00 % OooOoo
   o0 = IIiiii1IiIiII . get ( credits ) . get ( 'cast' )
   OOOooOOoo = dict ( )
   O00Oo [ 'cast' ] = list ( )
   for O00 in range ( 0 , 20 if len ( o0 ) >= 20 else len ( o0 ) ) :
    OOOooOOoo = { 'name' : o0 [ O00 ] . get ( 'name' ) ,
 'id' : o0 [ O00 ] . get ( 'id' ) ,
 'profile_path' : ''
 }
    if 88 - 88: OooOoo
    if o0 [ O00 ] . get ( 'profile_path' ) :
     OOOooOOoo [ 'profile_path' ] = IIIi1111iiIi1 + 'w300' + o0 [ O00 ] . get ( 'profile_path' )
    elif o0 [ O00 ] . get ( 'gender' ) == 1 :
     OOOooOOoo [ 'profile_path' ] = 'special://home/addons/plugin.video.palantir3/resources/media/mujer.png'
    elif o0 [ O00 ] . get ( 'gender' ) == 2 :
     OOOooOOoo [ 'profile_path' ] = 'special://home/addons/plugin.video.palantir3/resources/media/hombre.png'
    else :
     OOOooOOoo [ 'profile_path' ] = 'special://home/addons/plugin.video.palantir3/resources/media/nodefinido.png'
     if 20 - 20: i1i1i1111I + Oo / ii1I1iII1I1I % i11 % i11
    if 'character' in o0 [ O00 ] :
     OOOooOOoo [ 'character' ] = o0 [ O00 ] . get ( 'character' )
     if 29 - 29: i1I1IiIIiIi1 - oOo0O00 - ii1I1iII1I1I % iIi + i11
    elif 'roles' in o0 [ O00 ] :
     i1iI1 = list ( )
     for Oo0 in o0 [ O00 ] . get ( 'roles' ) :
      if not '/' in Oo0 . get ( 'character' ) :
       if Oo0 . get ( 'character' ) not in i1iI1 :
        i1iI1 . append ( Oo0 . get ( 'character' ) )
      else :
       for ii1ii in Oo0 . get ( 'character' ) . split ( '/' ) :
        if ii1ii . strip ( ) not in i1iI1 :
         i1iI1 . append ( ii1ii . strip ( ) )
     if i1iI1 :
      OOOooOOoo [ 'character' ] = ' / ' . join ( i1iI1 )
      if 1 - 1: i11 - oOo0O00 - i1 . oOo0O00
    O00Oo [ 'cast' ] . append ( OOOooOOoo )
    if 91 - 91: i1I1IiIIiIi1 * i1 . ooOOO
   if type == 'tv' :
    I1i = IIiiii1IiIiII . get ( 'networks' )
    if I1i :
     Iiii = I1i [ 0 ]
     O00Oo [ 'productora_name' ] = Iiii . get ( 'name' )
     if Iiii . get ( 'logo_path' ) :
      O00Oo [ 'productora_logo' ] = IIIi1111iiIi1 + "w300" + Iiii . get ( 'logo_path' )
      if 40 - 40: iIi * i1I1IiIIiIi1 + i1I1IiIIiIi1 . oOo0O00 * o0Oo
    Oo0oO0O0O = IIiiii1IiIiII . get ( 'created_by' , [ ] )
    i111i = ""
    for oooO in range ( 0 , 3 if len ( Oo0oO0O0O ) >= 3 else len ( Oo0oO0O0O ) ) :
     oO00 = Oo0oO0O0O [ oooO ] . get ( 'name' , '' )
     if oO00 :
      i111i += oO00 + ', '
    if i111i :
     O00Oo [ 'created_by' ] = i111i [ : - 2 ]
     if 57 - 57: iIi / oo0O000ooO - i1i1i1111I
    OOO0ooOO = IIiiii1IiIiII . get ( 'status' )
    if OOO0ooOO :
     OO0oOoOOOoO0 = load_json_file ( xbmcvfs . translatePath ( 'special://home/addons/plugin.video.palantir3/resources/status.json' ) )
     O00Oo [ 'status' ] = OO0oOoOOOoO0 . get ( OOO0ooOO , OOO0ooOO )
     if 1 - 1: i1I1IiIIiIi1 % Ii - iIIiiIIiii1 / i11 + i1I1IiIIiIi1 - Ii
    IiII1Iii11 = IIiiii1IiIiII . get ( 'poster_path' )
    if IiII1Iii11 :
     O00Oo [ 'tvshow_poster' ] = IIIi1111iiIi1 + 'w780' + IiII1Iii11
     if 31 - 31: oOo0O00 / Iii1i % ii1I1iII1I1I % i1 . i1I1IiIIiIi1 . Oo
     if 83 - 83: oOo0O00 - iIIiiIIiii1
   else :
    OOoO0oOo0 = IIiiii1IiIiII . get ( 'production_companies' )
    if OOoO0oOo0 :
     iII1Ii = OOoO0oOo0 [ 0 ]
     O00Oo [ 'productora_name' ] = iII1Ii . get ( 'name' )
     if iII1Ii . get ( 'logo_path' ) :
      O00Oo [ 'productora_logo' ] = IIIi1111iiIi1 + "w300" + iII1Ii . get ( 'logo_path' )
      if 37 - 37: iIi + oo0O000ooO % i1I1IiIIiIi1 / oo0O000ooO % i1iiIII111 + I11II1Ii
    Oo0o0Oo = IIiiii1IiIiII . get ( 'credits' , { } ) . get ( 'crew' )
    if Oo0o0Oo :
     o0O0OO0 = list ( )
     for Iioo0Oo0oO0 in Oo0o0Oo :
      if Iioo0Oo0oO0 . get ( 'job' ) == "Director" :
       o0O0OO0 . append ( Iioo0Oo0oO0 . get ( 'name' ) )
      if len ( o0O0OO0 ) == 3 : break
      if 20 - 20: oo0O000ooO
     O0O0oO00OO0 = ", " . join ( o0O0OO0 [ 0 : 3 ] )
     if O0O0oO00OO0 :
      O00Oo [ 'director' ] = O0O0oO00OO0
      if 92 - 92: Ii % i1i1i1111I % oOo0O00 / i1
    I11 = IIiiii1IiIiII . get ( 'budget' )
    if I11 :
     O00Oo [ 'budget' ] = "{:,}" . format ( I11 ) . replace ( "," , "." ) + '$'
    I1Ii = IIiiii1IiIiII . get ( 'revenue' )
    if I1Ii :
     O00Oo [ 'revenue' ] = "{:,}" . format ( I1Ii ) . replace ( "," , "." ) + '$'
     if 6 - 6: oOo0O00 . IiIIii11Ii + ii1I1iII1I1I
     if 19 - 19: ii1I1iII1I1I % iIi
   if OOoOoo000O00 :
    try :
     CACHE . set ( O00O , O00Oo , expiration = iIi1ii1I1iI11 )
    except :
     pass
     if 88 - 88: I1Ii1I1 / i1i1i1111I
  o0ooO0OOO = O00Oo . pop ( 'cast' , None )
  if resume_time :
   O00Oo [ 'resume_time' ] = '0' + str ( datetime . timedelta ( seconds = resume_time ) ) . split ( '.' ) [ 0 ]
   if 86 - 86: i1I1IiIIiIi1
   if 37 - 37: I1Ii1I1 % i1I1IiIIiIi1 . iIi + ii1I1iII1I1I + ooOOO * i1I1IiIIiIi1
  for IIIIIIi , oOooO0O0 in O00Oo . items ( ) :
   if 38 - 38: Iii1i + o0Oo * Iii1i + Ii % oo0O000ooO % oOo0O00
   try :
    xbmcgui . Window ( 10000 ) . setProperty ( 'p3Info_%s' % IIIIIIi , oOooO0O0 )
   except :
    xbmcgui . Window ( 10000 ) . setProperty ( 'p3Info_%s' % IIIIIIi , str ( oOooO0O0 ) )
    if 100 - 100: IiIIii11Ii % i1
  if o0ooO0OOO :
   if 82 - 82: ooOOO % OooOoo
   try :
    for iIi1I1 in o0ooO0OOO :
     iI1Iii = xbmcgui . ListItem ( label = iIi1I1 . get ( 'name' ) )
     iI1Iii . setArt ( { 'thumb' : iIi1I1 . get ( 'profile_path' ) } )
     iI1Iii . setProperty ( 'rol' , iIi1I1 . get ( 'character' ) )
     iI1Iii . setProperty ( 'actorID' , str ( iIi1I1 . get ( 'id' ) ) + "_" + type )
     xbmcplugin . addDirectoryItem ( int ( sys . argv [ 1 ] ) , url = "" , listitem = iI1Iii , isFolder = False )
    xbmcplugin . endOfDirectory ( handle = int ( sys . argv [ 1 ] ) )
   except :
    pass
    if 17 - 17: iIIiiIIiii1 + ooOOO % ooOOO / oOo0O00 - i1iiIII111
 def findByActor ( self , actorID , content ) :
  O00Oo = list ( )
  O00O = 'findByActor{0}_{1}' . format ( actorID , content )
  if 15 - 15: OooOoo . o0Oo / IiIIii11Ii % i1i1i1111I
  if OOoOoo000O00 :
   try :
    ii1IiIiiII = CACHE . get ( O00O )
    if ii1IiIiiII :
     if 51 - 51: ooOOO
     O00Oo = ii1IiIiiII
   except :
    pass
    if 69 - 69: i1I1IiIIiIi1
  if not O00Oo :
   IIiiii1IiIiII = self . request ( 'person' , '%s/combined_credits' % actorID )
   if 48 - 48: ooOOO * o0Oo % IiIIii11Ii * i1 . Iii1i - i11
   for oo0O0O0Ooooo in IIiiii1IiIiII . get ( 'cast' , [ ] ) :
    if oo0O0O0Ooooo . get ( 'media_type' ) == content :
     O00Oo . append ( oo0O0O0Ooooo . get ( 'id' ) )
     if 39 - 39: Oo . I11II1Ii / o0Oo / i1I1IiIIiIi1
   if OOoOoo000O00 :
    try :
     CACHE . set ( O00O , O00Oo , expiration = iIi1ii1I1iI11 )
    except :
     pass
     if 48 - 48: I11II1Ii * iIi - OooOoo * Oo - i11 - ii1I1iII1I1I
  return O00Oo
  if 36 - 36: IiIIii11Ii
