# -*- coding: utf-8 -*-
__all__ = [ 'load_cookies' , 'downloadpage' , 'DEFAULT_HEADERS' ]
import os
import re
import time
import gzip
import inspect
import ssl
if 82 - 82: Iii1i
from io import BytesIO
from threading import Lock
from decimal import Decimal
from urllib import parse , request , response
from urllib . error import HTTPError
from html . parser import HTMLParser
from http . cookiejar import MozillaCookieJar , Cookie
from http . client import HTTPConnection , HTTPSConnection
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import xbmcvfs
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from libs . iooooooOoO0 import logger , AES
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
iI111iiIi11i = Lock ( )
OoOoo0o = MozillaCookieJar ( )
I1i = xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/cookies.dat' )
if 17 - 17: I1Ii111i1I - OOooooOo00 - i11 / iI . I1Ii111i1I . i1
if 36 - 36: I1I - OooOoo % i11 * IIiIIiIi11I1 % IIiIIiIi11I1 / Ooo0Ooo
DEFAULT_HEADERS = dict ( )
if 25 - 25: Oo
DEFAULT_HEADERS [ "User-Agent" ] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
DEFAULT_HEADERS [ "Accept" ] = "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
DEFAULT_HEADERS [ "Accept-Language" ] = "es-ES,es;q=0.8,en-US;q=0.5,en;q=0.3"
DEFAULT_HEADERS [ "Accept-Charset" ] = "UTF-8"
DEFAULT_HEADERS [ "Accept-Encoding" ] = "gzip"
DEFAULT_HEADERS [ "Upgrade-Insecure-Requests" ] = '1'
if 85 - 85: Ooo0Ooo + iI1iII1I1I1i - Ii * Oo
if 8 - 8: i1iiIII111 * i1 . I1I / OOooooOo00
if 58 - 58: I1Ii1I1 - ooOOO
if hasattr ( ssl , '_create_unverified_context' ) :
 ssl . _create_default_https_context = ssl . _create_unverified_context
 if 60 - 60: iI1iII1I1I1i . OOooooOo00
 if 13 - 13: OOooooOo00
def iiIII ( url ) :
 with iI111iiIi11i :
  if 28 - 28: I1Ii1I1 . Iii1i - ooOOO - iI1iII1I1I1i
  if 37 - 37: OOooooOo00 * IIiIIiIi11I1 * I1I / oOo0O00
  if 28 - 28: i11
  if 95 - 95: i1iiIII111 . Ii . IIiIIiIi11I1 % I1Ii111i1I % I1Ii1I1
  if 8 - 8: I1Ii1I1 . iI . i1 . Oo - i11
  iiI1111IIi1 = getattr ( OoOoo0o , '_cookies' ) . get ( "." + parse . urlparse ( url ) [ 1 ] , { } ) . get ( "/" , { } )
  if 92 - 92: ooOOO / OooOoo - oOo0O00
 if "cf_clearance" not in iiI1111IIi1 :
  return url
  if 59 - 59: Iii1i . iI - i11
 ii1IiIiiII = dict ( )
 ii1IiIiiII [ "User-Agent" ] = DEFAULT_HEADERS [ "User-Agent" ]
 ii1IiIiiII [ "Cookie" ] = "; " . join ( [ "%s=%s" % ( c . name , c . value ) for c in iiI1111IIi1 . values ( ) ] )
 if 21 - 21: oOo0O00 % I1Ii111i1I % OOooooOo00 . oOo0O00
 return url + '|%s' % '&' . join ( [ '%s=%s' % ( k , v ) for k , v in ii1IiIiiII . items ( ) ] )
 if 85 - 85: OooOoo
 if 34 - 34: Oo
def load_cookies ( ) :
 with iI111iiIi11i :
  if 96 - 96: ooOOO / iI + i1iiIII111 / ooOOO / I1Ii111i1I
  if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
  if 6 - 6: i1iiIII111
  if os . path . isfile ( I1i ) :
   try :
    OoOoo0o . load ( I1i , ignore_discard = True )
   except Exception :
    logger ( "El fichero de cookies existe pero es ilegible, se borra" )
    os . remove ( I1i )
    if 99 - 99: ooOOO * I1Ii1I1
    if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
def I1iIiiIIiIi ( ) :
 with iI111iiIi11i :
  if 88 - 88: Oo * IiIIii11Ii
  if 100 - 100: iI - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
  if not os . path . exists ( os . path . dirname ( I1i ) ) :
   os . makedirs ( os . path . dirname ( I1i ) )
  OoOoo0o . save ( I1i , ignore_discard = True )
  if 29 - 29: IiIIii11Ii - oOo0O00
  if 30 - 30: I1I . ooo000
def OOO ( domain ) :
 with iI111iiIi11i :
  OooOoo0OO0OO0 = dict ( ( c . name , c . value ) for c in getattr ( OoOoo0o , '_cookies' ) . get ( domain , { } ) . get ( "/" , { } ) . values ( ) )
  OooOoo0OO0OO0 . update ( dict ( ( c . name , c . value ) for c in getattr ( OoOoo0o , '_cookies' ) . get ( "." + domain , { } ) . get ( "/" , { } ) . values ( ) ) )
 return OooOoo0OO0OO0
 if 66 - 66: ooo000
 if 74 - 74: Ii + Ooo0Ooo
