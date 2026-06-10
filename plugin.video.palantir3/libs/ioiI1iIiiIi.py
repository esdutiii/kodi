# -*- coding: utf-8 -*-
if 82 - 82: Iii1i
import re
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import xbmc
import xbmcgui
import xbmcvfs
import random
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
from libs . ioiIIIiII import downloadpage , DEFAULT_HEADERS
from libs . iooooooOoO0 import logger , localize , KODI_VERSION , set_setting , ISESTUARYPALANTIR , load_json , get_setting , CACHE , SetColor , WINDOW
from libs . ioIIiII11 import Watched , Trakt
from libs . ioI1iII import P3Item , setInfoTag
from libs . ioo00ooO0 import P3Player , info_nextEpisode , get_nextEpisode
from libs . ioOOO0oo import get_url , Resolver
from libs . ioiiI1II1 import MoriaDB
from libs . ioiiiIIIiI import Tmdb
if 31 - 31: i1I
def menu ( p3Item ) :
 i1I1 = list ( )
 I1Ii111i1I = list ( )
 WINDOW . clearProperty ( "p3_play" )
 if 52 - 52: OOooooOo00 * i1I / Iii1i / Ii . i1i1i1111I / Ii
 if not p3Item . page : p3Item . page = 0
 with MoriaDB ( ) as ooO0Oo0o00 :
  oOooo0OOO = ooO0Oo0o00 . executeSelect ( p3Item . sql )
  if 53 - 53: Ii * Oo * ooo000 . i1iiIII111
  if 14 - 14: I1I / oOO
 for ooOOooO0 , i1iiiiIIIiIi , II , OO0000 , oOoo0 in oOooo0OOO [ p3Item . page * 50 : 50 + p3Item . page * 50 ] :
  if re . findall ( r'(#\d+)' , ooOOooO0 ) :
   Iio0 = re . findall ( r'#(\d+)' , ooOOooO0 ) [ 0 ]
   ooOOooO0 = re . sub ( r'#%s' % Iio0 , localize ( int ( Iio0 ) ) , ooOOooO0 )
   if 11 - 11: OOooooOo00 . i1i1i1111I
  with Watched ( ) as I1i :
   if i1iiiiIIIiIi == 'Mis_serieS' :
    if not get_setting ( "follow-up3" ) or not I1i . getMisSeries ( ) :
     continue
   elif localize ( 30093 ) in ooOOooO0 :
    if 75 - 75: OOooooOo00 . Ooo0Ooo . i1I * I11iiIi11i1I % i1iiIII111
    if not get_setting ( "moviesUnfinished" ) or not I1i . getMoviesUnfinished ( ) :
     continue
     if 34 - 34: i1iiIII111 * i1
  if isinstance ( ooOOooO0 , int ) :
   ooOOooO0 = str ( ooOOooO0 )
   if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
  ii1IiIiiII = re . findall ( r'^\[G(\d)]' , ooOOooO0 )
  if ii1IiIiiII :
   I1I111i11I = int ( ii1IiIiiII [ 0 ] )
   ooOOooO0 = ooOOooO0 [ 4 : ]
   ii1IiIiiII = ' ' * I1I111i11I + '%s'
  else :
   ii1IiIiiII = '%s'
   if 85 - 85: OooOoo
  o00 = p3Item . clone (
 action = i1iiiiIIIiIi or ( 'menu' if OO0000 else '' ) ,
 fanart = oOoo0 if oOoo0 else p3Item . fanart ,
 page = 0 ,
 sql = OO0000 )
  if 20 - 20: OOooooOo00 + i1iiIII111 / I1I
  if re . findall ( r'^\[(?:B|I|COLOR\s&?\w+)\]' , ooOOooO0 ) :
   Ooo0OO = re . findall ( r']([^\[]+)' , ooOOooO0 )
   if Ooo0OO :
    o00 . label = re . sub ( Ooo0OO [ 0 ] , ii1IiIiiII % Ooo0OO [ 0 ] , ooOOooO0 )
  elif not i1iiiiIIIiIi and not OO0000 :
   o00 . label = SetColor ( ii1IiIiiII % ooOOooO0 , 'LabelColor' )
  elif i1iiiiIIIiIi == 'listas_trakt' and not get_setting ( 'trakt_enabled' ) :
   o00 . action = ''
   o00 . label = SetColor ( ooOOooO0 , 'LabelColor' , 'C0' )
   o00 . plot = localize ( 30528 )
  else :
   o00 . label = SetColor ( ii1IiIiiII % ooOOooO0 , 'MenuColor' )
   if 6 - 6: i1iiIII111
   if 99 - 99: ooOOO * I1Ii1I1
  if localize ( 30110 ) in ooOOooO0 :
   o00 . especial = 'mas_vista_mes'
  elif localize ( 30109 ) in ooOOooO0 :
   o00 . especial = 'mas_vistas'
  elif localize ( 30501 ) in ooOOooO0 :
   o00 . especial = 'recomendadas'
  elif localize ( 30093 ) in ooOOooO0 :
   o00 . especial = 'no_finalizadas'
   if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  if II :
   if II . startswith ( "http" ) :
    o00 . icon = II
   else :
    o00 . icon = 'special://home/addons/plugin.video.palantir3/resources/media/' + II
    if 70 - 70: IiIIii11Ii
  i1I1 . append ( o00 )
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
 if len ( oOooo0OOO ) > 50 + 50 * p3Item . page :
  o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 tag = p3Item . tag or p3Item . label ,
 sql = p3Item . sql )
  if ISESTUARYPALANTIR :
   o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
   o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
   o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
  i1I1 . append ( o00 )
  if 88 - 88: Oo * IiIIii11Ii
 return i1I1
 if 100 - 100: OOooooOo00 - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
def buscar3 ( p3Item ) :
 if xbmc . getInfoLabel ( 'Container.PluginName' ) in [ 'plugin.video.themoviedb.helper' ] :
  if 29 - 29: IiIIii11Ii - oOo0O00
  return list ( )
  if 30 - 30: I1I . ooo000
 OOO = xbmcgui . Dialog ( )
 i1I1 = list ( )
 if 83 - 83: oOO - Iii1i + ooOOO . i1I / ooOOO
 if WINDOW . getProperty ( "p3_play" ) :
  p3Item = P3Item ( ) . fromurl ( WINDOW . getProperty ( "p3_item_buscar" ) )
  WINDOW . clearProperty ( "p3_play" )
 else :
  iII1II11iI1 = OOO . input ( localize ( 30032 ) ,
 str ( get_setting ( "Query" ) ) if get_setting ( "RemenberQuery" ) and get_setting ( "Query" ) else "" )
  if not iII1II11iI1 :
   return None
  set_setting ( "Query" , iII1II11iI1 )
  if "'" in iII1II11iI1 :
   p3Item . sql = p3Item . sql . replace ( "'" , '"' )
  p3Item . sql = p3Item . sql % iII1II11iI1
  WINDOW . setProperty ( "p3_item_buscar" , p3Item . tourl ( ) )
  if 25 - 25: Ooo0Ooo . I11iiIi11i1I . oOO
 if 'rebuscar' in p3Item . sql :
  OO0000 = 'select sql FROM menus where action="buscar3" and menu_id >10 ORDER by menu_id asc'
  iII1II11iI1 = p3Item . sql . replace ( 'rebuscar ' , '' )
  with MoriaDB ( ) as ooO0Oo0o00 :
   for Ii1I1I1i in ooO0Oo0o00 . executeSelect ( OO0000 ) :
    Ii1I1I1i = Ii1I1I1i [ 0 ] % iII1II11iI1
    oOooo0OOO = ooO0Oo0o00 . executeSelect ( Ii1I1I1i )
    if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
    if oOooo0OOO :
     if 'v_pelis_Pelicula' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30100 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_peliculaS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_series_Novela' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30504 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_serieS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_series_General' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30101 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_serieS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_pelis_Dibujo' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30126 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_peliculaS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_series_Dibujo' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30127 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_serieS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_pelis_Anime' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30130 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_peliculaS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_series_Anime' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30131 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_serieS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_pelis_Musica' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30104 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_peliculaS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_pelis_Documental' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30132 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_peliculaS" ,
 sql = Ii1I1I1i
 ) )
     elif 'v_series_Documental' in Ii1I1I1i :
      i1I1 . append ( p3Item . clone (
 label = SetColor ( '%s (%s)' % ( localize ( 30133 ) , len ( oOooo0OOO ) ) , 'MenuColor' ) ,
 action = "listado_serieS" ,
 sql = Ii1I1I1i
 ) )
      if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * i1I % oOo0O00
 elif 'buscarPelis' in p3Item . sql :
  iII1II11iI1 = p3Item . sql . replace ( 'buscarPelis ' , '' )
  p3Item . sql = ( "SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration,mpaa,genero, trailer, clearlogo, "
 "rating, categoria FROM v_pelis where iREGEXP (')%s', titulo) ORDER by titulo COLLATE latin1" % iII1II11iI1 )
  i1I1 = listado_peliculaS ( p3Item )
  if 52 - 52: oOo0O00 . I1I + i1I - i1iiIII111 % iI1iII1I1I1i
 elif 'buscarSeries' in p3Item . sql :
  iII1II11iI1 = p3Item . sql . replace ( 'buscarSeries ' , '' )
  p3Item . sql = ( "SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa,genero, trailer, clearlogo, rating, "
 "categoria FROM v_series where iREGEXP ('%s', titulo) ORDER by titulo COLLATE latin1" % iII1II11iI1 )
  i1I1 = listado_serieS ( p3Item )
  if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
 elif 'v_series_' in p3Item . sql :
  i1I1 = listado_serieS ( p3Item )
 elif 'v_pelis_' in p3Item . sql :
  i1I1 = listado_peliculaS ( p3Item )
  if 37 - 37: OOooooOo00 * i1i1i1111I + oOo0O00 / I1I / OooOoo
 if not i1I1 :
  iI1iI = SetColor ( '%s [B]%s[/B]' % ( localize ( 30033 ) , iII1II11iI1 ) , 'LabelColor' )
  OOO . ok ( 'Palantir 3' , iI1iI )
 else :
  WINDOW . setProperty ( "p3_play" , "true" )
  if 54 - 54: I1I % ooo000 * ooo000 - OooOoo / Iii1i * Oo
 return i1I1
 if 100 - 100: I1Ii1I1 / I11iiIi11i1I * Ii - oOO
 if 32 - 32: iI1iII1I1I1i
