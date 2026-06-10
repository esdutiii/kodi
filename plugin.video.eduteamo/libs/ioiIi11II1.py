# -*- coding: utf-8 -*-
__all__ = [ 'searchYou' ]
if 82 - 82: Iii1i
import datetime
import xbmc
import xbmcgui
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
from urllib import parse
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from libs . ioiIIIiII import downloadpage , DEFAULT_HEADERS
from libs . iooooooOoO0 import logger , load_json , CACHE
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
def i1ii1 ( ) :
 ooo0O0oO00 = CACHE . get ( 'instancias_list' )
 if not ooo0O0oO00 or len ( ooo0O0oO00 ) < 3 :
  o00o0OO00O = load_json (
 downloadpage ( 'https://api.invidious.io/instances.json?pretty=1&sort_by=health' ) . data )
  ooo0O0oO00 = [ i [ 1 ] [ 'uri' ] for i in o00o0OO00O if i [ 1 ] . get ( 'type' ) == 'https' ]
  CACHE . set ( 'instancias_list' , ooo0O0oO00 , expiration = datetime . timedelta ( hours = 3 ) )
  if 57 - 57: iiIi1 - ii % Ii * i1i1i1111I / Ii
 return ooo0O0oO00
 if 43 - 43: I11iiIi11i1I
def IIi1i111IiII ( url ) :
 if 25 - 25: Oo
 if 85 - 85: Ooo0Ooo + iI1iII1I1I1i - Ii * Oo
 ooo0O0oO00 = i1ii1 ( )
 if 8 - 8: i1iiIII111 * i1 . I1I / oOO
 for ooOOooO0 in ooo0O0oO00 [ : ] :
  if 13 - 13: oOO
  try :
   iiIII = parse . urljoin ( ooOOooO0 , 'api/v1/%s' % url if not url . startswith ( '/' ) else url [ 1 : ] )
   if 28 - 28: I1Ii1I1 . Iii1i - ooOOO - iI1iII1I1I1i
   if 37 - 37: oOO * IIiIIiIi11I1 * I1I / oOo0O00
   i11i1Iii1I1 = downloadpage ( iiIII , no_decode = True )
   if 68 - 68: I11iiIi11i1I . i1i1i1111I
   if 24 - 24: ii
   if 9 - 9: ooo000 / iiIi1 . iiIi1 / Ii % i1i1i1111I % Ooo0Ooo
   O00Oo = load_json ( i11i1Iii1I1 . data )
   if O00Oo and i11i1Iii1I1 . code == 200 :
    if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
    return O00Oo , ooOOooO0
   else :
    raise ( )
  except :
   ooo0O0oO00 . remove ( ooOOooO0 )
   CACHE . set ( 'instancias_list' , ooo0O0oO00 , expiration = datetime . timedelta ( hours = 3 ) )
   if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
 return { } , None
 if 32 - 32: I1Ii1I1 + oOO - oOo0O00
def searchYou ( query = None ) :
 if not query :
  IiiIii11iII1 = xbmc . Keyboard ( '' , 'Buscar:' )
  IiiIii11iII1 . doModal ( )
  if IiiIii11iII1 . isConfirmed ( ) :
   query = IiiIii11iII1 . getText ( ) . strip ( )
  if not query :
   return False
   if 27 - 27: I1I + ooOOO * IIiIIiIi11I1 % Ii + Ooo0Ooo . ooOOO
 ii1Ii1I = 'search?q=%s&type=video&region=ES' % query . replace ( ' ' , '+' )
 o00o0OO00O , __ = IIi1i111IiII ( ii1Ii1I )
 if o00o0OO00O and isinstance ( o00o0OO00O , list ) :
  oo0 = list ( )
  i11iIii = list ( )
  for OO in o00o0OO00O :
   if OO . get ( 'type' , 'video' ) in [ 'video' , 'shortVideo' ] and ( OO . get ( 'lengthSeconds' ) or OO . get ( 'liveNow' ) ) :
    oo0 . append ( OO . get ( 'title' , 'Sin titulo' ) )
    i11iIii . append ( OO [ 'videoId' ] )
    if 27 - 27: Oo / oOO + ii - OooOoo * I1Ii1I1 / I1Ii1I1
  if oo0 :
   o0OO = 0
   if len ( oo0 ) > 1 :
    o0OO = xbmcgui . Dialog ( ) . select ( query , oo0 )
    if 86 - 86: ooOOO / Oo / Ii - i1 - iI1iII1I1I1i / IiIIii11Ii
   if o0OO > - 1 :
    xbmc . executebuiltin ( 'PlayMedia(plugin://plugin.video.youtube/play/?video_id=%s)' % i11iIii [ o0OO ] )
   return True
   if 40 - 40: Iii1i / I1I
 return False