def downloadpage ( url , post = None , headers = None , timeout = None , follow_redirects = True , cookies = True , replace_headers = False ,
 add_referer = False , only_headers = False , bypass_cloudflare = True , bypass_testcookie = True , no_decode = False ,
 method = None ) :
 iIi1I1I = locals ( ) . copy ( )
 if 85 - 85: oOo0O00
 if 65 - 65: Ooo0Ooo * ooo000 + oOo0O00
 if 71 - 71: Ooo0Ooo / ooo000
 if 87 - 87: iI / oOo0O00 % OOooooOo00 - oOo0O00 . I1I + Ooo0Ooo
 if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
 if 85 - 85: oOo0O00
 if 66 - 66: iI * i1i1i1111I + oOo0O00 / I1I / Iii1i / Ii
 if 32 - 32: i1i1i1111I % Ooo0Ooo - i11 * I1I
 if 92 - 92: IIiIIiIi11I1 - i1 - Iii1i / Ooo0Ooo . I1Ii1I1 / I1Ii111i1I
 if 60 - 60: OOooooOo00
 if 32 - 32: iI1iII1I1I1i
 if 18 - 18: I1Ii111i1I * iI % iI1iII1I1I1i + iI
 if 93 - 93: OOooooOo00 - I1Ii1I1 - IIiIIiIi11I1 * ooOOO - i1
 if 82 - 82: IIiIIiIi11I1 % i1 * ooOOO
 if 57 - 57: oOo0O00
 II1iiii = { }
 if 50 - 50: I1I / Ooo0Ooo . i1iiIII111 - iI1iII1I1I1i % Ii - I1I
 if 54 - 54: Iii1i % ooo000 % Iii1i - IiIIii11Ii
 if type ( post ) == dict :
  post = parse . urlencode ( post )
  if 39 - 39: OOooooOo00 - OOooooOo00 * i1 % IIiIIiIi11I1
  if 29 - 29: IIiIIiIi11I1 - ooo000 . i1iiIII111
 url = parse . quote ( url , safe = "%/:=&?~#+!$,;'@()*[]" )
 if 86 - 86: I1Ii1I1 - OooOoo - OOooooOo00 % ooo000 . i11 % Iii1i
 if 11 - 11: OooOoo - I1Ii1I1 - ooOOO . i1iiIII111 - iI1iII1I1I1i / i1iiIII111
 OOOoOo = DEFAULT_HEADERS . copy ( )
 if 96 - 96: IiIIii11Ii . i1i1i1111I / Ii * i1 . I1I
 if 3 - 3: i1 / IIiIIiIi11I1 / Oo * I1I % iI1iII1I1I1i
 if headers is not None :
  if not replace_headers :
   OOOoOo . update ( dict ( headers ) )
  else :
   OOOoOo = dict ( headers )
   if 90 - 90: I1Ii1I1 + iI % Oo
   if 100 - 100: Oo + i11
 if add_referer :
  OOOoOo [ "Referer" ] = "/" . join ( url . split ( "/" ) [ : 3 ] )
  if 4 - 4: ooo000 % I1I - i1i1i1111I
  if 76 - 76: i1 * oOo0O00 . iI * i11 . IiIIii11Ii . OOooooOo00
 O00 = list ( )
 O00 . append ( oOoOO0O0 ( debuglevel = False ) )
 O00 . append ( I111 ( debuglevel = False ) )
 O00 . append ( request . HTTPBasicAuthHandler ( ) )
 if 35 - 35: IIiIIiIi11I1 % Ooo0Ooo - i11 * i1iiIII111 + i1
 if 12 - 12: i1 - i11 - iI
 if not follow_redirects :
  O00 . append ( OO ( ) )
 else :
  O00 . append ( ooOOOO00O ( ) )
  if 72 - 72: I1Ii111i1I
  if 25 - 25: i1
 if type ( cookies ) == dict :
  for Oo0O00OOoo , o0oO00OO in cookies . items ( ) :
   if not type ( o0oO00OO ) == dict :
    o0oO00OO = { 'value' : o0oO00OO }
   O0OO0OOOOoo0o = Cookie (
 version = 0 ,
 name = Oo0O00OOoo ,
 value = o0oO00OO . get ( 'value' , '' ) ,
 port = None ,
 port_specified = False ,
 domain = o0oO00OO . get ( 'domain' , parse . urlparse ( url ) [ 1 ] ) ,
 domain_specified = False ,
 domain_initial_dot = False ,
 path = o0oO00OO . get ( 'path' , '/' ) ,
 path_specified = True ,
 secure = False ,
 expires = o0oO00OO . get ( 'expires' , time . time ( ) + 3600 * 24 ) ,
 discard = True ,
 comment = None ,
 comment_url = None ,
 rest = { 'HttpOnly' : None } ,
 rfc2109 = False
 )
   with iI111iiIi11i :
    OoOoo0o . set_cookie ( O0OO0OOOOoo0o )
    if 41 - 41: OOooooOo00
 if cookies :
  with iI111iiIi11i :
   O00 . append ( request . HTTPCookieProcessor ( OoOoo0o ) )
   if 98 - 98: I1I / IIiIIiIi11I1 / i11 + iI % Oo + I1I
   if 38 - 38: I1Ii1I1 + oOo0O00
 iii1I1 = request . build_opener ( * O00 )
 if 17 - 17: Oo - i11 . IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + Ii
 if 33 - 33: i1i1i1111I . IIiIIiIi11I1 - i11 . Ii
 iIiii1I111i = time . time ( )
 if 100 - 100: iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % i11 + iI
 if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
 iIOooO0O = ooO000oOo0o0 ( url , post . encode ( ) if post else None , OOOoOo , method = method )
 if 20 - 20: i1i1i1111I / I1Ii1I1 . oOo0O00
 try :
  if 77 - 77: oOo0O00 % Oo - oOo0O00 - ooo000 * I1Ii111i1I + OOooooOo00
  O0o = iii1I1 . open ( iIOooO0O , timeout = timeout )
  if 56 - 56: iI + Iii1i + i1 . i11 * Iii1i % ooOOO
  if 74 - 74: I1Ii1I1
 except HTTPError as O0o :
  if 61 - 61: iI1iII1I1I1i * I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
  II1iiii [ "sucess" ] = False
  II1iiii [ "code" ] = O0o . code
  II1iiii [ "error" ] = O0o . __dict__ . get ( "reason" , str ( O0o ) )
  II1iiii [ "headers" ] = dict ( O0o . headers . items ( ) )
  II1iiii [ 'cookies' ] = OOO ( parse . urlparse ( url ) [ 1 ] )
  if not only_headers :
   if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
   II1iiii [ "data" ] = O0o . read ( )
  else :
   II1iiii [ "data" ] = b""
  II1iiii [ "time" ] = time . time ( ) - iIiii1I111i
  II1iiii [ "url" ] = O0o . geturl ( )
  if 43 - 43: IIiIIiIi11I1 * ooo000 + Ii % iI1iII1I1I1i
 except Exception as IIiI1i :
  if 85 - 85: Ooo0Ooo - I1I . IiIIii11Ii % IIiIIiIi11I1 % iI1iII1I1I1i
  II1iiii [ "sucess" ] = False
  II1iiii [ "code" ] = IIiI1i . __dict__ . get ( "errno" , IIiI1i . __dict__ . get ( "code" , str ( IIiI1i ) ) )
  II1iiii [ "error" ] = IIiI1i . __dict__ . get ( "reason" , str ( IIiI1i ) )
  II1iiii [ "headers" ] = { }
  II1iiii [ 'cookies' ] = OOO ( parse . urlparse ( url ) [ 1 ] )
  II1iiii [ "data" ] = b""
  II1iiii [ "time" ] = time . time ( ) - iIiii1I111i
  II1iiii [ "url" ] = url
  if 98 - 98: I1I
 else :
  II1iiii [ "sucess" ] = True
  II1iiii [ "code" ] = O0o . code
  II1iiii [ "error" ] = None
  II1iiii [ "headers" ] = dict ( O0o . headers . items ( ) )
  II1iiii [ 'cookies' ] = OOO ( parse . urlparse ( url ) [ 1 ] )
  if not only_headers :
   if 35 - 35: oOo0O00 / IIiIIiIi11I1 - Iii1i . iI * i1
   II1iiii [ "data" ] = O0o . read ( )
  else :
   II1iiii [ "data" ] = b""
  II1iiii [ "time" ] = time . time ( ) - iIiii1I111i
  II1iiii [ "url" ] = O0o . geturl ( )
  if 91 - 91: OOooooOo00 + Iii1i
 II1iiii [ 'headers' ] = dict ( [ ( k . lower ( ) , v ) for k , v in II1iiii [ 'headers' ] . items ( ) ] )
 if 71 - 71: i1 . iI1iII1I1I1i . OooOoo . IIiIIiIi11I1
 if 92 - 92: ooOOO % IIiIIiIi11I1 - IIiIIiIi11I1
 if 32 - 32: OooOoo % I1I - I1Ii111i1I % OooOoo
 if 9 - 9: i1iiIII111 - ooOOO % Iii1i
 if 37 - 37: i11 + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + OOooooOo00
 if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
 if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
 if 85 - 85: IIiIIiIi11I1 / OooOoo . i11 % Oo + Oo - I1Ii111i1I
 if 59 - 59: OooOoo
 if 53 - 53: i1i1i1111I / ooOOO - iI + ooo000 * i1i1i1111I * i1iiIII111
 if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
 if 81 - 81: i1 + i1i1i1111I * Oo - Oo * I1Ii1I1 - oOo0O00
 if cookies :
  I1iIiiIIiIi ( )
  if 4 - 4: i1iiIII111
  if 8 - 8: IiIIii11Ii + OooOoo - i1
 if II1iiii [ "headers" ] . get ( 'content-encoding' ) == 'gzip' :
  II1iiii [ "data" ] = gzip . GzipFile ( fileobj = BytesIO ( II1iiii [ "data" ] ) ) . read ( )
  if 68 - 68: I1Ii1I1 % I1Ii1I1 / iI . ooo000
  if 80 - 80: IIiIIiIi11I1 / OooOoo % iI1iII1I1I1i / ooOOO * ooOOO - Iii1i
 if not O0ooOO0O0O0O ( II1iiii ) :
  II1iiii [ 'data' ] = str ( II1iiii [ 'data' ] , errors = 'replace' )
  if 59 - 59: ooo000 / Oo - i1
  if not no_decode :
   try :
    II1iiii [ "data" ] = str ( HTMLParser ( ) . unescape ( II1iiii [ 'data' ] ) )
   except :
    import html
    II1iiii [ "data" ] = str ( html . unescape ( II1iiii [ 'data' ] ) )
    if 49 - 49: i11 + oOo0O00 + ooo000 . Iii1i + i11
    if 88 - 88: iI . IIiIIiIi11I1 * i1 + IiIIii11Ii % I1I / iI
  if bypass_testcookie :
   if 'document.cookie="__test="+toHex(slowAES.decrypt(c,2,a,b))+"' in II1iiii [ 'data' ] :
    oo00oOOo0O0o = re . findall ( r'a=toNumbers\("([^"]+)"\)' , II1iiii [ 'data' ] ) [ 0 ] . decode ( "HEX" )
    I1Iiii1 = re . findall ( r'b=toNumbers\("([^"]+)"\)' , II1iiii [ 'data' ] ) [ 0 ] . decode ( "HEX" )
    OOOO = re . findall ( r'c=toNumbers\("([^"]+)"\)' , II1iiii [ 'data' ] ) [ 0 ] . decode ( "HEX" )
    if 96 - 96: iI1iII1I1I1i . OooOoo . i1
    iIi1I1I [ 'bypass_testcookie' ] = False
    if not type ( iIi1I1I [ 'cookies' ] ) == dict :
     iIi1I1I [ 'cookies' ] = { '__test' : AES . new ( oo00oOOo0O0o , AES . MODE_CBC , I1Iiii1 ) . decrypt ( OOOO ) . encode ( "HEX" ) }
    else :
     iIi1I1I [ 'cookies' ] [ '__test' ] = AES . new ( oo00oOOo0O0o , AES . MODE_CBC , I1Iiii1 ) . decrypt ( OOOO ) . encode ( "HEX" )
    II1iiii = downloadpage ( ** iIi1I1I ) . __dict__
    if 87 - 87: ooo000 * IiIIii11Ii % ooo000 . ooOOO . Oo % iI1iII1I1I1i
    if 48 - 48: ooOOO * ooo000 % IiIIii11Ii * i1 . Iii1i - iI
  if bypass_cloudflare :
   II1iiii = oo0O0O0Ooooo ( II1iiii , iIi1I1I )
   if 39 - 39: Oo . OOooooOo00 / ooo000 / iI1iII1I1I1i
   if 48 - 48: OOooooOo00 * i11 - OooOoo * Oo - iI - Ooo0Ooo
 return oOoOOoOo0O00O ( II1iiii )
 if 8 - 8: I1I + iI1iII1I1I1i . I1I . iI
