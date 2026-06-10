# -*- coding: utf-8 -*-
__all__ = [ 'SimpleCache' ]
if 82 - 82: Iii1i
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
import xbmcvfs
import xbmcgui
import xbmc
import datetime
import time
import sqlite3
import json
import hashlib
import pickle
if 98 - 98: I11iiIi11i1I % oOO
i1ii1 = xbmcgui . Window ( 10000 )
ooo0O0oO00 = False
if 55 - 55: I11II1Ii % iIi
class SimpleCache ( object ) :
 _exit = False
 if 76 - 76: I11II1Ii / Iii1i / Ii . i1i1i1111I / Ii
 _busy_tasks = [ ]
 _database = None
 if 43 - 43: I11iiIi11i1I
 def __init__ ( self ) :
  self . _monitor = xbmc . Monitor ( )
  self . _db_conn = None
  if 31 - 31: IIiIIiIi11I1 * oOO / OooOoo
  self . _log_msg ( "Initialized" )
  if 93 - 93: IIiIIiIi11I1 % IIiIIiIi11I1 / I1I - Oo . Ooo0Ooo
 def close ( self ) :
  self . _exit = True
  if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
  if 52 - 52: Oo + I1I / oOO / OooOoo - I1Ii1I1 - ooOOO
  while self . _busy_tasks and not self . _monitor . abortRequested ( ) :
   self . _monitor . waitForAbort ( 1 )
   if 60 - 60: iI1iII1I1I1i . oOO
  if self . _db_conn is not None :
   try :
    self . _db_conn . close ( )
   except : pass
   self . _db_conn = None
  self . _log_msg ( "Closed" )
  if 13 - 13: oOO
 def __del__ ( self ) :
  if not self . _exit :
   if 2 - 2: i1
   self . close ( )
  del self . _monitor
  if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
 def clear ( self , sub_categoria = None , noWidget = True ) :
  if sub_categoria :
   if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
   self . _log_msg ( "Clear : %s" % sub_categoria )
   iii111 = "delete from simplecache"
   if sub_categoria . lower ( ) != 'all' :
    Iio0 = list ( )
    Iio0 . append ( sub_categoria )
    if sub_categoria == "series_General" :
     Iio0 . append ( "series_Retro" )
     if 11 - 11: iIi . i1i1i1111I
    if not ooo0O0oO00 :
     I1i = list ( )
     for i1111IIi in Iio0 [ : ] :
      oOo00O = hashlib . md5 ( i1111IIi . encode ( 'utf-8' ) )
      I1i . append ( oOo00O . hexdigest ( ) )
     Iio0 = I1i
     if 59 - 59: Iii1i . iIi - I11II1Ii
    iii111 += ' where sub_categoria in (%s)' % str ( Iio0 ) [ 1 : - 1 ]
    if noWidget :
     iii111 += " and not id like 'Widget%'"
     if 13 - 13: oOO
   self . execute_sql ( iii111 )
   if 28 - 28: OooOoo + i1i1i1111I + IiIIii11Ii / I1Ii1I1 + iI1iII1I1I1i
 def actualizarWidgetsByIds ( self , ids ) :
  if not isinstance ( ids , list ) :
   ids = [ ids ]
   if 70 - 70: iIi + I11iiIi11i1I * oOO . Oo + ooOOO / Oo
  iii111 = "delete from simplecache where id in (%s)" % str ( ids ) [ 1 : - 1 ]
  self . execute_sql ( iii111 )
  if 14 - 14: OooOoo % oOo0O00 + I1I % i1iiIII111 * ooOOO / I11iiIi11i1I
  for id in ids :
   i1ii1 . setProperty ( id . replace ( 'Widget' , 'P3Reload' ) , str ( datetime . datetime . now ( ) ) )
   if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
 def actualizarWidgetsByTmdb ( self , content , tmdb ) :
  if 6 - 6: i1iiIII111
  if 99 - 99: ooOOO * I1Ii1I1
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
  if 70 - 70: IiIIii11Ii
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
  if content in [ 'episodes' , 'seasons' , 'tvshows' ] :
   content = 'tvshows'
   if 88 - 88: Oo * IiIIii11Ii
  if not ooo0O0oO00 :
   oOo00O = hashlib . md5 ( content . encode ( 'utf-8' ) )
   content = oOo00O . hexdigest ( )
   if 100 - 100: iIi - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
  iii111 = "select id from simplecache where sub_categoria = '{0}' and ','||inWidget||',' LIKE '%,{1},%';" . format ( content , tmdb )
  I11iIi1i = self . execute_sql ( iii111 ) . fetchall ( )
  if I11iIi1i :
   I11iIi1i = [ t [ 0 ] for t in I11iIi1i ]
   self . actualizarWidgetsByIds ( I11iIi1i )
   if 49 - 49: IIiIIiIi11I1
 def actualizarWidgetsBySub_categoria ( self , sub_categoria ) :
  if not ooo0O0oO00 :
   oOo00O = hashlib . md5 ( sub_categoria . encode ( 'utf-8' ) )
   sub_categoria = oOo00O . hexdigest ( )
   if 29 - 29: IiIIii11Ii - oOo0O00
  iii111 = "select id from simplecache where sub_categoria = '{0}' and id like 'Widget%'" . format ( sub_categoria )
  I11iIi1i = self . execute_sql ( iii111 ) . fetchall ( )
  if I11iIi1i :
   I11iIi1i = [ t [ 0 ] for t in I11iIi1i ]
   self . actualizarWidgetsByIds ( I11iIi1i )
   if 30 - 30: I1I . ooo000
 def remove ( self , endpoint ) :
  if isinstance ( endpoint , str ) and not ooo0O0oO00 and not endpoint . startswith ( 'Widget' ) :
   if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
   if 87 - 87: Iii1i + ooOOO . I11II1Ii / Ii + Oo
   if 77 - 77: i1iiIII111 + iIi - Oo % ooo000
   oOo00O = hashlib . md5 ( endpoint . encode ( 'utf-8' ) )
   endpoint = oOo00O . hexdigest ( )
   if 74 - 74: Ii + Ooo0Ooo
  iIi1I1I = "remove.%s" % endpoint
  self . _busy_tasks . append ( iIi1I1I )
  if 85 - 85: oOo0O00
  if not self . _exit :
   iii111 = 'delete from simplecache where id = "{0}"' . format ( endpoint )
   self . execute_sql ( iii111 )
   self . _log_msg ( 'remove: {0}' . format ( endpoint ) )
   if 65 - 65: Ooo0Ooo * ooo000 + oOo0O00
   if 71 - 71: Ooo0Ooo / ooo000
  self . _busy_tasks . remove ( iIi1I1I )
  if 87 - 87: iIi / oOo0O00 % oOO - oOo0O00 . I1I + Ooo0Ooo
  if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
 def get ( self , endpoint ) :
  I111Iii1Ii = self . _get_timestamp ( datetime . datetime . now ( ) )
  if 26 - 26: Ii . i1
  if 61 - 61: iI1iII1I1I1i . I11II1Ii - ooo000 / ooo000 - i1
  if 19 - 19: Iii1i * Ooo0Ooo . I1Ii1I1 / I11iiIi11i1I * Ii - oOO
  if 32 - 32: iI1iII1I1I1i
  I111II111I1I = None
  if isinstance ( endpoint , str ) and not ooo0O0oO00 and not endpoint . startswith ( 'Widget' ) :
   oOo00O = hashlib . md5 ( endpoint . encode ( 'utf-8' ) )
   endpoint = oOo00O . hexdigest ( )
   if 21 - 21: iI1iII1I1I1i - i1 + ooOOO * IIiIIiIi11I1 % i1 * ooOOO
  self . _log_msg ( 'get: {0}' . format ( endpoint ) )
  I111II111I1I = self . _get_db_cache ( endpoint , I111Iii1Ii )
  if 57 - 57: oOo0O00
  return I111II111I1I
  if 31 - 31: i1iiIII111 + i1i1i1111I % OooOoo
 def set ( self , endpoint , data , expiration = datetime . timedelta ( days = 30 ) , json_data = False , pickle_data = False , sub_categoria = '' , inWidget = '' ) :
  if isinstance ( endpoint , str ) and not ooo0O0oO00 and not endpoint . startswith ( 'Widget' ) :
   if 20 - 20: OooOoo - I1I
   if 9 - 9: i1iiIII111 - iI1iII1I1I1i % Ii - I1I
   if 54 - 54: Iii1i % ooo000 % Iii1i - IiIIii11Ii
   oOo00O = hashlib . md5 ( endpoint . encode ( 'utf-8' ) )
   endpoint = oOo00O . hexdigest ( )
   if 39 - 39: oOO - oOO * i1 % IIiIIiIi11I1
  self . _log_msg ( 'set: {0}' . format ( endpoint ) )
  iIi1I1I = "set.%s" % endpoint
  self . _busy_tasks . append ( iIi1I1I )
  if 29 - 29: IIiIIiIi11I1 - ooo000 . i1iiIII111
  if 86 - 86: I1Ii1I1 - OooOoo - oOO % ooo000 . I11II1Ii % Iii1i
  if not isinstance ( expiration , datetime . timedelta ) :
   expiration = datetime . timedelta ( minutes = expiration )
   if 11 - 11: OooOoo - I1Ii1I1 - ooOOO . i1iiIII111 - iI1iII1I1I1i / i1iiIII111
  OOOoOo = self . _get_timestamp ( datetime . datetime . now ( ) + expiration )
  if 96 - 96: IiIIii11Ii . i1i1i1111I / Ii * i1 . I1I
  if sub_categoria and not ooo0O0oO00 :
   oOo00O = hashlib . md5 ( sub_categoria . encode ( 'utf-8' ) )
   sub_categoria = oOo00O . hexdigest ( )
   if 3 - 3: i1 / IIiIIiIi11I1 / Oo * I1I % iI1iII1I1I1i
  if not self . _exit :
   self . _set_db_cache ( endpoint , OOOoOo , data , json_data , pickle_data , sub_categoria , inWidget )
   if 90 - 90: I1Ii1I1 + iIi % Oo
   if 100 - 100: Oo + I11II1Ii
  self . _busy_tasks . remove ( iIi1I1I )
  if 4 - 4: ooo000 % I1I - i1i1i1111I
 def _get_db_cache ( self , endpoint , cur_time ) :
  I111II111I1I = None
  if 76 - 76: i1 * oOo0O00 . iIi * I11II1Ii . IiIIii11Ii . oOO
  iii111 = "SELECT expires, data, type FROM simplecache WHERE id = ?"
  O00 = self . execute_sql ( iii111 , ( endpoint , ) )
  if O00 :
   O00 = O00 . fetchone ( )
   if O00 and O00 [ 0 ] > cur_time :
    if O00 [ 2 ] == 'pickle' :
     I111II111I1I = pickle . loads ( O00 [ 1 ] )
    elif O00 [ 2 ] == 'json' :
     I111II111I1I = json . loads ( O00 [ 1 ] )
    else :
     I111II111I1I = eval ( O00 [ 1 ] )
  return I111II111I1I
  if 44 - 44: Ooo0Ooo
 def _set_db_cache ( self , endpoint , expires , data , json_data , pickle_data , sub_categoria , inWidget ) :
  iii111 = "INSERT OR REPLACE INTO simplecache( id, expires, data, type, sub_categoria,inWidget) VALUES (?, ?, ?, ?, ?,?)"
  if 63 - 63: Ooo0Ooo
  if pickle_data :
   data = pickle . dumps ( data )
   type = 'pickle'
  elif json_data :
   data = json . dumps ( data )
   type = 'json'
  else :
   data = repr ( data )
   type = ''
   if 47 - 47: OooOoo - I1Ii1I1 - I11iiIi11i1I * ooOOO * oOO % IIiIIiIi11I1
  self . execute_sql ( iii111 , ( endpoint , expires , data , type , sub_categoria , inWidget ) )
  if 60 - 60: I11II1Ii * i1iiIII111 + i1i1i1111I / ooOOO
  if 58 - 58: I11II1Ii - iIi
 def _get_database ( self ) :
  if self . _db_conn is not None :
   try :
    self . _db_conn . execute ( 'SELECT 1' )
    return self . _db_conn
   except :
    self . _db_conn = None
  OO = 'special://profile/addon_data/plugin.video.eduteamo/'
  if 42 - 42: I1I - IiIIii11Ii
  O00O0o = xbmcvfs . translatePath ( "%scache.db" % OO )
  if 67 - 67: i1 . Ooo0Ooo
  if not xbmcvfs . exists ( OO ) :
   xbmcvfs . mkdirs ( OO )
   if 63 - 63: IIiIIiIi11I1 / IIiIIiIi11I1 * Iii1i - oOo0O00 . i1
  try :
   o00OO0 = sqlite3 . connect ( O00O0o , timeout = 30 , isolation_level = None )
   o00OO0 . execute ( 'SELECT * FROM simplecache LIMIT 1' )
   o00OO0 . execute (
 """CREATE TRIGGER IF NOT EXISTS cleanup AFTER INSERT ON simplecache 
                BEGIN DELETE FROM simplecache WHERE expires < strftime('%s','now'); END;""" )
   self . _db_conn = o00OO0
   return o00OO0
  except Exception as O0OO0OOOOoo0o :
   if 41 - 41: oOO
   if xbmcvfs . exists ( O00O0o ) :
    xbmcvfs . delete ( O00O0o )
   try :
    o00OO0 = sqlite3 . connect ( O00O0o , timeout = 30 , isolation_level = None )
    o00OO0 . execute (
 """CREATE TABLE IF NOT EXISTS simplecache(
                    id TEXT UNIQUE, expires INTEGER, data TEXT, type TEXT, sub_categoria TEXT,
                    inWidget TEXT)""" )
    self . _db_conn = o00OO0
    return o00OO0
   except Exception as O0OO0OOOOoo0o :
    self . _log_msg ( "Exception while initializing _database: %s" % str ( O0OO0OOOOoo0o ) , xbmc . LOGWARNING )
    self . close ( )
    del self . _monitor
    return None
    if 98 - 98: I1I / IIiIIiIi11I1 / I11II1Ii + iIi % Oo + I1I
 def execute_sql ( self , query , data = None ) :
  ooOo00o = 0
  if 36 - 36: Ii
  if 71 - 71: OooOoo * IIiIIiIi11I1 * Oo
  if 2 - 2: IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
  with self . _get_database ( ) as iIi111ii :
   while not ooOo00o == 10 and not self . _monitor . abortRequested ( ) :
    if self . _exit :
     return None
    try :
     if isinstance ( data , list ) :
      I111II111I1I = iIi111ii . executemany ( query , data )
     elif data :
      I111II111I1I = iIi111ii . execute ( query , data )
     else :
      I111II111I1I = iIi111ii . execute ( query )
      if 20 - 20: i1i1i1111I + Oo / Ooo0Ooo % iIi % iIi
     if 'delete' in query . lower ( ) or 'update' in query . lower ( ) :
      iIi111ii . commit ( )
      if 29 - 29: iI1iII1I1I1i - oOo0O00 - Ooo0Ooo % I11II1Ii + iIi
     return I111II111I1I
    except sqlite3 . OperationalError as O0OO0OOOOoo0o :
     if "_database is locked" in str ( O0OO0OOOOoo0o ) :
      self . _log_msg ( "retrying DB commit..." )
      ooOo00o += 1
      self . _monitor . waitForAbort ( 0.5 )
     else :
      self . _log_msg ( "_database ERROR ! -- %s" % str ( O0OO0OOOOoo0o ) , xbmc . LOGWARNING )
      break
    except Exception as O0OO0OOOOoo0o :
     self . _log_msg ( "_database ERROR ! -- %s" % str ( O0OO0OOOOoo0o ) , xbmc . LOGWARNING )
     break
     if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
  return None
  if 71 - 71: I1Ii1I1
 @ staticmethod
 def _log_msg ( msg , loglevel = xbmc . LOGINFO ) :
  if ooo0O0oO00 :
   if 1 - 1: iIi - oOo0O00 - i1 . oOo0O00
   xbmc . log ( "Simplecache --> %s" % msg , level = loglevel )
   if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
 @ staticmethod
 def _get_timestamp ( date_time ) :
  return int ( time . mktime ( date_time . timetuple ( ) ) )
