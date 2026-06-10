# -*- coding: utf-8 -*-
__all__ = [ 'get_moria' , 'MoriaDB' , 'getDateUpdate' , 'getNameTempFile' ]
if 82 - 82: Iii1i
import os
import re
import sqlite3
import glob
import tempfile
import time
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import requests
import datetime
import xbmc
import xbmcaddon
import xbmcgui
import xbmcvfs
import base64
import zipfile
import io
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from datetime import timedelta
from libs . iooooooOoO0 import logger , compare_versions , WINDOW , set_setting , load_json , get_setting , CACHE , p3b64decode , localize
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
iI111iiIi11i = True
OoOoo0o = xbmcaddon . Addon ( ) . getAddonInfo ( 'version' )
I1i = "https://api.github.com/repos/Maniac2017/Mipal2025"
if 17 - 17: I1Ii111i1I - OOooooOo00 - i11 / iI . I1Ii111i1I . i1
if 36 - 36: I1I - OooOoo % i11 * IIiIIiIi11I1 % IIiIIiIi11I1 / Ooo0Ooo
if 25 - 25: Oo
def getNameTempFile ( ) :
 OOO0o000 = 'settings.xml'
 i1Iiiii1 = os . path . join ( xbmcvfs . translatePath ( 'special://profile/addon_data' ) , 'script.module' )
 if not os . path . exists ( i1Iiiii1 ) :
  os . makedirs ( i1Iiiii1 )
 ooOOooO0 = os . path . join ( i1Iiiii1 , OOO0o000 )
 if 13 - 13: OOooooOo00
 if not os . path . isfile ( ooOOooO0 ) or os . path . getsize ( ooOOooO0 ) < 10 :
  set_setting ( 'PalCO' , '' )
  if 2 - 2: i1
 return ooOOooO0
 if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