def O0ooOO0O0O0O ( response ) :
 iii1ii1 = [
 'text/html' ,
 'application/json' ,
 'text/javascript'
 ]
 iIi1i = response [ 'headers' ] . get ( 'content-type' , '' )
 if 36 - 36: OOooooOo00 / ooOOO
 if 'charset' in iIi1i :
  iiiiIi1IiiIi = response [ 'headers' ] [ 'content-type' ] . split ( '=' ) [ 1 ]
  if iiiiIi1IiiIi . lower ( ) != 'utf-8' :
   response [ 'data' ] = response [ 'data' ] . decode ( iiiiIi1IiiIi , errors = 'replace' )
  return False
  if 17 - 17: I1Ii111i1I - i1i1i1111I . iI1iII1I1I1i - I1Ii111i1I + Oo % iI1iII1I1I1i
 iIi1i = iIi1i . split ( ' ' ) [ 0 ]
 if iIi1i in iii1ii1 :
  return False
  if 65 - 65: Ii % I1Ii111i1I
 if isinstance ( response [ 'data' ] , bytes ) :
  try :
   response [ 'data' ] . decode ( 'utf8' )
  except UnicodeDecodeError :
   return True
  else :
   return False
   if 39 - 39: Iii1i * IIiIIiIi11I1 . Ooo0Ooo - Oo
 if isinstance ( response [ 'data' ] , str ) :
  return False
  if 63 - 63: i1i1i1111I - i1iiIII111 . OooOoo % OooOoo . iI + i11
 if r'\0' not in response [ 'data' ] :
  return False
  if 71 - 71: ooo000 + I1Ii111i1I % iI1iII1I1I1i + iI % Oo - Oo
 return True
 if 84 - 84: I1I % iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + Ooo0Ooo - Oo
 if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
