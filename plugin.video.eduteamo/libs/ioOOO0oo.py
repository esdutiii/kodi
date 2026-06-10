# -*- coding: utf-8 -*-
if 82 - 82: Iii1i
import copy
import os
import sys
import re
import base64
import requests
import random
import string
import time
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import xbmc
import xbmcgui
import xbmcvfs
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from threading import Thread
from urllib import parse
from datetime import timedelta , timezone , datetime
from libs . ioiIIIiII import downloadpage , DEFAULT_HEADERS
from libs . iooooooOoO0 import logger , AES , p3b64encode , Proxydatetime , set_setting , load_json , get_setting , CACHE , p3b64decode , localize
from libs . ioiiI1II1 import MoriaDB
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
if 98 - 98: I11iiIi11i1I % oOO
def get_url ( enlace ) :
 i1ii1 = ""
 ooo0O0oO00 = ""
 o00o0OO00O = ""
 if 57 - 57: iiIi1 - ii % Ii * i1i1i1111I / Ii
 if isinstance ( enlace , tuple ) :
  ooO0Oo0o00 = enlace [ 0 ]
  o00o0OO00O = enlace [ 1 ]
  if len ( enlace ) > 2 :
   i1ii1 = enlace [ 2 ]
   ooo0O0oO00 = enlace [ 3 ]
 else :
  ooO0Oo0o00 = enlace
 if 74 - 74: IIiIIiIi11I1 / I1I - Oo . Ooo0Ooo
 if 46 - 46: iI1iII1I1I1i - Ii * Oo * Ii
 if 52 - 52: Oo + I1I / oOO / OooOoo - I1Ii1I1 - ooOOO
 if 60 - 60: iI1iII1I1I1i . oOO
 if 13 - 13: oOO
 if 2 - 2: i1
 if 22 - 22: IIiIIiIi11I1 - ooo000 / I1Ii1I1 . ooo000
 if 1 - 1: iI1iII1I1I1i + Ooo0Ooo + oOO * IIiIIiIi11I1
 if 20 - 20: I1I + Ii
 if 75 - 75: Ii % i1iiIII111 * Ii . IIiIIiIi11I1 % I11iiIi11i1I % I1Ii1I1
 if 8 - 8: I1Ii1I1 . ii . i1 . Oo - iiIi1
 if 32 - 32: Ii % i1i1i1111I % iiIi1 - I11iiIi11i1I % i1iiIII111
 if 34 - 34: i1iiIII111 * i1
 if 34 - 34: oOo0O00 / i1iiIII111 - Iii1i . iI1iII1I1I1i
 if 80 - 80: i1i1i1111I . I1I % ooOOO % IiIIii11Ii / i1i1i1111I
 if 32 - 32: I1Ii1I1 + oOO - oOo0O00
 if 79 - 79: Iii1i % oOO * Oo + ooOOO / Oo . oOO
 if 20 - 20: ii + i1iiIII111 / I1I
 if 88 - 88: I11iiIi11i1I + ooOOO - i1i1i1111I . Ooo0Ooo * Ii + Iii1i
 if 43 - 43: ooOOO * I1Ii1I1
 if 95 - 95: Ooo0Ooo % Iii1i % i1i1i1111I . OooOoo
 I1iIiiIIiIi = { "label" : 'One' ,
 "servidor" : '1fichier' ,
 "url" : str ( ooO0Oo0o00 ) ,
 "audio" : i1ii1 ,
 "info" : ooo0O0oO00 ,
 "quality" : o00o0OO00O
 }
 if 88 - 88: Oo * IiIIii11Ii
 return I1iIiiIIiIi
 if 100 - 100: ii - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
 if 23 - 23: Ooo0Ooo + i1 * I1Ii1I1 + Oo * Ii - IIiIIiIi11I1