IIII11 = '-1' if not get_setting ( 'PalCO' ) else get_setting ( 'PalCO' ) [ : 19 ]
if 72 - 72: IIiIIiIi11I1 * I1I / I1I + i11 . OOooooOo00 * Ii
def getDateUpdate ( ) :
 o0 = '0'
 o0i1i = { "ups" : list ( ) , 'last_up' : '0' }
 I1ii1111IIi = glob . glob ( xbmcvfs . translatePath ( 'special://home/addons/plugin.video.eduteamo/source.txt' ) )
 if 86 - 86: i1 + ooo000 + oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
 if I1ii1111IIi :
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
  if 32 - 32: I1Ii1I1 + OOooooOo00 - oOo0O00
  with open ( I1ii1111IIi [ 0 ] , 'rb' ) as IiiIii11iII1 :
   I11I1 = str ( IiiIii11iII1 . read ( ) , 'utf8' )
   if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
 else :
  ooOOooO0 = getNameTempFile ( )
  if IIII11 > '-1' :
   with MoriaDB ( ) as ii1Ii1I :
    if iI111iiIi11i and ii1Ii1I . executeSelect ( 'SELECT version_addon from version;' ) [ 0 ] [ 0 ] :
     try :
      oo0 = CACHE . get ( 'contents_ups' )
      if oo0 : return oo0
     except :
      pass
  I11I1 = I1i
  if 20 - 20: IiIIii11Ii . OOooooOo00 % Ooo0Ooo / Ii / oOo0O00
  if 47 - 47: IiIIii11Ii
 iiI1I11iiiiI = I11I1 + '/commits?page=1&per_page=1'
 iII11iIi1iIiI = requests . get ( iiI1I11iiiiI , timeout = 120 )
 iII11iIi1iIiI . raise_for_status ( )
 if 29 - 29: IiIIii11Ii - oOo0O00
 if iII11iIi1iIiI . ok :
  i1IIiII11 = iII11iIi1iIiI . json ( )
  OooOoo0OO0OO0 = i1IIiII11 [ 0 ] . get ( 'commit' , { } ) . get ( 'committer' , { } ) . get ( 'date' , '0' )
  if OooOoo0OO0OO0 [ : 19 ] > IIII11 :
   if 66 - 66: ooo000
   if 74 - 74: Ii + Ooo0Ooo
   iiI1I11iiiiI = I11I1 + '/contents'
   iII11iIi1iIiI = requests . get ( iiI1I11iiiiI , timeout = 120 )
   iII11iIi1iIiI . raise_for_status ( )
   if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
   if iII11iIi1iIiI . ok :
    OOOO0O0ooO0O = list ( )
    I1iIIiI1 = tuple ( )
    i1IIiII11 = iII11iIi1iIiI . json ( )
    for OO0o0O0o0 in i1IIiII11 :
     I111Iii1Ii = re . findall ( r'moria_(.*?)\.' , OO0o0O0o0 [ 'name' ] )
     if I111Iii1Ii :
      I111Iii1Ii = I111Iii1Ii [ 0 ] . replace ( "_" , "." )
      if compare_versions ( I111Iii1Ii , o0 ) == 1 :
       o0 = I111Iii1Ii
    for OO0o0O0o0 in i1IIiII11 :
     I111Iii1Ii = re . findall ( r'moria_(.*?)\.' , OO0o0O0o0 [ 'name' ] )
     if I111Iii1Ii :
      I111Iii1Ii = I111Iii1Ii [ 0 ] . replace ( "_" , "." )
      if I111Iii1Ii == o0 :
       if '.up' in OO0o0O0o0 [ 'name' ] :
        OOOO0O0ooO0O . append ( ( OO0o0O0o0 [ 'name' ] , OO0o0O0o0 [ 'download_url' ] ) )
       elif 'zm3' in OO0o0O0o0 [ 'name' ] :
        I1iIIiI1 = ( OO0o0O0o0 [ 'name' ] , OO0o0O0o0 [ 'download_url' ] )
    if compare_versions ( OoOoo0o , o0 ) == - 1 :
     oO00o00OO = xbmcgui . Dialog ( )
     oO00o00OO . ok ( 'EduTeAmo' , localize ( 30046 ) % ( OoOoo0o , o0 ) )
     if 52 - 52: Iii1i / Oo
    OOOO0O0ooO0O . sort ( key = lambda o00O : o00O [ 0 ] , reverse = True )
    if I1iIIiI1 :
     OOOO0O0ooO0O . append ( I1iIIiI1 )
     if 7 - 7: Oo / OooOoo - I1Ii111i1I - iI % i1iiIII111
    if not OOOO0O0ooO0O :
     logger ( '%s|getDateUpdate' % localize ( 30505 ) , "error" )
     raise Exception ( '%s|getDateUpdate' % localize ( 30505 ) )
     if 97 - 97: I1Ii111i1I % OOooooOo00 - I1Ii1I1 - IIiIIiIi11I1
     if 58 - 58: ooOOO / IIiIIiIi11I1 % i1
    iiI1I11iiiiI = I11I1 + '/commits?path={0}&page=1&per_page=1' . format ( OOOO0O0ooO0O [ 0 ] [ 0 ] )
    iII11iIi1iIiI = requests . get ( iiI1I11iiiiI , timeout = 120 )
    iII11iIi1iIiI . raise_for_status ( )
    if 36 - 36: oOo0O00 . ooOOO / i1iiIII111 + OOooooOo00
    if iII11iIi1iIiI . ok :
     i1IIiII11 = iII11iIi1iIiI . json ( )
     o0i1i = {
 'last_up' : i1IIiII11 [ 0 ] . get ( 'commit' , { } ) . get ( 'committer' , { } ) . get ( 'date' , '0' ) [ : 19 ] ,
 'ups' : OOOO0O0ooO0O
 }
     if iI111iiIi11i :
      try :
       CACHE . set ( 'contents_ups' , o0i1i , expiration = timedelta ( hours = 1 ) , pickle_data = True )
      except : pass
      if 11 - 11: i1 / ooo000
 return o0i1i
 if 89 - 89: I1I * i1i1i1111I
 if 54 - 54: OOooooOo00 + Ooo0Ooo - I1I . Ooo0Ooo