def oo0O0O0Ooooo ( response , args ) :
 iIi = oo000O0oOO ( response )
 if 86 - 86: Ii * iI + IiIIii11Ii + Oo
 if iIi . is_cloudflare :
  logger ( "cloudflare detectado, esperando %s segundos..." % iIi . wait_time )
  iIiiI1IiI1iI = iIi . get_url ( )
  if 72 - 72: OOooooOo00 % iI . ooOOO * I1Ii1I1 . ooOOO
  Oooo00O = args . copy ( )
  Oooo00O [ 'url' ] = iIiiI1IiI1iI
  Oooo00O [ 'follow_redirects' ] = False
  Oooo00O [ 'headers' ] = { 'Referer' : args [ 'url' ] }
  if not '&s=' in iIiiI1IiI1iI :
   Oooo00O [ 'url' ] = iIiiI1IiI1iI . split ( '?jschl_answer=' ) [ 0 ]
   Oooo00O [ 'post' ] = 'jschl_answer=' + iIiiI1IiI1iI . split ( '?jschl_answer=' ) [ 1 ]
   if 9 - 9: Iii1i * i1i1i1111I
  IIIiII1I = downloadpage ( ** Oooo00O )
  if IIIiII1I . sucess :
   logger ( "cloudflare: AutorizaciÃ³n correcta, descargando pÃ¡gina" )
   args [ 'bypass_cloudflare' ] = False if [ a [ 3 ] for a in inspect . stack ( ) ] . count ( 'retry_if_cloudflare' ) > 2 else True
   return downloadpage ( ** args ) . __dict__
  elif IIIiII1I . code == 403 and IIIiII1I . headers . get ( 'cf-chl-bypass' ) :
   if [ a [ 3 ] for a in inspect . stack ( ) ] . count ( 'retry_if_cloudflare' ) > 2 :
    logger ( "cloudflare: No se ha podido autorizar. Demasiados intentos" )
    return response
    if 100 - 100: i1i1i1111I % OooOoo . iI / i1i1i1111I . ooOOO
   return downloadpage ( ** args ) . __dict__
  else :
   logger ( "cloudflare: No se ha podido autorizar" )
 return response
 if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I1Ii111i1I / IiIIii11Ii . Ooo0Ooo
 if 15 - 15: i11 * I1Ii111i1I - oOo0O00