class Resolver ( object ) :
 subresolver = None
 if 29 - 29: IiIIii11Ii - oOo0O00
 def __new__ ( cls , enlace ) :
  if get_setting ( 'Alldebrid_enabled' ) and enlace . get ( 'servidor' ) in cls . getHosts ( 'Alldebrid' ) :
   cls . subresolver = "Alldebrid"
   enlace [ 'label' ] = enlace . get ( 'label' , '' ) + ' [Alldebrid]'
   if 30 - 30: I1I . ooo000
  elif get_setting ( 'Realdebrid_enabled' ) and enlace . get ( 'servidor' ) in cls . getHosts ( 'Realdebrid' ) :
   cls . subresolver = "Realdebrid"
   enlace [ 'label' ] = enlace . get ( 'label' , '' ) + ' [Realdebrid]'
   if 43 - 43: ooOOO . I11iiIi11i1I + ooo000
  elif enlace . get ( 'servidor' ) in [ "darkibox" ] :
   cls . subresolver = "Darkibox"
   if 87 - 87: Iii1i + ooOOO . iiIi1 / Ii + Oo
  elif enlace . get ( 'servidor' ) in [ "1fichier" , "One" ] :
   if os . path . exists ( os . path . join ( xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/' ) , '1fichier.txt' ) ) :
    cls . subresolver = "fichier"
   else :
    xbmcgui . Dialog ( ) . ok ( 'EduTeAmo' , localize ( 30506 ) )
    return
    if 77 - 77: i1iiIII111 + ii - Oo % ooo000
    if 74 - 74: Ii + Ooo0Ooo
    if 1 - 1: I1I % Ooo0Ooo + i1iiIII111 . i1iiIII111 % Oo
  else :
   if 93 - 93: oOo0O00 % Ooo0Ooo * i1iiIII111
   cls . subresolver = "Externo"
   enlace [ 'label' ] = enlace . get ( 'label' , '' ) + ' [ResolveUrl]'
   if 52 - 52: oOO + I1I / ooo000 - I1Ii1I1 * iiIi1 % oOo0O00
  return object . __new__ ( type ( cls . __name__ , ( getattr ( sys . modules [ __name__ ] , cls . subresolver ) , Resolver ) , { } ) )
  if 52 - 52: oOo0O00 . I1I + iiIi1 - i1iiIII111 % iI1iII1I1I1i
  if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
 @ classmethod
 def getHosts ( cls , debrid ) :
  I1iIiiIIiIi = list ( )
  Oo0 = ''
  if 40 - 40: OooOoo / Iii1i
  if debrid . lower ( ) == 'alldebrid' :
   Oo0 = "https://api.alldebrid.com/v4/hosts?agent=ResolveURL%20for%20Kodi&hostsOnly"
  elif debrid . lower ( ) == 'realdebrid' :
   Oo0 = "https://api.real-debrid.com/rest/1.0/hosts/domains"
   if 6 - 6: ii - i1i1i1111I
  try :
   O0o00OOOoo00 = CACHE . get ( Oo0 )
   if O0o00OOOoo00 : return O0o00OOOoo00
  except :
   pass
   if 1 - 1: Ooo0Ooo
  try :
   i1Ii1iiIiI111 = downloadpage ( Oo0 ) . data
   if 77 - 77: ii - I11iiIi11i1I * Ooo0Ooo
   if debrid . lower ( ) == 'alldebrid' :
    i1Ii1iiIiI111 = load_json ( i1Ii1iiIiI111 )
    if 71 - 71: IIiIIiIi11I1 / ooOOO - ooOOO / I11iiIi11i1I
    for oOo0Oo , O0ooooO in i1Ii1iiIiI111 [ 'data' ] [ 'hosts' ] . items ( ) :
     if oOo0Oo in [ 'darkibox' ] and O0ooooO . get ( 'status' , False ) == False :
      continue
     I1iIiiIIiIi . append ( oOo0Oo )
     if 89 - 89: I1I * i1i1i1111I
   elif debrid . lower ( ) == 'realdebrid' :
    I1iIiiIIiIi = [ oOo0Oo . split ( '.' ) [ 0 ] for oOo0Oo in eval ( i1Ii1iiIiI111 ) ]
    if 54 - 54: oOO + Ooo0Ooo - I1I . Ooo0Ooo
  except :
   I1iIiiIIiIi = [ '1fichier' ]
   if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
  try :
   if len ( I1iIiiIIiIi ) > 1 :
    CACHE . set ( Oo0 , I1iIiiIIiIi , expiration = timedelta ( hours = 12 ) )
  except :
   pass
   if 54 - 54: oOO * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
  return I1iIiiIIiIi
  if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - ii
 def __init__ ( self , enlace ) :
  self . url = enlace . get ( 'url' )
  self . servidor = enlace . get ( 'servidor' )
  self . enlace_label = enlace . get ( 'label' )
  if 69 - 69: ooo000
  if self . url :
   iIiIiiIIIiII = "%s %s..." % ( localize ( 30042 ) , self . enlace_label )
   self . dialog = P3DialogAnimation ( 'EduTeAmo' , iIiIiiIIIiII )
   if not self . url . startswith ( 'http' ) :
    if 44 - 44: Ooo0Ooo + i1i1i1111I + Iii1i - oOO
    I1i1i = b'hTh8uRnL5bX8PZC6Tc3t46nVDFfBpB6Tjw3qazQThpexpg8bLdimevNHj5vJR0nP'
    O0ooooO = base64 . b64decode ( I1i1i )
    ii1ii = AES . new ( O0ooooO [ 16 : ] , AES . MODE_OFB , O0ooooO [ : 16 ] )
    self . url = ii1ii . decrypt ( base64 . urlsafe_b64decode ( self . url ) ) . decode ( )
  else :
   iIiIiiIIIiII = ""
   if 17 - 17: Oo * I1I % ooOOO - IiIIii11Ii
   if 22 - 22: Oo % oOo0O00 / iiIi1 . oOo0O00 . iiIi1
   if 87 - 87: I1I - iiIi1 . i1 * Oo
 def __call__ ( self ) :
  ooO0O0Oo00O = list ( )
  iIiIiiIIIiII = [ '' ]
  if 2 - 2: Oo - IiIIii11Ii - iI1iII1I1I1i * OooOoo
  o00O00OOO00OO = Thread ( target = self . resolve_url , args = [ ooO0O0Oo00O , iIiIiiIIIiII ] )
  o00O00OOO00OO . daemon = True
  o00O00OOO00OO . start ( )
  if 32 - 32: ooOOO
  while not self . dialog . iscanceled ( ) and o00O00OOO00OO . is_alive ( ) :
   xbmc . sleep ( 250 )
   if 58 - 58: iiIi1 - ii
  if self . dialog . iscanceled ( ) :
   ooO0O0Oo00O = [ ]
   iIiIiiIIIiII . insert ( 0 , localize ( 30043 ) )
   if 86 - 86: Iii1i + i1iiIII111 - IIiIIiIi11I1 / I1I
  self . dialog . close ( )
  return ooO0O0Oo00O , iIiIiiIIIiII [ 0 ]
  if 46 - 46: ooOOO + ooOOO % oOO
  if 2 - 2: i1i1i1111I / Ooo0Ooo / oOO - IIiIIiIi11I1 / IIiIIiIi11I1
 def countdown ( self , timedown ) :
  iIiIiiIIIiII = self . dialog . message
  while timedown > 0 :
   self . dialog . update ( localize ( 30060 ) % ( iIiIiiIIIiII , timedown ) )
   xbmc . sleep ( 1000 )
   timedown -= 1
  self . dialog . message = iIiIiiIIIiII
  if 58 - 58: i1i1i1111I
  if 38 - 38: i1 - oOo0O00
 def remove_white_spaces ( self , html ) :
  if 85 - 85: IIiIIiIi11I1 + I11iiIi11i1I % Ooo0Ooo + oOO * i1iiIII111
  OOOoo0 = chr ( 92 ) + chr ( 92 ) . join ( [ 'n|' , 'r|' , 't|' , 's{2}|&nbsp;' ] )
  return re . sub ( OOOoo0 , '' , html )
  if 25 - 25: oOO . I1Ii1I1 * I1I
 def resolve_url ( self , itemlist , msg ) :
  raise NotImplementedError ( )
  if 28 - 28: ooOOO - iiIi1 * ii % Oo + oOo0O00 / i1
  if 47 - 47: Iii1i + oOO
class Alldebrid ( Resolver ) :
 AGENT = 'EduTeAmo'
 if 17 - 17: Ii . oOo0O00 % OooOoo
 def authorize_resolver ( self ) :
  def o0 ( check_url ) :
   I1iIiiIIiIi = False
   i1Ii1iiIiI111 = downloadpage ( check_url ) . data
   if "success" in i1Ii1iiIiI111 :
    i1Ii1iiIiI111 = load_json ( i1Ii1iiIiI111 ) . get ( 'data' )
    if i1Ii1iiIiI111 . get ( "activated" ) :
     set_setting ( 'Alldebrid_apikey' , i1Ii1iiIiI111 . get ( 'apikey' , '' ) )
     I1iIiiIIiIi = True
   elif i1Ii1iiIiI111 . get ( 'error' ) :
    logger ( i1Ii1iiIiI111 . get ( 'message' , 'Alldebrid Pin Error' ) )
   return I1iIiiIIiIi
   if 37 - 37: iI1iII1I1I1i - I1Ii1I1 + ooOOO . IIiIIiIi11I1
  set_setting ( 'Alldebrid_apikey' , '' )
  iIi111ii = Iii = False
  oOOOO0OO00 = - 1
  i1Ii1iiIiI111 = downloadpage ( "https://api.alldebrid.com/v4/pin/get?agent=%s" % self . AGENT ) . data
  if 8 - 8: Oo * I1I / i1i1i1111I + i1 / I1Ii1I1
  if "success" in i1Ii1iiIiI111 :
   i1Ii1iiIiI111 = load_json ( i1Ii1iiIiI111 ) . get ( 'data' )
   if i1Ii1iiIiI111 . get ( "check_url" ) :
    oOOOO0OO00 = i1Ii1iiIiI111 . get ( "expires_in" , 130 )
    iIiIiiIIIiII = localize ( 30074 ) % ( 'Alldebrid' , i1Ii1iiIiI111 . get ( "base_url" , "" ) , i1Ii1iiIiI111 . get ( "pin" , "" ) ) + localize ( 30075 )
    while not self . dialog . iscanceled ( ) and oOOOO0OO00 > 0 :
     if oOOOO0OO00 % 5 == 0 and o0 ( i1Ii1iiIiI111 . get ( "check_url" ) ) :
      iIi111ii = True
      break
     xbmc . sleep ( 1000 )
     oOOOO0OO00 -= 1
     self . dialog . update ( iIiIiiIIIiII % divmod ( oOOOO0OO00 , 60 ) )
    self . dialog . close ( )
    if 71 - 71: I1Ii1I1
   if iIi111ii :
    if 1 - 1: ii - oOo0O00 - i1 . oOo0O00
    Iii = localize ( 30076 ) % 'Alldebrid'
   elif oOOOO0OO00 == 0 :
    if 91 - 91: iI1iII1I1I1i * i1 . ooOOO
    Iii = localize ( 30078 )
   elif not self . dialog . iscanceled ( ) :
    if 81 - 81: I1I * Oo - i1 % OooOoo * ooOOO
    Iii = localize ( 30077 ) % 'Alldebrid'
   if Iii :
    xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' , Iii ,
 "special://home/addons/plugin.video.eduteamo/resources/media/alldebrid.png" )
    if 19 - 19: Ii
   return iIi111ii
   if 22 - 22: iiIi1 % iI1iII1I1I1i + Oo
 def getExpiration ( self ) :
  I1iIiiIIiIi = None
  try :
   OOO00OOo0oO0O = get_setting ( 'Alldebrid_apikey' )
   if OOO00OOo0oO0O :
    Oo0 = "https://api.alldebrid.com/v4/user?agent={0}&apikey={1}" . format ( self . AGENT , OOO00OOo0oO0O )
    i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 ) . data )
    oo0 = i1Ii1iiIiI111 . get ( 'data' , [ ] ) . get ( 'user' )
    if not oo0 [ 'isTrial' ] and oo0 [ 'isPremium' ] :
     I1iIiiIIiIi = Proxydatetime . fromtimestamp ( oo0 [ 'premiumUntil' ] )
  except : pass
  return I1iIiiIIiIi
  if 74 - 74: ooOOO . Ii % IIiIIiIi11I1 / iI1iII1I1I1i % ooOOO
 def deleteRemoteHistory ( self ) :
  try :
   downloadpage (
 url = 'https://api.alldebrid.com/v4/user/history/delete?agent=EduTeAmo&apikey=%s' % get_setting (
 'Alldebrid_apikey' ) )
  except : pass
  if 24 - 24: IIiIIiIi11I1 - IIiIIiIi11I1 . Ooo0Ooo + i1iiIII111 + Oo
 def resolve_url ( self , itemlist , msg ) :
  if get_setting ( 'Alldebrid_apikey' ) or self . authorize_resolver ( ) :
   Oo0 = "https://api.alldebrid.com/v4/link/unlock?agent=%s&apikey=%s" % (
 self . AGENT , get_setting ( 'Alldebrid_apikey' ) )
   if 21 - 21: IIiIIiIi11I1 - ooo000 + oOO
   i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 + "&link=%s" % parse . quote_plus ( self . url ) ,
 headers = { 'User-Agent' : self . AGENT } ) . data )
   if 5 - 5: i1iiIII111 . i1iiIII111 + ooo000 . I11iiIi11i1I
   if i1Ii1iiIiI111 . get ( "status" , "error" ) == 'success' :
    Iii1I1I1 = None
    try :
     oO0oO = ( self . getExpiration ( ) - Proxydatetime . now ( ) ) . days
     if 57 - 57: Oo - ii . I1Ii1I1 / oOO + oOO . Ooo0Ooo
     if oO0oO == 0 :
      Iii1I1I1 = 'La cuenta caduca hoy'
     elif 6 > oO0oO and oO0oO > 0 and get_setting ( 'Alldebrid_info' ) :
      Iii1I1I1 = '{0} caducara en {1} dias' . format ( self . __class__ . subresolver , oO0oO )
      if 12 - 12: iI1iII1I1I1i . Oo
     if Iii1I1I1 :
      logger ( Iii1I1I1 )
      xbmcgui . Dialog ( ) . notification ( "EduTeAmo" , Iii1I1I1 ,
 "special://home/addons/plugin.video.eduteamo/resources/media/alldebrid.png" )
    except : pass
    if 83 - 83: oOo0O00 - I11iiIi11i1I
    ooO0Oo0o00 = i1Ii1iiIiI111 [ 'data' ] . get ( 'link' )
    itemlist . append ( Video ( server = self . enlace_label , url = ooO0Oo0o00 , res = 'Original' ) )
    if 91 - 91: IIiIIiIi11I1 - i1 - iI1iII1I1I1i
   elif i1Ii1iiIiI111 . get ( "error" ) :
    I111i = i1Ii1iiIiI111 [ 'error' ] . get ( "message" , "Generic unlocking error." )
    if 'apikey is invalid' in I111i :
     set_setting ( 'Alldebrid_apikey' , '' )
     self . resolve_url ( itemlist , msg )
     return
     if 9 - 9: i1iiIII111 - ooOOO % Iii1i
    msg . insert ( 0 , "%s: %s" % ( self . enlace_label , I111i ) )
    itemlist = [ ]
    if 37 - 37: iiIi1 + IIiIIiIi11I1 % iI1iII1I1I1i / IIiIIiIi11I1 % i1iiIII111 + oOO
   self . deleteRemoteHistory ( )
   if 98 - 98: iI1iII1I1I1i - I1I + i1 * ooo000 % i1
  else :
   itemlist = [ ]
   msg . insert ( 0 , "%s: %s" % ( self . enlace_label , localize ( 30077 ) ) )
   if 100 - 100: i1iiIII111 . IIiIIiIi11I1 * ooo000 * ooo000