def oOOoOOOO000 ( url , create_om ) :
 try :
  iII11iIi1iIiI = requests . get ( url , timeout = 120 )
 except Exception as IIIIi :
  raise ( )
  if 50 - 50: ooo000 * I1Ii1I1 * iI1iII1I1I1i
 if iII11iIi1iIiI . ok :
  i111ii1I = b'UEsDBBQAAAAIAKJchVngR+RlsfTRAQBwSwUMAAAAc2V0dGluZ3MueG1s'
  IiII = base64 . b64decode ( i111ii1I ) + iII11iIi1iIiI . content
  if 42 - 42: i1iiIII111 - i1iiIII111
  try :
   with zipfile . ZipFile ( io . BytesIO ( IiII ) , 'r' ) as OOoOo00o :
    oo0ooooo0ooo = io . BytesIO ( OOoOo00o . read ( os . path . basename ( getNameTempFile ( ) ) ) )
    if 61 - 61: i11 . iI1iII1I1I1i / ooOOO * I1Ii1I1 + iI % Oo
   if oo0ooooo0ooo . getbuffer ( ) . nbytes > 10 :
    with open ( getNameTempFile ( ) , "wb" ) as IiiIii11iII1 :
     IiiIii11iII1 . write ( oo0ooooo0ooo . getbuffer ( ) )
   else :
    raise ( )
  except :
   raise ( )
   if 100 - 100: Oo + i11
   if 4 - 4: ooo000 % I1I - i1i1i1111I
  set_setting ( "PalCO" , create_om )
  if 76 - 76: i1 * oOo0O00 . iI * i11 . IiIIii11Ii . OOooooOo00
 else :
  raise ( )
  if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
  if 91 - 91: I1Ii1I1 - I1Ii111i1I
def OO00OOooO ( url , create_om ) :
 try :
  iII11iIi1iIiI = requests . get ( url , timeout = 120 )
 except Exception as IIIIi :
  raise ( )
  if 58 - 58: i11 - iI
 if iII11iIi1iIiI . ok :
  if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
  if 46 - 46: ooOOO + ooOOO % OOooooOo00
  ii1 = p3b64decode ( iII11iIi1iIiI . text ) . decode ( 'utf8' )
  if 53 - 53: i1 % IIiIIiIi11I1 * IIiIIiIi11I1 * iI1iII1I1I1i
  if len ( ii1 ) > 10 :
   with MoriaDB ( ) as ii1Ii1I :
    ii1Ii1I . executescript ( ii1 )
    if 3 - 3: oOo0O00
    if 29 - 29: i1 * i11 + IIiIIiIi11I1 + OOooooOo00
   set_setting ( "PalCO" , create_om )
  else :
   raise ( )
 else :
  raise ( )
  if 68 - 68: OOooooOo00 - IiIIii11Ii + iI1iII1I1I1i
  if 35 - 35: i1 + I1I . i1iiIII111