class I111 ( request . HTTPSHandler ) :
 def __init__ ( self , * args , ** kwargs ) :
  request . HTTPSHandler . __init__ ( self , * args , ** kwargs )
  if 6 - 6: iI - Ii
 def https_open ( self , req ) :
  iiiIII = [
 "ECDHE+AESGCM" ,
 "ECDHE+CHACHA20" ,
 "DHE+AESGCM" ,
 "DHE+CHACHA20" ,
 "ECDH+AESGCM" ,
 "DH+AESGCM" ,
 "ECDH+AES" ,
 "DH+AES" ,
 "RSA+AESGCM" ,
 "RSA+AES" ,
 "!aNULL" ,
 "!eNULL" ,
 "!MD5" ,
 "!ECDHE+SHA" ,
 "!AESCCM" ,
 "!DHE" ,
 "!ARIA"
 ]
  if 16 - 16: IIiIIiIi11I1
  oO00 = ssl . create_default_context ( ssl . Purpose . SERVER_AUTH )
  oO00 . set_ciphers ( ':' . join ( iiiIII ) )
  if hasattr ( oO00 , 'set_alpn_protocols' ) :
   oO00 . set_alpn_protocols ( [ 'http/1.1' ] )
  oO00 . check_hostname = False
  oO00 . verify_mode = ssl . CERT_NONE
  oO00 . options |= ( ssl . OP_NO_SSLv2 | ssl . OP_NO_SSLv3 | ssl . OP_NO_TLSv1 | ssl . OP_NO_TLSv1_1 )
  if 30 - 30: IiIIii11Ii % ooo000 . Ii * Iii1i - iI1iII1I1I1i
  return self . do_open ( HTTPSConnection , req ,
 context = oO00 )
  if 10 - 10: Ooo0Ooo % ooo000 % Ooo0Ooo
  if 38 - 38: ooo000
class HTTPSConnection ( HTTPSConnection ) :
 def connect ( self ) :
  I1I1 = self . host
  if 47 - 47: Ooo0Ooo
  if isinstance ( I1I1 , str ) :
   setattr ( self , 'sock' , self . _create_connection ( ( I1I1 , self . port ) , self . timeout , self . source_address ) )
  else :
   for i1I1iII1 in I1I1 :
    try :
     setattr ( self , 'sock' , self . _create_connection ( ( i1I1iII1 , self . port ) , self . timeout , self . source_address ) )
    except Exception :
     if I1I1 . index ( i1I1iII1 ) == len ( I1I1 ) - 1 :
      raise
    else :
     break
     if 44 - 44: I1Ii1I1 + i1i1i1111I
  if self . _tunnel_host :
   iI11iii = self . _tunnel_host
   self . _tunnel ( )
  else :
   iI11iii = self . host
   if 19 - 19: I1Ii1I1 / OooOoo % i1i1i1111I
  setattr ( self , 'sock' , self . _context . wrap_socket ( self . sock , server_hostname = iI11iii ) )
  if 23 - 23: iI1iII1I1I1i - i11 % i11 - iI * i1iiIII111 + OooOoo
  if 57 - 57: IIiIIiIi11I1
class oOoOO0O0 ( request . HTTPHandler ) :
 def http_open ( self , req ) :
  return self . do_open ( HTTPConnection , req )
  if 57 - 57: ooOOO + Ii % I1Ii111i1I + oOo0O00 . iI1iII1I1I1i - Ii
  if 8 - 8: i1i1i1111I + i1i1i1111I * iI