class Realdebrid ( Resolver ) :
 def getToken ( self , device_code = None ) :
  try :
   Oo0 = "https://api.real-debrid.com/oauth/v2/token"
   Iioo0Oo0oO0 = { "grant_type" : "http://oauth.net/grant_type/device/1.0" ,
 "client_id" : get_setting ( 'Realdebrid_client_id' ) ,
 "client_secret" : get_setting ( 'Realdebrid_client_secret' ) ,
 "code" : get_setting ( 'Realdebrid_refresh_token' ) or device_code
 }
   i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 , post = Iioo0Oo0oO0 ) . data )
   set_setting ( 'Realdebrid_token' , i1Ii1iiIiI111 . get ( 'access_token' , '' ) )
   set_setting ( 'Realdebrid_refresh_token' , i1Ii1iiIiI111 . get ( 'refresh_token' , '' ) )
   return True
  except :
   return False
   if 20 - 20: IIiIIiIi11I1
 def authorize_resolver ( self ) :
  def O0O0oO00OO0 ( ) :
   Oo0 = "https://api.real-debrid.com/oauth/v2/device/credentials?client_id=X245A4XAIBGVM&code=%s" % ooo00Oo0oOo
   i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 ) . data )
   if "client_secret" in i1Ii1iiIiI111 :
    set_setting ( 'Realdebrid_client_id' , i1Ii1iiIiI111 . get ( 'client_id' , '' ) )
    set_setting ( 'Realdebrid_client_secret' , i1Ii1iiIiI111 . get ( 'client_secret' , '' ) )
    return True
    if 98 - 98: Oo * I1Ii1I1 - oOo0O00 * Ii . Ii + oOo0O00
  if get_setting ( 'Realdebrid_refresh_token' ) and get_setting ( 'Realdebrid_client_secret' ) and get_setting (
 'Realdebrid_client_id' ) :
   self . getToken ( )
   return True
   if 46 - 46: OooOoo - I11iiIi11i1I / Ooo0Ooo
   if 73 - 73: I1Ii1I1 / i1i1i1111I / ooo000 % i1 % iiIi1 - OooOoo
   if 30 - 30: ooOOO * ooOOO - Iii1i * iI1iII1I1I1i
  Oo0 = "https://api.real-debrid.com/oauth/v2/device/code?client_id=X245A4XAIBGVM&new_credentials=yes"
  i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 ) . data )
  ooo00Oo0oOo = i1Ii1iiIiI111 . get ( "device_code" )
  if 37 - 37: I1Ii1I1 % iI1iII1I1I1i . iiIi1 + Ooo0Ooo + ooOOO * iI1iII1I1I1i
  if 39 - 39: IIiIIiIi11I1 - Oo
  iIi111ii = Iii = False
  oOOOO0OO00 = i1Ii1iiIiI111 . get ( "expires_in" , 130 )
  iIiIiiIIIiII = localize ( 30074 ) % ( 'Real-Debrid' , i1Ii1iiIiI111 . get ( "verification_url" , "" ) , i1Ii1iiIiI111 . get ( "user_code" , "" ) ) + localize ( 30075 )
  while not self . dialog . iscanceled ( ) and oOOOO0OO00 > 0 :
   if oOOOO0OO00 % 5 == 0 and O0O0oO00OO0 ( ) :
    iIi111ii = True
    break
   xbmc . sleep ( 1000 )
   oOOOO0OO00 -= 1
   self . dialog . update ( iIiIiiIIIiII % divmod ( oOOOO0OO00 , 60 ) )
  self . dialog . close ( )
  if 31 - 31: IiIIii11Ii % oOo0O00 % oOo0O00 * Iii1i
  if iIi111ii :
   if self . getToken ( ooo00Oo0oOo ) :
    if 85 - 85: Iii1i + Ii % IIiIIiIi11I1 % oOo0O00
    Iii = localize ( 30076 ) % 'RealDebrid'
  elif oOOOO0OO00 == 0 :
   if 100 - 100: IiIIii11Ii % i1
   Iii = localize ( 30078 )
  elif not self . dialog . iscanceled ( ) :
   if 82 - 82: ooOOO % OooOoo
   Iii = localize ( 30077 ) % 'RealDebrid'
  if Iii :
   xbmcgui . Dialog ( ) . notification ( 'EduTeAmo' , Iii ,
 "special://home/addons/plugin.video.eduteamo/resources/media/realdebrid.png" )
   if 81 - 81: Ii
  return iIi111ii
  if 40 - 40: iiIi1 . OooOoo + oOo0O00 . i1iiIII111
 def getExpiration ( self ) :
  I1iIiiIIiIi = None
  try :
   if get_setting ( 'Realdebrid_token' ) :
    Oo0 = "https://api.real-debrid.com/rest/1.0/user"
    oo0O0 = { 'Authorization' : 'Bearer %s' % get_setting ( 'Realdebrid_token' ) }
    i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 , headers = oo0O0 ) . data )
    if i1Ii1iiIiI111 . get ( 'error' ) == 'bad_token' :
     if get_setting ( 'Realdebrid_refresh_token' ) and get_setting (
 'Realdebrid_client_secret' ) and get_setting (
 'Realdebrid_client_id' ) :
      self . getToken ( )
      I1iIiiIIiIi = self . getExpiration ( )
    elif i1Ii1iiIiI111 [ 'type' ] == "premium" :
     if 65 - 65: ooOOO / oOo0O00 - i1iiIII111
     I1iIiiIIiIi = Proxydatetime . strptime ( i1Ii1iiIiI111 [ 'expiration' ] . split ( '.' ) [ 0 ] , "%Y-%m-%dT%H:%M:%S" )
  except : pass
  return I1iIiiIIiIi
  if 15 - 15: OooOoo . ooo000 / IiIIii11Ii % i1i1i1111I
 def _copy1F ( self , link ) :
  I1iIiiIIiIi = None
  o0oOO0 = '' . join ( random . choices ( string . ascii_uppercase + string . digits , k = 14 ) )
  o0oOO0 += str ( time . time ( ) ) . split ( '.' ) [ 0 ]
  if 96 - 96: iiIi1 + IiIIii11Ii - i1 . Iii1i - oOO % i1iiIII111
  with MoriaDB ( ) as iI1I1IiiiiII :
   i1iII = iI1I1IiiiiII . executeSelect ( "SELECT * FROM keys ORDER BY RANDOM() LIMIT 1;" ) [ 0 ] [ 0 ]
  i1iII = p3b64decode ( i1iII ) . decode ( "utf-8" )
  if 48 - 48: oOO * iiIi1 - OooOoo * Oo - ii - Ooo0Ooo
  if 36 - 36: IiIIii11Ii
  if 28 - 28: i1 - Oo + IiIIii11Ii * oOO
  if 83 - 83: ooo000 . I1I + Oo
  if 59 - 59: I1I
  if 83 - 83: Iii1i % i1iiIII111 . OooOoo / I1I % oOO . I1I
  if 76 - 76: i1iiIII111 / OooOoo
  if 77 - 77: ooOOO
  iIii1iiiIi = requests . post ( 'https://api.1fichier.com/v1/file/cp.cgi' ,
 headers = { "Authorization" : "Bearer {0}" . format ( i1iII ) ,
 "Content-Type" : "application/json" } ,
 json = { "urls" : [ self . url ] , "rename" : o0oOO0 } )
  if iIii1iiiIi . ok :
   oOoo = iIii1iiiIi . json ( )
   if 95 - 95: Oo % i1i1i1111I * iI1iII1I1I1i - IiIIii11Ii
   if oOoo . get ( 'urls' ) :
    link = oOoo [ 'urls' ] [ 0 ] [ 'to_url' ]
   else :
    logger ( "Error _copy1F: {0}" . format ( i1iII ) )
    if 66 - 66: iI1iII1I1I1i . i1 % Ii % I11iiIi11i1I * oOo0O00
  return link
  if 59 - 59: Ii . ooo000 - Oo - iI1iII1I1I1i - i1i1i1111I . i1iiIII111
 def resolve_url ( self , itemlist , msg ) :
  if get_setting ( 'Realdebrid_token' ) or self . authorize_resolver ( ) :
   if 78 - 78: OooOoo . ooOOO
   for O0OO00Oo0o0 in [ 1 , 2 ] :
    if O0OO00Oo0o0 == 1 :
     ooO0Oo0o00 = self . url
    else :
     ooO0Oo0o00 = self . _copy1F ( self . url )
     if 84 - 84: I1I * iI1iII1I1I1i - Ooo0Ooo / iI1iII1I1I1i + ooo000
    Oo0 = "https://api.real-debrid.com/rest/1.0/unrestrict/link"
    oo0O0 = { 'Authorization' : 'Bearer %s' % get_setting ( 'Realdebrid_token' ) }
    i1Ii1iiIiI111 = load_json ( downloadpage ( Oo0 , headers = oo0O0 , post = { 'link' : ooO0Oo0o00 } ) . data )
    if 54 - 54: i1iiIII111 . i1iiIII111 - ooOOO * OooOoo + IIiIIiIi11I1 * i1i1i1111I
    if 'download' in i1Ii1iiIiI111 :
     itemlist . append ( Video ( server = self . enlace_label , url = i1Ii1iiIiI111 [ 'download' ] ) )
     Iii1I1I1 = None
     try :
      oO0oO = ( self . getExpiration ( ) - Proxydatetime . now ( ) ) . days
      if 12 - 12: i1i1i1111I
      if oO0oO == 0 :
       Iii1I1I1 = 'La cuenta caduca hoy'
      elif 6 > oO0oO and oO0oO > 0 and get_setting ( 'Realdebrid_info' ) :
       Iii1I1I1 = '{0} caducara en {1} dias' . format ( self . __class__ . subresolver , oO0oO )
       if 56 - 56: IiIIii11Ii
      if Iii1I1I1 :
       logger ( Iii1I1I1 )
       xbmcgui . Dialog ( ) . notification ( "EduTeAmo" , Iii1I1I1 ,
 "special://home/addons/plugin.video.eduteamo/resources/media/realdebrid.png" )
     except : pass
     break
     if 17 - 17: iiIi1 . oOO % Oo + IiIIii11Ii - Ooo0Ooo
    elif i1Ii1iiIiI111 . get ( 'error' ) == 'bad_token' :
     set_setting ( 'Realdebrid_token' , '' )
     self . resolve_url ( itemlist , msg )
     break
     if 93 - 93: oOo0O00
    elif i1Ii1iiIiI111 . get ( 'error' ) == 'unavailable_file' :
     logger ( "error RD: fichero eliminado: %s" % ooO0Oo0o00 , "error" )
     break
     if 77 - 77: Oo + I11iiIi11i1I % I1I
    else :
     if 20 - 20: i1 - IiIIii11Ii . IiIIii11Ii % ooOOO . i1 % Ooo0Ooo
     logger ( "error RD: %s" % i1Ii1iiIiI111 )
     if 72 - 72: oOO % ii . ooOOO * I1Ii1I1 . ooOOO
     if 90 - 90: IiIIii11Ii + I1Ii1I1 . OooOoo
     if 73 - 73: i1i1i1111I - Iii1i / I11iiIi11i1I . ooo000 / iI1iII1I1I1i - i1iiIII111