def listado_colecciones_series ( p3Item ) :
 i1I1 = list ( )
 if 18 - 18: I11iiIi11i1I * OOooooOo00 % iI1iII1I1I1i + OOooooOo00
 if 93 - 93: oOO - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
 if 'v_series_General' in p3Item . sql :
  OoOOo0OoOOO0 = 'v_series_General'
 elif 'v_series_Novela' in p3Item . sql :
  OoOOo0OoOOO0 = 'v_series_Novela'
 elif 'v_series_Dibujo' in p3Item . sql :
  OoOOo0OoOOO0 = 'v_series_Dibujo'
 elif 'v_series_Anime' in p3Item . sql :
  OoOOo0OoOOO0 = 'v_series_Anime'
 elif 'v_series_Documental' in p3Item . sql :
  OoOOo0OoOOO0 = 'v_series_Documental'
  if 11 - 11: i1 / ooo000
 Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa, genero, trailer, clearlogo, rating,categoria  from {0} where INICIAL(titulo,"{1}") order by titulo COLLATE latin1'
 if localize ( 30114 ) in p3Item . label :
  Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa, genero, trailer, clearlogo, rating,categoria  from {0} where genero REGEXP "{1}"'
  Ii1I1I1i += get_setting ( "OrderGenre" , " order by titulo COLLATE latin1" )
 elif localize ( 30116 ) in p3Item . label :
  Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa, genero, trailer, clearlogo, rating,categoria  from {0} where fecha like "{1}%"'
  Ii1I1I1i += get_setting ( "OrderYear" , " order by titulo COLLATE latin1" )
  if 89 - 89: I1I * i1i1i1111I
 with MoriaDB ( ) as ooO0Oo0o00 :
  oOooo0OOO = ooO0Oo0o00 . executeSelect ( p3Item . sql )
 if oOooo0OOO :
  O0OOooO = get_setting ( 'limitItemList' )
  for ooOOooO0 , oOOoOOOO000 , IIIIi , oOoo0 , id in oOooo0OOO [ p3Item . page * O0OOooO : O0OOooO + p3Item . page * O0OOooO ] :
   if not IIIIi :
    if p3Item . poster and '/mas.png' in p3Item . poster :
     IIIIi = IIIIi . replace ( '/mas.png' , '/buscar.png' )
    elif p3Item . poster :
     IIIIi = p3Item . poster
    else :
     IIIIi = p3Item . icon
     if 50 - 50: ooo000 * I1Ii1I1 * iI1iII1I1I1i
   o00 = p3Item . clone (
 title = ooOOooO0 ,
 label = SetColor ( ooOOooO0 , 'MenuColor' ) ,
 action = 'listado_serieS' ,
 plot = oOOoOOOO000 ,
 poster = IIIIi ,
 fanart = oOoo0 if oOoo0 else p3Item . fanart ,
 page = 0 ,
 sql = Ii1I1I1i . format ( OoOOo0OoOOO0 , id )
 )
   if 17 - 17: Iii1i % i1I - Iii1i % Ooo0Ooo . OooOoo
   i1I1 . append ( o00 )
   if 60 - 60: ooOOO . ooo000
  if len ( oOooo0OOO ) > O0OOooO + O0OOooO * p3Item . page :
   o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 tag = p3Item . tag or p3Item . label ,
 sql = p3Item . sql )
   if ISESTUARYPALANTIR :
    o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
    o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
    o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
   i1I1 . append ( o00 )
   if 42 - 42: i1iiIII111 - i1iiIII111
 elif not p3Item . isWidget :
  iI1iI = SetColor ( '%s %s' % ( localize ( 30033 ) , localize ( 30500 ) ) , 'LabelColor' )
  xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , iI1iI )
  if 98 - 98: Ooo0Ooo + i1i1i1111I + Iii1i - oOO
 return i1I1
 if 7 - 7: i1i1i1111I / Ii * Iii1i
 if 32 - 32: OOooooOo00 . OooOoo