class HTTPConnection ( HTTPConnection ) :
 def connect ( self ) :
  I1I1 = self . host
  if 77 - 77: iI1iII1I1I1i - OOooooOo00 % Ii * i11 - I1I
  if isinstance ( I1I1 , str ) :
   setattr ( self , 'sock' , self . _create_connection ( ( I1I1 , self . port ) , self . timeout , self . source_address ) )
  else :
   for i1I1iII1 in I1I1 :
    try :
     setattr ( self , 'sock' , self . _create_connection ( ( i1I1iII1 , self . port ) , self . timeout , self . source_address ) )
    except Exception :
     if I1I1 . index ( i1I1iII1 ) == len ( I1I1 ) - 1 :
      raise
    else :
     break
     if 42 - 42: I1Ii111i1I - Ii / Oo - i1i1i1111I + I1Ii111i1I
  if self . _tunnel_host :
   self . _tunnel ( )
   if 83 - 83: i1 . iI1iII1I1I1i
 def _send_request ( self , * args , ** kwargs ) :
  from collections import OrderedDict
  oOOOOO0 = [ "Host" , 'User-Agent' , 'Accept' ]
  if len ( args ) > 3 :
   ii1IiIiiII = args [ 3 ]
  else :
   ii1IiIiiII = kwargs [ 'headers' ]
   if 77 - 77: i1iiIII111
  ii1IiIiiII = OrderedDict ( [ ( k , v ) for k , v in sorted (
 list ( ii1IiIiiII . items ( ) ) ,
 key = lambda I11 : oOOOOO0 . index ( I11 [ 0 ] ) if I11 [ 0 ] in oOOOOO0 else len ( oOOOOO0 ) ,
 ) ] )
  if len ( args ) > 3 :
   args = list ( args )
   args [ 3 ] = ii1IiIiiII
  else :
   kwargs [ 'headers' ] = ii1IiIiiII
  getattr ( HTTPConnection , '_send_request' ) ( self , * args , ** kwargs )
  if 50 - 50: iI + i1iiIII111 / i1i1i1111I
  if 75 - 75: IiIIii11Ii / ooo000 + iI / i1i1i1111I * OOooooOo00 + ooo000
class OO ( request . HTTPRedirectHandler ) :
 def __init__ ( self ) :
  pass
  if 83 - 83: I1Ii111i1I / Ooo0Ooo . I1Ii111i1I
 def http_error_302 ( self , req , fp , code , msg , headers ) :
  oOooOOo = response . addinfourl ( fp , headers , req . get_full_url ( ) )
  oOooOOo . status = code
  oOooOOo . code = code
  return oOooOOo
  if 29 - 29: i1i1i1111I / oOo0O00
 http_error_300 = http_error_302
 http_error_301 = http_error_302
 http_error_303 = http_error_302
 http_error_307 = http_error_302
 if 13 - 13: I1Ii111i1I % i1iiIII111 . OooOoo % ooo000 % OooOoo
 if 21 - 21: iI * I1Ii1I1
class ooOOOO00O ( request . HTTPRedirectHandler ) :
 def __init__ ( self ) :
  pass
  if 93 - 93: Ooo0Ooo . i1 + iI - oOo0O00
 def redirect_request ( self , req , fp , code , msg , headers , newurl ) :
  if 'Authorization' in req . headers :
   req . headers . pop ( 'Authorization' )
  return request . HTTPRedirectHandler . redirect_request ( self , req , fp , code , msg , headers , newurl )
  if 97 - 97: i1 - i1 % IIiIIiIi11I1 + IiIIii11Ii / i11 * iI1iII1I1I1i
  if 60 - 60: I1Ii111i1I - Ooo0Ooo % I1Ii1I1
  if 26 - 26: ooOOO / IIiIIiIi11I1 . OOooooOo00 + I1Ii111i1I . Oo
  if 37 - 37: I1Ii1I1