class Externo ( Resolver ) :
 def resolve_url ( self , itemlist , msg ) :
  try :
   import resolveurl
   if resolveurl . HostedMediaFile ( self . url ) :
    Oo0 = resolveurl . resolve ( self . url )
    if Oo0 :
     itemlist . append ( Video ( server = self . enlace_label , url = Oo0 ) )
  except ModuleNotFoundError :
   msg . insert ( 0 , "%s: %s" % ( self . enlace_label , localize ( 30152 ) ) )
  except Exception as I1I11i :
   msg . insert ( 0 , "%s: %s" % ( self . enlace_label , I1I11i ) )
   if 7 - 7: ii / Ii
   if 87 - 87: ooOOO
class Darkibox ( Resolver ) :
 def resolve_url ( self , itemlist , msg ) :
  i1Ii1iiIiI111 = downloadpage ( self . url ) . data
  self . countdown ( 60 )
  if 57 - 57: IIiIIiIi11I1 - iI1iII1I1I1i % ooOOO - I11iiIi11i1I / IiIIii11Ii . Ooo0Ooo
  Iioo0Oo0oO0 = { key : value for ( key , value ) in re . findall ( r'name="([^"]+)" value="([^"]*)"' , i1Ii1iiIiI111 ) }
  i1Ii1iiIiI111 = downloadpage ( self . url , post = Iioo0Oo0oO0 ) . data
  if 15 - 15: iiIi1 * I11iiIi11i1I - oOo0O00
  Oo0 = re . findall ( r'src: "([^"]+)"' , i1Ii1iiIiI111 )
  if Oo0 :
   itemlist . append ( Video ( server = self . enlace_label , url = Oo0 [ 0 ] ) )
   if 6 - 6: ii - Ii
   if 1 - 1: I1I + OooOoo