def listado_colecciones_pelis ( p3Item ) :
 i1I1 = list ( )
 i1i1iI1II = re . sub ( r'\[.*?]' , '' , p3Item . tag or p3Item . label ) . strip ( )
 i1i1iI1II = i1i1iI1II . replace ( 'Buscar:' , '' ) . strip ( ) . lower ( )
 if 22 - 22: Oo % oOo0O00 / i1I . oOo0O00 . i1I
 if p3Item . sql :
  if not p3Item . page :
   p3Item . page = 0
   if 87 - 87: I1I - i1I . i1 * Oo
   if 90 - 90: OOooooOo00 * i1I . Ii
  if 'v_pelis_Pelicula' in p3Item . sql :
   OoOOo0OoOOO0 = 'v_pelis_Pelicula'
  elif 'v_pelis_Dibujo' in p3Item . sql :
   OoOOo0OoOOO0 = 'v_pelis_Dibujo'
  elif 'v_pelis_Anime' in p3Item . sql :
   OoOOo0OoOOO0 = 'v_pelis_Anime'
  elif 'v_pelis_Documental' in p3Item . sql :
   OoOOo0OoOOO0 = 'v_pelis_Documental'
   if 45 - 45: IiIIii11Ii - I11iiIi11i1I . i1iiIII111 * Ooo0Ooo . IIiIIiIi11I1
  Ii1I1I1i = r'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb, duration, mpaa, genero,trailer,clearlogo,rating,categoria from {0} where coleccion like "{1}#%" ' r'or coleccion like "%#{1}" or coleccion like "%#{1}#%" or coleccion = "{1}"'
  if 14 - 14: iI1iII1I1I1i + OooOoo * I1Ii1I1 - I11iiIi11i1I
  if 84 - 84: oOO % iI1iII1I1I1i - Ooo0Ooo
  if localize ( 30111 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i += get_setting ( "OrderSpecial" , " order by titulo COLLATE latin1" )
  elif localize ( 30119 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i += " order by sagas"
   p3Item . sql = p3Item . sql . split ( 'order' ) [ 0 ] + get_setting ( 'OrderSagas' )
  elif localize ( 30114 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration, mpaa, genero,trailer,clearlogo,rating,categoria from {0} where genero REGEXP "{1}"'
   Ii1I1I1i += get_setting ( "OrderGenre" , " order by titulo COLLATE latin1" )
  elif localize ( 30115 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration, mpaa, genero,trailer,clearlogo,rating,categoria from {0} where INICIAL(titulo,"{1}")'
   Ii1I1I1i += " order by titulo COLLATE latin1"
  elif localize ( 30116 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration, mpaa, genero,trailer,clearlogo,rating,categoria from {0} where fecha like "{1}%"'
   Ii1I1I1i += get_setting ( "OrderYear" , " order by titulo COLLATE latin1" )
  elif localize ( 30117 ) . lower ( ) in i1i1iI1II :
   Ii1I1I1i = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration, mpaa, genero,trailer,clearlogo,rating,categoria from {0} where calidad REGEXP "{1}"'
   Ii1I1I1i += get_setting ( "OrderQuality" , " order by updated desc" )
   if 94 - 94: i1iiIII111 + i1i1i1111I / iI1iII1I1I1i + iI1iII1I1I1i / i1I
  with MoriaDB ( ) as ooO0Oo0o00 :
   oOooo0OOO = ooO0Oo0o00 . executeSelect ( p3Item . sql )
  if oOooo0OOO :
   O0OOooO = get_setting ( 'limitItemList' )
   for ooOOooO0 , oOOoOOOO000 , IIIIi , oOoo0 , id in oOooo0OOO [ p3Item . page * O0OOooO : O0OOooO + p3Item . page * O0OOooO ] :
    if 'REGEXP' in Ii1I1I1i :
     id = id . replace ( r'(' , r'\W' ) . replace ( r')' , r'\W' )
     if 79 - 79: i1iiIII111 - IIiIIiIi11I1 . I1Ii1I1 + I1I - ooOOO + i1iiIII111
    if not IIIIi :
     if p3Item . poster and '/mas.png' in p3Item . poster :
      IIIIi = IIIIi . replace ( '/mas.png' , '/buscar.png' )
     elif p3Item . poster :
      IIIIi = p3Item . poster
     else :
      IIIIi = p3Item . icon
      if 36 - 36: ooOOO * Iii1i % I1I % i1 . Ooo0Ooo
    o00 = p3Item . clone (
 title = ooOOooO0 ,
 label = SetColor ( ooOOooO0 , 'MenuColor' ) ,
 action = 'listado_peliculaS' ,
 plot = oOOoOOOO000 ,
 poster = IIIIi ,
 fanart = oOoo0 if oOoo0 else p3Item . fanart ,
 page = 0 ,
 sql = Ii1I1I1i . format ( OoOOo0OoOOO0 , id )
 )
    i1I1 . append ( o00 )
    if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
   if len ( oOooo0OOO ) > O0OOooO + O0OOooO * p3Item . page :
    o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 tag = p3Item . tag or p3Item . label ,
 sql = p3Item . sql )
    if ISESTUARYPALANTIR :
     o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
     o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
     o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
    i1I1 . append ( o00 )
    if 52 - 52: oOo0O00 / i1I * IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO
  elif not p3Item . isWidget :
   iI1iI = SetColor ( '%s %s' % ( localize ( 30033 ) , localize ( 30500 ) ) , 'LabelColor' )
   xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , iI1iI )
   if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
 return i1I1
 if 30 - 30: I1I
 if 41 - 41: oOO
def listas_trakt ( p3Item ) :
 i1I1 = list ( )
 i1II1 = oOoOo = None
 if 39 - 39: oOO
 with Watched ( ) as I1i :
  if get_setting ( 'trakt_enabled' ) and get_setting ( 'trakt_user_lists' ) :
   if 17 - 17: Ii . oOo0O00 % OooOoo
   I1i . addLiTraktUser ( )
   if 82 - 82: Iii1i . oOo0O00 % IIiIIiIi11I1 - iI1iII1I1I1i
  oO , oOOii1I = I1i . getWatchlist ( )
  if 11 - 11: oOO . Ooo0Ooo
  for III1II11i , iiI1iiii1iii , O0OOooO0O0Oo0 , oOOoOOOO000 , I11iIi1i1iIi , iI11 , OO0 in I1i . getAllLiTrakt ( ) :
   O00OOo = {
 'user' : III1II11i ,
 'list_id' : iiI1iiii1iii ,
 'content' : I11iIi1i1iIi ,
 'sort_by' : iI11 ,
 'sort_how' : OO0
 }
   if 77 - 77: Ooo0Ooo
   if III1II11i == get_setting ( 'trakt_slug' ) :
    ooOOooO0 = SetColor ( O0OOooO0O0Oo0 , 'MenuColor' )
   else :
    ooOOooO0 = O0OOooO0O0Oo0
    if 95 - 95: ooOOO % i1i1i1111I . i1
   o00 = p3Item . clone (
 label = ooOOooO0 ,
 title = O0OOooO0O0Oo0 ,
 action = 'listado_trakt' ,
 plot = oOOoOOOO000 ,
 trakt_list = '{0}|{1}|{2}' . format ( III1II11i , iiI1iiii1iii , I11iIi1i1iIi ) ,
 data_json = O00OOo
 )
   if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
   if iiI1iiii1iii == '-1' :
    if oO and I11iIi1i1iIi == 'movie' :
     o00 . title += ' [{0}]' . format ( len ( oO ) )
     o00 . label = SetColor ( o00 . title , 'MenuColor' )
     i1II1 = o00
    elif oOOii1I and I11iIi1i1iIi == 'show' :
     o00 . title += ' [{0}]' . format ( len ( oOOii1I ) )
     o00 . label = SetColor ( o00 . title , 'MenuColor' )
     oOoOo = o00
   else :
    i1I1 . append ( o00 )
    if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
 i1I1 . sort ( key = lambda OOO0ooOO : OOO0ooOO . title )
 if oOoOo :
  i1I1 . insert ( 0 , oOoOo )
  if 89 - 89: ooo000 + Ii % i1i1i1111I - i1iiIII111
 if i1II1 :
  i1I1 . insert ( 0 , i1II1 )
  if 33 - 33: ooo000 . Iii1i % oOO
  if 60 - 60: I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
 i1I1 . append ( p3Item . clone (
 label = SetColor ( localize ( 30518 ) , 'MenuColor' ) ,
 action = 'add_lista_trakt'
 ) )
 if 98 - 98: I1I
 return i1I1
 if 35 - 35: oOo0O00 / IIiIIiIi11I1 - Iii1i . OOooooOo00 * i1
 if 91 - 91: oOO + Iii1i
def add_lista_trakt ( p3Item ) :
 with Watched ( ) as I1i :
  if I1i . addLiTrakt ( ) :
   xbmc . executeJSONRPC ( '{"jsonrpc":"2.0","method":"Input.ExecuteAction","params": {"action": "back"},"id":1}' )
   if 71 - 71: i1 . iI1iII1I1I1i . OooOoo . IIiIIiIi11I1
   if 92 - 92: ooOOO % IIiIIiIi11I1 - IIiIIiIi11I1
def listado_trakt ( p3Item ) :
 def IiIi111iiI ( ) :
  OOoO0O000O = get_setting ( "OrderSpecial" , "titulo" )
  if 'titulo' in OOoO0O000O :
   return 'titulo'
  elif 'fecha' in OOoO0O000O :
   return 'fecha'
  elif 'random' in OOoO0O000O :
   return 'random'
  else :
   return 'updated'
   if 20 - 20: IIiIIiIi11I1 % i1iiIII111 + oOO % ooo000
 O0o0O = list ( )
 if 30 - 30: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
 if not p3Item . data_json :
  if 85 - 85: IIiIIiIi11I1 / OooOoo . i1I % Oo + Oo - I11iiIi11i1I
  O00OOo = re . sub ( r"\\." , "" , p3Item . sql , 0 , re . MULTILINE )
  p3Item . data_json = load_json ( O00OOo )
  if 59 - 59: OooOoo
  if 'pelis' in p3Item . data_json [ 'tabla' ] :
   p3Item . data_json [ 'content' ] = 'movie'
   p3Item . sql = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration,mpaa,genero,trailer,clearlogo,rating,categoria ' . format ( )
  else :
   p3Item . data_json [ 'content' ] = 'show'
   p3Item . sql = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa, genero,trailer,clearlogo,rating,categoria ' . format ( )
   if 53 - 53: i1i1i1111I / ooOOO - OOooooOo00 + ooo000 * i1i1i1111I * i1iiIII111
  if not p3Item . data_json . get ( 'sort_by' ) :
   p3Item . data_json [ 'sort_by' ] = IiIi111iiI ( )
   if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
 elif p3Item . data_json [ 'content' ] == 'movie' :
  p3Item . data_json [ 'tabla' ] = 'v_pelis'
  p3Item . sql = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration,mpaa, genero,trailer,clearlogo,rating,categoria ' . format ( )
 else :
  p3Item . data_json [ 'tabla' ] = 'v_series'
  p3Item . sql = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa, genero,trailer,clearlogo,rating,categoria ' . format ( )
  if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
 iI11 = p3Item . data_json . get ( 'sort_by' , IiIi111iiI ( ) )
 OO0 = p3Item . data_json . get ( 'sort_how' , 'desc' if iI11 != 'titulo' else 'asc' )
 if 'listaTmdbIds' in p3Item . data_json :
  iiIIIIi = p3Item . data_json . get ( 'listaTmdbIds' )
 else :
  with Watched ( ) as I1i :
   if p3Item . data_json . get ( 'list_id' ) == '-1' :
    oO , oOOii1I = I1i . getWatchlist ( )
    if p3Item . data_json [ 'content' ] == 'movie' :
     iiIIIIi = oO
    else :
     iiIIIIi = oOOii1I
   else :
    iiIIIIi = I1i . getLiTraktItems ( p3Item . data_json )
    if 32 - 32: i1I - I1Ii1I1 * I1Ii1I1 / OOooooOo00 . ooo000
 if iiIIIIi :
  p3Item . sql += 'FROM {0} where tmdb in (%s)' . format ( p3Item . data_json [ "tabla" ] ) % ( str ( iiIIIIi ) [ 1 : - 1 ] )
  if iI11 in [ 'titulo' , 'fecha' , 'rating' , 'random' , 'updated' ] :
   if iI11 == 'titulo' :
    OO0 = OO0 if OO0 in [ 'asc' , 'desc' ] else 'asc'
    p3Item . sql += ' ORDER BY titulo COLLATE latin1 {0}' . format ( OO0 )
   elif iI11 == 'fecha' :
    OO0 = OO0 if OO0 in [ 'asc' , 'desc' ] else 'desc'
    p3Item . sql += ' ORDER BY fecha {0}, updated {1}' . format ( OO0 , OO0 )
   elif iI11 == 'rating' :
    OO0 = OO0 if OO0 in [ 'asc' , 'desc' ] else 'desc'
    p3Item . sql += " ORDER BY (substr(rating, instr(rating, '/')+1)+0) {0}" . format ( OO0 )
   elif iI11 == 'random' :
    p3Item . sql += ' ORDER BY random()'
   else :
    OO0 = OO0 if OO0 in [ 'asc' , 'desc' ] else 'desc'
    p3Item . sql += ' ORDER BY updated {0}' . format ( OO0 )
  else :
   iI11 = None
   p3Item . limitItemList = len ( iiIIIIi )
   if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
  if p3Item . data_json [ 'content' ] == 'movie' :
   p3Item . sub_categoria = "movies"
   O00OOo = p3Item . pop ( 'data_json' )
   O0o0O = listado_peliculaS ( p3Item )
  else :
   p3Item . sub_categoria = "tvshows"
   O00OOo = p3Item . pop ( 'data_json' )
   O0o0O = listado_serieS ( p3Item )
   if 60 - 60: oOO * i1i1i1111I / iI1iII1I1I1i
  OO0OOOoOOooO = None
  if O0o0O and O0o0O [ - 1 ] . action == 'listado_trakt' :
   OO0OOOoOOooO = O0o0O . pop ( )
   OO0OOOoOOooO . data_json = O00OOo
   if 74 - 74: oOo0O00 % oOo0O00 * Iii1i
  if not iI11 :
   if 85 - 85: Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
   O0o0O . sort ( key = lambda OOO0ooOO : iiIIIIi . index ( int ( OOO0ooOO . tmdb ) ) )
   if 100 - 100: IiIIii11Ii % i1
   if 82 - 82: ooOOO % OooOoo
  if OO0OOOoOOooO :
   O0o0O . append ( OO0OOOoOOooO )
   if 81 - 81: Ii
 else :
  iI1iI = SetColor ( '%s [B]%s[/B]' % ( localize ( 30033 ) , p3Item . label ) , 'LabelColor' )
  xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , iI1iI )
  if 40 - 40: i1I . OooOoo + oOo0O00 . i1iiIII111
 return O0o0O
 if 96 - 96: I1I / oOO / I11iiIi11i1I + I11iiIi11i1I
 if 35 - 35: IIiIIiIi11I1 + oOo0O00
def listado_content_actor ( p3Item ) :
 if 96 - 96: iI1iII1I1I1i . OooOoo . i1
 iiIIIIi = Tmdb ( ) . findByActor ( p3Item . actorID , p3Item . content )
 p3Item . data_json = { 'content' : p3Item . content ,
 'listaTmdbIds' : iiIIIIi ,
 'sort_by' : 'fecha' if p3Item . content == 'movie' else 'updated' ,
 'sort_how' : 'desc'
 }
 if 87 - 87: ooo000 * IiIIii11Ii % ooo000 . ooOOO . Oo % iI1iII1I1I1i
 return listado_trakt ( p3Item )
 if 48 - 48: ooOOO * ooo000 % IiIIii11Ii * i1 . Iii1i - OOooooOo00
 if 72 - 72: i1 % i1i1i1111I * iI1iII1I1I1i
def listado_random ( p3Item ) :
 if 90 - 90: Ooo0Ooo * OooOoo . Ii
 i1I1 = list ( )
 Iiii1iIII = list ( )
 o0oO0OOo = list ( )
 oOoOo0O00 = list ( )
 oOooOo0o = 0
 if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % oOO . I1I
 with open ( xbmcvfs . translatePath ( 'special://profile/addon_data/skin.estuary.palantir/settings.xml' ) , 'r' , encoding = 'utf-8' ) as ii1iIii :
  o0o = ii1iIii . read ( )
  if 17 - 17: IiIIii11Ii
 for Ooo0OO , Iio0O0 , iII11iI1i in re . findall ( r'"hidespotlight(.*?)_(.*?)" type="bool">([^<]+)<' , o0o ) :
  if iII11iI1i == 'false' :
   Iio0O0 = Iio0O0 . capitalize ( ) . replace ( 'Pelicula' , 'Película' ) . replace ( 'Musica' , 'Música' )
   if Ooo0OO == 'pelis' :
    o0oO0OOo . append ( Iio0O0 )
   else :
    oOoOo0O00 . append ( Iio0O0 )
    if 79 - 79: I11iiIi11i1I
 if not oOoOo0O00 and not o0oO0OOo :
  o0oO0OOo = [ 'Película' ]
  oOoOo0O00 = [ 'General' ]
  if 39 - 39: Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
 if o0oO0OOo :
  p3Item . sql = ( "SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration,mpaa,genero, trailer, clearlogo, rating, categoria FROM v_pelis WHERE mpaa <> '+18' "
 "and categoria in (%s) ORDER by random()" ) % str ( o0oO0OOo ) [ 1 : - 1 ]
  oOooOo0o = 17 if not oOoOo0O00 else random . randint ( 1 , 10 )
  p3Item . limitItemList = oOooOo0o
  i1I1 . extend ( listado_peliculaS ( p3Item ) [ : - 1 ] )
  if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . OOooooOo00 + i1I
  if 71 - 71: ooo000 + I11iiIi11i1I % iI1iII1I1I1i + OOooooOo00 % Oo - Oo
 if oOoOo0O00 :
  p3Item . sql = ( "SELECT titulo, fecha, plot, poster, fondo, tmdb, audio,mpaa,genero, trailer, clearlogo, rating, categoria from v_series WHERE mpaa <> '+18' "
 "and categoria in (%s) ORDER by random()" ) % str ( oOoOo0O00 ) [ 1 : - 1 ]
  p3Item . limitItemList = 17 - oOooOo0o
  i1I1 . extend ( listado_serieS ( p3Item ) [ : - 1 ] )
  if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
 random . shuffle ( i1I1 )
 CACHE . set ( p3Item . nameWidget , i1I1 [ : 20 ] , pickle_data = True , expiration = 720 )
 return i1I1 [ : 20 ]
 if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
 if 12 - 12: i1i1i1111I
def listado_peliculaS ( p3Item ) :
 if 56 - 56: IiIIii11Ii
 i1I1 = list ( )
 iiIIIIi = list ( )
 i11I1iII1I1 = False
 oOooo0OOO = None
 if 7 - 7: oOo0O00 % Oo + i1I
 if p3Item . limitItemList :
  O0OOooO = p3Item . pop ( 'limitItemList' )
  if p3Item . isWidget :
   O0OOooO -= 1
 else :
  O0OOooO = get_setting ( 'limitItemList' )
  if 65 - 65: IIiIIiIi11I1 / i1
 if p3Item . sql :
  if p3Item . sub_categoria :
   IIiI1iI111 = p3Item . sub_categoria
  elif p3Item . label == "PelisFavoritas" :
   IIiI1iI111 = "PelisFavoritas"
  else :
   IIiI1iI111 = re . findall ( r'\sv_(.*?)\s' , p3Item . sql + ' ' ) [ 0 ]
   if '_' not in IIiI1iI111 :
    IIiI1iI111 = None
    if 87 - 87: Iii1i % ooOOO % I1Ii1I1 . oOo0O00 + IiIIii11Ii + Iii1i
  if not p3Item . page :
   p3Item . page = 0
   if 24 - 24: ooo000 % i1i1i1111I
  if "News" in p3Item . label or "Novedades" in p3Item . label :
   if 19 - 19: Iii1i * I11iiIi11i1I . ooo000 / iI1iII1I1I1i - I1Ii1I1 + IiIIii11Ii
   p3Item . sql += get_setting ( 'OrderNovedades' )
   if 40 - 40: i1I + i1i1i1111I % OooOoo . OOooooOo00 / i1i1i1111I . ooOOO
  OO0000 = p3Item . sql
  with Watched ( ) as I1i :
   if p3Item . especial == 'mas_vista_mes' :
    if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
    iiIIIIi = I1i . getMasVistas ( 'movies' , 'monthly' )
    i11I1iII1I1 = True
   elif p3Item . especial == 'mas_vistas' :
    if 15 - 15: i1I * I11iiIi11i1I - oOo0O00
    iiIIIIi = I1i . getMasVistas ( 'movies' , 'all' )
    i11I1iII1I1 = True
   elif p3Item . nameWidget == 'WidgetTop10Pelis' :
    if 6 - 6: OOooooOo00 - Ii
    iiIIIIi = I1i . getMasVistas ( 'movies' , 'weekly' )
    i11I1iII1I1 = True
   elif p3Item . nameWidget == 'WidgetPelisWatchlist' :
    if 1 - 1: I1I + OooOoo
    iiIIIIi , OooO0Oo = I1i . getWatchlist ( )
    iiIIIIi = list ( map ( str , iiIIIIi ) )
    i11I1iII1I1 = True
   elif p3Item . especial == 'recomendadas' :
    if 17 - 17: i1 % oOO % IiIIii11Ii * i1i1i1111I
    iiIIIIi = I1i . getRecomendadas ( 'movies' )
    i11I1iII1I1 = True
   elif p3Item . especial == 'no_finalizadas' :
    if 51 - 51: Ooo0Ooo . iI1iII1I1I1i . i1iiIII111 . Ooo0Ooo % ooo000 % Ooo0Ooo
    iiIIIIi = I1i . getMoviesUnfinished ( )
    i11I1iII1I1 = True
   elif 'saga' in OO0000 :
    if 38 - 38: ooo000
    OO0000 = OO0000 . replace ( " order by sagas" , " order by fecha asc" )
   elif 'coleccion' in OO0000 :
    if 3 - 3: OOooooOo00 / IiIIii11Ii - i1i1i1111I
    OO0000 = OO0000 . split ( 'order' ) [ 0 ] + get_setting ( 'OrderSpecial' )
    if 56 - 56: i1
    if 56 - 56: I11iiIi11i1I - ooo000 . i1iiIII111 + i1iiIII111 / I1Ii1I1
  OO0000 = OO0000 . replace ( ';' , '' )
  if iiIIIIi :
   i1iII11iii = ' ' . join ( "WHEN tmdb = {0} THEN {1}" . format ( id , i ) for i , id in enumerate ( iiIIIIi ) )
   OO0000 = OO0000 % ',' . join ( iiIIIIi ) + " ORDER BY CASE {0} END" . format ( i1iII11iii )
   if 19 - 19: I1Ii1I1 / OooOoo % i1i1i1111I
  OO0000 += " limit {0} offset {1}" . format ( O0OOooO + 1 , p3Item . page * O0OOooO )
  if 23 - 23: iI1iII1I1I1i - i1I % i1I - OOooooOo00 * i1iiIII111 + OooOoo
  if iiIIIIi or not i11I1iII1I1 :
   try :
    if not p3Item . isWidget and 'random()' not in OO0000 :
     oO0OO0oO0 = CACHE . get ( OO0000 )
     if oO0OO0oO0 :
      if 10 - 10: iI1iII1I1I1i - Ii . IiIIii11Ii
      return oO0OO0oO0
   except : pass
   with MoriaDB ( ) as ooO0Oo0o00 :
    oOooo0OOO = ooO0Oo0o00 . executeSelect ( OO0000 )
    if 37 - 37: i1i1i1111I
  if oOooo0OOO :
   if iiIIIIi :
    oOooo0OOO . sort ( key = lambda OOO0ooOO : iiIIIIi . index ( str ( OOO0ooOO [ 7 ] ) ) )
   with Watched ( ) as I1i :
    O00oO00oO0O = I1i . getProgressMovies ( )
    if 65 - 65: iI1iII1I1I1i . Oo
   for o0ooo0OO00 in oOooo0OOO [ : O0OOooO ] :
    O0OOooO0O0Oo0 , IIIII11 , oOOoOOOO000 , IIIIi , oOoo0 , IIi , O000oO , iI111Ii , II1Ii11111 , IIiIIiiIIi , iiIi , Ii1Iiii11i1 , oO00oO0O , ooOOoO00OO = o0ooo0OO00 [ : 14 ]
    O0Ooo0oOo0 = None if len ( o0ooo0OO00 ) == 14 else o0ooo0OO00 [ 14 ]
    if 62 - 62: Oo % I11iiIi11i1I * Oo
    O0OOooO0O0Oo0 = O0OOooO0O0Oo0 . replace ( "\\n" , "" )
    oOO0 = SetColor ( ' %s' % O0OOooO0O0Oo0 , 'TituloColor' )
    if IIIII11 :
     IiI = SetColor ( '(%s)' % IIIII11 [ : 4 ] , 'DateColor' )
     ooOOooO0 = "%s %s" % ( oOO0 , IiI )
    if IIi :
     ooO0OoOo = SetColor ( '[%s]' % getIdiomas ( IIi ) , 'AudioColor' )
     ooOOooO0 += " %s" % ooO0OoOo
    if O000oO :
     oOIiiI = SetColor ( '[%s]' % ', ' . join ( set ( O000oO . split ( '#' ) ) ) , 'QltColor' )
     ooOOooO0 += " %s" % oOIiiI
     if 61 - 61: IIiIIiIi11I1 / OOooooOo00 - i1i1i1111I . ooOOO . OooOoo / oOO
    o00 = p3Item . clone (
 label = ooOOooO0 ,
 title = O0OOooO0O0Oo0 ,
 fecha = IIIII11 ,
 plot = oOOoOOOO000 ,
 poster = IIIIi ,
 icon = "" ,
 fanart = oOoo0 ,
 content = 'movies' ,
 tmdb = str ( iI111Ii ) ,
 isPlayable = True ,
 duration = II1Ii11111 ,
 mpaa = IIiIIiiIIi if IIiIIiiIIi else '' ,
 genre = iiIi ,
 trailer = Ii1Iiii11i1 ,
 clearlogo = oO00oO0O ,
 rating = ooOOoO00OO ,
 action = "selectvideos_"
 )
    if 94 - 94: Ooo0Ooo % oOo0O00 . oOo0O00 / Ii . i1
    if O0Ooo0oOo0 :
     o00 . categoria = O0Ooo0oOo0
     if 54 - 54: iI1iII1I1I1i % Oo . OOooooOo00 - Iii1i % I11iiIi11i1I * i1I
    if O0Ooo0oOo0 == 'Película' :
     o00 . sub_categoria = 'pelis_Pelicula'
    elif O0Ooo0oOo0 == 'Música' :
     o00 . sub_categoria = 'pelis_Musica'
    elif O0Ooo0oOo0 :
     o00 . sub_categoria = 'pelis_' + O0Ooo0oOo0
     if 31 - 31: oOo0O00 / Iii1i - IiIIii11Ii % i1I / I1Ii1I1 - i1i1i1111I
    if O00oO00oO0O and iI111Ii in O00oO00oO0O :
     o00 . playCount , o00 . percentPlayed , o00 . totalTime , o00 . lastPlayed = O00oO00oO0O . get ( iI111Ii )
     if 68 - 68: I11iiIi11i1I . I11iiIi11i1I % I11iiIi11i1I
    i1I1 . append ( o00 )
    if 71 - 71: ooo000
   if len ( oOooo0OOO ) > O0OOooO :
    o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 action = "listado_peliculaS" ,
 limitItemList = O0OOooO ,
 sql = p3Item . sql )
    if 61 - 61: ooo000
    if ISESTUARYPALANTIR :
     o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
     o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
     o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
     if 48 - 48: Iii1i * i1i1i1111I + IiIIii11Ii
    if p3Item . isWidget :
     o00 . page = p3Item . page
     o00 . limitItemList = get_setting ( 'limitItemList' )
     if 31 - 31: Oo * i1iiIII111 % Ii / oOO + I1Ii1I1 + iI1iII1I1I1i
    i1I1 . append ( o00 )
    if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
   try :
    if not p3Item . isWidget :
     CACHE . set ( OO0000 , i1I1 , expiration = 10 , pickle_data = True , sub_categoria = IIiI1iI111 )
   except : pass
   if 38 - 38: I1I . Ii
  elif p3Item . action != 'buscar3' and not p3Item . isWidget :
   iI1iI = SetColor ( "%s %s" % ( localize ( 30033 ) , localize ( 30500 ) ) , 'LabelColor' )
   xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , iI1iI )
   if 41 - 41: ooo000 % IIiIIiIi11I1 % ooOOO
 return i1I1
 if 5 - 5: oOo0O00 / Ii + i1iiIII111 * Oo + Ooo0Ooo + ooo000
 if 96 - 96: i1iiIII111 - IIiIIiIi11I1 / IIiIIiIi11I1 * IiIIii11Ii