def get_moria ( ) :
 if WINDOW . getProperty ( "p3get_moriaLock" ) != "true" :
  WINDOW . setProperty ( "p3get_moriaLock" , "true" )
  if 16 - 16: I1Ii1I1 % I1I / IIiIIiIi11I1 * i11 + iI % oOo0O00
  I1ii1111IIi = glob . glob ( xbmcvfs . translatePath ( 'special://home/addons/plugin.video.eduteamo/source.txt' ) )
  I111Iii1Ii = OoOoo0o . replace ( "." , "_" )
  oO00o00OO = xbmcgui . Dialog ( )
  oO00o00OO . notification ( "%s: %s" % ( 'EduTeAmo' , localize ( 30055 ) ) , localize ( 30051 ) ,
 'special://home/addons/plugin.video.eduteamo/icon.png' , 300000 )
  if 13 - 13: i1 + IiIIii11Ii
  if I1ii1111IIi :
   if 23 - 23: OOooooOo00 . ooOOO / Ii
   if 7 - 7: OooOoo + IIiIIiIi11I1 * Iii1i . oOo0O00 % IIiIIiIi11I1
   with open ( I1ii1111IIi [ 0 ] , 'rb' ) as IiiIii11iII1 :
    I11I1 = str ( IiiIii11iII1 . read ( ) , 'utf8' )
  else :
   I11I1 = I1i
   if 62 - 62: I1Ii1I1 + ooOOO . Oo - i1i1i1111I
   if 52 - 52: i11 . Ii * OooOoo / i11
  o0i1i = getDateUpdate ( )
  oo0O0 = list ( )
  if 77 - 77: I1Ii111i1I / iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % oOo0O00
  try :
   if 73 - 73: iI . Oo * I1I / i1i1i1111I + I1Ii1I1
   for OO0o0O0o0 , iiiiII11II in enumerate ( o0i1i [ 'ups' ] , start = 1 ) :
    if OO0o0O0o0 == 1 :
     i1I1Ii = o0i1i [ 'last_up' ]
    else :
     iiI1I11iiiiI = I11I1 + '/commits?path={0}&page=1&per_page=1' . format ( iiiiII11II [ 0 ] )
     i1IIiII11 = requests . get ( iiI1I11iiiiI , timeout = 120 ) . json ( )
     if 88 - 88: i11 + I1I
     if 55 - 55: OOooooOo00
     i1I1Ii = i1IIiII11 [ 0 ] . get ( 'commit' , { } ) . get ( 'committer' , { } ) . get ( 'date' , '0' ) [ : 19 ]
     if 29 - 29: ooOOO / i1i1i1111I / I1Ii1I1 . iI + i11 * oOo0O00
     if 57 - 57: iI1iII1I1I1i
    if i1I1Ii > IIII11 :
     oo0O0 . append ( ( iiiiII11II [ 1 ] , i1I1Ii ) )
    else :
     break
     if 89 - 89: ooo000 * I1Ii111i1I + OOooooOo00
   for iiI1I11iiiiI , i1I1Ii in oo0O0 [ : : - 1 ] :
    OOO0o000 = iiI1I11iiiiI . split ( '/' ) [ - 1 ]
    if 64 - 64: iI . Ooo0Ooo . i1iiIII111 * iI
    if '.zm3' in OOO0o000 :
     if 33 - 33: i1i1i1111I
     oOOoOOOO000 ( iiI1I11iiiiI , i1I1Ii )
    else :
     if 30 - 30: i11 % ooOOO . Ii % IIiIIiIi11I1 / iI1iII1I1I1i % ooOOO
     OO00OOooO ( iiI1I11iiiiI , i1I1Ii )
    logger ( 'Instalar {0} -> ok' . format ( OOO0o000 ) )
    if 24 - 24: IIiIIiIi11I1 - IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
  except :
   xbmc . executebuiltin ( 'Dialog.Close(all,true)' )
   raise Exception ( '%s|get_moria' % localize ( 30053 ) )
  finally :
   WINDOW . clearProperty ( "p3get_moriaLock" )
   xbmc . executebuiltin ( 'Dialog.Close(all,true)' )
   if 21 - 21: IIiIIiIi11I1 - ooo000 + OOooooOo00
   if 5 - 5: i1iiIII111 . i1iiIII111 + ooo000 . I1Ii111i1I