class fichier ( Resolver ) :
 def get_api ( self ) :
  try :
   O0o00OOOoo00 = CACHE . get ( 'R48wQ93uvh0f' )
   if O0o00OOOoo00 :
    return O0o00OOOoo00
  except :
   pass
   if 98 - 98: i1iiIII111 + Iii1i . IIiIIiIi11I1
  oO00 = xbmcvfs . translatePath ( 'special://profile/addon_data/plugin.video.eduteamo/1fichier.txt' )
  with open ( oO00 , 'r' ) as II1 :
   I1iIiiIIiIi = II1 . read ( ) . strip ( )
   if 6 - 6: iI1iII1I1I1i . i1iiIII111 . Ooo0Ooo % iiIi1
  try :
   CACHE . set ( 'R48wQ93uvh0f' , I1iIiiIIiIi , expiration = timedelta ( hours = 24 ) )
  except :
   pass
   if 52 - 52: Ooo0Ooo * Oo + Iii1i - I1Ii1I1 + iI1iII1I1I1i % IiIIii11Ii
  return I1iIiiIIiIi
  if 12 - 12: i1 . iiIi1 - I11iiIi11i1I - i1i1i1111I
  if 51 - 51: i1iiIII111 * i1iiIII111 / I1Ii1I1
 def resolve_url ( self , itemlist , msg ) :
  import requests
  if 10 - 10: Oo * I11iiIi11i1I % IiIIii11Ii / OooOoo + i1
  iii1i1 = self . get_api ( )
  iII11I11111I = requests . Session ( )
  iIii1iiiIi = iII11I11111I . post ( 'https://api.1fichier.com/v1/download/get_token.cgi' ,
 json = { "url" : self . url } ,
 headers = { 'Authorization' : 'Bearer {0}' . format ( iii1i1 ) , 'Content-Type' : 'application/json' } )
  if 81 - 81: iI1iII1I1I1i / IIiIIiIi11I1 . iI1iII1I1I1i
  if iIii1iiiIi . ok :
   try :
    OoO0oOOOooO = iIii1iiiIi . json ( )
   except Exception as I1I11i :
    msg . insert ( 0 , "%s: %s" % ( self . enlace_label , I1I11i ) )
    return
    if 37 - 37: i1i1i1111I
   if 'status' in OoO0oOOOooO and OoO0oOOOooO [ 'status' ] != 'OK' :
    O00oO00oO0O = iIii1iiiIi . json ( ) [ 'message' ]
    msg . insert ( 0 , "%s: %s" % ( self . enlace_label , O00oO00oO0O ) )
    return
    if 65 - 65: iI1iII1I1I1i . Oo
   if 'url' in OoO0oOOOooO :
    itemlist . append ( Video ( server = self . enlace_label , url = OoO0oOOOooO [ 'url' ] ) )
    if 44 - 44: I11iiIi11i1I . I1Ii1I1 * i1 . iI1iII1I1I1i * I11iiIi11i1I - I11iiIi11i1I
    if 79 - 79: IiIIii11Ii + oOo0O00
