# -*- coding: utf-8 -*-
__all__ = [ 'Watched' , 'Trakt' ]
if 82 - 82: Iii1i
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
if 31 - 31: i1I
if 9 - 9: IiI11Ii111 / oOo0O00 / IiIIii11Ii - I11iiIi11i1I - iI1iII1I1I1i
if 16 - 16: i1i1i1111I / i1iiIII111
import os
import re
import sqlite3
import xbmc
import xbmcgui
import xbmcvfs
import requests
import random
if 3 - 3: i1 % i1 % i1i1i1111I . Ii * i1
from threading import Thread
from libs . ioiIIIiII import downloadpage
from libs . iooooooOoO0 import logger , localize , Proxydatetime , set_setting , ISESTUARYeduteamo , load_json , get_setting , CACHE , WINDOW
from libs . ioiiI1II1 import MoriaDB
from libs . ioiiiIIIiI import Tmdb
from libs . ioI1iII import P3Item
if 9 - 9: i1iiIII111
from datetime import timedelta , timezone
from collections import OrderedDict
if 10 - 10: ooOOO / IIiIIiIi11I1 * oOO / i1I / i1I
class Watched ( object ) :
 def __init__ ( self ) :
  self . trakt = None
  self . conn = None
  if 61 - 61: Ooo0Ooo - I1I
  if get_setting ( 'trakt_enabled' ) :
   iIIIII1i111i = Trakt ( )
   if iIIIII1i111i . access_token :
    self . trakt = iIIIII1i111i
    if 8 - 8: i1iiIII111 * i1 . I1I / oOO
  if not os . path . exists ( xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/' ) ) :
   os . makedirs ( xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/' ) , exist_ok = True )
   if 58 - 58: I1Ii1I1 - ooOOO
  self . db_file = xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/watched.db' )
  if 60 - 60: iI1iII1I1I1i . oOO
  if 13 - 13: oOO
 def connect ( self ) :
  if 2 - 2: i1
  self . conn = sqlite3 . connect ( self . db_file , check_same_thread = False )
  self . cursor = self . conn . cursor ( )
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS episodes_watched

                                (tmdb_id INTEGER, 

                                season INTEGER NOT NULL DEFAULT 1, 

                                episode INTEGER NOT NULL DEFAULT 1, 

                                playcount INTEGER DEFAULT 0,

                                progress DOUBLE, 

                                runtime INTEGER, 

                                lastPlayed TEXT, 

                                PRIMARY KEY (tmdb_id, season, episode))''' )
  if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS movies_watched

                                (tmdb_id INTEGER PRIMARY KEY, 

                                playcount	INTEGER DEFAULT 0, 

                                progress	DOUBLE, 

                                runtime INTEGER, 

                                lastPlayed TEXT)''' )
  if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS last_activities_trakt 

                                (type TEXT,

                                action TEXT,

                                date TEXT,

                                PRIMARY KEY(type, action))''' )
  if 20 - 20: I1I + Ii
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS favorites

                                (tmdb_id INTEGER, content TEXT,

                                PRIMARY KEY (tmdb_id, content))''' )
  if 75 - 75: Ii % i1iiIII111 * Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS listas_trakt

                                (user TEXT, 

                                list_id TEXT,

                                label TEXT,

                                plot TEXT, 

                                content TEXT,

                                sort_by TEXT, 

                                sort_how TEXT,

                                PRIMARY KEY (user, list_id, content))''' )
  if 8 - 8: I1Ii1I1 . IiI11Ii111 . i1 . Oo - i1I
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS CERTIFICATE

                                (SERVER	TEXT PRIMARY KEY,

                                 VERIFYPEER INTEGER NOT NULL DEFAULT 1,

                                  PLAYCOUNT INTEGER NOT NULL DEFAULT 0)''' )
  if 32 - 32: Ii % i1i1i1111I % i1I - I11iiIi11i1I % i1iiIII111
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS shows_watched 

                                (tmdb_id INTEGER PRIMARY KEY,

                                num_total_episodios INTEGER NOT NULL DEFAULT 0,

                                completa INTEGER NOT NULL DEFAULT 0,

                                ocultar INTEGER NOT NULL DEFAULT 0,

                                actualizada INTEGER NOT NULL DEFAULT 0

                                )''' )
  if 34 - 34: i1iiIII111 * i1
  self . cursor . execute ( '''CREATE TABLE IF NOT EXISTS views 
 
                                (skin TEXT,
 
                                 content TEXT,
 
                                 view INTEGER NOT NULL DEFAULT 55,
 
                                 PRIMARY KEY(skin, content))''' )
  if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
  self . cursor . execute ( '''CREATE INDEX IF NOT EXISTS idx_lastPlayed ON episodes_watched (lastPlayed)''' )
  if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
  self . cursor . execute ( '''CREATE TRIGGER IF NOT EXISTS agregar_serie_si_no_existe

                AFTER INSERT

                ON episodes_watched

                BEGIN

                    INSERT OR IGNORE INTO shows_watched (tmdb_id)

                    SELECT NEW.tmdb_id

                    WHERE NOT EXISTS (

                        SELECT 1

                        FROM shows_watched

                        WHERE tmdb_id = NEW.tmdb_id

                    );

                END;''' )
  if 32 - 32: I1Ii1I1 + oOO - oOo0O00
  self . cursor . execute ( '''CREATE TRIGGER IF NOT EXISTS eliminar_serie_si_no_quedan_episodios

                                    AFTER DELETE

                                    ON episodes_watched

                                    BEGIN

                                        DELETE FROM shows_watched

                                        WHERE tmdb_id = OLD.tmdb_id

                                        AND NOT EXISTS (

                                            SELECT 1

                                            FROM episodes_watched

                                            WHERE tmdb_id = OLD.tmdb_id

                                        );

                                    END;''' )
  if 79 - 79: Iii1i % oOO * Oo + ooOOO / Oo . oOO
 def close ( self ) :
  if self . conn :
   if 20 - 20: IiI11Ii111 + i1iiIII111 / I1I
   self . conn . close ( )
   if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
 def __enter__ ( self ) :
  self . connect ( )
  if 43 - 43: ooOOO * I1Ii1I1
  return self
  if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
 def __exit__ ( self , exc_type , exc_value , traceback ) :
  self . close ( )
  if 70 - 70: IiIIii11Ii
  if 75 - 75: Ooo0Ooo / Ii / IiIIii11Ii + IiIIii11Ii . I1I
 def clear ( self ) :
  for i1I11ii in [ 'shows_watched' , 'episodes_watched' , 'movies_watched' , 'last_activities_trakt' ] :
   self . cursor . execute ( "DELETE FROM {0}" . format ( i1I11ii ) )
  self . conn . commit ( )
  if 21 - 21: Iii1i - I1Ii1I1
 def _acquire_lock ( self ) :
  count = 0
  while WINDOW . getProperty ( "p3WatchedLock" ) == "true" and count < 25 :
   xbmc . sleep ( 100 )
   count += 1
  WINDOW . setProperty ( "p3WatchedLock" , "true" )
 def _release_lock ( self ) :
  if 30 - 30: I1I . ooo000
  WINDOW . clearProperty ( "p3WatchedLock" )
  if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
 def scrobble ( self , action , p3Item , currentTime , totalTime ) :
  if currentTime < 180 or action not in [ 'start' , 'stop' , 'pause' ] or totalTime <= 0 :
   if 87 - 87: Iii1i + ooOOO . i1I / Ii + Oo
   return
   if 77 - 77: i1iiIII111 + IiI11Ii111 - Oo % ooo000
  I1 = ( currentTime * 100.0 ) / totalTime
  if 56 - 56: I11iiIi11i1I
  self . _acquire_lock ( )
  if p3Item . content == 'episodes' and p3Item . season > - 1 and p3Item . episode > - 1 :
   if 69 - 69: I1I * Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo * oOo0O00
   if self . trakt :
    self . trakt . scrobble ( action , I1 , p3Item . content , p3Item . tmdb , p3Item . season , p3Item . episode )
    if 65 - 65: Ooo0Ooo * ooo000 + oOo0O00
    if 71 - 71: Ooo0Ooo / ooo000
   if action == 'stop' :
    self . cursor . execute (
 "INSERT OR IGNORE INTO episodes_watched (progress, lastplayed, runtime, tmdb_id, season, episode) "
 "VALUES (?,strftime('%Y-%m-%dT%H:%M:%S.000Z','now'),?,?,?,?);" ,
 ( I1 , totalTime , p3Item . tmdb , p3Item . season , p3Item . episode )
 )
    if 87 - 87: IiI11Ii111 / oOo0O00 % oOO - oOo0O00 . I1I + Ooo0Ooo
    if 75 - 75: i1iiIII111 * iI1iII1I1I1i - I1I - IIiIIiIi11I1 % I1Ii1I1
    self . cursor . execute ( 'SELECT num_total_episodios FROM shows_watched where tmdb_id={0}' . format ( p3Item . tmdb ) )
    I111Iii1Ii = self . cursor . fetchall ( )
    if I111Iii1Ii :
     I111Iii1Ii = I111Iii1Ii [ 0 ] [ 0 ]
    else :
     I111Iii1Ii = Tmdb ( ) . getSeasons ( p3Item . tmdb ) . get ( 'num_total_episodios' )
     self . cursor . execute ( 'INSERT OR REPLACE INTO shows_watched VALUES(?,?,0,0,0);' ,
 ( p3Item . tmdb , I111Iii1Ii ) )
     if 26 - 26: Ii . i1
    if I1 < 80.0 :
     self . cursor . execute (
 "UPDATE episodes_watched SET progress = ?, runtime = ?, "
 "lastplayed = strftime('%Y-%m-%dT%H:%M:%S.000Z','now') "
 "where tmdb_id = ? and season = ? and episode = ?" ,
 ( I1 , totalTime , p3Item . tmdb , p3Item . season , p3Item . episode )
 )
    else :
     self . cursor . execute (
 "UPDATE episodes_watched SET progress =0, runtime = ?, playcount = playcount + 1,"
 " lastplayed = strftime('%Y-%m-%dT%H:%M:%S.000Z','now') where"
 " tmdb_id = ? and season = ? and episode = ?" ,
 ( totalTime , p3Item . tmdb , p3Item . season , p3Item . episode )
 )
     if 61 - 61: iI1iII1I1I1i . i1I - ooo000 / ooo000 - i1
     self . cursor . execute (
 'SELECT count(*) FROM episodes_watched WHERE tmdb_id = {0} and season > 0' . format ( p3Item . tmdb ) )
     iIi = self . cursor . fetchall ( ) [ 0 ] [ 0 ]
     if 23 - 23: iI1iII1I1I1i % oOO . Oo / OooOoo - I11iiIi11i1I - oOO
     if I111Iii1Ii and iIi == I111Iii1Ii :
      self . cursor . execute (
 'UPDATE shows_watched SET completa= 1, ocultar=0, actualizada = 0 where tmdb_id={0};' . format ( p3Item . tmdb ) )
     elif I111Iii1Ii and iIi < I111Iii1Ii :
      self . cursor . execute (
 'UPDATE shows_watched SET completa= 0, ocultar=0 where tmdb_id={0};' . format ( p3Item . tmdb ) )
      self . setShowUpdated ( lock = True )
     else :
      I111Iii1Ii = Tmdb ( ) . getSeasons ( p3Item . tmdb ) . get ( 'num_total_episodios' )
      if I111Iii1Ii and iIi == I111Iii1Ii :
       self . cursor . execute (
 'UPDATE shows_watched SET completa= 1, ocultar=0, actualizada = 0, num_total_episodios={0} where tmdb_id={1};' . format ( I111Iii1Ii , p3Item . tmdb ) )
      else :
       self . cursor . execute (
 'UPDATE shows_watched SET completa= 0, ocultar=0, num_total_episodios={0} where tmdb_id={1};' . format ( I111Iii1Ii , p3Item . tmdb ) )
       self . setShowUpdated ( lock = True )
       if 77 - 77: IiI11Ii111 - I11iiIi11i1I * Ooo0Ooo
    self . conn . commit ( )
    if 71 - 71: IIiIIiIi11I1 / ooOOO - ooOOO / I11iiIi11i1I
    if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + oOO
    CACHE . remove ( "listado_episodioS:{0}_{1}" . format ( p3Item . tmdb , p3Item . season ) )
    if 11 - 11: i1 / ooo000
  elif p3Item . content == 'movies' :
   if 89 - 89: I1I * i1i1i1111I
   if self . trakt :
    self . trakt . scrobble ( action , I1 , p3Item . content , p3Item . tmdb )
    if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
    if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
   if action == 'stop' :
    self . cursor . execute (
 "INSERT OR IGNORE INTO movies_watched(progress, lastplayed, runtime, tmdb_id) "
 "VALUES (?,strftime('%Y-%m-%dT%H:%M:%S.000Z','now'),?,?);" ,
 ( I1 , totalTime , p3Item . tmdb ) )
    if 54 - 54: oOO * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
    if I1 < 80.0 :
     self . cursor . execute (
 "UPDATE movies_watched SET progress = ?, lastplayed = strftime('%Y-%m-%dT%H:%M:%S.000Z','now'), "
 "runtime = ? where tmdb_id = ?" , ( I1 , totalTime , p3Item . tmdb ) )
     if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - IiI11Ii111
    else :
     self . cursor . execute (
 "UPDATE movies_watched SET progress = 0.0, playcount = playcount + 1, runtime = ?  where tmdb_id = ?" ,
 ( totalTime , p3Item . tmdb ) )
    self . conn . commit ( )
    if 69 - 69: ooo000
  self . _release_lock ( )
  if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
 def markAsWatched ( self , content , tmdb , season = None , episode = None ) :
  def OOOOO ( list_tmdb_season_episode ) :
   if 36 - 36: i1i1i1111I + Iii1i - oOO * Ii
   if self . trakt :
    for oo0ooooo0ooo in list_tmdb_season_episode :
     ooO0OOo0000 = Thread ( target = self . trakt . markAsWatched ,
 args = [ 'episodes' ,
 oo0ooooo0ooo [ 0 ] ,
 oo0ooooo0ooo [ 1 ] ,
 oo0ooooo0ooo [ 2 ] ] )
     ooO0OOo0000 . daemon = True
     ooO0OOo0000 . start ( )
     if 15 - 15: Oo + i1I
   self . cursor . executemany (
 "INSERT OR IGNORE INTO episodes_watched (progress, lastplayed, runtime, tmdb_id, season, episode) "
 "VALUES (0.0,strftime('%Y-%m-%dT%H:%M:%fZ','now'),0,?,?,?);" , list_tmdb_season_episode
 )
   self . cursor . executemany (
 "UPDATE episodes_watched SET progress =0.0, playcount = playcount + 1  where"
 " tmdb_id = ? and season = ? and episode = ?" , list_tmdb_season_episode
 )
   if 4 - 4: ooo000 % I1I - i1i1i1111I
   if 76 - 76: i1 * oOo0O00 . IiI11Ii111 * i1I . IiIIii11Ii . oOO
   if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
   I111 = Tmdb ( ) . getSeasons ( tmdb )
   I111Iii1Ii = I111 [ 'num_total_episodios' ]
   self . cursor . execute ( 'SELECT count(*) FROM episodes_watched WHERE tmdb_id = {0} and season > 0' . format ( tmdb ) )
   iIi = self . cursor . fetchall ( ) [ 0 ] [ 0 ]
   OO00OOooO = 1 if content == 'tvshows' or ( I111Iii1Ii and iIi >= I111Iii1Ii ) else 0
   self . cursor . execute ( 'INSERT OR REPLACE INTO shows_watched  VALUES(?,?,?,0,0);' ,
 ( tmdb , I111Iii1Ii , OO00OOooO ) )
   self . conn . commit ( )
   if 58 - 58: i1I - IiI11Ii111
   if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
   if 46 - 46: ooOOO + ooOOO % oOO
  self . _acquire_lock ( )
  if content == 'movies' :
   if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
   if self . trakt :
    self . trakt . markAsWatched ( content , tmdb )
    if 58 - 58: i1i1i1111I
    if 38 - 38: i1 - oOo0O00
   self . cursor . execute (
 "INSERT OR IGNORE INTO movies_watched(progress, lastplayed, runtime, tmdb_id) "
 "VALUES (0.0,strftime('%Y-%m-%dT%H:%M:%S.000Z','now'),0,?);" , ( tmdb , )
 )
   self . cursor . execute (
 "UPDATE movies_watched SET progress = 0.0, playcount = playcount + 1  where tmdb_id = ?" , ( tmdb , )
 )
   self . conn . commit ( )
   if 85 - 85: IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO * i1iiIII111
  elif content == 'tvshows' :
   OOOoo0 = list ( )
   with MoriaDB ( ) as I11 :
    i1II1 = I11 . getP3TotalEpisodesInSeasons ( tmdb )
    if 76 - 76: oOo0O00 % I1I . i1 + I1Ii1I1 + oOo0O00
   for season , iii1I1 in i1II1 . items ( ) :
    OOOoo0 . extend ( [ ( tmdb , season , ep ) for ep in range ( 1 , iii1I1 + 1 ) ] )
   OOOOO ( OOOoo0 )
   if 17 - 17: Oo - i1I . IIiIIiIi11I1 + iI1iII1I1I1i - I1Ii1I1 + Ii
   if 33 - 33: i1i1i1111I . IIiIIiIi11I1 - i1I . Ii
  elif content == 'seasons' and season != None :
   with MoriaDB ( ) as I11 :
    i1II1 = I11 . getP3TotalEpisodesInSeasons ( tmdb , especiales = True )
   iii1I1 = i1II1 . get ( int ( season ) , 0 )
   OOOoo0 = [ ( tmdb , season , ep ) for ep in range ( 1 , iii1I1 + 1 ) ]
   OOOOO ( OOOoo0 )
   if 20 - 20: oOo0O00 % i1i1i1111I
   if 32 - 32: oOO
  elif content == 'episodes' and season != None and episode != None :
   OOOoo0 = [ ( tmdb , season , episode ) ]
   OOOOO ( OOOoo0 )
   if 98 - 98: IiI11Ii111 % i1 % ooo000 % iI1iII1I1I1i
   if 57 - 57: Ooo0Ooo % i1I + IiI11Ii111
  self . _release_lock ( )
  if content in [ 'episodes' , 'seasons' , 'tvshows' ] :
   self . setShowUpdated ( )
   if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
 def markAsUnwatched ( self , content , tmdb , season = None , episode = None ) :
  self . _acquire_lock ( )
  if content == 'movies' :
   if 71 - 71: I1Ii1I1
   if self . trakt :
    self . trakt . markAsUnwatched ( content , tmdb )
    if 1 - 1: IiI11Ii111 - oOo0O00 - i1 . oOo0O00
    if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
   self . cursor . execute ( "DELETE FROM movies_watched WHERE tmdb_id = ?" , ( tmdb , ) )
   self . conn . commit ( )
   if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
  elif content == 'tvshows' :
   if 19 - 19: Ii
   if self . trakt :
    self . trakt . markAsUnwatched ( content , tmdb )
    self . trakt . remove_show_playback ( tmdb )
    if 22 - 22: i1I % iI1iII1I1I1i + Oo
    if 60 - 60: ooo000 + I11iiIi11i1I + IIiIIiIi11I1 % i1i1i1111I - Ii % Ooo0Ooo
   self . cursor . execute ( "DELETE FROM episodes_watched WHERE tmdb_id = ?" , ( tmdb , ) )
   try :
    self . cursor . execute ( 'DELETE FROM shows_watched WHERE tmdb_id = {0}' . format ( tmdb ) )
   except :
    pass
   self . conn . commit ( )
   if 95 - 95: ooOOO % i1i1i1111I . i1
  elif content == 'seasons' and season :
   if 87 - 87: Iii1i % ooOOO * Ii % IIiIIiIi11I1 / I11iiIi11i1I
   if self . trakt :
    self . trakt . markAsUnwatched ( content , tmdb , season )
    if 84 - 84: I1Ii1I1 + Ooo0Ooo % IIiIIiIi11I1 * i1i1i1111I
    if 61 - 61: i1iiIII111 - Oo + I1Ii1I1
   self . cursor . execute ( "DELETE FROM episodes_watched WHERE tmdb_id = ? and season=?" , ( tmdb , season ) )
   self . cursor . execute ( 'update OR IGNORE shows_watched set completa = 0 where tmdb_id={0}' . format ( tmdb ) )
   self . conn . commit ( )
   if 43 - 43: IIiIIiIi11I1 * ooo000 + Ii % iI1iII1I1I1i
  elif content == 'episodes' and season and episode :
   if 12 - 12: i1iiIII111 + ooo000 . I11iiIi11i1I
   if self . trakt :
    self . trakt . markAsUnwatched ( content , tmdb , season , episode )
    if 1 - 1: iI1iII1I1I1i % Ii - I11iiIi11i1I / IiI11Ii111 + iI1iII1I1I1i - Ii
    if 27 - 27: OooOoo % iI1iII1I1I1i + IIiIIiIi11I1
   self . cursor . execute (
 "DELETE FROM episodes_watched WHERE tmdb_id = ? and season = ? and episode = ?" ,
 ( tmdb , season , episode )
 )
   self . cursor . execute ( 'update OR IGNORE shows_watched set completa = 0 where tmdb_id={0}' . format ( tmdb ) )
   self . conn . commit ( )
   if 16 - 16: IiI11Ii111
  self . _release_lock ( )
  if 31 - 31: oOo0O00 / Iii1i % Ooo0Ooo % i1 . iI1iII1I1I1i . Oo
  if 83 - 83: oOo0O00 - I11iiIi11i1I
 def resetResumeTime ( self , content , tmdb , season = None , episode = None ) :
  self . _acquire_lock ( )
  if content == 'movies' :
   if 91 - 91: IIiIIiIi11I1 - i1 - iI1iII1I1I1i
   if self . trakt :
    self . trakt . remove_movie_playback ( tmdb )
    if 71 - 71: I1I - IiI11Ii111
    if 66 - 66: i1i1i1111I / Ooo0Ooo + I11iiIi11i1I + Iii1i + oOo0O00 + i1I
   self . cursor . execute ( "SELECT playcount FROM movies_watched WHERE tmdb_id = ?" , ( tmdb , ) )
   if self . cursor . fetchall ( ) [ 0 ] [ 0 ] :
    self . cursor . execute ( "UPDATE movies_watched SET progress = 0.0 where tmdb_id = ?" , ( tmdb , ) )
   else :
    self . cursor . execute ( "DELETE FROM movies_watched WHERE tmdb_id = ?" , ( tmdb , ) )
   self . conn . commit ( )
   if 75 - 75: OooOoo - oOO - IiIIii11Ii - oOO + ooo000 % iI1iII1I1I1i
  elif content == 'episodes' and season and episode :
   if 42 - 42: i1 * i1I
   if self . trakt :
    self . trakt . remove_episode_playback ( tmdb , season , episode )
    if 50 - 50: Ii - i1iiIII111
    if 96 - 96: ooo000 * OooOoo - Ii - OooOoo
   self . cursor . execute (
 "SELECT playcount FROM episodes_watched WHERE tmdb_id = ? and season = ? and episode = ?" ,
 ( tmdb , season , episode )
 )
   if 65 - 65: Oo + Oo - iI1iII1I1I1i % OooOoo . Ooo0Ooo
   if self . cursor . fetchall ( ) [ 0 ] [ 0 ] :
    self . cursor . execute (
 "UPDATE episodes_watched SET progress =0.0 where tmdb_id = ? and season = ? and episode = ?" ,
 ( tmdb , season , episode )
 )
   else :
    self . cursor . execute (
 "DELETE FROM episodes_watched WHERE tmdb_id = ? and season = ? and episode = ?" ,
 ( tmdb , season , episode )
 )
   self . conn . commit ( )
   if 84 - 84: IIiIIiIi11I1 . ooOOO
  self . _release_lock ( )
  if 44 - 44: ooo000 * i1i1i1111I * oOO + i1iiIII111 - IIiIIiIi11I1
  if 70 - 70: IiI11Ii111
 def getMisSeries ( self , lock = None , ignore_hide_watched = False ) :
  i1Ii1iIi11iI = OrderedDict ( )
  if not lock : self . _acquire_lock ( )
  if 22 - 22: Iii1i + i1iiIII111 . oOo0O00 . IiIIii11Ii + OooOoo - i1
  if 68 - 68: I1Ii1I1 % I1Ii1I1 / IiI11Ii111 . ooo000
  IiiI1III1iI = list ( )
  if not ignore_hide_watched and get_setting ( 'hide_watched' , False ) :
   self . cursor . execute ( 'SELECT tmdb_id FROM shows_watched WHERE completa= 1' )
   IiiI1III1iI = list ( map ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ 0 ] , self . cursor . fetchall ( ) ) )
   if 38 - 38: Iii1i + ooo000 * Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
   if 100 - 100: IiIIii11Ii % i1
  self . cursor . execute ( 'SELECT tmdb_id FROM shows_watched WHERE ocultar= 1' )
  I111i1i11iII = list ( map ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ 0 ] , self . cursor . fetchall ( ) ) )
  if 5 - 5: OooOoo + oOo0O00 . Ooo0Ooo + I1I / OooOoo
  OOOO = """SELECT ew.tmdb_id, ew.season, ew.episode, ew.progress

                    FROM episodes_watched ew INNER JOIN (SELECT tmdb_id, MAX(lastPlayed) AS max_lastPlayed FROM episodes_watched

                     GROUP BY tmdb_id) ew2 ON ew.tmdb_id = ew2.tmdb_id AND ew.lastPlayed = ew2.max_lastPlayed ORDER by ew.lastPlayed DESC;"""
  self . cursor . execute ( OOOO )
  for oooo000O0 , ooO0oOO0 , OOo0oOo00O0o , I1 in self . cursor . fetchall ( ) :
   if oooo000O0 in IiiI1III1iI or oooo000O0 in I111i1i11iII :
    continue
   oooo000O0 = str ( oooo000O0 )
   if oooo000O0 not in i1Ii1iIi11iI :
    i1Ii1iIi11iI [ oooo000O0 ] = { 'ultimo_episodio' : ( ooO0oOO0 , OOo0oOo00O0o , I1 ) }
   else :
    II1IiiiiIIiii = i1Ii1iIi11iI [ oooo000O0 ] [ 'ultimo_episodio' ] [ 0 ]
    if ooO0oOO0 > II1IiiiiIIiii :
     i1Ii1iIi11iI [ oooo000O0 ] [ 'ultimo_episodio' ] = ( ooO0oOO0 , OOo0oOo00O0o , I1 )
    elif ooO0oOO0 == II1IiiiiIIiii :
     II1111I11 = i1Ii1iIi11iI [ oooo000O0 ] [ 'ultimo_episodio' ] [ 1 ]
     if OOo0oOo00O0o > II1111I11 :
      i1Ii1iIi11iI [ oooo000O0 ] [ 'ultimo_episodio' ] = ( ooO0oOO0 , OOo0oOo00O0o , I1 )
      if 94 - 94: Oo - IIiIIiIi11I1
  if not lock : self . _release_lock ( )
  return i1Ii1iIi11iI
  if 79 - 79: Ii + IiIIii11Ii * iI1iII1I1I1i / iI1iII1I1I1i
 def getMoviesUnfinished ( self ) :
  self . _acquire_lock ( )
  I1IoOooOo0o = Proxydatetime . now ( tz = timezone . utc ) - timedelta ( days = get_setting ( 'hideUnfinished' ) )
  self . cursor . execute (
 'select tmdb_id FROM movies_watched where progress > 0.0 and lastPlayed > "{0}" order by lastPlayed DESC' . format ( I1IoOooOo0o ) )
  iii1ii1 = [ str ( elt [ 0 ] ) for elt in self . cursor . fetchall ( ) ]
  self . _release_lock ( )
  return iii1ii1
  if 27 - 27: i1 / OooOoo + Iii1i % OooOoo + OooOoo
 def setShowUpdated ( self , lock = None ) :
  i1Ii1iIi11iI = self . getMisSeries ( lock = lock , ignore_hide_watched = True )
  if 70 - 70: Oo / Iii1i * OooOoo
  if 2 - 2: i1I / Iii1i + I1Ii1I1
  OOOO = """SELECT t.tmdb, t.temporada AS ultima_temporada, MAX(t.episodio) AS ultimo_episodio

                    FROM enlaces_series t

                    JOIN (

                        SELECT tmdb, MAX(temporada) AS ultima_temporada

                        FROM enlaces_series

                        WHERE tmdb IN (%s)

                        GROUP BY tmdb

                    ) sub ON t.tmdb = sub.tmdb AND t.temporada = sub.ultima_temporada 

                    GROUP BY t.tmdb, t.temporada;""" % ',' . join ( i1Ii1iIi11iI . keys ( ) )
  if 34 - 34: OooOoo
  if not lock : self . _acquire_lock ( )
  with MoriaDB ( ) as I11 :
   for oooo000O0 , ooOOO00oO0o0o , OooOOO0oO0Oo in I11 . executeSelect ( OOOO ) :
    IiiiI11111I , O00Oo0o00 , IiIIIII1i = i1Ii1iIi11iI [ str ( oooo000O0 ) ] [ 'ultimo_episodio' ]
    if 41 - 41: ooOOO + OooOoo + IIiIIiIi11I1 * i1i1i1111I
    if ( ooOOO00oO0o0o * 10000 + OooOOO0oO0Oo ) > ( IiiiI11111I * 10000 + O00Oo0o00 ) :
     self . cursor . execute ( 'UPDATE shows_watched SET completa = 0 where tmdb_id={0}' . format ( oooo000O0 ) )
     if 12 - 12: i1i1i1111I
     self . cursor . execute ( 'SELECT actualizada from shows_watched WHERE tmdb_id={0}' . format ( oooo000O0 ) )
     o0Oo0o000O0oO = self . cursor . fetchall ( ) [ 0 ] [ 0 ]
     if not o0Oo0o000O0oO :
      self . cursor . execute ( 'UPDATE shows_watched SET actualizada = 1 where tmdb_id={0}' . format ( oooo000O0 ) )
      if 46 - 46: Ii - IiI11Ii111 + IiIIii11Ii + i1I . I1I % OooOoo
      self . cursor . execute (
 "UPDATE episodes_watched SET lastplayed = strftime('%Y-%m-%dT%H:%M:%fZ','now') where"
 " tmdb_id = ? and season = ? and episode = ?" ,
 ( oooo000O0 , IiiiI11111I , O00Oo0o00 )
 )
    else :
     self . cursor . execute ( 'UPDATE shows_watched SET actualizada = 0 where tmdb_id={0}' . format ( oooo000O0 ) )
  self . conn . commit ( )
  if not lock : self . _release_lock ( )
  if 85 - 85: Oo / oOO + Oo + ooOOO
 def setShowHide ( self , tmdb ) :
  self . _acquire_lock ( )
  self . cursor . execute ( 'UPDATE shows_watched SET ocultar = 1 where tmdb_id={0}' . format ( tmdb ) )
  self . conn . commit ( )
  self . _release_lock ( )
  if 74 - 74: oOO - IiI11Ii111
 def getWatchedEpisodes ( self , tmdb , season ) :
  iii1ii1 = 0
  self . _acquire_lock ( )
  try :
   self . cursor . execute (
 "SELECT count(*) from episodes_watched where playcount > 0 and tmdb_id= ? and season= ?;" ,
 ( tmdb , season ) )
   iii1ii1 = self . cursor . fetchall ( ) [ 0 ] [ 0 ]
  except :
   pass
  self . _release_lock ( )
  return iii1ii1
  if 79 - 79: oOO * IiI11Ii111 . ooOOO * I1Ii1I1 . oOo0O00 + i1iiIII111
 def getWatchedShows ( self ) :
  self . _acquire_lock ( )
  self . cursor . execute ( 'SELECT tmdb_id FROM shows_watched WHERE completa = 1' )
  self . _release_lock ( )
  return list ( map ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ 0 ] , self . cursor . fetchall ( ) ) )
  if 45 - 45: I1Ii1I1
 def getUpdatedShows ( self ) :
  self . _acquire_lock ( )
  self . cursor . execute ( 'SELECT tmdb_id FROM shows_watched WHERE actualizada = 1' . format ( ) )
  self . _release_lock ( )
  return list ( map ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ 0 ] , self . cursor . fetchall ( ) ) )
  if 19 - 19: ooo000 * OooOoo . Iii1i * I11iiIi11i1I . I1I
 def getProgressEpisodes ( self , tmdb , season ) :
  iii1ii1 = dict ( )
  if 49 - 49: i1iiIII111 - IiIIii11Ii / i1iiIII111 + i1I
  self . _acquire_lock ( )
  try :
   OOOO = "SELECT episode, playcount, progress, runtime, lastPlayed FROM episodes_watched WHERE tmdb_id = %s and season = %s" % (
 tmdb , season )
   self . cursor . execute ( OOOO )
   if 77 - 77: Ii
   for ii1iII1II1I in self . cursor . fetchall ( ) :
    iii1ii1 [ ii1iII1II1I [ 0 ] ] = ( ii1iII1II1I [ 1 ] , ii1iII1II1I [ 2 ] , ii1iII1II1I [ 3 ] , ii1iII1II1I [ 4 ] )
  except :
   pass
  self . _release_lock ( )
  if 54 - 54: I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
  return iii1ii1
  if 15 - 15: i1I * I11iiIi11i1I - oOo0O00
 def getProgressMovies ( self , tmdb = None ) :
  iii1ii1 = dict ( )
  if 6 - 6: IiI11Ii111 - Ii
  self . _acquire_lock ( )
  try :
   OOOO = "SELECT tmdb_id, playcount, progress, runtime, lastPlayed FROM movies_watched"
   if tmdb :
    OOOO += ' where tmdb_id=%s' % tmdb
    if 1 - 1: I1I + OooOoo
   self . cursor . execute ( OOOO )
   if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
   for ii1iII1II1I in self . cursor . fetchall ( ) :
    iii1ii1 [ ii1iII1II1I [ 0 ] ] = ( ii1iII1II1I [ 1 ] , ii1iII1II1I [ 2 ] , ii1iII1II1I [ 3 ] , ii1iII1II1I [ 4 ] )
  except :
   pass
  self . _release_lock ( )
  if 96 - 96: OooOoo / oOO - i1 * I11iiIi11i1I
  return iii1ii1
  if 72 - 72: i1i1i1111I + Ii - Iii1i - i1i1i1111I - i1I + Ooo0Ooo
 def actualizarWidgetFavoritos ( self , content = None ) :
  if not content :
   content = [ 'movies' , 'tvshows' ]
  elif not isinstance ( content , list ) :
   content = [ content ]
   if 74 - 74: Ooo0Ooo * Oo + Iii1i - i1iiIII111
  for IIiIiiI1I1iII in content :
   if IIiIiiI1I1iII == 'movies' :
    CACHE . actualizarWidgetsByIds ( 'WidgetPelisFavoritas' )
    ooo00o0 = self . getFavoritos ( 'movies' )
    if ooo00o0 :
     OOOO = 'SELECT titulo,fecha,plot,poster,fondo,audio,calidad,tmdb,duration,mpaa,genero, trailer, clearlogo, rating, categoria  FROM v_pelis where tmdb in (%s)' % ',' . join (
 ooo00o0 )
     WINDOW . setProperty ( 'p3PelisFavoritasPath' ,
 'plugin://plugin.video.eduteamo/?' + P3Item ( nameWidget = "WidgetPelisFavoritas" ,
 action = "listado_peliculaS" ,
 sql = OOOO ,
 isWidget = True ,
 content = 'movies' ) . tourl ( ) )
    else :
     WINDOW . clearProperty ( 'p3PelisFavoritasPath' )
   elif IIiIiiI1I1iII in [ 'tvshows' , 'shows' ] :
    CACHE . actualizarWidgetsByIds ( 'WidgetSeriesFavoritas' )
    I11iiii = self . getFavoritos ( 'shows' )
    if I11iiii :
     OOOO = 'SELECT titulo,fecha,plot,poster,fondo,tmdb,audio,mpaa,genero, trailer, clearlogo, rating, categoria FROM v_series where tmdb in (%s)' % ',' . join (
 I11iiii )
     WINDOW . setProperty ( 'p3SeriesFavoritasPath' ,
 'plugin://plugin.video.eduteamo/?' + P3Item ( nameWidget = "WidgetSeriesFavoritas" ,
 action = "listado_serieS" ,
 sql = OOOO ,
 isWidget = True ,
 content = 'tvshows' ) . tourl ( ) )
    else :
     WINDOW . clearProperty ( 'p3SeriesFavoritasPath' )
     if 33 - 33: IiI11Ii111 / OooOoo
 def addFavorito ( self , p3Item ) :
  iII11I11111I = p3Item . content
  if iII11I11111I in [ 'tvshows' , 'seasons' , 'episodes' ] :
   iII11I11111I = 'shows'
  elif iII11I11111I != 'movies' :
   return
   if 81 - 81: iI1iII1I1I1i / IIiIIiIi11I1 . iI1iII1I1I1i
   if 81 - 81: i1I + IiIIii11Ii . I11iiIi11i1I
  if self . trakt :
   self . trakt . add_favorite ( iII11I11111I , p3Item . tmdb )
   if 10 - 10: iI1iII1I1I1i - Ii . IiIIii11Ii
   if 37 - 37: i1i1i1111I
  self . _acquire_lock ( )
  self . cursor . execute ( "INSERT OR IGNORE INTO favorites (tmdb_id, content) VALUES (?,?);" ,
 ( p3Item . tmdb , iII11I11111I ) )
  self . conn . commit ( )
  self . _release_lock ( )
  if 79 - 79: ooo000 % i1I - Ii % i1I - I1I
  if ISESTUARYeduteamo :
   self . actualizarWidgetFavoritos ( iII11I11111I )
   if 42 - 42: I11iiIi11i1I - Ii / Oo - i1i1i1111I + I11iiIi11i1I
   if 83 - 83: i1 . iI1iII1I1I1i
 def delFavorito ( self , p3Item ) :
  iII11I11111I = p3Item . content
  if iII11I11111I in [ 'tvshows' , 'seasons' , 'episodes' ] :
   iII11I11111I = 'shows'
  elif iII11I11111I != 'movies' :
   return
   if 57 - 57: IiI11Ii111 % IiIIii11Ii / oOo0O00 + Ooo0Ooo - i1iiIII111
   if 87 - 87: i1iiIII111 . i1iiIII111 . oOO . ooo000 * oOo0O00
  if self . trakt :
   self . trakt . del_favorite ( iII11I11111I , p3Item . tmdb )
   if 33 - 33: IiI11Ii111 * i1iiIII111 / i1I . OooOoo * oOo0O00 + ooo000
   if 17 - 17: i1i1i1111I * oOO + i1iiIII111 - I11iiIi11i1I / i1i1i1111I
  self . _acquire_lock ( )
  self . cursor . execute ( 'DELETE FROM favorites WHERE tmdb_id = {0} and content = "{1}";' . format ( p3Item . tmdb , iII11I11111I ) )
  self . conn . commit ( )
  self . _release_lock ( )
  if 83 - 83: I11iiIi11i1I - Iii1i + oOo0O00 + I1I / IIiIIiIi11I1 + I1I
  if ISESTUARYeduteamo :
   self . actualizarWidgetFavoritos ( iII11I11111I )
   if 29 - 29: i1i1i1111I / oOo0O00
   if 13 - 13: I11iiIi11i1I % i1iiIII111 . OooOoo % ooo000 % OooOoo
 def getFavoritos ( self , content ) :
  if content in [ 'tvshows' , 'shows' ] :
   content = 'shows'
  elif content != 'movies' :
   return
   if 21 - 21: IiI11Ii111 * I1Ii1I1
  self . _acquire_lock ( )
  OOOO = 'SELECT tmdb_id FROM favorites where content = "{0}"' . format ( content )
  self . cursor . execute ( OOOO )
  self . _release_lock ( )
  iii1ii1 = [ str ( elt [ 0 ] ) for elt in self . cursor . fetchall ( ) ]
  return iii1ii1
  if 93 - 93: Ooo0Ooo . i1 + IiI11Ii111 - oOo0O00
 def getVerifypeer2Certificate ( self , server ) :
  ooOOoO00OO = True
  O0Ooo0oOo0 = 0
  OOOO = "SELECT VERIFYPEER, PLAYCOUNT FROM CERTIFICATE WHERE SERVER = '%s'" % server
  if 62 - 62: Oo % I11iiIi11i1I * Oo
  self . cursor . execute ( OOOO )
  oOO0 = self . cursor . fetchall ( )
  if oOO0 :
   ooOOoO00OO , O0Ooo0oOo0 = oOO0 [ 0 ]
   if 19 - 19: i1 . IiIIii11Ii - Ooo0Ooo . Ii
  return bool ( ooOOoO00OO ) , O0Ooo0oOo0
  if 51 - 51: i1 + i1i1i1111I - i1 + i1iiIII111 . Oo
 def getServers2Certificate ( self ) :
  OOOO = 'select SERVER, PLAYCOUNT from CERTIFICATE'
  self . cursor . execute ( OOOO )
  oOO0 = self . cursor . fetchall ( )
  if oOO0 :
   iii1ii1 = dict ( oOO0 )
  else :
   iii1ii1 = dict ( )
   if 92 - 92: OooOoo + Ii / IIiIIiIi11I1 + OooOoo * IIiIIiIi11I1 * iI1iII1I1I1i
  return iii1ii1
  if 79 - 79: i1i1i1111I
 def setCertificate ( self , server , verifypeer , playcount ) :
  OOOO = "INSERT OR REPLACE INTO CERTIFICATE (SERVER,VERIFYPEER, PLAYCOUNT) VALUES('%s',%s,%s)" % (
 server , int ( verifypeer ) , playcount + 1 )
  self . cursor . execute ( OOOO )
  self . conn . commit ( )
  if 3 - 3: OooOoo / IiI11Ii111 % I11iiIi11i1I
 def setView ( self , content ) :
  ooOooo = xbmc . getSkinDir ( ) . replace ( 'skin.' , '' )
  OoO = xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( )
  OOOO = "INSERT OR REPLACE INTO views (skin, content, view) VALUES ('%s','%s',%s)" % ( ooOooo , content , OoO )
  self . cursor . execute ( OOOO )
  if 77 - 77: I11iiIi11i1I . i1 % OooOoo * Ooo0Ooo + Iii1i
  self . conn . commit ( )
  if 79 - 79: i1I / I1Ii1I1 - i1i1i1111I
 def getView ( self , content ) :
  if ISESTUARYeduteamo :
   return xbmcgui . Window ( xbmcgui . getCurrentWindowId ( ) ) . getFocusId ( )
   if 68 - 68: I11iiIi11i1I . I11iiIi11i1I % I11iiIi11i1I
  ooOooo = xbmc . getSkinDir ( ) . replace ( 'skin.' , '' )
  OOOO = "select view from views where skin = '%s' and content ='%s'" % ( ooOooo , content )
  try :
   self . cursor . execute ( OOOO )
   return self . cursor . fetchall ( ) [ 0 ] [ 0 ]
  except :
   return 55
   if 71 - 71: ooo000
   if 61 - 61: ooo000
   if 48 - 48: Iii1i * i1i1i1111I + IiIIii11Ii
   if 31 - 31: Oo * i1iiIII111 % Ii / oOO + I1Ii1I1 + iI1iII1I1I1i
 def _activarTrakt ( self ) :
  if xbmcgui . Dialog ( ) . yesno ( 'EduTeAmo' , localize ( 30507 ) ) :
   iIIIII1i111i = Trakt ( )
   if iIIIII1i111i . access_token :
    self . trakt = iIIIII1i111i
    set_setting ( 'trakt_enabled' , True )
    if 90 - 90: I1Ii1I1 * i1i1i1111I / iI1iII1I1I1i * Ii
    if 38 - 38: I1I . Ii
 def syncToTrakt ( self ) :
  if 41 - 41: ooo000 % IIiIIiIi11I1 % ooOOO
  if self . trakt :
   self . cursor . execute ( 'SELECT date FROM last_activities_trakt' )
   if self . cursor . fetchall ( ) :
    if WINDOW . getProperty ( 'P3syncToTrakt' ) and ( Proxydatetime . strptime ( WINDOW . getProperty ( 'P3syncToTrakt' ) , "%Y-%m-%d %H:%M:%S.%f" ) -
    # I1I
 Proxydatetime . now ( ) ) <= timedelta ( minutes = 5 ) :
     if 37 - 37: i1iiIII111 . Oo + IiIIii11Ii
     return
   WINDOW . setProperty ( 'P3syncToTrakt' , str ( Proxydatetime . now ( ) ) )
   if 56 - 56: iI1iII1I1I1i * i1iiIII111 - IIiIIiIi11I1 / IIiIIiIi11I1
   logger ( "Sincronizando vistos con Trakt.tv ..." )
   try :
    O0O = False
    for type , Ii1IIiiI1II , O0OO in self . trakt . get_last_activities ( ) :
     if 58 - 58: IiIIii11Ii
     self . cursor . execute ( 'SELECT date FROM last_activities_trakt WHERE type = ? and action = ?' ,
 ( type , Ii1IIiiI1II ) )
     Ooo00OO000oo = self . cursor . fetchall ( )
     if not Ooo00OO000oo or Ooo00OO000oo [ 0 ] [ 0 ] == '' :
      Ooo00OO000oo = '2000-01-01T00:01:01.000Z'
     else :
      Ooo00OO000oo = Ooo00OO000oo [ 0 ] [ 0 ]
      if 19 - 19: iI1iII1I1I1i * OooOoo . i1 . IiIIii11Ii * IiIIii11Ii
     if Proxydatetime . strptime ( O0OO , "%Y-%m-%dT%H:%M:%S.000Z" ) - Proxydatetime . strptime ( Ooo00OO000oo , "%Y-%m-%dT%H:%M:%S.000Z" ) > timedelta ( minutes = 2 ) :
      if 50 - 50: IiI11Ii111 . iI1iII1I1I1i / IiIIii11Ii + i1i1i1111I - i1I
      try :
       if type == "movies" and Ii1IIiiI1II == "watched_at" :
        II1Iiii1 = self . trakt . get_movies_watched ( )
        self . cursor . execute ( "SELECT * from movies_watched where progress=0.0" )
        II1iII1Ii1 = self . cursor . fetchall ( )
        if 37 - 37: I1I - OooOoo . iI1iII1I1I1i . iI1iII1I1I1i / i1iiIII111 . IiIIii11Ii
        if 91 - 91: oOO
        O000 = list (
 filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 not in II1Iiii1 , II1iII1Ii1 ) )
        O000 = list (
 map ( lambda oOOOOOOoOOooO0O0 : ( oOOOOOOoOOooO0O0 [ 0 ] , ) , O000 ) )
        self . cursor . executemany (
 'DELETE from movies_watched where tmdb_id=?;' , O000 )
        if 82 - 82: I11iiIi11i1I + i1
        if 16 - 16: i1 / IIiIIiIi11I1
        I1II1i1iiI = list (
 filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 not in II1iII1Ii1 , II1Iiii1 ) )
        self . cursor . executemany ( 'INSERT OR REPLACE INTO movies_watched VALUES(?,?,?,?,?);' ,
 I1II1i1iiI )
        if 51 - 51: IIiIIiIi11I1 * Ooo0Ooo % i1I - OooOoo . i1i1i1111I + iI1iII1I1I1i
       elif type == "movies" and Ii1IIiiI1II == "paused_at" :
        II1Iiii1 = self . trakt . get_movies_playback ( Ooo00OO000oo )
        self . cursor . executemany (
 'INSERT OR REPLACE INTO movies_watched (progress, lastplayed, runtime, tmdb_id) VALUES(?,?,?,?);' ,
 II1Iiii1 )
        if 60 - 60: IiIIii11Ii % oOO / i1I * OooOoo / I11iiIi11i1I - Ii
       elif type == "movies" and Ii1IIiiI1II == "watchlisted_at" :
        CACHE . actualizarWidgetsByIds ( 'WidgetPelisWatchlist' )
        if 16 - 16: oOo0O00 / I1Ii1I1 / i1 + I11iiIi11i1I + oOo0O00
       elif type == "episodes" and Ii1IIiiI1II == "watched_at" :
        II1Iiii1 = self . trakt . get_episodes_watched ( )
        if 11 - 11: oOO / OooOoo + oOo0O00
        self . cursor . execute ( "SELECT * from episodes_watched where progress=0.0" )
        i1ii1111I1i = self . cursor . fetchall ( )
        if 4 - 4: Ii
        if 83 - 83: I1I + Ooo0Ooo % Iii1i % oOO - oOo0O00
        O000 = list (
 filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 not in II1Iiii1 , i1ii1111I1i ) )
        O000 = list (
 map ( lambda oOOOOOOoOOooO0O0 : ( oOOOOOOoOOooO0O0 [ 0 ] , oOOOOOOoOOooO0O0 [ 1 ] , oOOOOOOoOOooO0O0 [ 2 ] ) , O000 ) )
        if 83 - 83: i1 - ooo000 * oOo0O00
        self . cursor . executemany (
 "DELETE from episodes_watched where tmdb_id=? and season=? and episode=?;" ,
 O000 )
        if 59 - 59: Ii
        if 21 - 21: IIiIIiIi11I1 - I1I - IiI11Ii111 + OooOoo
        OOOoO00oOoOoO = list (
 filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 not in i1ii1111I1i , II1Iiii1 ) )
        self . cursor . executemany (
 'INSERT OR REPLACE INTO episodes_watched VALUES(?,?,?,?,?,?,?);' ,
 OOOoO00oOoOoO )
        if 58 - 58: Oo / Ii
        if 38 - 38: Ooo0Ooo % I1Ii1I1 / i1I + i1iiIII111
        self . cursor . execute (
 'SELECT tmdb_id, count(*) FROM episodes_watched where season > 0 group by tmdb_id' )
        iIi = dict ( self . cursor . fetchall ( ) )
        if 25 - 25: I11iiIi11i1I - iI1iII1I1I1i
        self . cursor . execute ( 'SELECT tmdb_id, num_total_episodios FROM shows_watched' )
        OooO0Ooo0 = dict ( self . cursor . fetchall ( ) )
        if 46 - 46: Ii
        for O00OO0ooOoO , OoOo00o in iIi . items ( ) :
         I111Iii1Ii = OooO0Ooo0 . get ( O00OO0ooOoO )
         if not I111Iii1Ii :
          I111Iii1Ii = Tmdb ( ) . getSeasons ( O00OO0ooOoO ) . get ( 'num_total_episodios' )
          try :
           OO00OOooO = 1 if OoOo00o >= I111Iii1Ii else 0
          except :
           logger ( "Serie no sincronizada: https://www.themoviedb.org/tv/{0}" . format ( O00OO0ooOoO ) )
           OO00OOooO = 0
          self . cursor . execute ( 'INSERT OR REPLACE INTO shows_watched  VALUES(?,?,?,0,0);' ,
 ( O00OO0ooOoO , I111Iii1Ii , OO00OOooO ) )
         else :
          if OoOo00o == I111Iii1Ii :
           OO00OOooO = 1
           self . cursor . execute (
 'UPDATE shows_watched SET actualizada = 0 where tmdb_id={0}' . format ( O00OO0ooOoO ) )
          elif OoOo00o < I111Iii1Ii :
           OO00OOooO = 0
          elif OoOo00o > I111Iii1Ii :
           OO0 = Tmdb ( ) . getSeasons ( O00OO0ooOoO ) . get ( 'num_total_episodios' )
           if I111Iii1Ii != OO0 :
            self . cursor . execute (
 'UPDATE shows_watched SET num_total_episodios={0} where tmdb_id={1};' . format ( OO0 , O00OO0ooOoO ) )
           OO00OOooO = 1 if OoOo00o == OO0 else 0
           if 58 - 58: IiI11Ii111 + IiI11Ii111 * OooOoo . ooo000 . IiIIii11Ii
          self . cursor . execute (
 'UPDATE shows_watched SET completa= {0} where tmdb_id={1};' . format ( OO00OOooO , O00OO0ooOoO ) )
          if 44 - 44: OooOoo + IiI11Ii111 / ooo000 % Ii % Ii
          if 5 - 5: i1iiIII111 * IIiIIiIi11I1
       elif type == "episodes" and Ii1IIiiI1II == "paused_at" :
        II1Iiii1 = self . trakt . get_episodes_playback ( )
        if 67 - 67: IiI11Ii111 / OooOoo % IiI11Ii111 + i1iiIII111
        self . cursor . execute ( "SELECT tmdb_id, season, episode from episodes_watched where progress>0.0" )
        I1I1I111I11 = self . cursor . fetchall ( )
        if 39 - 39: IiIIii11Ii . Oo + i1I - oOo0O00
        if 93 - 93: Iii1i * IIiIIiIi11I1 % i1I + i1 % Ii * i1I
        o000Oo0oo0 = [ ( ii1iII1II1I [ 0 ] , ii1iII1II1I [ 1 ] , ii1iII1II1I [ 2 ] ) for ii1iII1II1I in II1Iiii1 ]
        if 90 - 90: I1I
        if 3 - 3: Ooo0Ooo + Ooo0Ooo / I1I * Ooo0Ooo
        O000 = list (
 filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 not in o000Oo0oo0 , I1I1I111I11 ) )
        if 65 - 65: Ii - OooOoo * I1I % i1iiIII111 % IIiIIiIi11I1
        self . cursor . executemany (
 "DELETE from episodes_watched where tmdb_id=? and season=? and episode=?;" ,
 O000 )
        if 68 - 68: I1Ii1I1 + oOO - oOO + IiIIii11Ii
        if 87 - 87: ooOOO * IIiIIiIi11I1 % i1 / oOO + i1 + oOo0O00
        self . cursor . executemany (
 'INSERT OR REPLACE INTO episodes_watched (tmdb_id, season, episode, progress, runtime, lastplayed) VALUES(?,?,?,?,?,?);' ,
 II1Iiii1 )
        if 99 - 99: I1I * IIiIIiIi11I1 * i1iiIII111
       elif type == "shows" and Ii1IIiiI1II == "watchlisted_at" :
        CACHE . actualizarWidgetsByIds ( 'WidgetSeriesWatchlist' )
        if 62 - 62: ooOOO % Oo + i1I
       else :
        continue
        if 87 - 87: ooo000 - OooOoo + Ii + i1i1i1111I + IiIIii11Ii
      except sqlite3 . Error :
       self . conn . rollback ( )
       if 57 - 57: IIiIIiIi11I1 + I1I / ooOOO % ooOOO % Oo / IiI11Ii111
      else :
       if 95 - 95: i1 / I11iiIi11i1I . i1 / Oo . Ooo0Ooo
       self . cursor . execute (
 'INSERT OR REPLACE INTO last_activities_trakt (type, action, date) VALUES (?,?,?)' ,
 ( type , Ii1IIiiI1II , O0OO ) )
       self . conn . commit ( )
       O0O = True
       if type == "episodes" :
        if Ii1IIiiI1II == "watched_at" :
         self . setShowUpdated ( )
        CACHE . actualizarWidgetsBySub_categoria ( 'tvshows' )
       elif type == "movies" :
        CACHE . actualizarWidgetsBySub_categoria ( 'movies' )
        if 43 - 43: Oo - OooOoo * oOO . Ooo0Ooo / IIiIIiIi11I1 * IIiIIiIi11I1
    if O0O :
     logger ( '... vistos actualizados' )
    else :
     logger ( '... vistos sin cambios' )
     if 84 - 84: i1iiIII111 + oOo0O00
   except Exception as ii1iII1II1I :
    logger ( "Error al sincronizar vistos: %s" % ii1iII1II1I , 'error' )
    if 83 - 83: i1i1i1111I
    if 84 - 84: oOO / Ii * Ooo0Ooo / Ii / ooo000
   logger ( "Sincronizando favoritos con Trakt.tv ..." )
   try :
    O0O = False
    for i1I11ii , iII11I11111I in [ ( 'pelis' , 'movies' ) , ( 'series' , 'shows' ) ] :
     with MoriaDB ( ) as I11 :
      oOooO00oOOO00 = set ( [ id [ 0 ] for id in I11 . executeSelect ( "select tmdb FROM %s" % i1I11ii ) ] )
     oOOooOo0O0 = list ( filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 in oOooO00oOOO00 , self . trakt . get_favorite ( iII11I11111I ) ) )
     o0 = set ( self . getFavoritos ( iII11I11111I ) )
     if 44 - 44: I1I % IiI11Ii111 / ooo000
     OO0iIIi = list ( filter ( lambda oOOOOOOoOOooO0O0 : int ( oOOOOOOoOOooO0O0 ) not in oOOooOo0O0 , o0 ) )
     if OO0iIIi :
      OOOO = 'DELETE FROM favorites WHERE content = "{}" and tmdb_id ' 'in ({})' . format ( iII11I11111I , ", " . join ( "?" * len ( OO0iIIi ) ) )
      if 1 - 1: i1 - ooOOO - i1iiIII111
      self . cursor . execute ( OOOO , OO0iIIi )
      O0O = True
      if 39 - 39: i1I * ooOOO . IiIIii11Ii * i1 * Ii
     IiI111 = list ( filter ( lambda oOOOOOOoOOooO0O0 : str ( oOOOOOOoOOooO0O0 ) not in o0 , oOOooOo0O0 ) )
     if IiI111 :
      OOOO = 'INSERT INTO favorites VALUES (?,?)'
      self . cursor . executemany ( OOOO , [ ( x , iII11I11111I ) for x in IiI111 ] )
      O0O = True
      if 99 - 99: Oo * oOo0O00 * IiIIii11Ii
    if O0O :
     self . conn . commit ( )
     logger ( '... favoritos actualizados' )
    else :
     logger ( '... favoritos sin cambios' )
     if 79 - 79: OooOoo / IIiIIiIi11I1
   except Exception as ii1iII1II1I :
    logger ( "Error al sincronizar favoritos: %s" % ii1iII1II1I , 'error' )
    if 20 - 20: IiI11Ii111 * Ooo0Ooo + oOO * IIiIIiIi11I1
 def getWatchlist ( self ) :
  if not self . trakt :
   self . _activarTrakt ( )
   if 97 - 97: I1I * IiI11Ii111 / I11iiIi11i1I . I11iiIi11i1I - IiIIii11Ii
  if self . trakt :
   if 10 - 10: Ii . I11iiIi11i1I % i1I / OooOoo % I1Ii1I1
   O0o = get_setting ( 'trakt_slug' )
   for iII11I11111I in [ 'movie' , 'show' ] :
    if iII11I11111I == 'movie' :
     oOoOo0OO0o = "Watchlist {0}" . format ( localize ( 30100 ) )
     OoOOo0o0ooOO0 = localize ( 30536 )
    else :
     oOoOo0OO0o = "Watchlist {0}" . format ( localize ( 30101 ) )
     OoOOo0o0ooOO0 = localize ( 30537 )
     if 9 - 9: i1i1i1111I . Ii - Ooo0Ooo + OooOoo / Ooo0Ooo
    OOOO = 'INSERT or IGNORE INTO listas_trakt (user,list_id,label,plot,content,sort_by,sort_how) VALUES ' . format ( ) + '("{0}", -1, "{1}","{2}","{3}","titulo","asc")' . format ( O0o , oOoOo0OO0o , OoOOo0o0ooOO0 , iII11I11111I )
    if 48 - 48: ooo000 - i1i1i1111I - oOO * OooOoo
    self . cursor . execute ( OOOO )
   self . conn . commit ( )
   if 84 - 84: I1Ii1I1 . ooo000 % I11iiIi11i1I
   ii , O00O0OooOOoO = self . trakt . get_watchlist ( )
   with MoriaDB ( ) as I11 :
    if ii :
     OOOO = "select tmdb FROM v_pelis where tmdb in ({0})" . format ( str ( ii ) [ 1 : - 1 ] )
     i1oooo0 = list ( [ id [ 0 ] for id in I11 . executeSelect ( OOOO ) ] )
     if 5 - 5: Ii % Ii / iI1iII1I1I1i - i1
    if O00O0OooOOoO :
     OOOO = "select tmdb FROM v_series where tmdb in ({0})" . format ( str ( O00O0OooOOoO ) [ 1 : - 1 ] )
     i1Ii = list ( [ id [ 0 ] for id in I11 . executeSelect ( OOOO ) ] )
     if 94 - 94: i1I + i1iiIII111 % oOo0O00 / I11iiIi11i1I / i1
   return list ( filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 in i1oooo0 , ii ) ) , list ( filter ( lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 in i1Ii , O00O0OooOOoO ) )
   if 53 - 53: Ii + i1I % I1Ii1I1
 def getMasVistas ( self , tipo , period ) :
  if not self . trakt :
   self . _activarTrakt ( )
   if 81 - 81: oOO - Ii - ooo000 + i1iiIII111 % Ooo0Ooo * Ooo0Ooo
  if self . trakt :
   return self . trakt . get_mostWatched ( tipo , period )
   if 20 - 20: I1Ii1I1 - IIiIIiIi11I1 % i1
 def getRecomendadas ( self , tipo ) :
  if not self . trakt :
   self . _activarTrakt ( )
   if 29 - 29: OooOoo * Ii - oOO
  if self . trakt :
   return self . trakt . get_recommendations ( tipo )
   if 53 - 53: I11iiIi11i1I % ooo000 / ooOOO / I1I
 def getAllLiTrakt ( self ) :
  if 43 - 43: iI1iII1I1I1i . i1i1i1111I + I1I % ooOOO . IiI11Ii111 - IiI11Ii111
  self . cursor . execute ( 'SELECT * FROM listas_trakt where content != "hidden" ORDER by label' )
  return self . cursor . fetchall ( )
  if 6 - 6: I1I
 def getLiTraktItems ( self , data_json ) :
  if 98 - 98: oOO * IIiIIiIi11I1 / i1iiIII111 / Iii1i + I1I
  if not self . trakt :
   self . _activarTrakt ( )
   if 25 - 25: IIiIIiIi11I1 . IiI11Ii111 / I1I * i1 - i1iiIII111 % oOo0O00
  if self . trakt :
   return self . trakt . get_items_list ( data_json [ 'user' ] , data_json [ 'list_id' ] , data_json [ 'content' ] , data_json . get ( 'sort_by' ) , data_json . get ( 'sort_how' ) )
   if 49 - 49: IiIIii11Ii % ooOOO + I11iiIi11i1I + IIiIIiIi11I1
 def getLiTraktUser ( self , content ) :
  if 60 - 60: IIiIIiIi11I1
  iii1ii1 = list ( )
  if self . trakt :
   O0o = get_setting ( 'trakt_slug' )
   if content == 'movies' :
    content = 'movie'
   elif content in [ 'tvshows' , 'seasons' , 'episodes' ] :
    content = 'show'
    if 98 - 98: IiIIii11Ii / Ooo0Ooo + Ii
   self . cursor . execute (
 'SELECT label, list_id FROM listas_trakt where user = "{0}" and content = "{1}"' . format ( O0o , content ) )
   iii1ii1 = self . cursor . fetchall ( )
   if 73 - 73: OooOoo * Iii1i
  return iii1ii1
  if 34 - 34: i1I % Ooo0Ooo * OooOoo + i1iiIII111 / i1
 def delLiTrakt ( self , trakt_list ) :
  O0o , o000OOO00 , iII11I11111I = trakt_list . split ( '|' )
  if O0o != get_setting ( 'trakt_slug' ) :
   self . cursor . execute (
 'DELETE FROM listas_trakt WHERE user="{0}" and list_id="{1}" and content="{2}"' . format ( O0o , o000OOO00 , iII11I11111I ) )
  else :
   if 95 - 95: I1Ii1I1 - IiIIii11Ii * OooOoo / oOO
   self . cursor . execute (
 'UPDATE listas_trakt SET content = "hidden" where user="{0}" and list_id = "{1}" and content="{2}"' . format ( O0o , o000OOO00 , iII11I11111I ) )
  self . conn . commit ( )
  if 63 - 63: Ii % I11iiIi11i1I
 def setSortLiTrakt ( self , trakt_list ) :
  iiiIi1ii1iii = "Ordenar "
  O0o , o000OOO00 , iII11I11111I = trakt_list . split ( '|' )
  self . cursor . execute (
 'select label from listas_trakt where user="{0}" and list_id={1} and content="{2}"' . format ( O0o , o000OOO00 , iII11I11111I ) )
  oOoOo0OO0o = self . cursor . fetchall ( )
  if oOoOo0OO0o :
   iiiIi1ii1iii += oOoOo0OO0o [ 0 ] [ 0 ]
   if 65 - 65: Ii + IiI11Ii111 % IIiIIiIi11I1 - Iii1i
  IiO0 = [ 'Por tÃ­tulo A-Z' , 'Por tÃ­tulo Z-A' , 'Fecha de estreno, mas antigua primero' ,
 'Fecha de estreno, mas nueva primero' , 'Por valoraciÃ³n, de menor a mayor' ,
 'Por valoraciÃ³n, de mayor a menor' , 'Fecha de agregado, mas antigua primero' ,
 'Fecha de agregado, mas reciente primero' , 'Aleatorio' , 'No ordenar' ]
  oo0 = xbmcgui . Dialog ( )
  iii1ii1 = oo0 . select ( iiiIi1ii1iii , IiO0 )
  if iii1ii1 != - 1 :
   i11II = 'desc' if iii1ii1 % 2 else 'asc'
   if iii1ii1 < 2 :
    OOO = 'titulo'
   elif iii1ii1 >= 2 and iii1ii1 < 4 :
    OOO = 'fecha'
   elif iii1ii1 >= 4 and iii1ii1 < 6 :
    OOO = 'rating'
   elif iii1ii1 >= 6 and iii1ii1 < 8 :
    OOO = 'added'
   elif iii1ii1 == 8 :
    OOO = 'random'
    i11II = ''
   else :
    OOO = ''
    i11II = ''
    if 59 - 59: i1 / i1i1i1111I + Ii * ooo000 . ooo000
   self . cursor . execute (
 'UPDATE listas_trakt SET sort_by = "{0}", sort_how = "{1}" where user="{2}" and list_id = "{3}" and content="{4}"' . format ( OOO , i11II , O0o , o000OOO00 , iII11I11111I ) )
   self . conn . commit ( )
   if 49 - 49: Ii - Iii1i * I1Ii1I1 * IIiIIiIi11I1 . Ooo0Ooo
 def addLiTrakt ( self ) :
  iii1ii1 = False
  if 83 - 83: Oo % Ii % i1
  try :
   Iii1I1 = self . trakt . get_list ( )
   if Iii1I1 :
    O0o , o000OOO00 , oOoOo0OO0o , OoOOo0o0ooOO0 , iII11I11111I , OOO , i11II = Iii1I1
    OOOO = 'INSERT OR REPLACE INTO listas_trakt (user,list_id,label,plot,content,sort_by,sort_how) VALUES ' . format ( ) + '("{0}",{1},"{2}","{3}","{4}","{5}","{6}")' . format ( O0o , o000OOO00 , oOoOo0OO0o , OoOOo0o0ooOO0 , iII11I11111I , OOO , i11II )
    if 73 - 73: I1Ii1I1 . Iii1i + i1I / ooo000 / oOo0O00 . I1Ii1I1
    self . cursor . execute ( OOOO )
    self . conn . commit ( )
    iii1ii1 = True
    if 73 - 73: ooo000 % oOO
  except :
   if 43 - 43: OooOoo * i1i1i1111I * IiIIii11Ii % Ii
   xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' ,
 localize ( 30516 ) ,
 xbmcgui . NOTIFICATION_ERROR )
  return iii1ii1
  if 13 - 13: i1i1i1111I / IiI11Ii111 + IiI11Ii111 % ooo000
 def addLiTraktUser ( self ) :
  if 100 - 100: ooOOO . IIiIIiIi11I1 - i1
  O0OO = self . trakt . get_last_activities ( onlyUpdateLists = True )
  if 46 - 46: Ooo0Ooo - i1I / ooo000 * IiI11Ii111 . oOo0O00
  self . cursor . execute ( 'SELECT date FROM last_activities_trakt WHERE type ="lists"' )
  Ooo00OO000oo = self . cursor . fetchall ( )
  if not Ooo00OO000oo or Ooo00OO000oo [ 0 ] [ 0 ] == '' :
   Ooo00OO000oo = '2000-01-01T00:01:01.000Z'
  else :
   Ooo00OO000oo = Ooo00OO000oo [ 0 ] [ 0 ]
   if 32 - 32: i1i1i1111I . OooOoo + OooOoo - ooo000 * IiIIii11Ii + Oo
   if 12 - 12: oOo0O00
  if Proxydatetime . strptime ( O0OO , "%Y-%m-%dT%H:%M:%S.000Z" ) - Proxydatetime . strptime ( Ooo00OO000oo , "%Y-%m-%dT%H:%M:%S.000Z" ) > timedelta ( minutes = 2 ) :
   if 57 - 57: Oo + i1i1i1111I / I1Ii1I1
   if 56 - 56: oOO % Ooo0Ooo % Iii1i . i1i1i1111I
   O0o = get_setting ( 'trakt_slug' )
   self . cursor . execute ( 'SELECT list_id FROM listas_trakt where user = "{0}"' . format ( O0o ) )
   o0OOoOOOo00 = set ( [ int ( oOOOOOOoOOooO0O0 [ 0 ] ) for oOOOOOOoOOooO0O0 in self . cursor . fetchall ( ) ] )
   if 32 - 32: I1Ii1I1 % ooo000 * OooOoo / oOo0O00 + ooOOO
   if 64 - 64: I1Ii1I1 . Ooo0Ooo
   OOoOOo = requests . get ( 'https://api.trakt.tv/users/{0}/lists' . format ( O0o ) , headers = self . trakt . headers ) . json ( )
   oooOoOO0O = set ( [ oOOOOOOoOOooO0O0 [ 'ids' ] [ 'trakt' ] for oOOOOOOoOOooO0O0 in OOoOOo ] )
   if 43 - 43: Ooo0Ooo + IiI11Ii111 * oOo0O00 / i1iiIII111
   if 78 - 78: IIiIIiIi11I1 / I1Ii1I1 + i1iiIII111 - IIiIIiIi11I1 + i1 % i1iiIII111
   OOo0o00o = list ( oooOoOO0O - o0OOoOOOo00 )
   if 88 - 88: iI1iII1I1I1i . I1I * oOo0O00 - i1i1i1111I * Ooo0Ooo
   for oOOOOOOoOOooO0O0 in OOoOOo :
    o000OOO00 = oOOOOOOoOOooO0O0 [ 'ids' ] [ 'trakt' ]
    if 87 - 87: oOo0O00 / ooOOO / OooOoo * Ooo0Ooo
    if o000OOO00 in OOo0o00o :
     if 49 - 49: iI1iII1I1I1i
     oOoOo0OO0o = oOOOOOOoOOooO0O0 [ 'name' ] . replace ( '"' , "'" )
     OoOOo0o0ooOO0 = oOOOOOOoOOooO0O0 [ 'description' ] . replace ( '"' , "'" )
     OOO = oOOOOOOoOOooO0O0 [ 'sort_by' ]
     i11II = oOOOOOOoOOooO0O0 [ 'sort_how' ]
     if 77 - 77: ooo000 % I11iiIi11i1I % Ooo0Ooo * oOO
     if OOO == 'released' :
      OOO = 'fecha'
     elif OOO == 'title' :
      OOO = 'titulo'
     else :
      OOO = 'rating'
      i11II = 'desc'
      if 5 - 5: oOO * i1i1i1111I % Oo
     I11i = localize ( 30517 ) % oOoOo0OO0o
     OoooOo00 = xbmcgui . Dialog ( ) . yesnocustom ( 'EduTeAmo' , I11i , localize ( 30529 ) , localize ( 30101 ) ,
 localize ( 30100 ) )
     if OoooOo00 == 1 :
      iII11I11111I = 'movie'
     elif OoooOo00 == 0 :
      iII11I11111I = 'show'
     else :
      iII11I11111I = 'hidden'
      if 67 - 67: i1I % iI1iII1I1I1i / ooo000 + i1I - I11iiIi11i1I
     if iII11I11111I :
      OOOO = 'INSERT OR REPLACE INTO listas_trakt (user,list_id,label,plot,content,sort_by,sort_how) VALUES ' . format ( ) + '("{0}",{1},"{2}","{3}","{4}","{5}","{6}")' . format ( O0o , o000OOO00 , oOoOo0OO0o , OoOOo0o0ooOO0 , iII11I11111I , OOO , i11II )
      if 20 - 20: IIiIIiIi11I1 . oOo0O00 . Ooo0Ooo
      self . cursor . execute ( OOOO )
      if 11 - 11: OooOoo
      if 45 - 45: iI1iII1I1I1i + I11iiIi11i1I / IIiIIiIi11I1
   for o000OOO00 in list ( o0OOoOOOo00 - oooOoOO0O ) :
    self . cursor . execute ( 'DELETE FROM listas_trakt where list_id={0}' . format ( o000OOO00 ) )
    if 45 - 45: iI1iII1I1I1i . iI1iII1I1I1i * i1i1i1111I + oOo0O00
    if 6 - 6: Iii1i . Oo + I1Ii1I1 * i1 * I1Ii1I1 % oOO
   self . cursor . execute (
 'INSERT OR REPLACE INTO last_activities_trakt (type, action, date) VALUES ("lists", "updated_at", "{0}")' . format ( O0OO ) )
   self . conn . commit ( )
   if 21 - 21: Ooo0Ooo % i1 - ooo000
 def addItem2Trakt ( self , content , tmdb , list_id ) :
  iii1ii1 = self . trakt . addItem2Trakt ( content , tmdb , list_id )
  if iii1ii1 > 0 :
   if content == 'movies' :
    CACHE . actualizarWidgetsByIds ( 'WidgetPelisWatchlist' )
   elif content in [ 'tvshows' , 'seasons' , 'episodes' ] :
    CACHE . actualizarWidgetsByIds ( 'WidgetSeriesWatchlist' )
    if 81 - 81: Ooo0Ooo / ooo000
  return iii1ii1
  if 4 - 4: I1I % i1I - ooo000 - I1I . ooOOO / i1i1i1111I
class Trakt ( object ) :
 def __init__ ( self ) :
  self . CLIENT_ID = "9c0d7bbf0e3e4601ab5efce4936ad3633a6cdc18cdc2ebfd2fb5d4ea4b9c30ca"
  self . CLIENT_SECRET = "6b3e48c94872a4e9f0be05a413ea11141e1586d9725b8e27b301da619e9d5683"
  if 74 - 74: oOO
  IiIiI1I = get_setting ( 'trakt_access_token' )
  I1IoOooOo0o = int ( get_setting ( 'trakt_token_expired_at' ) or '0' )
  OO0oOOO0o00 = get_setting ( 'trakt_refresh_token' )
  if 39 - 39: i1i1i1111I % OooOoo * Oo + oOo0O00 / Oo
  self . headers = {
 'Content-Type' : 'application/json' ,
 'trakt-api-version' : '2' ,
 'trakt-api-key' : self . CLIENT_ID
 }
  if 24 - 24: OooOoo * ooo000 % Ooo0Ooo
  if not ( IiIiI1I and I1IoOooOo0o and OO0oOOO0o00 ) :
   if WINDOW . getProperty ( "p3TraktAuthenticationLock" ) != "true" :
    WINDOW . setProperty ( "p3TraktAuthenticationLock" , "true" )
    try :
     IiIiI1I = self . authenticationDevices ( )
    finally :
     WINDOW . clearProperty ( "p3TraktAuthenticationLock" )
   else :
    IiIiI1I = None
    if 77 - 77: ooo000 % Ooo0Ooo
  if IiIiI1I and I1IoOooOo0o and OO0oOOO0o00 :
   I111i1iIIiiI = Proxydatetime . now ( tz = timezone . utc )
   I1IoOooOo0o = Proxydatetime . fromtimestamp ( I1IoOooOo0o , tz = timezone . utc )
   if 58 - 58: IiIIii11Ii . IIiIIiIi11I1 . I1I / oOO - I11iiIi11i1I
   if I1IoOooOo0o < I111i1iIIiiI :
    IiIiI1I = None
    OOO0OOoo0ooO = 'https://api.trakt.tv/oauth/token'
    I1IiI = {
 "client_id" : self . CLIENT_ID ,
 "client_secret" : self . CLIENT_SECRET ,
 "refresh_token" : OO0oOOO0o00 ,
 "redirect_uri" : "urn:ietf:wg:oauth:2.0:oob" ,
 "grant_type" : "refresh_token"
 }
    ooO0O0o0O0o = downloadpage ( OOO0OOoo0ooO , post = I1IiI )
    if ooO0O0o0O0o . code == 200 :
     II1Iiii1 = load_json ( ooO0O0o0O0o . data )
     set_setting ( 'trakt_access_token' , II1Iiii1 . get ( "access_token" ) )
     set_setting ( 'trakt_refresh_token' , II1Iiii1 . get ( "refresh_token" ) )
     set_setting ( 'trakt_token_expired_at' ,
 str ( II1Iiii1 . get ( "created_at" ) + II1Iiii1 . get ( "expires_in" ) ) )
     IiIiI1I = II1Iiii1 . get ( "access_token" )
     if 55 - 55: i1
  if IiIiI1I :
   self . access_token = IiIiI1I
   self . headers [ 'Authorization' ] = "Bearer %s" % IiIiI1I
   self . slug = get_setting ( 'trakt_slug' )
   if not self . slug :
    II1Iiii1 = load_json ( downloadpage ( 'https://api.trakt.tv/users/settings' , headers = self . headers ) . data )
    self . slug = II1Iiii1 [ "user" ] [ "ids" ] [ "slug" ]
    set_setting ( 'trakt_slug' , self . slug )
  else :
   self . access_token = None
   if 39 - 39: iI1iII1I1I1i
 def authenticationDevices ( self ) :
  if xbmcgui . getCurrentWindowId ( ) == 12999 :
   if 34 - 34: iI1iII1I1I1i . i1 . I1I
   return False
   if 95 - 95: IiIIii11Ii * IiI11Ii111 * Ooo0Ooo * IiI11Ii111 / OooOoo
  self . dialog = xbmcgui . DialogProgress ( )
  self . dialog . create ( 'EduTeAmo' , "Trakt.tv" )
  if 27 - 27: i1I . IiIIii11Ii
  def o0OO0O0 ( device_code ) :
   I1IiI = {
 "code" : device_code ,
 "client_id" : self . CLIENT_ID ,
 "client_secret" : self . CLIENT_SECRET
 }
   if 87 - 87: OooOoo
   ooO0O0o0O0o = downloadpage ( 'https://api.trakt.tv/oauth/device/token' , I1IiI )
   if ooO0O0o0O0o . code == 200 :
    II1Iiii1 = load_json ( ooO0O0o0O0o . data )
    set_setting ( 'trakt_access_token' , II1Iiii1 . get ( "access_token" ) )
    set_setting ( 'trakt_refresh_token' , II1Iiii1 . get ( "refresh_token" ) )
    set_setting ( 'trakt_token_expired_at' ,
 str ( II1Iiii1 . get ( "created_at" ) + II1Iiii1 . get ( "expires_in" ) ) )
    return II1Iiii1 . get ( "access_token" )
   else :
    return False
    if 97 - 97: ooOOO . OooOoo * OooOoo * i1
  OOO0OOoo0ooO = 'https://api.trakt.tv/oauth/device/code'
  I1IiI = { 'client_id' : self . CLIENT_ID }
  ooO0O0o0O0o = downloadpage ( OOO0OOoo0ooO , post = I1IiI )
  II1Iiii1 = load_json ( ooO0O0o0O0o . data )
  I1IIi = False
  OOo0oO00 = II1Iiii1 . get ( "expires_in" , 130 )
  OOO0o0o0O = 100 / OOo0oO00
  oOoOoOOOOO = II1Iiii1 . get ( "interval" , 5 )
  I11i = localize ( 30074 ) % ( 'Trakt.tv' , II1Iiii1 . get ( "verification_url" , "" ) ,
 II1Iiii1 . get ( "user_code" , "" ) ) + localize ( 30075 )
  while not self . dialog . iscanceled ( ) and OOo0oO00 > 0 and I1IIi == False :
   self . dialog . update ( int ( OOo0oO00 * OOO0o0o0O ) , I11i % divmod ( OOo0oO00 , 60 ) )
   if OOo0oO00 % oOoOoOOOOO == 0 :
    I1IIi = o0OO0O0 ( II1Iiii1 . get ( "device_code" ) )
   xbmc . sleep ( 1000 )
   OOo0oO00 -= 1
   if 71 - 71: i1I / i1iiIII111 - Ii * Oo . iI1iII1I1I1i
  self . dialog . close ( )
  return I1IIi
  if 3 - 3: I1Ii1I1
 def get_last_activities ( self , onlyUpdateLists = False ) :
  iii1ii1 = list ( )
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/last_activities"
   II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data )
   if 57 - 57: Ooo0Ooo . OooOoo / oOo0O00 * I1Ii1I1
   if onlyUpdateLists :
    iii1ii1 = II1Iiii1 [ 'lists' ] [ 'updated_at' ]
   else :
    for type in [ 'movies' , 'episodes' ] :
     for Ii1IIiiI1II in [ 'watched_at' , 'paused_at' ] :
      iii1ii1 . append ( ( type , Ii1IIiiI1II , II1Iiii1 [ type ] [ Ii1IIiiI1II ] ) )
      if 36 - 36: IiIIii11Ii
    iii1ii1 . append ( ( 'movies' , 'watchlisted_at' , II1Iiii1 [ 'movies' ] [ 'watchlisted_at' ] ) )
    iii1ii1 . append ( ( 'shows' , 'watchlisted_at' , II1Iiii1 [ 'shows' ] [ 'watchlisted_at' ] ) )
    if 33 - 33: IiIIii11Ii
  return iii1ii1
  if 86 - 86: Ii / oOo0O00 - i1 * i1i1i1111I - Oo * Iii1i
 def get_movies_playback ( self , last_updated_at = None ) :
  iii1ii1 = list ( )
  if 28 - 28: OooOoo . i1 % iI1iII1I1I1i % Iii1i
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/movies?extended=full"
   II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data )
   if 2 - 2: Oo + OooOoo - i1i1i1111I - ooo000 / Oo . Oo
   for OoOo00 in II1Iiii1 :
    if not last_updated_at or (
 Proxydatetime . strptime ( OoOo00 [ 'paused_at' ] , "%Y-%m-%dT%H:%M:%S.000Z" ) >
 Proxydatetime . strptime ( last_updated_at , "%Y-%m-%dT%H:%M:%S.000Z" ) ) :
     i1i11iII1i = (
 OoOo00 [ 'progress' ] ,
 OoOo00 [ 'paused_at' ] ,
 OoOo00 [ 'movie' ] [ 'runtime' ] * 60 if OoOo00 [ 'movie' ] [ 'runtime' ] else 0 ,
 OoOo00 [ 'movie' ] [ 'ids' ] [ 'tmdb' ]
 )
     iii1ii1 . append ( i1i11iII1i )
  return iii1ii1
  if 81 - 81: Ooo0Ooo / iI1iII1I1I1i % i1i1i1111I / OooOoo . i1I . ooo000
 def get_episodes_playback ( self ) :
  iii1ii1 = list ( )
  if 45 - 45: OooOoo + ooOOO / i1i1i1111I * i1
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/episodes?extended=full"
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   if 71 - 71: IiI11Ii111 % Iii1i + oOo0O00 * I11iiIi11i1I / IiI11Ii111
   for I1iiII in load_json ( II1Iiii1 ) :
    OOo0oOo00O0o = ( I1iiII [ 'show' ] [ 'ids' ] [ 'tmdb' ] , I1iiII [ 'episode' ] [ 'season' ] , I1iiII [ 'episode' ] [ 'number' ] ,
 I1iiII [ 'progress' ] ,
 I1iiII [ 'episode' ] [ 'runtime' ] * 60 if I1iiII [ 'episode' ] [ 'runtime' ] else 0 ,
 I1iiII [ 'paused_at' ] )
    iii1ii1 . append ( OOo0oOo00O0o )
  return iii1ii1
  if 15 - 15: IiI11Ii111 - i1i1i1111I
 def get_movies_watched ( self ) :
  iii1ii1 = list ( )
  if 68 - 68: IiIIii11Ii
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/watched/movies?extended=full"
   II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data )
   if 41 - 41: i1I - Ooo0Ooo
   for OoOo00 in II1Iiii1 :
    iii1ii1 . append (
 (
 OoOo00 [ 'movie' ] [ 'ids' ] [ 'tmdb' ] ,
 OoOo00 [ 'plays' ] ,
 0.0 ,
 OoOo00 [ 'movie' ] [ 'runtime' ] * 60 if OoOo00 [ 'movie' ] [ 'runtime' ] else 0 ,
 OoOo00 [ 'last_watched_at' ]
 )
 )
    if 47 - 47: I1Ii1I1 * i1i1i1111I - i1I . Iii1i . ooOOO
  return iii1ii1
  if 28 - 28: Ii
 def get_episodes_watched ( self ) :
  iii1ii1 = list ( )
  O00OO0Oo0000 = False
  if 20 - 20: oOo0O00 . I11iiIi11i1I . I1I
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/watched/shows?extended=full"
   II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data )
   if 20 - 20: ooo000 + i1i1i1111I % Ooo0Ooo + i1 * Ii
   for iiI11iI1 in II1Iiii1 :
    O00OO0ooOoO = iiI11iI1 [ 'show' ] [ 'ids' ] [ 'tmdb' ]
    for i1iII1 in iiI11iI1 [ 'seasons' ] :
     ooO0oOO0 = i1iII1 [ 'number' ]
     for ii1iII1II1I in i1iII1 [ 'episodes' ] :
      OOo0oOo00O0o = list ( )
      OOo0oOo00O0o . append ( O00OO0ooOoO )
      OOo0oOo00O0o . append ( ooO0oOO0 )
      OOo0oOo00O0o . append ( ii1iII1II1I [ 'number' ] )
      OOo0oOo00O0o . append ( ii1iII1II1I [ 'plays' ] )
      OOo0oOo00O0o . append ( 0.0 )
      OOo0oOo00O0o . append ( 0 )
      OOo0oOo00O0o . append ( ii1iII1II1I [ 'last_watched_at' ] )
      iii1ii1 . append ( tuple ( OOo0oOo00O0o ) )
  return iii1ii1
  if 67 - 67: I1Ii1I1 + OooOoo + ooOOO * Oo * i1iiIII111 . Ooo0Ooo
 def scrobble ( self , action , progress , content , tmdb , season = None , episode = None ) :
  if self . access_token :
   try :
    if content == 'episodes' :
     OOO0OOoo0ooO = 'https://api.trakt.tv/search/tmdb/%s?type=show' % tmdb
     II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data ) [ 0 ]
     o000oO = II1Iiii1 [ 'show' ] [ 'ids' ] [ 'trakt' ]
     if 59 - 59: Ii + i1I - IiIIii11Ii / ooOOO / Oo
     OOO0OOoo0ooO = 'https://api.trakt.tv/shows/%s/seasons/%s/episodes/%s' % (
 o000oO , season , episode )
     II1Iiii1 = load_json ( downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data )
     i1iiiiiIIIiii = II1Iiii1 [ 'ids' ] [ 'trakt' ]
     I1IiI = '''{"episode": {"ids":{"trakt":%s}},"progress": %s}''' % ( i1iiiiiIIIiii , progress )
     downloadpage ( "https://api.trakt.tv/scrobble/" + action , post = I1IiI , headers = self . headers )
     if 71 - 71: Ooo0Ooo * i1iiIII111 / Ooo0Ooo / i1iiIII111 * i1i1i1111I + i1I
    elif content == 'movies' :
     if 48 - 48: I11iiIi11i1I
     I1IiI = '''{"movie": {"ids": {"tmdb": %s}}, "progress": %s}''' % ( tmdb , progress )
     downloadpage ( "https://api.trakt.tv/scrobble/" + action , post = I1IiI , headers = self . headers )
   except Exception as ii1iII1II1I :
    logger ( 'scrobble error: %s' % ii1iII1II1I , 'error' )
    if 87 - 87: I1Ii1I1
 def markAsWatched ( self , content , tmdb , season = None , episode = None ) :
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/history"
   if 29 - 29: ooo000 . iI1iII1I1I1i . oOo0O00 + i1i1i1111I + oOO
   if content == 'tvshows' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s}}]}''' % ( tmdb )
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 59 - 59: IiIIii11Ii
   elif content == 'seasons' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s},"seasons":[{"number":%s}]}]}''' % (
 tmdb , season )
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 26 - 26: oOo0O00 % IiI11Ii111 * i1
   elif content == 'episodes' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s},"seasons":[{"number":%s,"episodes":[{"number":%s}]}]}]}''' % (
 tmdb , season , episode )
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 60 - 60: IIiIIiIi11I1 % oOO / i1
   elif content == 'movies' :
    I1IiI = '''{"movies":[{"ids": {"tmdb": %s}}]}''' % tmdb
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 20 - 20: Ooo0Ooo
 def markAsUnwatched ( self , content , tmdb , season = None , episode = None ) :
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/history/remove"
   if content == 'episodes' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s},"seasons":[{"number":%s,"episodes":[{"number":%s}]}]}]}''' % (
 tmdb , season , episode )
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 4 - 4: IiIIii11Ii % Iii1i
   elif content == 'seasons' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s},"seasons":[{"number":%s}]}]}''' % ( tmdb , season )
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 43 - 43: ooo000
   elif content == 'tvshows' :
    I1IiI = '''{"shows":[{"ids":{"tmdb":%s}}]}''' % tmdb
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 95 - 95: Oo + I11iiIi11i1I / Ooo0Ooo / Ii - ooOOO / i1i1i1111I
   elif content == 'movies' :
    I1IiI = '''{"movies":[{"ids": {"tmdb": %s}}]}''' % tmdb
    II1Iiii1 = downloadpage ( OOO0OOoo0ooO , post = I1IiI , headers = self . headers ) . data
    if 6 - 6: Ooo0Ooo % IiIIii11Ii
    if 59 - 59: i1I . I11iiIi11i1I . ooo000 / i1I . Ii % Ooo0Ooo
    if 85 - 85: oOo0O00 / ooOOO
 def remove_episode_playback ( self , tmdb , season , episode ) :
  if 41 - 41: i1iiIII111 * iI1iII1I1I1i + i1 + i1i1i1111I
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/episodes"
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   for iiiiiIIIIi1 in load_json ( II1Iiii1 ) :
    if iiiiiIIIIi1 [ 'show' ] [ 'ids' ] [ 'tmdb' ] == int ( tmdb ) and iiiiiIIIIi1 [ 'episode' ] [ 'season' ] == season and iiiiiIIIIi1 [ 'episode' ] [ 'number' ] == episode :
     if 46 - 46: oOo0O00 - iI1iII1I1I1i
     OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/%s" % iiiiiIIIIi1 [ 'id' ]
     downloadpage ( OOO0OOoo0ooO , headers = self . headers , method = 'DELETE' )
     break
     if 34 - 34: i1i1i1111I
 def remove_show_playback ( self , tmdb ) :
  if 21 - 21: IiI11Ii111 + I1I . OooOoo + i1 . ooo000 + I11iiIi11i1I
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/episodes"
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   for iiiiiIIIIi1 in load_json ( II1Iiii1 ) :
    if iiiiiIIIIi1 [ 'show' ] [ 'ids' ] [ 'tmdb' ] == int ( tmdb ) :
     OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/%s" % iiiiiIIIIi1 [ 'id' ]
     downloadpage ( OOO0OOoo0ooO , headers = self . headers , method = 'DELETE' )
     if 7 - 7: ooOOO + Iii1i / iI1iII1I1I1i - oOO % Oo / iI1iII1I1I1i
 def remove_movie_playback ( self , tmdb ) :
  if 14 - 14: Iii1i . Ii
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/movies"
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   for iiiiiIIIIi1 in load_json ( II1Iiii1 ) :
    if iiiiiIIIIi1 [ 'movie' ] [ 'ids' ] [ 'tmdb' ] == int ( tmdb ) :
     OOO0OOoo0ooO = "https://api.trakt.tv/sync/playback/%s" % iiiiiIIIIi1 [ 'id' ]
     downloadpage ( OOO0OOoo0ooO , headers = self . headers , method = 'DELETE' )
     break
     if 100 - 100: I1I / ooo000
 def get_mostWatched ( self , tipo , period ) :
  if 48 - 48: i1i1i1111I * i1I % i1i1i1111I + i1i1i1111I . iI1iII1I1I1i / OooOoo
  if 12 - 12: Ii . Ii - I1Ii1I1
  if 74 - 74: ooo000 * Iii1i - Ooo0Ooo - I1Ii1I1
  if self . access_token :
   iii1ii1 = list ( )
   oOOO = 'get_mostWatched_' + tipo + '_' + period
   if 20 - 20: IiI11Ii111
   try :
    II1IiiIIi = CACHE . get ( oOOO )
    if II1IiiIIi :
     return II1IiiIIi
   except : pass
   if 54 - 54: I11iiIi11i1I * i1
   OOO0OOoo0ooO = "https://api.trakt.tv/%s/watched/%s?limit=100" % ( tipo , period )
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   if 81 - 81: ooo000 . IiIIii11Ii * oOO - IiIIii11Ii - i1I
   for iiiiiIIIIi1 in load_json ( II1Iiii1 ) :
    try :
     oooo000O0 = iiiiiIIIIi1 . get ( 'movie' , iiiiiIIIIi1 . get ( 'show' ) ) [ 'ids' ] [ 'tmdb' ]
     if oooo000O0 :
      iii1ii1 . append ( str ( oooo000O0 ) )
    except :
     pass
     if 65 - 65: ooOOO - Iii1i / i1iiIII111
   if iii1ii1 :
    CACHE . set ( oOOO , iii1ii1 , expiration = timedelta ( hours = 6 ) )
    if 77 - 77: ooOOO . Ii
   return iii1ii1
   if 61 - 61: i1I + I1Ii1I1 / i1 . i1 * ooOOO
 def get_watchlist ( self ) :
  if 69 - 69: i1 . ooo000 % I1Ii1I1 + i1 / i1iiIII111 % IiIIii11Ii
  I1i1iI1IiIi = list ( )
  i1ii1 = list ( )
  if 62 - 62: i1iiIII111
  if self . access_token :
   OOO0OOoo0ooO = "https://api.trakt.tv/users/{0}/watchlist" . format ( self . slug )
   i1iIiii = requests . get ( OOO0OOoo0ooO , headers = self . headers )
   iIiI11I1iI = i1iIiii . json ( )
   iIiI11I1iI . sort ( key = lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ 'listed_at' ] , reverse = True )
   if 39 - 39: I1Ii1I1 / Ooo0Ooo * IIiIIiIi11I1
   for iiiiiIIIIi1 in iIiI11I1iI :
    if 'movie' in iiiiiIIIIi1 :
     if iiiiiIIIIi1 [ 'movie' ] [ 'ids' ] . get ( 'tmdb' ) :
      I1i1iI1IiIi . append ( iiiiiIIIIi1 [ 'movie' ] [ 'ids' ] [ 'tmdb' ] )
    elif 'show' in iiiiiIIIIi1 :
     if iiiiiIIIIi1 [ 'show' ] [ 'ids' ] . get ( 'tmdb' ) :
      i1ii1 . append ( iiiiiIIIIi1 [ 'show' ] [ 'ids' ] [ 'tmdb' ] )
      if 84 - 84: oOO / IiI11Ii111 * IiIIii11Ii
  return I1i1iI1IiIi , i1ii1
  if 29 - 29: I1Ii1I1 % oOo0O00 - oOo0O00 * I1Ii1I1 / Iii1i * i1I
  if 51 - 51: I1Ii1I1 . i1iiIII111 % i1 % i1I * Oo
 def get_recommendations ( self , tipo ) :
  if 64 - 64: i1i1i1111I + i1
  if 45 - 45: i1i1i1111I / i1iiIII111 * iI1iII1I1I1i
  if self . access_token :
   iii1ii1 = list ( )
   oOOO = 'get_recommendations_' + tipo
   if 2 - 2: i1 / i1i1i1111I * IiIIii11Ii
   try :
    II1IiiIIi = CACHE . get ( oOOO )
    if II1IiiIIi :
     return II1IiiIIi
   except : pass
   if 33 - 33: Iii1i
   OOO0OOoo0ooO = "https://api.trakt.tv/recommendations/%s?limit=100" % tipo
   II1Iiii1 = downloadpage ( OOO0OOoo0ooO , headers = self . headers ) . data
   if 7 - 7: Ooo0Ooo - Ooo0Ooo / ooo000 - IiIIii11Ii
   for iiiiiIIIIi1 in load_json ( II1Iiii1 ) :
    try :
     oooo000O0 = iiiiiIIIIi1 [ 'ids' ] [ 'tmdb' ]
     if oooo000O0 :
      iii1ii1 . append ( str ( oooo000O0 ) )
    except :
     pass
     if 70 - 70: IIiIIiIi11I1 . i1 % iI1iII1I1I1i / i1i1i1111I
   if iii1ii1 :
    CACHE . set ( oOOO , iii1ii1 , expiration = timedelta ( hours = 6 ) )
    if 5 - 5: i1iiIII111 . Oo + i1i1i1111I
   return iii1ii1
   if 44 - 44: I1Ii1I1 - i1i1i1111I
 def add_favorite ( self , content , tmdb ) :
  if 71 - 71: i1iiIII111
  OOO0OOoo0ooO = 'https://api.trakt.tv/sync/favorites'
  I1IiI = { content : [ { "ids" : { "tmdb" : int ( tmdb ) } } ] }
  requests . post ( OOO0OOoo0ooO , headers = self . headers , json = I1IiI )
  if 77 - 77: Iii1i - I1Ii1I1 - Ooo0Ooo % Ii / Oo
 def del_favorite ( self , content , tmdb ) :
  if 43 - 43: Ooo0Ooo / oOO
  OOO0OOoo0ooO = 'https://api.trakt.tv/sync/favorites/remove'
  I1IiI = { content : [ { "ids" : { "tmdb" : int ( tmdb ) } } ] }
  requests . post ( OOO0OOoo0ooO , headers = self . headers , json = I1IiI )
  if 93 - 93: ooOOO % oOo0O00 * i1 + Ii . i1I - oOO
 def get_favorite ( self , content ) :
  OOO0OOoo0ooO = 'https://api.trakt.tv/sync/favorites/{0}' . format ( content )
  II1Iiii1 = requests . get ( OOO0OOoo0ooO , headers = self . headers ) . json ( )
  oO = [ pl [ content [ : - 1 ] ] [ 'ids' ] [ 'tmdb' ] for pl in II1Iiii1 ]
  if 1 - 1: oOo0O00 . IiI11Ii111 * I1I - Oo
  return oO
  if 4 - 4: oOo0O00 / i1i1i1111I
 def get_items_list ( self , user , list_id , content , sort_by = None , sort_how = None ) :
  oO = list ( )
  if 61 - 61: oOo0O00
  if 51 - 51: ooOOO - oOO . I1Ii1I1 - IiIIii11Ii
  if 49 - 49: iI1iII1I1I1i / ooOOO . iI1iII1I1I1i
  if 60 - 60: ooOOO / Ii % OooOoo
  OOO0OOoo0ooO = 'https://api.trakt.tv/users/{0}/lists/{1}/items/{2}' . format ( user , list_id , content )
  i1iIiii = requests . get ( OOO0OOoo0ooO , headers = self . headers )
  if 97 - 97: Oo * IiIIii11Ii . Ooo0Ooo % i1 % Ii % ooo000
  try :
   iIiI11I1iI = i1iIiii . json ( )
   if sort_by in [ 'added' ] :
    sort_by = 'listed_at'
    iIiI11I1iI . sort ( key = lambda oOOOOOOoOOooO0O0 : oOOOOOOoOOooO0O0 [ sort_by ] , reverse = True if sort_how == 'desc' else False )
    if 67 - 67: IIiIIiIi11I1 % i1 % oOo0O00 - i1i1i1111I
   oO = [ pl [ content ] [ 'ids' ] [ 'tmdb' ] for pl in iIiI11I1iI if pl [ content ] [ 'ids' ] [ 'tmdb' ] ]
   if 51 - 51: I11iiIi11i1I . I11iiIi11i1I % IiI11Ii111 % Oo / I1Ii1I1 - I1Ii1I1
  except :
   pass
   if 28 - 28: Ii / Ooo0Ooo
  return oO
  if 11 - 11: I1I - OooOoo * ooOOO % i1i1i1111I + ooo000 . oOO
 def get_list ( self ) :
  o000OOO00 = None
  if 51 - 51: ooOOO + iI1iII1I1I1i % IiI11Ii111 . I11iiIi11i1I % Ooo0Ooo
  Ii11 = xbmcgui . Dialog ( ) . input ( localize ( 30512 ) )
  if Ii11 :
   if re . findall ( r'\d+$' , Ii11 ) :
    o000OOO00 = re . findall ( r'\d+$' , Ii11 ) [ 0 ]
   elif re . findall ( r'trakt.tv/users/(.*?)/lists/(.*?)$' , Ii11 . split ( '?' ) [ 0 ] ) :
    if 75 - 75: Oo
    O0o , o000OOO00 = re . findall ( r'trakt.tv/users/(.*?)/lists/(.*?)$' , Ii11 . split ( '?' ) [ 0 ] ) [ 0 ]
    OOoOOo = requests . get ( 'https://api.trakt.tv/users/{0}/lists/{1}' . format ( O0o , o000OOO00 ) , headers = self . headers ) . json ( )
    o000OOO00 = OOoOOo [ 'ids' ] [ 'trakt' ]
    if 73 - 73: oOo0O00
   if not o000OOO00 :
    raise ( )
  else :
   return
   if 69 - 69: ooOOO - IIiIIiIi11I1 - i1I
   if 78 - 78: I1Ii1I1 . ooo000 + IiI11Ii111 / IiI11Ii111
  OOoOOo = requests . get ( 'https://api.trakt.tv/lists/{0}' . format ( o000OOO00 ) , headers = self . headers ) . json ( )
  if 88 - 88: Ii - i1iiIII111 - i1 * IIiIIiIi11I1 . IiIIii11Ii + Iii1i
  if 44 - 44: ooOOO + Oo - i1
  O0o = OOoOOo [ 'user' ] [ 'ids' ] [ 'slug' ]
  oOoOo0OO0o = OOoOOo [ 'name' ] . replace ( '"' , "'" )
  OoOOo0o0ooOO0 = OOoOOo [ 'description' ] . replace ( '"' , "'" )
  OOO = OOoOOo [ 'sort_by' ]
  i11II = OOoOOo [ 'sort_how' ]
  if 18 - 18: iI1iII1I1I1i * ooOOO + Ooo0Ooo
  if OOO == 'released' :
   OOO = 'fecha'
  elif OOO == 'title' :
   OOO = 'titulo'
  else :
   OOO = 'rating'
   i11II = 'desc'
   if 78 - 78: I1I . I1I - IIiIIiIi11I1 - IiIIii11Ii % I11iiIi11i1I . I1Ii1I1
  I1Ii11iiiiiii = xbmcgui . Dialog ( ) . input ( localize ( 30513 ) , oOoOo0OO0o )
  if I1Ii11iiiiiii :
   oOoOo0OO0o = I1Ii11iiiiiii . replace ( '"' , "'" )
   if 59 - 59: IiIIii11Ii
  I11i = '{0}[CR]{1}[CR]' . format ( oOoOo0OO0o , OoOOo0o0ooOO0 ) + localize ( 30514 )
  OoooOo00 = xbmcgui . Dialog ( ) . yesnocustom ( 'EduTeAmo' , I11i , localize ( 30515 ) , localize ( 30101 ) ,
 localize ( 30100 ) )
  if OoooOo00 == 1 :
   iII11I11111I = 'movie'
  elif OoooOo00 == 0 :
   iII11I11111I = 'show'
  else :
   return
   if 91 - 91: IiIIii11Ii + iI1iII1I1I1i
  return ( O0o , o000OOO00 , oOoOo0OO0o , OoOOo0o0ooOO0 , iII11I11111I , OOO , i11II )
  if 65 - 65: Oo * Iii1i * IiIIii11Ii / IIiIIiIi11I1
 def addItem2Trakt ( self , content , tmdb , list_id ) :
  iii1ii1 = - 1
  try :
   if content in [ 'tvshows' , 'seasons' , 'episodes' ] :
    content = 'shows'
   elif content != 'movies' :
    raise ( )
    if 77 - 77: IIiIIiIi11I1 / oOO % IiIIii11Ii + I1Ii1I1
   if list_id == '-1' :
    OOO0OOoo0ooO = 'https://api.trakt.tv/sync/watchlist'
   else :
    OOO0OOoo0ooO = 'https://api.trakt.tv/users/{0}/lists/{1}/items' . format ( self . slug , list_id )
    if 34 - 34: i1i1i1111I * Iii1i + Ii - i1I / i1 / i1
   I1IiI = dict ( )
   I1IiI [ content ] = [ { 'ids' : { 'tmdb' : tmdb } } ]
   OOoOOo = requests . post ( OOO0OOoo0ooO , headers = self . headers , json = I1IiI ) . json ( )
   if 87 - 87: Ooo0Ooo + I11iiIi11i1I
   if OOoOOo [ 'added' ] [ content ] :
    iii1ii1 = 1
   elif OOoOOo [ 'existing' ] [ content ] :
    iii1ii1 = 0
  except : pass
  if 3 - 3: IIiIIiIi11I1 . I1Ii1I1 / Iii1i % ooOOO / oOo0O00 % ooOOO
  return iii1ii1
  if 55 - 55: iI1iII1I1I1i + I1I + oOo0O00 - I11iiIi11i1I
 def addRatings ( self , content , label , tmdb , seasonNumber = 1 , episodeNumber = 1 , forzado = False ) :
  if not forzado :
   o0O0oOoO = get_setting ( 'probAddRanting' )
   if not random . choices ( [ True , False ] , weights = ( o0O0oOoO , 100 - o0O0oOoO ) ) [ 0 ] :
    return
    if 36 - 36: ooOOO + oOo0O00 + OooOoo / i1 % IiI11Ii111 . ooo000
  if self . access_token and content in [ 'tvshows' , 'tvshow' , 'seasons' , 'episodes' , 'movies' , 'movie' ] :
   if content in [ 'tvshows' , 'tvshow' ] :
    oo0OOOOOO0o00 = "Â¿Que te pareciÃ³ esta serie?"
   elif content == 'seasons' :
    oo0OOOOOO0o00 = "Â¿Que te pareciÃ³ esta temporada?"
   elif content == 'episodes' :
    oo0OOOOOO0o00 = "Â¿Que te pareciÃ³ este episodio?"
   else :
    oo0OOOOOO0o00 = "Â¿Que te pareciÃ³ esta pelÃ­cula?"
    if 74 - 74: i1 + oOO
   OOo00oOoOo = oO0ooOo0OOOO ( content , oo0OOOOOO0o00 , label )
   OOo00oOoOo . doModal ( )
   if 34 - 34: iI1iII1I1I1i + IIiIIiIi11I1 . i1I . IiI11Ii111 % i1i1i1111I
   if OOo00oOoOo . rating :
    oo0O0OOooo = OOo00oOoOo . rating
    OOO0OOoo0ooO = "https://api.trakt.tv/sync/ratings"
    if content in [ 'tvshows' , 'tvshow' ] :
     I1IiI = { 'shows' : [ { 'rating' : oo0O0OOooo , 'ids' : { 'tmdb' : tmdb } } ] }
    elif content == 'seasons' :
     I1IiI = { 'shows' : [ { 'ids' : { 'tmdb' : tmdb } , 'seasons' : [ { 'rating' : oo0O0OOooo , 'number' : seasonNumber } ] } ] }
    elif content == 'episodes' :
     I1IiI = { 'shows' : [ { 'ids' : { 'tmdb' : tmdb } , 'seasons' : [
 { 'number' : seasonNumber , 'episodes' : [ { "rating" : oo0O0OOooo , "number" : episodeNumber } ] } ] } ] }
    else :
     I1IiI = { 'movies' : [ { 'rating' : oo0O0OOooo , 'ids' : { 'tmdb' : tmdb } } ] }
     if 26 - 26: i1I - OooOoo - i1iiIII111
    OOoOOo = requests . post ( OOO0OOoo0ooO , headers = self . headers , json = I1IiI )
    if 92 - 92: IIiIIiIi11I1 . i1iiIII111
   del OOo00oOoOo
   if 81 - 81: Ii + Iii1i
   if 58 - 58: I1Ii1I1 / I1Ii1I1 % IIiIIiIi11I1