def getIdiomas ( audio ) :
 oOoO0o0OOooO0 = { 'spa' : 'Esp' }
 audio = audio . replace ( '[' , '' ) . replace ( ']' , '' ) . replace ( '#' , ',' ) . split ( ',' )
 O00Oo0OOO = list ( )
 for III1ii11II1 in audio :
  if ' ' in III1ii11II1 :
   O00Oo0OOO += III1ii11II1 . strip ( ) . split ( ' ' )
  else :
   O00Oo0OOO . append ( III1ii11II1 )
   if 96 - 96: Iii1i / OOooooOo00 / iI1iII1I1I1i * OooOoo . i1 . IiIIii11Ii
 audio = set ( map ( lambda OOO0ooOO : OOO0ooOO . strip ( ) . lower ( ) , O00Oo0OOO ) )
 audio = set ( map ( lambda OOO0ooOO : oOoO0o0OOooO0 . get ( OOO0ooOO , OOO0ooOO . capitalize ( ) ) , audio ) )
 return ', ' . join ( audio )
 if 47 - 47: Ii % OooOoo % iI1iII1I1I1i * IiIIii11Ii
 if 48 - 48: i1I . I11iiIi11i1I / ooo000 + i1iiIII111
def listado_serieS ( p3Item ) :
 if 84 - 84: Oo / I1Ii1I1 . IIiIIiIi11I1
 i1I1 = list ( )
 iiIIIIi = list ( )
 i11I1iII1I1 = False
 oOooo0OOO = None
 if 67 - 67: Oo % ooOOO + iI1iII1I1I1i * I1I
 if p3Item . limitItemList :
  O0OOooO = p3Item . pop ( 'limitItemList' )
  if p3Item . isWidget :
   O0OOooO -= 1
 else :
  O0OOooO = get_setting ( 'limitItemList' )
  if 79 - 79: IIiIIiIi11I1 * Oo / OooOoo
 if p3Item . sql :
  OO0000 = p3Item . sql
  if 10 - 10: iI1iII1I1I1i / i1iiIII111 . IiIIii11Ii * i1i1i1111I
  if not p3Item . page :
   p3Item . page = 0
   if 71 - 71: oOo0O00 + I1Ii1I1 / I11iiIi11i1I + Oo / I1I
  if 'coleccion' in OO0000 :
   if 18 - 18: Iii1i - IiIIii11Ii
   OO0000 = OO0000 . split ( 'order' ) [ 0 ] + get_setting ( 'OrderSpecial' )
   if 71 - 71: iI1iII1I1I1i + OooOoo % i1i1i1111I % oOo0O00 . ooo000
  with Watched ( ) as I1i :
   if p3Item . especial == 'mas_vista_mes' :
    if 92 - 92: I11iiIi11i1I - Ooo0Ooo - i1i1i1111I % i1iiIII111 / i1i1i1111I * iI1iII1I1I1i
    iiIIIIi = I1i . getMasVistas ( 'shows' , 'monthly' )
    i11I1iII1I1 = True
   elif p3Item . especial == 'mas_vistas' :
    if 60 - 60: IiIIii11Ii % oOO / i1I * OooOoo / I11iiIi11i1I - Ii
    iiIIIIi = I1i . getMasVistas ( 'shows' , 'all' )
    i11I1iII1I1 = True
   elif p3Item . nameWidget == 'WidgetTop10Series' :
    if 16 - 16: oOo0O00 / I1Ii1I1 / i1 + I11iiIi11i1I + oOo0O00
    iiIIIIi = I1i . getMasVistas ( 'shows' , 'weekly' )
    i11I1iII1I1 = True
   elif p3Item . nameWidget == 'WidgetSeriesWatchlist' :
    if 11 - 11: oOO / OooOoo + oOo0O00
    OooO0Oo , iiIIIIi = I1i . getWatchlist ( )
    iiIIIIi = list ( map ( str , iiIIIIi ) )
    i11I1iII1I1 = True
   elif p3Item . especial == 'recomendadas' :
    if 79 - 79: I11iiIi11i1I . I1Ii1I1 * i1I % I1Ii1I1 / OOooooOo00
    iiIIIIi = I1i . getRecomendadas ( 'shows' )
    i11I1iII1I1 = True
   elif p3Item . sub_categoria == 'Mis_series' :
    for iI111Ii , oo in I1i . getMisSeries ( ) . items ( ) :
     Ii1I11iI11I1 , O0OOO , iIII = oo . get ( 'ultimo_episodio' )
     if Ii1I11iI11I1 == 1 and O0OOO == 1 and iIII > 0.0 :
      continue
     iiIIIIi . append ( iI111Ii )
    i11I1iII1I1 = True
    if 60 - 60: OOooooOo00 + OooOoo
  OO0000 = OO0000 . replace ( ';' , '' )
  if iiIIIIi :
   i1iII11iii = ' ' . join ( "WHEN tmdb = {0} THEN {1}" . format ( id , i ) for i , id in enumerate ( iiIIIIi ) )
   OO0000 = OO0000 % ',' . join ( iiIIIIi ) + " ORDER BY CASE {0} END" . format ( i1iII11iii )
   if 41 - 41: IiIIii11Ii + OooOoo - I11iiIi11i1I + Oo % i1 + iI1iII1I1I1i
  OO0000 += " limit {0} offset {1}" . format ( O0OOooO + 1 , p3Item . page * O0OOooO )
  if 16 - 16: i1 - Oo / Ii
  if iiIIIIi or not i11I1iII1I1 :
   try :
    if not p3Item . isWidget and 'random()' not in OO0000 :
     oO0OO0oO0 = CACHE . get ( OO0000 )
     if oO0OO0oO0 :
      if 38 - 38: Ooo0Ooo % I1Ii1I1 / i1I + i1iiIII111
      return oO0OO0oO0
   except : pass
   with MoriaDB ( ) as ooO0Oo0o00 :
    oOooo0OOO = ooO0Oo0o00 . executeSelect ( OO0000 )
    if 25 - 25: I11iiIi11i1I - iI1iII1I1I1i
  if oOooo0OOO :
   if 64 - 64: Iii1i - ooo000 . I11iiIi11i1I
   if p3Item . sub_categoria :
    IIiI1iI111 = p3Item . sub_categoria
   elif p3Item . label == "SeriesFavoritas" :
    IIiI1iI111 = "SeriesFavoritas"
   else :
    IIiI1iI111 = re . findall ( r'\sv_(.*?)\s' , p3Item . sql + ' ' ) [ 0 ]
    if '_' not in IIiI1iI111 :
     IIiI1iI111 = None
     if 59 - 59: i1I / IiIIii11Ii
     if 7 - 7: oOo0O00
   with Watched ( ) as I1i :
    O0ooOo = I1i . getWatchedShows ( )
    OOoOo00o = I1i . getUpdatedShows ( )
    OO0O00oooOOO0O = I1i . getMisSeries ( )
    if OO0O00oooOOO0O :
     OO0O00oooOOO0O = list ( OO0O00oooOOO0O . keys ( ) )
     if 97 - 97: OOooooOo00 / I11iiIi11i1I
   with MoriaDB ( ) as ooO0Oo0o00 :
    if 52 - 52: Ii . OooOoo . i1iiIII111 * I11iiIi11i1I - iI1iII1I1I1i
    Ii1I1I1i = 'select tmdb, temporada from enlaces_series where temporada > 0 group by tmdb, temporada'
    if 20 - 20: OooOoo % OOooooOo00 + I1Ii1I1 + OOooooOo00 - oOo0O00
    O0OOoOO0oO0O0 = dict ( )
    for I111i1 , I111 in ooO0Oo0o00 . executeSelect ( Ii1I1I1i ) :
     if I111i1 not in O0OOoOO0oO0O0 :
      O0OOoOO0oO0O0 [ I111i1 ] = list ( )
      if 80 - 80: i1 / i1I . Oo * I1I
     O0OOoOO0oO0O0 [ I111i1 ] . append ( I111 )
     if 3 - 3: Ooo0Ooo + Ooo0Ooo / I1I * Ooo0Ooo
    Ii1I1I1i = 'select tmdb, count(*) from (select tmdb, temporada, episodio from enlaces_series where temporada > 0 group by tmdb, temporada, episodio) GROUP by tmdb;'
    if 65 - 65: Ii - OooOoo * I1I % i1iiIII111 % IIiIIiIi11I1
    if 68 - 68: I1Ii1I1 + oOO - oOO + IiIIii11Ii
    OoO0O = dict ( ooO0Oo0o00 . executeSelect ( Ii1I1I1i ) )
    if 29 - 29: I1I + IIiIIiIi11I1 * i1iiIII111
   for o0ooo0OO00 in oOooo0OOO [ : O0OOooO ] :
    O0OOooO0O0Oo0 , IIIII11 , oOOoOOOO000 , IIIIi , oOoo0 , iI111Ii , IIi , IIiIIiiIIi , iiIi , Ii1Iiii11i1 , oO00oO0O , ooOOoO00OO = o0ooo0OO00 [ : 12 ]
    O0Ooo0oOo0 = None if len ( o0ooo0OO00 ) == 12 else o0ooo0OO00 [ 12 ]
    if 62 - 62: ooOOO % Oo + i1I
    ooOOooO0 = ''
    oOO0 = SetColor ( ' %s' % O0OOooO0O0Oo0 , 'TituloColor' )
    if IIIII11 :
     IiI = SetColor ( '(%s)' % IIIII11 [ : 4 ] , 'DateColor' )
     ooOOooO0 = "%s %s" % ( oOO0 , IiI )
    if IIi :
     ooO0OoOo = SetColor ( '[%s]' % getIdiomas ( IIi ) , 'AudioColor' )
     ooOOooO0 += " %s" % ooO0OoOo
     if 87 - 87: ooo000 - OooOoo + Ii + i1i1i1111I + IiIIii11Ii
    o00 = p3Item . clone (
 label = ooOOooO0 ,
 tvshowtitle = O0OOooO0O0Oo0 ,
 page = 0 ,
 fecha = IIIII11 ,
 plot = oOOoOOOO000 ,
 poster = IIIIi ,
 tmdb = str ( iI111Ii ) ,
 fanart = oOoo0 ,
 mpaa = IIiIIiiIIi if IIiIIiiIIi else '' ,
 content = 'tvshows' ,
 genre = iiIi ,
 trailer = Ii1Iiii11i1 ,
 clearlogo = oO00oO0O ,
 rating = ooOOoO00OO ,
 action = "listado_temporadaS" if str ( iI111Ii ) not in OO0O00oooOOO0O else 'play_mis_serieS'
 )
    if 57 - 57: IIiIIiIi11I1 + I1I / ooOOO % ooOOO % Oo / OOooooOo00
    if O0Ooo0oOo0 and IIiI1iI111 != 'Mis_series' :
     o00 . categoria = O0Ooo0oOo0
     o00 . sub_categoria = 'series_' + O0Ooo0oOo0
     if 95 - 95: i1 / I11iiIi11i1I . i1 / Oo . Ooo0Ooo
    if iI111Ii in O0ooOo : o00 . playCount = 1
    if iI111Ii in OOoOo00o : o00 . newEpisodes = True
    if iI111Ii in O0OOoOO0oO0O0 :
     o00 . p3Seasons = O0OOoOO0oO0O0 . get ( iI111Ii )
     if 43 - 43: Oo - OooOoo * oOO . Ooo0Ooo / IIiIIiIi11I1 * IIiIIiIi11I1
     o00 . p3TotalSeasons = len ( O0OOoOO0oO0O0 . get ( iI111Ii ) )
    if iI111Ii in OoO0O :
     o00 . p3TotalEpisodes = OoO0O . get ( iI111Ii )
     if 84 - 84: i1iiIII111 + oOo0O00
     if 83 - 83: i1i1i1111I
    i1I1 . append ( o00 )
    if 84 - 84: oOO / Ii * Ooo0Ooo / Ii / ooo000
   if len ( oOooo0OOO ) > O0OOooO :
    o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 action = "listado_serieS" ,
 limitItemList = O0OOooO ,
 sql = p3Item . sql )
    if 64 - 64: oOo0O00 * Ii
    if ISESTUARYPALANTIR :
     o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
     o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
     o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
     if 2 - 2: OOooooOo00 % i1iiIII111 . oOo0O00
    if p3Item . isWidget :
     o00 . page = p3Item . page
     o00 . limitItemList = get_setting ( 'limitItemList' )
     if 59 - 59: I11iiIi11i1I % OooOoo - iI1iII1I1I1i % I1I + i1iiIII111 . I1Ii1I1
    i1I1 . append ( o00 )
    if 94 - 94: ooOOO * I1Ii1I1 * i1iiIII111 . oOo0O00
   try :
    if not p3Item . isWidget :
     CACHE . set ( OO0000 , i1I1 , expiration = 10 , pickle_data = True , sub_categoria = IIiI1iI111 )
   except : pass
   if 73 - 73: I1Ii1I1 / ooo000 % I11iiIi11i1I - i1i1i1111I + Oo - I1Ii1I1
  elif p3Item . action != 'buscar3' and not p3Item . isWidget :
   iI1iI = SetColor ( "%s %s" % ( localize ( 30033 ) , localize ( 30500 ) ) , 'LabelColor' )
   xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , iI1iI )
   if 18 - 18: i1 + ooOOO . i1 - iI1iII1I1I1i
 return i1I1
 if 97 - 97: oOo0O00 + i1I % Iii1i
 if 34 - 34: i1 + Oo . oOo0O00 - ooo000 / I11iiIi11i1I * oOo0O00