class P3DialogAnimation ( object ) :
 dialog = xbmcgui . DialogProgress ( )
 percent = 0
 closed = False
 canceled = False
 if 50 - 50: ii + i1iiIII111 . i1iiIII111 . Oo
 def __init__ ( self , heading , message ) :
  self . heading = heading
  self . message = message
  self . dialog . create ( self . heading , self . message )
  o00O00OOO00OO = Thread ( target = self . _action , args = [ ] )
  o00O00OOO00OO . daemon = True
  o00O00OOO00OO . start ( )
  if 72 - 72: oOo0O00 - ii + i1iiIII111 / iiIi1 . OooOoo * IiIIii11Ii
 def update ( self , message ) :
  self . message = message
  if 40 - 40: ooo000 * ii / i1i1i1111I * oOO + i1iiIII111 - OooOoo
 def close ( self ) :
  self . closed = True
  if 86 - 86: I11iiIi11i1I * Ooo0Ooo . IiIIii11Ii % IiIIii11Ii . I1Ii1I1 + I1I
 def cancel ( self ) :
  self . canceled = True
  if 44 - 44: i1 / OooOoo / oOo0O00 . Oo
 def iscanceled ( self ) :
  return self . canceled or self . dialog . iscanceled ( )
  if 65 - 65: I11iiIi11i1I * i1iiIII111 . OooOoo % ooo000 % OooOoo
 def _action ( self ) :
  iII11I11111I = 1
  while not self . canceled and not self . dialog . iscanceled ( ) and not self . closed :
   self . percent += ( 10 * iII11I11111I )
   self . dialog . update ( self . percent , self . message )
   if self . percent == 0 or self . percent == 100 : iII11I11111I = - iII11I11111I
   xbmc . sleep ( 250 )
  self . dialog . close ( )
  if 21 - 21: ii * I1Ii1I1
  if 93 - 93: Ooo0Ooo . i1 + ii - oOo0O00