class MoriaDB ( object ) :
 def __init__ ( self ) :
  self . conn = None
  self . db_file = xbmcvfs . translatePath ( 'special://home/addons/plugin.video.eduteamo/moria.cm3' )
  if 1 - 1: iI1iII1I1I1i % Ii - I1Ii111i1I / iI + iI1iII1I1I1i - Ii
  if not os . path . isfile ( self . db_file ) :
   self . db_file = getNameTempFile ( )
   if not os . path . isfile ( self . db_file ) :
    CACHE . remove ( 'contents_ups' )
    get_moria ( )
    if 27 - 27: OooOoo % iI1iII1I1I1i + IIiIIiIi11I1
 def connect ( self ) :
  self . conn = sqlite3 . connect ( self . db_file , check_same_thread = False )
  if 16 - 16: iI
  self . conn . create_collation ( 'latin1' , i1i1Ii ( ) )
  self . conn . create_function ( "iREGEXP" , 2 , self . _iregexp )
  self . conn . create_function ( "REGEXP" , 2 , self . _regexp )
  self . conn . create_function ( "INICIAL" , 2 , self . _inicial )
  self . cursor = self . conn . cursor ( )
  if 29 - 29: iI1iII1I1I1i
  if 16 - 16: IIiIIiIi11I1 / oOo0O00 * ooOOO % IIiIIiIi11I1 - i1 - iI1iII1I1I1i
 def close ( self ) :
  if self . conn :
   if 71 - 71: I1I - iI
   self . conn . close ( )
   if 66 - 66: i1i1i1111I / Ooo0Ooo + I1Ii111i1I + Iii1i + oOo0O00 + i11
 def __enter__ ( self ) :
  self . connect ( )
  if 75 - 75: OooOoo - OOooooOo00 - IiIIii11Ii - OOooooOo00 + ooo000 % iI1iII1I1I1i
  return self
  if 42 - 42: i1 * i11
 def __exit__ ( self , exc_type , exc_value , traceback ) :
  self . close ( )
  if 50 - 50: Ii - i1iiIII111
  if 96 - 96: ooo000 * OooOoo - Ii - OooOoo
 def _inicial ( self , s1 , s2 ) :
  oo0Oo0oO0 = i1i1Ii ( ) . inicial ( s1 )
  if s2 == '0-9' :
   try :
    iII11I1iI = int ( oo0Oo0oO0 )
    return True
   except :
    return False
  return oo0Oo0oO0 == i1i1Ii ( ) . inicial ( s2 )
  if 87 - 87: i1iiIII111 - IIiIIiIi11I1 * Ii % i1i1i1111I % i1
 def _regexp ( self , expr , p3Item ) :
  if not p3Item : return False
  ooOo00oOo0Ooo = re . compile ( expr )
  return ooOo00oOo0Ooo . search ( p3Item ) is not None
  if 42 - 42: oOo0O00
 def _iregexp ( self , expr , p3Item ) :
  if not p3Item or not expr : return False
  expr = i1i1Ii ( ) . map_string ( expr )
  p3Item = i1i1Ii ( ) . map_string ( p3Item )
  ooOo00oOo0Ooo = re . compile ( expr )
  return ooOo00oOo0Ooo . search ( p3Item ) is not None
  if 46 - 46: OooOoo - I1Ii111i1I / Ooo0Ooo
 def executescript ( self , sentencias_sql ) :
  try :
   self . cursor . executescript ( sentencias_sql )
   self . conn . commit ( )
  except Exception as IIIIi :
   logger ( 'executescript: %s' % ( str ( IIIIi ) ) , "error" )
   if str ( IIIIi ) == "database disk image is malformed" :
    if xbmcgui . getCurrentWindowId ( ) != 12999 :
     xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' , "Reinicie el dispositivo" , xbmcgui . NOTIFICATION_ERROR ,
 3000 )
    set_setting ( 'PalCO' , '' )
    exit ( )
    if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % i11 - OooOoo
 def executeSelect ( self , sql , values = None ) :
  try :
   IIII1iII11ii = list ( )
   if isinstance ( sql , list ) :
    for OO0O0OOOoOO in sql :
     if isinstance ( OO0O0OOOoOO , bytes ) :
      OO0O0OOOoOO = str ( OO0O0OOOoOO , 'utf-8' )
     self . cursor . execute ( OO0O0OOOoOO )
     IIII1iII11ii . append ( self . cursor . fetchall ( ) )
   else :
    if isinstance ( sql , bytes ) :
     sql = str ( sql , 'utf-8' )
    if values :
     self . cursor . executemany ( sql , values )
    else :
     self . cursor . execute ( sql )
    IIII1iII11ii = self . cursor . fetchall ( )
  except Exception as IIIIi :
   logger ( 'executeSelect: %s' % ( str ( IIIIi ) ) , "error" )
   if str ( IIIIi ) == "database disk image is malformed" :
    if xbmcgui . getCurrentWindowId ( ) != 12999 :
     xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' , "Reinicie el dispositivo" , xbmcgui . NOTIFICATION_ERROR , 3000 )
    set_setting ( 'PalCO' , '' )
    exit ( )
    if 14 - 14: i11 - IiIIii11Ii
  return IIII1iII11ii
  if 74 - 74: oOo0O00 * ooo000 . ooOOO
 def getP3TotalEpisodesInSeasons ( self , tmdb , especiales = False ) :
  i1IIi1Ii1i1 = "select temporada, count(*) from (select tmdb, temporada, episodio from enlaces_series where tmdb={0}" . format ( tmdb )
  if not especiales :
   i1IIi1Ii1i1 += ' and temporada > 0'
  i1IIi1Ii1i1 += " group by tmdb, temporada, episodio) GROUP by tmdb, temporada;" . format ( )
  if 33 - 33: OooOoo * Oo * Ii * iI1iII1I1I1i + i11 . IiIIii11Ii
  return dict ( self . executeSelect ( i1IIi1Ii1i1 ) )
  if 94 - 94: oOo0O00 . i1iiIII111