def listado_temporadaS ( p3Item ) :
 if 89 - 89: oOo0O00
 i1I1 = list ( )
 if 48 - 48: i1 / IIiIIiIi11I1 / iI1iII1I1I1i / OOooooOo00 * IiIIii11Ii
 OO0000 = 'select temporada FROM enlaces_series where tmdb =%s group by temporada ORDER by temporada' % p3Item . tmdb
 if not p3Item . page :
  p3Item . page = 0
  if 54 - 54: IIiIIiIi11I1 % I1I % OOooooOo00 / I11iiIi11i1I . I11iiIi11i1I - IiIIii11Ii
 try :
  i1iI1I = "listado_temporadaS:{0}-{1}" . format ( p3Item . tmdb , p3Item . page )
  if not p3Item . isWidget :
   oO0OO0oO0 = CACHE . get ( i1iI1I )
   if oO0OO0oO0 :
    if 15 - 15: i1I / i1i1i1111I - iI1iII1I1I1i % iI1iII1I1I1i . I11iiIi11i1I / Ooo0Ooo
    return oO0OO0oO0
 except :
  pass
  if 59 - 59: oOO . oOo0O00 - Iii1i * ooOOO - Iii1i
 with MoriaDB ( ) as ooO0Oo0o00 :
  iI = ooO0Oo0o00 . executeSelect ( OO0000 )
  if 45 - 45: oOO . i1i1i1111I . Ii - Ooo0Ooo + OooOoo / Ooo0Ooo
  if iI :
   iI = list ( map ( lambda OOO0ooOO : OOO0ooOO [ 0 ] , iI ) )
   OOOo000o0 = Tmdb ( ) . getSeasons ( p3Item . tmdb )
   if 45 - 45: I1Ii1I1
   ooooOO000O0Oo = ooO0Oo0o00 . getP3TotalEpisodesInSeasons ( p3Item . tmdb )
   if 32 - 32: OooOoo + I1I + Oo * Ii
   for oooo0 in iI :
    I11ii1iIIi1 = OOOo000o0 . get ( oooo0 , { } )
    ooOOooO0 = I11ii1iIIi1 . get ( 'titulo' , 'Temporada %s' % oooo0 if oooo0 > 0 else localize ( 30111 ) )
    if 28 - 28: OooOoo
    with Watched ( ) as I1i :
     o0O000OoOo00o = I1i . getWatchedEpisodes ( p3Item . tmdb , oooo0 )
     if 53 - 53: Ii + i1I % I1Ii1I1
    o00 = p3Item . clone (
 label = SetColor ( ooOOooO0 , 'MenuColor' ) ,
 action = "listado_episodioS" ,
 page = 0 ,
 content = 'seasons' ,
 watchedEpisodes = o0O000OoOo00o ,
 p3TotalEpisodes = ooooOO000O0Oo . get ( oooo0 ) ,
 season = oooo0 )
    if 81 - 81: oOO - Ii - ooo000 + i1iiIII111 % Ooo0Ooo * Ooo0Ooo
    if OOOo000o0 . get ( 'num_total_seasons' ) : o00 . totalSeasons = OOOo000o0 . get ( 'num_total_seasons' )
    if I11ii1iIIi1 . get ( 'plot' ) : o00 . plot = I11ii1iIIi1 . get ( 'plot' )
    if I11ii1iIIi1 . get ( 'poster' ) : o00 . poster = I11ii1iIIi1 . get ( 'poster' )
    if I11ii1iIIi1 . get ( 'air_date' ) : o00 . fecha = I11ii1iIIi1 . get ( 'air_date' )
    if I11ii1iIIi1 . get ( 'num_episodios' ) :
     o00 . totalEpisodes = I11ii1iIIi1 . get ( 'num_episodios' )
     o00 . unWatchedEpisodes = int ( o00 . totalEpisodes ) - int ( o00 . watchedEpisodes )
     if 20 - 20: I1Ii1I1 - IIiIIiIi11I1 % i1
    if I11ii1iIIi1 . get ( 'rating' ) :
     o00 . rating = str ( I11ii1iIIi1 . get ( 'rating' ) )
     if p3Item . rating and '/' in p3Item . rating :
      if 29 - 29: OooOoo * Ii - oOO
      o00 . rating += '/%s' % p3Item . rating . split ( '/' ) [ 1 ]
      if 53 - 53: I11iiIi11i1I % ooo000 / ooOOO / I1I
      if 43 - 43: iI1iII1I1I1i . i1i1i1111I + I1I % ooOOO . OOooooOo00 - OOooooOo00
    o00 . playCount = 0
    try :
     if o00 . totalEpisodes and o00 . totalEpisodes == o00 . watchedEpisodes :
      o00 . playCount = 1
    except : pass
    if 6 - 6: I1I
    i1I1 . append ( o00 )
    if 98 - 98: oOO * IIiIIiIi11I1 / i1iiIII111 / Iii1i + I1I
 iIi111iIi1III = len ( i1I1 )
 O0OOooO = get_setting ( 'limitItemList' )
 i1I1 = i1I1 [ p3Item . page * O0OOooO : O0OOooO + p3Item . page * O0OOooO ]
 if 60 - 60: IiIIii11Ii * ooOOO + I11iiIi11i1I + iI1iII1I1I1i - Oo
 if iIi111iIi1III > O0OOooO + O0OOooO * p3Item . page :
  o00 = p3Item . clone (
 label = SetColor ( localize ( 30031 ) , 'MenuColor' ) ,
 specialSort = "bottom" ,
 page = p3Item . page + 1 ,
 tag = p3Item . tag or p3Item . label ,
 has_content = True ,
 sql = p3Item . sql )
  if ISESTUARYPALANTIR :
   o00 . fanart = "special://home/addons/plugin.video.palantir3/resources/media/fanartmas.png"
   o00 . poster = "special://home/addons/plugin.video.palantir3/resources/media/mas.png"
   o00 . clearlogo = "special://home/addons/plugin.video.palantir3/resources/media/clearlogomas.png"
  i1I1 . append ( o00 )
  if 93 - 93: I1I + i1iiIII111 + Ii - i1I
 if len ( i1I1 ) == 1 and i1I1 [ 0 ] . season == 1 and not ISESTUARYPALANTIR :
  i1I1 = listado_episodioS ( i1I1 [ 0 ] )
  if 29 - 29: Iii1i / oOO + i1I % Ooo0Ooo * OooOoo + I1I
 try :
  if not p3Item . isWidget :
   CACHE . set ( i1iI1I , i1I1 , expiration = 3 , pickle_data = True , sub_categoria = p3Item . sub_categoria )
 except :
  pass
  if 43 - 43: i1I - i1
 return i1I1
 if 64 - 64: i1iiIII111 * IIiIIiIi11I1 + IIiIIiIi11I1 * I1Ii1I1 - IiIIii11Ii
 if 22 - 22: oOO * IIiIIiIi11I1