class Video ( object ) :
 def __init__ ( self , ** kwargs ) :
  self . __dict__ . update ( kwargs )
  if 97 - 97: i1 - i1 % IIiIIiIi11I1 + IiIIii11Ii / iiIi1 * iI1iII1I1I1i
 def __str__ ( self ) :
  return repr ( self . __dict__ )
  if 60 - 60: I11iiIi11i1I - Ooo0Ooo % I1Ii1I1
 def __repr__ ( self ) :
  return repr ( self . __dict__ )
  if 26 - 26: ooOOO / IIiIIiIi11I1 . oOO + I11iiIi11i1I . Oo
 def __getattr__ ( self , name ) :
  if name . startswith ( "__" ) :
   return super ( Video , self ) . __getattribute__ ( name )
   if 37 - 37: I1Ii1I1
  elif name == 'type' :
   return self . _get_type ( )
   if 35 - 35: OooOoo % i1i1i1111I - iI1iII1I1I1i / IiIIii11Ii
  elif name == 'is_InputStream' :
   if self . type in [ 'mpd' , 'rtmp' , 'hls' ] :
    return True
   return False
   if 4 - 4: ooo000 . IiIIii11Ii % ooo000 / i1i1i1111I
  elif name == 'label' :
   if 'label' in self . __dict__ :
    return self . label
   else :
    oO = { 'es' : u'Castellano' , 'fr' : u'Frances' , 'en' : u'Ingles' , 'ru' : u'Ruso' , 'de' : u'Aleman' ,
 'it' : u'Italiano' }
    IiiI = ( "%s: " % self . server ) if 'server' in self . __dict__ else ''
    IiiI += ( "%s " % oO . get ( self . lang , localize ( 30045 ) ) ) if self . lang else ''
    if 61 - 61: IIiIIiIi11I1 / ii - i1i1i1111I . ooOOO . OooOoo / oOO
    if self . res :
     IiiI += ( "%s " % self . type . upper ( ) ) if self . is_InputStream else ''
     if 94 - 94: Ooo0Ooo % oOo0O00 . oOo0O00 / Ii . i1
     OoO = None
     if not self . res . lower ( ) in [ '4k' , '3d' , '8k' ] :
      OoO = re . findall ( r'(\d+)' , self . res )
     IiiI += "[%s]" % ( OoO [ 0 ] + 'p' ) if OoO else self . res
    else :
     IiiI += ( "(%s)" % self . type . upper ( ) )
    return IiiI
    if 77 - 77: I11iiIi11i1I . i1 % OooOoo * Ooo0Ooo + Iii1i
  else :
   return ''
   if 79 - 79: iiIi1 / I1Ii1I1 - i1i1i1111I
 def __deepcopy__ ( self , memo ) :
  o0000oOOo0 = Video ( ** self . __dict__ )
  return o0000oOOo0
  if 50 - 50: Iii1i + i1i1i1111I + IiIIii11Ii
 def _get_type ( self ) :
  if self . url . startswith ( 'rtmp' ) :
   return 'rtmp'
  else :
   i1IiiI1I1i1 = os . path . splitext ( self . url . split ( '?' ) [ 0 ] . split ( '|' ) [ 0 ] ) [ 1 ]
   if i1IiiI1I1i1 . startswith ( '.' ) : i1IiiI1I1i1 = i1IiiI1I1i1 [ 1 : ]
   return i1IiiI1I1i1
   if 60 - 60: I1Ii1I1 - i1i1i1111I / iI1iII1I1I1i * oOo0O00 . Ii / I1I
 def clone ( self , ** kwargs ) :
  I1I1II = copy . deepcopy ( self )
  for iIi1II , II1IIIiI in kwargs . items ( ) :
   setattr ( I1I1II , iIi1II , II1IIIiI )
  return I1I1II