if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
if 19 - 19: Ii
if 22 - 22: I11II1Ii % iI1iII1I1I1i + Oo
if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
if 95 - 95: ooOOO % i1i1i1111I . i1
if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
if 43 - 43: IIiIIiIi11I1 * ooo000 + Ii % iI1iII1I1I1i
if 12 - 12: i1iiIII111 + ooo000 . I11iiIi11i1I
if 1 - 1: iI1iII1I1I1i % Ii - I11iiIi11i1I / iIi + iI1iII1I1I1i - Ii
if 27 - 27: OooOoo % iI1iII1I1I1i + IIiIIiIi11I1
if 16 - 16: iIi
if 31 - 31: oOo0O00 / Iii1i % Ooo0Ooo % i1 . iI1iII1I1I1i . Oo
if 83 - 83: oOo0O00 - I11iiIi11i1I
if 91 - 91: IIiIIiIi11I1 - i1 - iI1iII1I1I1i
if 71 - 71: I1I - iIi
if 66 - 66: i1i1i1111I / Ooo0Ooo + I11iiIi11i1I + Iii1i + oOo0O00 + I11II1Ii
if 75 - 75: OooOoo - oOO - IiIIii11Ii - oOO + ooo000 % iI1iII1I1I1i
if 42 - 42: i1 * I11II1Ii
if 50 - 50: Ii - i1iiIII111
if 96 - 96: ooo000 * OooOoo - Ii - OooOoo
if 65 - 65: Oo + Oo - iI1iII1I1I1i % OooOoo . Ooo0Ooo
if 84 - 84: IIiIIiIi11I1 . ooOOO
if 44 - 44: ooo000 * i1i1i1111I * oOO + i1iiIII111 - IIiIIiIi11I1
if 70 - 70: iIi
if 9 - 9: oOo0O00 * i1
if 96 - 96: Ooo0Ooo
if 13 - 13: Oo * I1Ii1I1 - oOo0O00 * Ii . Ii + oOo0O00
if 46 - 46: OooOoo - I11iiIi11i1I / Ooo0Ooo
if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % I11II1Ii - OooOoo
if 30 - 30: ooOOO * ooOOO - Iii1i * iI1iII1I1I1i
if 37 - 37: I1Ii1I1 % iI1iII1I1I1i . I11II1Ii + Ooo0Ooo + ooOOO * iI1iII1I1I1i
if 39 - 39: IIiIIiIi11I1 - Oo