def listado_episodioS ( p3Item ) :
 if 24 - 24: Ii * Ii % Ii . Ooo0Ooo . OooOoo
 i1I1 = list ( )
 if 81 - 81: OooOoo . Iii1i
 OO0000 = 'select DISTINCT episodio FROM enlaces_series where tmdb = %s and temporada = %s' % ( p3Item . tmdb , p3Item . season )
 if not p3Item . page :
  p3Item . page = 0
  if 28 - 28: IiIIii11Ii - OOooooOo00 . OOooooOo00 * IIiIIiIi11I1 - Iii1i
 with MoriaDB ( ) as ooO0Oo0o00 :
  IiO0 = ooO0Oo0o00 . executeSelect ( OO0000 )
  if 90 - 90: I1Ii1I1 - Oo . OooOoo % I1I / I11iiIi11i1I % ooOOO
 if IiO0 :
  IiO0 = list ( map ( lambda OOO0ooOO : OOO0ooOO [ 0 ] , IiO0 ) )
  OoOOO0o0 = Tmdb ( ) . getEpisodes ( p3Item . tmdb , p3Item . season )
  with Watched ( ) as I1i :
   Ii11iiIII1Ii = I1i . getProgressEpisodes ( p3Item . tmdb , p3Item . season )
   if 82 - 82: I1Ii1I1
  for I1I1i1ii in IiO0 :
   Iii1I1 = OoOOO0o0 . get ( I1I1i1ii , { } )
   ooOOooO0 = Iii1I1 . get ( 'titulo' , 'Episodio %s' % I1I1i1ii )
   if not ISESTUARYPALANTIR :
    ooOOooO0 = '%dx%02d %s' % ( int ( p3Item . season ) , int ( I1I1i1ii ) , ooOOooO0 )
    if 73 - 73: I1Ii1I1 . Iii1i + i1I / ooo000 / oOo0O00 . I1Ii1I1
   o00 = p3Item . clone (
 label = SetColor ( ooOOooO0 , 'MenuColor' ) ,
 action = "selectvideos_" ,
 page = 0 ,
 content = 'episodes' ,
 episode = I1I1i1ii ,
 isPlayable = True
 )
   if 73 - 73: ooo000 % oOO
   if Iii1I1 . get ( 'plot' ) : o00 . plot = Iii1I1 . get ( 'plot' )
   if Iii1I1 . get ( 'still' ) :
    o00 . season_poster = o00 . pop ( 'poster' )
    o00 . still = Iii1I1 . get ( 'still' )
   if Iii1I1 . get ( 'duration' ) : o00 . duration = int ( Iii1I1 . get ( 'duration' ) * 60 )
   if Iii1I1 . get ( 'air_date' ) : o00 . fecha = Iii1I1 . get ( 'air_date' )
   if Iii1I1 . get ( 'rating' ) :
    o00 . rating = str ( Iii1I1 . get ( 'rating' ) )
    if p3Item . rating and '/' in p3Item . rating :
     if 43 - 43: OooOoo * i1i1i1111I * IiIIii11Ii % Ii
     o00 . rating += '/%s' % p3Item . rating . split ( '/' ) [ 1 ]
     if 13 - 13: i1i1i1111I / OOooooOo00 + OOooooOo00 % ooo000
   if Ii11iiIII1Ii and I1I1i1ii in Ii11iiIII1Ii :
    o00 . playCount , o00 . percentPlayed , o00 . totalTime , o00 . lastPlayed = Ii11iiIII1Ii . get ( I1I1i1ii )
    if 100 - 100: ooOOO . IIiIIiIi11I1 - i1
   i1I1 . append ( o00 )
   if 46 - 46: Ooo0Ooo - i1I / ooo000 * OOooooOo00 . oOo0O00
 return i1I1
 if 32 - 32: i1i1i1111I . OooOoo + OooOoo - ooo000 * IiIIii11Ii + Oo
 if 12 - 12: oOo0O00
def OooooO ( qlt ) :
 O0o0O = 100
 qlt = qlt . upper ( )
 if 58 - 58: I11iiIi11i1I % Oo - i1i1i1111I . oOO + i1i1i1111I
 if '1080' in qlt :
  O0o0O = 1.0
 elif '4K' in qlt :
  O0o0O = 2.0
 elif 'DV' in qlt or 'DOLBY' in qlt :
  O0o0O = 3.0
 elif 'HD' in qlt :
  O0o0O = 4.0
 elif '720' in qlt or 'SD' in qlt :
  O0o0O = 5.0
 elif 'IMAX' in qlt :
  O0o0O = 6.0
  if 77 - 77: ooo000 + oOo0O00 . ooo000 - oOO . i1
 if '(R)' in qlt :
  O0o0O += 0.2
  if 74 - 74: ooo000 / OooOoo / oOo0O00 + IIiIIiIi11I1 + OooOoo
 return O0o0O
 if 9 - 9: ooOOO - Ooo0Ooo
 if 39 - 39: IiIIii11Ii . i1 + IIiIIiIi11I1 * OOooooOo00