class oo000O0oOO :
 def __init__ ( self , response ) :
  self . timeout = 5
  self . domain = parse . urlparse ( response [ "url" ] ) [ 1 ]
  self . protocol = parse . urlparse ( response [ "url" ] ) [ 0 ]
  self . response = response
  self . js_data = { }
  self . header_data = { }
  if 35 - 35: OooOoo % i1i1i1111I - iI1iII1I1I1i / IiIIii11Ii
  if not "var s,t,o,p,b,r,e,a,k,i,n,g,f" in response [ "data" ] or "chk_jschl" in response [ "url" ] :
   return
   if 4 - 4: ooo000 . IiIIii11Ii % ooo000 / i1i1i1111I
  try :
   self . js_data [ "auth_url" ] = re . compile ( '<form id="challenge-form" action="([^"]+)"' ) . findall ( response [ "data" ] ) [ 0 ]
   if 48 - 48: i1iiIII111 . Oo
   self . js_data [ "params" ] = { }
   self . js_data [ "params" ] [ "jschl_vc" ] = re . compile ( '<input type="hidden" name="jschl_vc" value="([^"]+)"' ) . findall ( response [ "data" ] ) [ 0 ]
   if 92 - 92: OooOoo + Ii / IIiIIiIi11I1 + OooOoo * IIiIIiIi11I1 * iI1iII1I1I1i
   self . js_data [ "params" ] [ "pass" ] = re . compile ( '<input type="hidden" name="pass" value="([^"]+)"' ) . findall ( response [ "data" ] ) [ 0 ]
   if 79 - 79: i1i1i1111I
   try :
    self . js_data [ "params" ] [ "s" ] = re . compile ( '<input type="hidden" name="s" value="([^"]+)"' ) . findall ( response [ "data" ] ) [ 0 ]
    if 3 - 3: OooOoo / iI % I1Ii111i1I
   except :
    pass
   try :
    self . js_data [ "params" ] [ "r" ] = re . compile ( '<input type="hidden" name="r" value="([^"]+)"' ) . findall ( response [ "data" ] ) [ 0 ]
    if 55 - 55: oOo0O00
   except :
    pass
   Iii , self . js_data [ "value" ] = re . compile ( r'var s,t,o,p,b,r,e,a,k,i,n,g,f[^:]+"([^"]+)":([^\n]+)};' , re . DOTALL ) . findall ( response [ "data" ] ) [ 0 ]
   if 54 - 54: iI1iII1I1I1i % Oo . iI - Iii1i % I1Ii111i1I * i11
   if 31 - 31: oOo0O00 / Iii1i - IiIIii11Ii % i11 / I1Ii1I1 - i1i1i1111I
   if 68 - 68: I1Ii111i1I . I1Ii111i1I % I1Ii111i1I
   if 71 - 71: ooo000
   if 61 - 61: ooo000
   self . js_data [ "old_way" ] = True
   if 'function(p){var p =' in response [ "data" ] :
    OoOoOo000o00O = re . compile ( "k = '([^']+)';" ) . findall ( response [ "data" ] ) [ 0 ]
    i1I1i1I = re . compile ( ' id="%s">(.*?)</div>' % OoOoOo000o00O ) . findall ( response [ "data" ] ) [ 0 ]
    response [ "data" ] = re . sub ( r'function\(p\)\{var p =.*?\}\(\)' , i1I1i1I , response [ "data" ] )
    self . js_data [ "old_way" ] = False
    if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
   if '(function(p){return' in response [ "data" ] :
    oo = re . compile ( r"\(function\(p\)\{return.*?\}\((.*?)\)\)\);" ) . findall ( response [ "data" ] ) [ 0 ]
    oo = int ( self . decode ( oo + '/+(+1)' ) )
    I1I1II = ord ( self . domain [ oo ] )
    response [ "data" ] = re . sub ( r'\(function\(p\)\{return.*?\}\(.*?\)\)\);' , '(' + str ( I1I1II ) + '));' ,
 response [ "data" ] )
    self . js_data [ "old_way" ] = False
    if 5 - 5: oOo0O00 / Ii + i1iiIII111 * Oo + Ooo0Ooo + ooo000
    if 96 - 96: i1iiIII111 - IIiIIiIi11I1 / IIiIIiIi11I1 * IiIIii11Ii
    if 67 - 67: Ooo0Ooo . Ooo0Ooo . iI
   self . js_data [ "op" ] = re . compile ( Iii + r"([\+|\-|\*|\/])=([^;]+)" , re . MULTILINE ) . findall ( response [ "data" ] )
   self . js_data [ "wait" ] = int ( re . compile ( r"\}, ([\d]+)\);" , re . MULTILINE ) . findall ( response [ "data" ] ) [ 0 ] ) / 1000
  except :
   logger ( "Metodo #1 (javascript): NO disponible" )
   self . js_data = { }
   if 24 - 24: i1iiIII111 + i1i1i1111I . oOo0O00 + iI1iII1I1I1i + iI
  if "refresh" in response [ "headers" ] :
   try :
    self . header_data [ "wait" ] = int ( response [ "headers" ] [ "refresh" ] . split ( ";" ) [ 0 ] )
    self . header_data [ "auth_url" ] = response [ "headers" ] [ "refresh" ] . split ( "=" ) [ 1 ] . split ( "?" ) [ 0 ]
    self . header_data [ "params" ] = { }
    self . header_data [ "params" ] [ "pass" ] = response [ "headers" ] [ "refresh" ] . split ( "=" ) [ 2 ]
   except :
    logger ( "Metodo #2 (headers): NO disponible" )
    self . header_data = { }
    if 92 - 92: iI1iII1I1I1i / iI1iII1I1I1i + IiIIii11Ii . iI
 @ property
 def wait_time ( self ) :
  if self . js_data . get ( "wait" , 0 ) :
   return self . js_data [ "wait" ]
  else :
   return self . header_data . get ( "wait" , 0 )
   if 56 - 56: Ii * ooo000 . IiIIii11Ii
 @ property
 def is_cloudflare ( self ) :
  if 66 - 66: I1Ii1I1 * OooOoo . iI1iII1I1I1i % OooOoo . i1 . IiIIii11Ii
  return self . header_data . get ( "wait" , 0 ) > 0 or self . js_data . get ( "wait" , 0 ) > 0
  if 47 - 47: Ii % OooOoo % iI1iII1I1I1i * IiIIii11Ii
  if 48 - 48: i11 . I1Ii111i1I / ooo000 + i1iiIII111
 def get_url ( self ) :
  if 84 - 84: Oo / I1Ii1I1 . IIiIIiIi11I1
  if self . js_data . get ( "wait" , 0 ) :
   oO0Oo0 = self . decode ( self . js_data [ "value" ] )
   if 37 - 37: I1I - OooOoo . iI1iII1I1I1i . iI1iII1I1I1i / i1iiIII111 . IiIIii11Ii
   if 91 - 91: OOooooOo00
   for O000 , IiiiiiIiI1 in self . js_data [ "op" ] :
    if 74 - 74: OOooooOo00 - iI / i1i1i1111I
    if O000 == '+' :
     oO0Oo0 = oO0Oo0 + self . decode ( IiiiiiIiI1 )
    elif O000 == '-' :
     oO0Oo0 = oO0Oo0 - self . decode ( IiiiiiIiI1 )
    elif O000 == '*' :
     oO0Oo0 = oO0Oo0 * self . decode ( IiiiiiIiI1 )
    elif O000 == '/' :
     oO0Oo0 = oO0Oo0 / self . decode ( IiiiiiIiI1 )
     if 9 - 9: IIiIIiIi11I1 - Ooo0Ooo % Ooo0Ooo
     if 74 - 74: OooOoo
   if self . js_data [ "old_way" ] :
    self . js_data [ "params" ] [ "jschl_answer" ] = round ( oO0Oo0 , 10 ) + len ( self . domain )
   else :
    self . js_data [ "params" ] [ "jschl_answer" ] = round ( oO0Oo0 , 10 )
    if 41 - 41: iI1iII1I1I1i . I1Ii111i1I - OooOoo + i11 % OooOoo / Ooo0Ooo
    if 65 - 65: Oo
   II1iiii = "%s://%s%s?%s" % (
 self . protocol , self . domain , self . js_data [ "auth_url" ] , parse . urlencode ( self . js_data [ "params" ] ) )
   if 67 - 67: I1Ii1I1 + I1Ii1I1
   if 42 - 42: IiIIii11Ii / oOo0O00 % ooOOO . OOooooOo00 / OooOoo + oOo0O00
   time . sleep ( self . js_data [ "wait" ] )
   if 79 - 79: I1Ii111i1I . I1Ii1I1 * i11 % I1Ii1I1 / iI
   return II1iiii
   if 93 - 93: i11 + Iii1i . Ii . i11 * ooOOO
   if 84 - 84: Ooo0Ooo % iI
  if self . header_data . get ( "wait" , 0 ) :
   II1iiii = "%s://%s%s?%s" % (
 self . protocol , self . domain , self . header_data [ "auth_url" ] , parse . urlencode ( self . header_data [ "params" ] ) )
   if 82 - 82: IIiIIiIi11I1
   time . sleep ( self . header_data [ "wait" ] )
   if 81 - 81: oOo0O00 + i1 - ooo000 * iI1iII1I1I1i + i1i1i1111I
   return II1iiii
   if 89 - 89: I1Ii1I1
 def decode ( self , data ) :
  data = re . sub ( r"\!\+\[\]" , "1" , data )
  data = re . sub ( r"\!\!\[\]" , "1" , data )
  data = re . sub ( r"\[\]" , "0" , data )
  if 57 - 57: iI1iII1I1I1i - i1iiIII111 / OooOoo % i1iiIII111
  OoO00oOo = data . find ( "/" )
  oOoooo = data [ : OoO00oOo ]
  OOooO00OooO = data [ OoO00oOo + 1 : ]
  if 66 - 66: oOo0O00 - Iii1i - ooo000 . I1Ii111i1I
  o0Ooo = re . compile ( r'\(([0-9\+]+)\)' ) . findall ( oOoooo )
  O00OO0ooOoO = ""
  for OoOo00o in o0Ooo :
   O00OO0ooOoO += str ( eval ( OoOo00o ) )
   if 47 - 47: i1i1i1111I + I1Ii111i1I - OOooooOo00 - iI + iI
  o0Ooo = re . compile ( r'\(([0-9\+]+)\)' ) . findall ( OOooO00OooO )
  iII = ""
  for OoOo00o in o0Ooo :
   if 44 - 44: OooOoo + iI / ooo000 % Ii % Ii
   if 5 - 5: i1iiIII111 * IIiIIiIi11I1
   if '+' in OoOo00o :
    iII += str ( eval ( OoOo00o ) )
   else :
    iII = str ( int ( iII ) + int ( OoOo00o ) )
    if 67 - 67: iI / OooOoo % iI + i1iiIII111
    if 21 - 21: oOo0O00 % i1iiIII111 % I1Ii111i1I % OOooooOo00
  return Decimal ( Decimal ( O00OO0ooOoO ) / Decimal ( iII ) ) . quantize ( Decimal ( '.0000000000000001' ) )
  if 63 - 63: oOo0O00 % Iii1i - i1iiIII111 + Oo * i11 - oOo0O00
  if 93 - 93: Iii1i * IIiIIiIi11I1 % i11 + i1 % Ii * i11
class oOoOOoOo0O00O :
 def __init__ ( self , response ) :
  self . sucess = None
  self . code = None
  self . error = None
  self . headers = None
  self . cookies = None
  self . data = None
  self . time = None
  self . url = None
  self . __dict__ = response
  if 62 - 62: iI % ooo000
  if 19 - 19: Ii / Oo % Iii1i / i1iiIII111 - OooOoo - Ooo0Ooo
class ooO000oOo0o0 ( request . Request ) :
 def __init__ ( self , * args , ** kwargs ) :
  if 'method' in kwargs :
   if kwargs . get ( 'method' ) :
    self . method = kwargs . pop ( 'method' )
   else :
    kwargs . pop ( 'method' )
    if 89 - 89: I1Ii111i1I - iI
  request . Request . __init__ ( self , * args , ** kwargs )
  if 61 - 61: Ii * OooOoo * I1I % i1iiIII111 % IIiIIiIi11I1 * I1Ii111i1I
 def get_method ( self ) :
  OO0O = "POST" if self . data is not None else "GET"
  return getattr ( self , 'method' , OO0O )
  if 70 - 70: ooOOO * IIiIIiIi11I1 % I1I