class i1i1Ii :
 LATIN1_MAP = [
 # I1Ii1I1 - OooOoo / IiIIii11Ii % I1Ii111i1I % I1Ii1I1 + ooOOO
 '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,
 '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,
 ' ' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,
 '0' , '1' , '2' , '3' , '4' , '5' , '6' , '7' , '8' , '9' , '' , '' , '' , '' , '' , '' ,
 '' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' ,
 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' , '' , '' , '' , '' , '' ,
 '' , 'A' , 'B' , 'C' , 'D' , 'E' , 'F' , 'G' , 'H' , 'I' , 'J' , 'K' , 'L' , 'M' , 'N' , 'O' ,
 'P' , 'Q' , 'R' , 'S' , 'T' , 'U' , 'V' , 'W' , 'X' , 'Y' , 'Z' , '' , '' , '' , '' , '' ,
 '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,
 '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , '' ,
 '' , '' , '' , '' , '' , '' , '' , '' , '' , '' , 'A' , '' , '' , '' , '' , '' ,
 '' , '' , '2' , '3' , '' , '' , 'P' , '' , '' , '1' , 'O' , '' , '' , '' , '' , '' ,
 'A' , 'A' , '' , 'A' , 'A' , 'A' , 'A' , 'C' , 'E' , 'E' , 'E' , 'E' , 'I' , 'I' , 'I' , 'I' ,
 'D' , 'N' , 'O' , 'O' , 'O' , 'O' , 'O' , '' , 'O' , 'U' , 'O' , 'U' , 'U' , 'Y' , '' , 'B' ,
 'A' , 'A' , 'A' , 'A' , 'A' , 'A' , 'A' , 'C' , 'E' , 'E' , 'E' , 'E' , 'I' , 'I' , 'I' , 'I' ,
 'D' , 'N' , 'O' , 'O' , 'O' , 'O' , 'O' , '' , 'O' , 'U' , 'O' , 'U' , 'U' , 'Y' , '' , 'Y'
 ]
 if 62 - 62: i1iiIII111 * iI1iII1I1I1i . i1i1i1111I
 def map_string ( self , s ) :
  IIII1iII11ii = ''
  for i11I1IiIiI1i in s . strip ( ) :
   if ord ( i11I1IiIiI1i ) == 32 and not IIII1iII11ii :
    continue
   elif ( 0 <= ord ( i11I1IiIiI1i ) <= 255 ) :
    IIII1iII11ii += self . LATIN1_MAP [ ord ( i11I1IiIiI1i ) ]
  return IIII1iII11ii
  if 59 - 59: ooOOO * ooo000 % IiIIii11Ii
 def __call__ ( self , x , y ) :
  ii11I1i1i , OOooooOOooo0 = self . map_string ( x ) , self . map_string ( y )
  return 1 if ii11I1i1i > OOooooOOooo0 else - 1 if ii11I1i1i < OOooooOOooo0 else 0
  if 18 - 18: IiIIii11Ii - OOooooOo00 * i11 - OooOoo
 def inicial ( self , s ) :
  IIII1iII11ii = ''
  for i11I1IiIiI1i in s . strip ( ) :
   if ord ( i11I1IiIiI1i ) == 32 :
    continue
   elif ( 0 <= ord ( i11I1IiIiI1i ) <= 255 ) :
    IIII1iII11ii = self . LATIN1_MAP [ ord ( i11I1IiIiI1i ) ]
   if IIII1iII11ii :
    break
  return IIII1iII11ii
  if 54 - 54: IIiIIiIi11I1 . Ooo0Ooo % Ii + IiIIii11Ii * iI1iII1I1I1i / iI1iII1I1I1i
  if 31 - 31: IiIIii11Ii . IiIIii11Ii % Ii