def selectvideos_ ( p3Item , lista_enlaces_previa = None ) :
 if 79 - 79: Oo - OooOoo
 xbmc . executebuiltin ( 'Dialog.Close(all,true)' )
 OOO = xbmcgui . Dialog ( )
 if 39 - 39: ooo000
 if 43 - 43: i1iiIII111 - i1iiIII111 - OOooooOo00 - oOo0O00 / i1iiIII111
 if '+18' in p3Item . mpaa and get_setting ( 'parental_enabled' ) and not WINDOW . getProperty ( "p3_pass" ) :
  if not xbmcgui . Dialog ( ) . input ( localize ( 30509 ) ,
 defaultt = get_setting ( 'parental_passw' ) ,
 option = xbmcgui . PASSWORD_VERIFY ,
 type = xbmcgui . INPUT_PASSWORD ) :
   if 78 - 78: IIiIIiIi11I1 / I1Ii1I1 + i1iiIII111 - IIiIIiIi11I1 + i1 % i1iiIII111
   xbmcgui . Dialog ( ) . ok ( 'Palantir 3' , localize ( 30519 ) )
   return False
  else :
   WINDOW . setProperty ( "p3_pass" , 'True' )
   if 49 - 49: IiIIii11Ii - i1I . I1I
 if lista_enlaces_previa :
  iI1iII1iI1Ii1 = lista_enlaces_previa
 else :
  if p3Item . content == 'episodes' :
   OO0000 = 'select link,calidad, audio, info from enlaces_series where tmdb=%s and temporada=%s and episodio=%s' % ( p3Item . tmdb , p3Item . season , p3Item . episode )
  else :
   OO0000 = 'SELECT link, calidad, audio, info from enlaces_pelis where tmdb=%s' % p3Item . tmdb
   if 39 - 39: OooOoo + Ooo0Ooo
  with MoriaDB ( ) as ooO0Oo0o00 :
   iI1iII1iI1Ii1 = list ( map ( get_url , ooO0Oo0o00 . executeSelect ( OO0000 ) ) )
   if 49 - 49: iI1iII1I1I1i
 O00O0oO000 = 0
 if len ( iI1iII1iI1Ii1 ) > 1 :
  i11Ii = list ( )
  if 83 - 83: i1I . ooo000 * Ooo0Ooo + Iii1i . Oo
  o000000oOO = list ( )
  if get_setting ( "autoplay_1080" ) :
   oO0OO0oO0 = None
   try :
    oO0OO0oO0 = CACHE . get ( "autoplay_tmdb" )
   except : pass
   if not ( oO0OO0oO0 and oO0OO0oO0 == p3Item . tmdb ) :
    o000000oOO = list ( filter ( lambda OOO0ooOO : OOO0ooOO [ 'quality' ] == '1080p' , iI1iII1iI1Ii1 ) )
    if o000000oOO :
     iI1iII1iI1Ii1 = random . sample ( o000000oOO , len ( o000000oOO ) )
     try :
      CACHE . set ( "autoplay_tmdb" , p3Item . tmdb , 5 )
     except : pass
     if 51 - 51: i1I * I11iiIi11i1I * IiIIii11Ii / Iii1i
  if not o000000oOO :
   with Watched ( ) as I1i :
    oOoo0o = I1i . getServers2Certificate ( )
    if 45 - 45: iI1iII1I1I1i + I11iiIi11i1I / IIiIIiIi11I1
   if not lista_enlaces_previa :
    iI1iII1iI1Ii1 = sorted ( random . sample ( iI1iII1iI1Ii1 , len ( iI1iII1iI1Ii1 ) ) , key = lambda OOO0ooOO : (
 OooooO ( OOO0ooOO [ 'quality' ] ) , - oOoo0o . get ( OOO0ooOO [ 'servidor' ] , 0 ) ) )
    if 45 - 45: iI1iII1I1I1i . iI1iII1I1I1i * i1i1i1111I + oOo0O00
   for iIii1i1iI1IIiI1 in iI1iII1iI1Ii1 :
    ooOOooO0 = "Ver en: %s" % SetColor ( iIii1i1iI1IIiI1 [ 'label' ] , 'ServerColor' )
    if iIii1i1iI1IIiI1 [ 'quality' ] :
     ooOOooO0 += SetColor ( " (%s)" % iIii1i1iI1IIiI1 [ 'quality' ] , 'QltColor' )
    if iIii1i1iI1IIiI1 [ 'audio' ] :
     ooOOooO0 += SetColor ( " [%s]" % getIdiomas ( iIii1i1iI1IIiI1 [ 'audio' ] ) , 'AudioColor' )
    if iIii1i1iI1IIiI1 [ 'info' ] :
     ooOOooO0 += SetColor ( " [%s]" % iIii1i1iI1IIiI1 [ 'info' ] , 'AudioColor' )
     if 24 - 24: Ooo0Ooo * ooo000
    i11Ii . append ( ooOOooO0 )
    if 4 - 4: I1I % i1I - ooo000 - I1I . ooOOO / i1i1i1111I
   iIiIiI1 = p3Item . tvshowtitle + ': ' if p3Item . tvshowtitle else ''
   iIiIiI1 += p3Item . label2 or p3Item . label
   if 63 - 63: i1iiIII111 * ooo000 % ooo000 % Oo % IiIIii11Ii
   O00O0oO000 = OOO . select ( iIiIiI1 , i11Ii )
   if O00O0oO000 == - 1 :
    return False
    if 46 - 46: I1Ii1I1 % oOo0O00 * i1I % i1i1i1111I
 if not p3Play ( p3Item , iI1iII1iI1Ii1 [ O00O0oO000 ] ) and len ( iI1iII1iI1Ii1 ) > 2 :
  del iI1iII1iI1Ii1 [ O00O0oO000 ]
  p3Item . playContext = True
  selectvideos_ ( p3Item , iI1iII1iI1Ii1 . copy ( ) )
  if 87 - 87: Oo + i1
  if 40 - 40: I1Ii1I1
def favoritos ( p3Item ) :
 i1I1 = list ( )
 OO0000 = None
 if 48 - 48: I11iiIi11i1I / Ooo0Ooo - OooOoo % ooo000 % I1Ii1I1 - IIiIIiIi11I1
 with Watched ( ) as I1i :
  iIiiII1iI = I1i . getFavoritos ( 'movies' )
  IiI1 = I1i . getFavoritos ( 'shows' )
  if 65 - 65: Ooo0Ooo - IIiIIiIi11I1 * iI1iII1I1I1i - I1Ii1I1 - i1I . Iii1i
 for IIII11 in menu ( p3Item ) :
  if not IIII11 . action :
   i1I1 . append ( IIII11 )
   continue
  elif not IIII11 . sql :
   continue
   if 99 - 99: I11iiIi11i1I % i1I . ooOOO . oOO
  if 'v_pelis_' in IIII11 . sql :
   oO0oOo00oOoOO = iIiiII1iI
  else :
   oO0oOo00oOoOO = IiI1
   if 45 - 45: iI1iII1I1I1i
  if oO0oOo00oOoOO :
   OO0000 = IIII11 . sql % ',' . join ( oO0oOo00oOoOO )
   with MoriaDB ( ) as ooO0Oo0o00 :
    oOooo0OOO = ooO0Oo0o00 . executeSelect ( OO0000 )
   Iio0 = len ( oOooo0OOO )
  else :
   Iio0 = 0
   if 16 - 16: i1I / IiIIii11Ii
  o00 = IIII11 . clone ( label = IIII11 . label + SetColor ( ' (%s)' % Iio0 , 'MenuColor' ) )
  if Iio0 > 0 :
   o00 . sql = OO0000
  else :
   o00 . action = ''
   if 91 - 91: Ooo0Ooo * OOooooOo00 / I1I / Ii / i1I
  i1I1 . append ( o00 )
  if 45 - 45: OOooooOo00 + I1Ii1I1 % oOo0O00 + i1I + ooOOO
 return i1I1
 if 66 - 66: OooOoo . Ii - OooOoo + OooOoo * OooOoo / i1iiIII111
 if 32 - 32: IIiIIiIi11I1 - i1I / ooOOO * Ooo0Ooo * iI1iII1I1I1i - i1i1i1111I
def Mis_serieS ( p3Item ) :
 p3Item . sub_categoria = 'Mis_series'
 i1I1 = listado_serieS ( p3Item )
 if i1I1 :
  return i1I1
 else :
  return [ P3Item ( label = SetColor ( localize ( 30063 ) , 'LabelColor' ) , content = p3Item . content ) ]
  if 82 - 82: ooo000
  if 66 - 66: IiIIii11Ii + IIiIIiIi11I1 - i1I + i1i1i1111I . iI1iII1I1I1i * IiIIii11Ii
def play_mis_serieS ( p3Item ) :
 if get_setting ( 'NextEpisode' ) :
  play_nextEpisode ( p3Item , 0 )
 return listado_temporadaS ( p3Item )
 if 9 - 9: I1I - I1I - ooOOO - oOo0O00 + i1iiIII111
 if 71 - 71: i1I / i1iiIII111 - Ii * Oo . iI1iII1I1I1i
def play_nextEpisode ( p3Item , timedown , episodioSiguiente = None ) :
 if 3 - 3: I1Ii1I1
 if 57 - 57: Ooo0Ooo . OooOoo / oOo0O00 * I1Ii1I1
 if not episodioSiguiente :
  oOOoO00ooO0O = get_nextEpisode ( p3Item )
  if 93 - 93: Ooo0Ooo / i1i1i1111I * Oo * I1I . i1i1i1111I - OooOoo
  if not oOOoO00ooO0O :
   return
  elif isinstance ( oOOoO00ooO0O , str ) :
   if 76 - 76: iI1iII1I1I1i % Iii1i
   OOO = xbmcgui . Dialog ( )
   OOO . ok ( 'Palantir 3' , oOOoO00ooO0O )
   if get_setting ( 'trakt_enabled' ) :
    Trakt ( ) . addRatings ( 'tvshows' , p3Item . tvshowtitle , p3Item . tmdb , forzado = True )
   return
 else :
  oOOoO00ooO0O = episodioSiguiente
  if 2 - 2: Oo + OooOoo - i1i1i1111I - ooo000 / Oo . Oo
 if p3Item . season and oOOoO00ooO0O . season > p3Item . season :
  if 41 - 41: OooOoo + OooOoo - OooOoo
  if get_setting ( 'trakt_enabled' ) :
   i1iII1i11iI = Tmdb ( ) . getSeasons ( p3Item . tmdb )
   Trakt ( ) . addRatings ( 'seasons' , '{0}: {1}' . format ( p3Item . tvshowtitle , i1iII1i11iI [ p3Item . season ] [ "titulo" ] ) , p3Item . tmdb ,
 p3Item . season , forzado = True )
   if 79 - 79: I1I - Oo . Oo / ooo000 % Ooo0Ooo + i1iiIII111
 OO0000 = 'select * from enlaces_series where tmdb = %s and temporada = %s and episodio = %s' % (
 oOOoO00ooO0O . tmdb , oOOoO00ooO0O . season , oOOoO00ooO0O . episode )
 if 18 - 18: i1i1i1111I + i1
 with MoriaDB ( ) as ooO0Oo0o00 :
  oOooo0OOO = ooO0Oo0o00 . executeSelect ( OO0000 )
 if oOooo0OOO :
  if timedown > 0 :
   oOo000o0OO0o = xbmcgui . DialogProgress ( )
   oOo000o0OO0o . create ( 'Palantir 3' )
   IiiI11i1 = localize ( 30030 ) % ( SetColor ( '%s (%sx%s)' % ( oOOoO00ooO0O . tvshowtitle , oOOoO00ooO0O . season , oOOoO00ooO0O . episode ) , 'TituloColor' ) , '%s' )
   IiI1II1 = 0
   while timedown > 0.5 and not oOo000o0OO0o . iscanceled ( ) :
    IiI1II1 += int ( 100 / 16 )
    oOo000o0OO0o . update ( IiI1II1 , IiiI11i1 % int ( timedown ) )
    xbmc . sleep ( 500 )
    timedown -= 0.5
  else :
   oOo000o0OO0o = None
   if 88 - 88: i1i1i1111I - Iii1i
  if not oOo000o0OO0o or not oOo000o0OO0o . iscanceled ( ) :
   if oOo000o0OO0o : oOo000o0OO0o . close ( )
   if not episodioSiguiente :
    oOOoO00ooO0O = info_nextEpisode ( oOOoO00ooO0O )
    if 76 - 76: Iii1i
    if 34 - 34: Ii . ooo000
    OO0000 = "select count(*) from (select episodio from enlaces_series where tmdb = {0} and temporada = {1} GROUP by episodio)" . format ( oOOoO00ooO0O . tmdb , oOOoO00ooO0O . season )
    with MoriaDB ( ) as ooO0Oo0o00 :
     oOooo0OOO = ooO0Oo0o00 . executeSelect ( OO0000 )
     if oOooo0OOO :
      oOOoO00ooO0O . p3TotalEpisodes = oOooo0OOO [ 0 ] [ 0 ]
      if 65 - 65: I11iiIi11i1I * Ooo0Ooo - ooo000
   selectvideos_ ( oOOoO00ooO0O )
  else :
   oOo000o0OO0o . close ( )
   if 11 - 11: oOO % OooOoo % i1i1i1111I + i1i1i1111I + I1I % OooOoo
 else :
  OOO = xbmcgui . Dialog ( )
  OOO . ok ( 'Palantir 3' , localize ( 30503 ) % (
 int ( oOOoO00ooO0O . season ) , int ( oOOoO00ooO0O . episode ) , oOOoO00ooO0O . tvshowtitle ) )
  if 69 - 69: i1I - i1i1i1111I * oOo0O00
  if 90 - 90: i1 * i1 . Ooo0Ooo . Oo