class oO0ooOo0OOOO ( xbmcgui . WindowXMLDialog ) :
 buttons = { 11030 : 1 , 11031 : 2 , 11032 : 3 , 11033 : 4 , 11034 : 5 , 11035 : 6 , 11036 : 7 , 11037 : 8 , 11038 : 9 , 11039 : 10 }
 if 98 - 98: OooOoo
 def __init__ ( self , content , title , label ) :
  self . title = title
  self . label = label
  self . rating = None
  self . default_rating = 5
  if 79 - 79: Ooo0Ooo * Ooo0Ooo - ooo000 - Iii1i
  if content == 'episodes' :
   self . focus_labels = {
 11030 : "Â¡Apesta!" ,
 11031 : "Terrible" ,
 11032 : "Malo" ,
 11033 : "Pobre" ,
 11034 : "Ni fÃº, ni fÃ¡" ,
 11035 : "Justo" ,
 11036 : "Bueno" ,
 11037 : "Muy Bueno" ,
 11038 : "Espectacular" ,
 11039 : "Â¡Una pasada!"
 }
  else :
   self . focus_labels = {
 11030 : "Â¡Apesta!" ,
 11031 : "Terrible" ,
 11032 : "Mala" ,
 11033 : "Pobre" ,
 11034 : "Ni fÃº, ni fÃ¡" ,
 11035 : "Justa" ,
 11036 : "Buena" ,
 11037 : "Muy Buena" ,
 11038 : "Espectacular" ,
 11039 : "Â¡Una pasada!"
 }
   if 5 - 5: IiIIii11Ii / i1iiIII111 . I1I % Iii1i . i1
 def __new__ ( cls , content , title , label ) :
  return super ( oO0ooOo0OOOO , cls ) . __new__ ( cls , "RatingDialog.xml" , 'special://home/addons/plugin.video.eduteamo' )
  if 29 - 29: oOo0O00 + Oo / I11iiIi11i1I - oOo0O00 % i1i1i1111I / Ii
 def onInit ( self ) :
  self . getControl ( 10011 ) . setLabel ( self . title )
  self . getControl ( 10012 ) . setLabel ( self . label )
  if 39 - 39: I11iiIi11i1I - I11iiIi11i1I % i1iiIII111
  oOOooOo = 11029 + self . default_rating
  self . setFocus ( self . getControl ( oOOooOo ) )
  if 30 - 30: OooOoo * I1I
 def onClick ( self , controlID ) :
  if controlID in self . buttons :
   self . rating = self . buttons [ controlID ]
   self . close ( )
   if 94 - 94: i1I
 def onFocus ( self , controlID ) :
  if controlID in self . focus_labels :
   i1iII1 = '{0} - {1}' . format ( self . buttons [ controlID ] , self . focus_labels [ controlID ] )
   self . getControl ( 10013 ) . setLabel ( i1iII1 )
  else :
   self . getControl ( 10013 ) . setLabel ( '' )