def p3Play ( p3Item , enlace ) :
 if 59 - 59: Ii % I1Ii1I1 + Iii1i . OooOoo * Iii1i
 I111IiI = ( xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( ) == 0 and p3Item . action == 'play_mis_serieS' )
 OOO = xbmcgui . Dialog ( )
 O0o0O = True
 if 17 - 17: Oo + i1iiIII111 . ooOOO - i1i1i1111I % i1I + i1i1i1111I
 OOoO0oOoOo , IiiI11i1 = Resolver ( enlace ) ( )
 if len ( OOoO0oOoOo ) > 1 :
  if 74 - 74: Oo * I11iiIi11i1I / Ii . i1 . IIiIIiIi11I1 . IiIIii11Ii
  def oo00 ( res ) :
   res = res . lower ( ) . replace ( 'p' , '' ) . strip ( )
   if not res :
    return 0
   ooO0OOo = re . findall ( r'(\d+)\s*k' , res )
   if ooO0OOo :
    return - int ( ooO0OOo [ 0 ] ) * 1000
   elif res . isdigit ( ) :
    return - int ( res )
   else :
    return - 20000
    if 74 - 74: I11iiIi11i1I . Ii * I1Ii1I1
  def iiIIIIi1 ( l ) :
   ooO0O00 = { 'es' : 1 , 'en' : 2 }
   if l == xbmc . getLanguage ( xbmc . ISO_639_1 ) :
    return 0
   else :
    return ooO0O00 . get ( l , 100 )
    if 32 - 32: i1I + I1I - oOO * i1
  iii1I11i = list ( filter ( lambda OOO0ooOO : OOO0ooOO . res == 'Original' , OOoO0oOoOo ) )
  if iii1I11i :
   iii1I11i = sorted ( iii1I11i , key = lambda OOO0ooOO : iiIIIIi1 ( OOO0ooOO . lang ) )
   if 43 - 43: ooo000
  o0oOO = list ( set ( OOoO0oOoOo ) - set ( iii1I11i ) )
  if o0oOO :
   o0oOO = sorted ( o0oOO , key = lambda OOO0ooOO : ( iiIIIIi1 ( OOO0ooOO . lang ) , oo00 ( OOO0ooOO . res ) ) )
   if 8 - 8: ooOOO * i1i1i1111I
  OOoO0oOoOo = iii1I11i + o0oOO
  if 6 - 6: Ooo0Ooo % IiIIii11Ii
  if 59 - 59: i1I . I11iiIi11i1I . ooo000 / i1I . Ii % Ooo0Ooo
  iIII11 = [ ( v . label , v ) for v in OOoO0oOoOo ]
  O0o0O = OOO . select ( "%s" % localize ( 30036 ) , [ i [ 0 ] for i in iIII11 ] )
  if O0o0O == - 1 :
   return True
   if 42 - 42: ooOOO - i1i1i1111I / I1I
  OOoO0oOoOo = OOoO0oOoOo [ O0o0O ]
  if 18 - 18: OooOoo . I1Ii1I1 . iI1iII1I1I1i - Ooo0Ooo + Oo
  if 'api.alldebrid.com/v4' in OOoO0oOoOo . url :
   oOOOooo0O = load_json ( downloadpage ( OOoO0oOoOo . url , headers = { 'User-Agent' : 'Palantir3' } ) . data )
   if oOOOooo0O . get ( "status" , "error" ) == 'success' and oOOOooo0O . get ( 'data' ) . get ( 'link' ) :
    OOoO0oOoOo . url = oOOOooo0O . get ( 'data' ) . get ( 'link' )
   else :
    OOoO0oOoOo . url = ""
    if 91 - 91: Ii % i1iiIII111 / i1i1i1111I / i1 * ooo000 + I11iiIi11i1I
 elif OOoO0oOoOo :
  OOoO0oOoOo = OOoO0oOoOo [ 0 ]
  if 7 - 7: ooOOO + Iii1i / iI1iII1I1I1i - oOO % Oo / iI1iII1I1I1i
 if OOoO0oOoOo and OOoO0oOoOo . url :
  OOoO0oOoOo . url = OOoO0oOoOo . url . replace ( ' ' , '%20' )
  iii = xbmcgui . ListItem ( p3Item . title or p3Item . label )
  setInfoTag ( iii , p3Item )
  if 100 - 100: I1I / ooo000
  if 48 - 48: i1i1i1111I * i1I % i1i1i1111I + i1i1i1111I . iI1iII1I1I1i / OooOoo
  if OOoO0oOoOo . headers :
   p3Item . headers = OOoO0oOoOo . headers
   if 12 - 12: Ii . Ii - I1Ii1I1
  if OOoO0oOoOo . is_InputStream :
   try :
    from inputstreamhelper import Helper
   except :
    OOO . ok ( 'Palantir 3' , localize ( 30037 ) )
    return True
    if 74 - 74: ooo000 * Iii1i - Ooo0Ooo - I1Ii1I1
   iii . setProperty ( 'IsPlayable' , 'true' )
   iii . setPath ( OOoO0oOoOo . url )
   if 46 - 46: ooOOO / ooOOO
   o0 = Helper ( OOoO0oOoOo . type , drm = OOoO0oOoOo . license_type )
   if o0 . check_inputstream ( ) :
    iii . setProperty ( 'inputstream' , o0 . inputstream_addon )
    if 80 - 80: oOo0O00 / Ooo0Ooo - IIiIIiIi11I1 % i1i1i1111I . ooOOO
    iii . setProperty ( 'inputstream.adaptive.manifest_type' , OOoO0oOoOo . type )
    if OOoO0oOoOo . stream_headers :
     iii . setProperty ( 'inputstream.adaptive.stream_headers' , OOoO0oOoOo . stream_headers )
    else :
     iii . setProperty ( 'inputstream.adaptive.stream_headers' ,
 'user-agent=%s' % DEFAULT_HEADERS [ 'User-Agent' ] )
     if 50 - 50: I1I - I11iiIi11i1I
    if OOoO0oOoOo . MimeType :
     iii . setMimeType ( OOoO0oOoOo . MimeType )
     iii . setContentLookup ( False )
     if 32 - 32: Iii1i % IiIIii11Ii - oOO - IiIIii11Ii - I11iiIi11i1I % i1iiIII111
    if OOoO0oOoOo . drm :
     iii . setProperty ( 'inputstream.adaptive.license_type' , OOoO0oOoOo . license_type )
     if OOoO0oOoOo . license_key :
      iii . setProperty ( 'inputstream.adaptive.license_key' , OOoO0oOoOo . license_key + '||R{SSM}|' )
      if 50 - 50: Iii1i / OOooooOo00 + i1
  if type ( p3Item . headers ) == dict :
   if '|' not in OOoO0oOoOo . url :
    OOoO0oOoOo . url += '|'
   from urllib import parse
   p3Item . headers = parse . urlencode ( '&' . join ( [ '%s=%s' % ( k , v ) for k , v in p3Item . headers . items ( ) ] ) )
   if 4 - 4: IIiIIiIi11I1 . IiIIii11Ii % i1I
  OOoO0oOoOo . url += p3Item . headers
  if OOoO0oOoOo . subtitles :
   iii . setSubtitles ( OOoO0oOoOo . subtitles )
   if 30 - 30: i1 . i1
  o0OOo = P3Player ( ) . playStream ( p3Item , OOoO0oOoOo , iii , enlace )
  if 23 - 23: i1iiIII111 % IiIIii11Ii
  if o0OOo [ 'status' ] == 'failed' :
   IiiI11i1 = localize ( 30059 )
   OOO . ok ( 'Palantir 3' , IiiI11i1 )
   logger ( IiiI11i1 )
   O0o0O = False
   if 76 - 76: IiIIii11Ii
  elif o0OOo [ 'status' ] == 'stopped' and o0OOo [ 'current_time' ] <= 180 :
   if 73 - 73: i1I / IIiIIiIi11I1 / oOo0O00 % IIiIIiIi11I1 / Ii
   O0o0O = False
   if 12 - 12: i1
  elif o0OOo [ 'status' ] == 'finished' :
   CACHE . remove ( "autoplay_tmdb" )
   if p3Item . content == 'episodes' :
    if get_setting ( 'NextEpisode' ) :
     if p3Item . season > 0 :
      if 78 - 78: I11iiIi11i1I . IIiIIiIi11I1
      if o0OOo [ 'respuesta_dialog_nextPlay' ] > 0 :
       if 1 - 1: I1I % i1iiIII111 / I1Ii1I1
       play_nextEpisode ( p3Item , 0 , o0OOo [ 'nextEpisode' ] )
       if 42 - 42: Iii1i
      elif o0OOo [ 'respuesta_dialog_nextPlay' ] == 0 :
       if 19 - 19: OooOoo * I11iiIi11i1I . i1i1i1111I + ooo000 + i1I
       play_nextEpisode ( p3Item , 6 , o0OOo [ 'nextEpisode' ] )
       if 13 - 13: i1iiIII111 + I1Ii1I1 / Ooo0Ooo
    elif get_setting ( 'trakt_enabled' ) :
     if 82 - 82: i1iiIII111 * oOO / OOooooOo00 * IiIIii11Ii
     ooOOooO0 = re . sub ( r'\[/?COLOR.*?]' , '' , p3Item . label )
     Trakt ( ) . addRatings ( 'episodes' , '{0}: {1}' . format ( p3Item . tvshowtitle , ooOOooO0 ) , p3Item . tmdb , p3Item . season ,
 p3Item . episode )
   elif p3Item . content == 'movies' and get_setting ( 'trakt_enabled' ) :
    if 29 - 29: I1Ii1I1 % oOo0O00 - oOo0O00 * I1Ii1I1 / Iii1i * i1I
    Trakt ( ) . addRatings ( 'movies' , p3Item . title , p3Item . tmdb )
    if 51 - 51: I1Ii1I1 . i1iiIII111 % i1 % i1I * Oo
  if I111IiI :
   xbmc . executebuiltin ( 'ActivateWindow(home)' )
  else :
   id = xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( )
   if 64 - 64: i1i1i1111I + i1
   O0o0 = 0
   while id == 0 and O0o0 < 50 :
    xbmc . sleep ( 100 )
    id = xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( )
    O0o0 += 1
    if 86 - 86: i1iiIII111 * Iii1i - I1I + i1i1i1111I / ooOOO + Oo
    if 93 - 93: Ii
    if 50 - 50: Ooo0Ooo * Ooo0Ooo / ooo000 - IiIIii11Ii
 else :
  if not IiiI11i1 :
   IiiI11i1 = localize ( 30038 )
   if 70 - 70: IIiIIiIi11I1 . i1 % iI1iII1I1I1i / i1i1i1111I
  OOO . ok ( 'Palantir 3' , IiiI11i1 )
  logger ( IiiI11i1 )
  xbmc . executebuiltin ( 'Dialog.Close(all,true)' )
  O0o0O = False
  if 5 - 5: i1iiIII111 . Oo + i1i1i1111I
 return O0o0O
