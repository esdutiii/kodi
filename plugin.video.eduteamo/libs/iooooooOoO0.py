# -*- coding: utf-8 -*-
__all__ = [ 'load_json_file' , 'Proxydatetime' , 'KODI_VERSION' , 'get_setting' , 'CACHE' , 'SetColor' , 'localize' , 'WINDOW' , 'compare_versions' , 'logger' , 'dump_json' , 'AES' , 'set_setting' , 'ISESTUARYeduteamo' , 'load_json' , 'p3b64decode' , 'p3b64encode' , 'DialogImage' ]
if 82 - 82: Iii1i
import re
import os
import json
import datetime
import base64
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
import xbmc
import xbmcaddon
import xbmcgui
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
from urllib import parse
from libs . ioiiiiIi1i1 import SimpleCache
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
iI111iiIi11i = xbmcaddon . Addon ( )
OoOoo0o = re . match ( r"\d+\.\d+" , xbmc . getInfoLabel ( 'System.BuildVersion' ) )
KODI_VERSION = float ( OoOoo0o . group ( 0 ) ) if OoOoo0o else 0.0
CACHE = SimpleCache ( )
WINDOW = xbmcgui . Window ( 10000 )
ISESTUARYeduteamo = xbmc . getSkinDir ( ) == 'skin.estuary.eduteamo'
if 11 - 11: i1I1 - O000o / O0OO0OooooOo * ii % Ii * i1
if 9 - 9: i1iiIII111
if 10 - 10: ooOOO / IIiIIiIi11I1 * O000o / O0OO0OooooOo / O0OO0OooooOo
class Proxydatetime ( datetime . datetime ) :
 @ staticmethod
 def strptime ( date_string , format ) :
  import time
  return datetime . datetime ( * ( time . strptime ( date_string , format ) [ 0 : 6 ] ) )
  if 61 - 61: Ooo0Ooo - I1I
def p3b64encode ( value ) :
 if not isinstance ( value , bytes ) :
  value = str ( value ) . encode ( )
 value = base64 . b64encode ( value )
 if 13 - 13: Ooo0Ooo
 OO0o000o = len ( value )
 IIiiii1IiIiII = int ( OO0o000o / 4 )
 if 32 - 32: iI1iII1I1I1i
 value = re . sub ( b'=' , b'' , value )
 i1iiiiIIIiIi = value [ : IIiiii1IiIiII ] [ : : - 1 ] + value [ IIiiii1IiIiII : ] [ : : - 1 ]
 if 22 - 22: ooo000 . iI1iII1I1I1i + Ooo0Ooo + O000o
 return parse . quote ( i1iiiiIIIiIi )
 if 85 - 85: OooOoo - oOo0O00 / Ii / O000o % i1iiIII111 . Ii
 if 7 - 7: i1I1 - I1Ii1I1 % i1I1 . I1Ii1I1 . i1i1i1111I
def p3b64decode ( value ) :
 if not isinstance ( value , bytes ) :
  value = parse . unquote ( value ) . encode ( )
 else :
  value = parse . unquote ( value )
  if 77 - 77: i1
 value = re . sub ( r'\?' . encode ( ) , b'' , value )
 if 52 - 52: O0OO0OooooOo
 iiI1111IIi1 = b''
 OO0o000o = len ( value )
 if OO0o000o % 4 :
  oOo00O = 4 - ( OO0o000o % 4 )
  OO0o000o += oOo00O
  iiI1111IIi1 = b'=' * oOo00O
  if 59 - 59: Iii1i . ii - O0OO0OooooOo
 IIiiii1IiIiII = int ( OO0o000o / 4 )
 i1iiiiIIIiIi = value [ : IIiiii1IiIiII ] [ : : - 1 ] + value [ IIiiii1IiIiII : ] [ : : - 1 ]
 if 13 - 13: O000o
 return base64 . b64decode ( i1iiiiIIIiIi + iiI1111IIi1 )
 if 28 - 28: OooOoo + i1i1i1111I + IiIIii11Ii / I1Ii1I1 + iI1iII1I1I1i
 if 70 - 70: ii + i1I1 * O000o . Oo + ooOOO / Oo
def localize ( id ) :
 return iI111iiIi11i . getLocalizedString ( id )
 if 14 - 14: OooOoo % oOo0O00 + I1I % i1iiIII111 * ooOOO / i1I1
 if 63 - 63: i1i1i1111I . Ooo0Ooo * ooOOO
def logger ( message , level = None ) :
 def ii1Ii1I ( data = "" ) :
  try :
   oo0 = str ( data )
  except Exception :
   oo0 = repr ( data )
  if isinstance ( oo0 , bytes ) :
   oo0 = str ( oo0 , 'utf8' , 'replace' )
  return oo0
  if 20 - 20: IiIIii11Ii . O000o % Ooo0Ooo / Ii / oOo0O00
 oo0o0oO = '[%s] %s' % ( iI111iiIi11i . getAddonInfo ( 'id' ) , ii1Ii1I ( message ) )
 try :
  if level == 'info' :
   xbmc . log ( oo0o0oO , xbmc . LOGINFO )
  elif level == 'error' :
   xbmc . log ( "######## ERROR #########" , xbmc . LOGERROR )
   xbmc . log ( oo0o0oO , xbmc . LOGERROR )
  else :
   xbmc . log ( "######## DEBUG #########" , xbmc . LOGINFO )
   xbmc . log ( oo0o0oO , xbmc . LOGINFO )
 except :
  xbmc . log ( str ( [ oo0o0oO ] ) , xbmc . LOGINFO )
  if 100 - 100: ii - OooOoo * I1Ii1I1 / Ooo0Ooo / Iii1i
def load_json ( * args , ** kwargs ) :
 def I11iIi1i ( dct ) :
  if isinstance ( dct , dict ) :
   return dict ( ( I11iIi1i ( key ) , I11iIi1i ( value ) ) for key , value in dct . items ( ) )
  elif isinstance ( dct , list ) :
   return [ I11iIi1i ( element ) for element in dct ]
  else :
   return dct
   if 49 - 49: IIiIIiIi11I1
 if "object_hook" not in kwargs :
  kwargs [ "object_hook" ] = I11iIi1i
 try :
  oo0 = json . loads ( * args , ** kwargs )
 except Exception as iIIiii1iI :
  if 43 - 43: ooOOO . i1I1 + ooo000
  oo0 = { }
  if 87 - 87: Iii1i + ooOOO . O0OO0OooooOo / Ii + Oo
 return oo0
 if 77 - 77: i1iiIII111 + ii - Oo % ooo000
def load_json_file ( path ) :
 I1 = dict ( )
 try :
  with open ( path , 'r' , encoding = 'utf-8' ) as o000000oOO :
   I1 = load_json ( o000000oOO . read ( ) )
 except : pass
 return I1
 if 9 - 9: ii + Oo + oOo0O00 * oOo0O00 % Ooo0Ooo * i1iiIII111
def dump_json ( * args , ** kwargs ) :
 if not kwargs :
  kwargs = {
 'indent' : 4 ,
 'skipkeys' : True ,
 'sort_keys' : True ,
 'ensure_ascii' : False
 }
 try :
  oo0 = json . dumps ( * args , ** kwargs )
 except Exception as iIIiii1iI :
  logger ( iIIiii1iI , 'error' )
  oo0 = ''
  if 52 - 52: O000o + I1I / ooo000 - I1Ii1I1 * O0OO0OooooOo % oOo0O00
 return oo0
 if 52 - 52: oOo0O00 . I1I + O0OO0OooooOo - i1iiIII111 % iI1iII1I1I1i
 if 57 - 57: I1I * IIiIIiIi11I1 % I1Ii1I1 * i1i1i1111I
 if 37 - 37: ii * i1i1i1111I + oOo0O00 / I1I / OooOoo
def get_setting ( name , default = None ) :
 oo0 = iI111iiIi11i . getSetting ( name )
 if 4 - 4: i1
 if not oo0 :
  return default
 elif oo0 == 'true' :
  return True
 elif oo0 == 'false' :
  return False
 else :
  try :
   oo0 = int ( oo0 )
  except ValueError :
   try :
    oO00o00OO = load_json ( oo0 )
    if oO00o00OO : oo0 = oO00o00OO
   except ValueError :
    pass
  return oo0
  if 52 - 52: Iii1i / Oo
  if 100 - 100: I1Ii1I1 / i1I1 * Ii - O000o
def set_setting ( name , value ) :
 try :
  if isinstance ( value , bool ) :
   if value :
    value = "true"
   else :
    value = "false"
  elif isinstance ( value , ( int ) ) :
   value = str ( value )
  elif not isinstance ( value , str ) :
   value = dump_json ( value )
  iI111iiIi11i . setSetting ( name , value )
 except Exception as iiI1111II :
  logger ( r"Error al convertir '%s' no se guarda el valor \n%s" % ( name , iiI1111II ) , 'error' )
  return None
  if 79 - 79: Ooo0Ooo % iI1iII1I1I1i % IIiIIiIi11I1 / ooOOO - ooOOO / i1I1
 return value
 if 63 - 63: ooOOO / i1i1i1111I - oOo0O00 * ooOOO / i1iiIII111 + O000o
 if 11 - 11: i1 / ooo000
def compare_versions ( version1 , version2 ) :
 i1iiiiIIIiIi = list ( map ( int , version1 . split ( '.' ) ) )
 if 89 - 89: I1I * i1i1i1111I
 if 54 - 54: O000o + Ooo0Ooo - I1I . Ooo0Ooo
 if 50 - 50: Iii1i * ooo000 % Iii1i - oOo0O00 + ooo000
 if 54 - 54: O000o * i1 % i1 - Ooo0Ooo + IIiIIiIi11I1
 if 4 - 4: ooo000 + I1Ii1I1 * OooOoo - ii
 if 69 - 69: ooo000
 if 76 - 76: Iii1i * Ooo0Ooo . iI1iII1I1I1i / Ii / ooOOO
 if 49 - 49: iI1iII1I1I1i / i1iiIII111 + ooo000
 if 36 - 36: i1i1i1111I + Iii1i - O000o * Ii
 oo0ooooo0ooo = list ( map ( int , version2 . split ( '.' ) ) )
 while i1iiiiIIIiIi or oo0ooooo0ooo :
  if not i1iiiiIIIiIi :
   return - 1
  if not oo0ooooo0ooo :
   return 1
  if i1iiiiIIIiIi [ 0 ] < oo0ooooo0ooo [ 0 ] :
   return - 1
  if i1iiiiIIIiIi [ 0 ] > oo0ooooo0ooo [ 0 ] :
   return 1
  i1iiiiIIIiIi = i1iiiiIIIiIi [ 1 : ]
  oo0ooooo0ooo = oo0ooooo0ooo [ 1 : ]
 return 0
 if 61 - 61: O0OO0OooooOo . iI1iII1I1I1i / ooOOO * I1Ii1I1 + ii % Oo
 if 100 - 100: Oo + O0OO0OooooOo
try :
 try :
  from Cryptodome . Cipher import AES as AES
 except :
  from Crypto . Cipher import AES as AES
  if 4 - 4: ooo000 % I1I - i1i1i1111I
except Exception as iIIiii1iI :
 logger ( "%s: %s" % ( localize ( 30056 ) , iIIiii1iI ) , "error" )
 xbmcgui . Dialog ( ) . ok ( 'EduTeAmo' , localize ( 30056 ) )
 exit ( )
 if 76 - 76: i1 * oOo0O00 . ii * O0OO0OooooOo . IiIIii11Ii . O000o
 if 55 - 55: i1i1i1111I + i1iiIII111 % Ooo0Ooo . Oo - IiIIii11Ii - iI1iII1I1I1i
class SetColor ( ) :
 colores = dict ( )
 COLOR_GOLD = 'ffd700'
 COLOR_CSS = { 'aliceblue' : 'f0f8ff' , 'antiquewhite' : 'faebd7' , 'aqua' : '00ffff' , 'aquamarine' : '7fffd4' , 'azure' : 'f0ffff' , 'beige' : 'f5f5dc' , 'bisque' : 'ffe4c4' , 'black' : '000000' , 'blanchedalmond' : 'ffebcd' , 'blue' : '0000ff' , 'blueviolet' : '8a2be2' , 'brown' : 'a52a2a' , 'burlywood' : 'deb887' , 'cadetblue' : '5f9ea0' , 'chartreuse' : '7fff00' , 'chocolate' : 'd2691e' , 'coral' : 'ff7f50' , 'cornflowerblue' : '6495ed' , 'cornsilk' : 'fff8dc' , 'crimson' : 'dc143c' , 'cyan' : '00ffff' , 'darkblue' : '00008b' , 'darkcyan' : '008b8b' , 'darkgoldenrod' : 'b8860b' , 'darkgray' : 'a9a9a9' , 'darkgreen' : '006400' , 'darkgrey' : 'a9a9a9' , 'darkkhaki' : 'bdb76b' , 'darkmagenta' : '8b008b' , 'darkolivegreen' : '556b2f' , 'darkorange' : 'ff8c00' , 'darkorchid' : '9932cc' , 'darkred' : '8b0000' , 'darksalmon' : 'e9967a' , 'darkseagreen' : '8fbc8f' , 'darkslateblue' : '483d8b' , 'darkslategray' : '2f4f4f' , 'darkslategrey' : '2f4f4f' , 'darkturquoise' : '00ced1' , 'darkviolet' : '9400d3' , 'deeppink' : 'ff1493' , 'deepskyblue' : '00bfff' , 'dimgray' : '696969' , 'dimgrey' : '696969' , 'dodgerblue' : '1e90ff' , 'firebrick' : 'b22222' , 'floralwhite' : 'fffaf0' , 'forestgreen' : '228b22' , 'fuchsia' : 'ff00ff' , 'gainsboro' : 'dcdcdc' , 'ghostwhite' : 'f8f8ff' , 'gold' : 'ffd700' , 'goldenrod' : 'daa520' , 'gray' : '808080' , 'green' : '008000' , 'greenyellow' : 'adff2f' , 'grey' : '808080' , 'honeydew' : 'f0fff0' , 'hotpink' : 'ff69b4' , 'indianred' : 'cd5c5c' , 'indigo' : '4b0082' , 'ivory' : 'fffff0' , 'khaki' : 'f0e68c' , 'lavender' : 'e6e6fa' , 'lavenderblush' : 'fff0f5' , 'lawngreen' : '7cfc00' , 'lemonchiffon' : 'fffacd' , 'lightblue' : 'add8e6' , 'lightcoral' : 'f08080' , 'lightcyan' : 'e0ffff' , 'lightgoldenrodyellow' : 'fafad2' , 'lightgray' : 'd3d3d3' , 'lightgreen' : '90ee90' , 'lightgrey' : 'd3d3d3' , 'lightpink' : 'ffb6c1' , 'lightsalmon' : 'ffa07a' , 'lightseagreen' : '20b2aa' , 'lightskyblue' : '87cefa' , 'lightslategray' : '778899' , 'lightslategrey' : '778899' , 'lightsteelblue' : 'b0c4de' , 'lightyellow' : 'ffffe0' , 'lime' : '00ff00' , 'limegreen' : '32cd32' , 'linen' : 'faf0e6' , 'magenta' : 'ff00ff' , 'maroon' : '800000' , 'mediumaquamarine' : '66cdaa' , 'mediumblue' : '0000cd' , 'mediumorchid' : 'ba55d3' , 'mediumpurple' : '9370db' , 'mediumseagreen' : '3cb371' , 'mediumslateblue' : '7b68ee' , 'mediumspringgreen' : '00fa9a' , 'mediumturquoise' : '48d1cc' , 'mediumvioletred' : 'c71585' , 'midnightblue' : '191970' , 'mintcream' : 'f5fffa' , 'mistyrose' : 'ffe4e1' , 'moccasin' : 'ffe4b5' , 'navajowhite' : 'ffdead' , 'navy' : '000080' , 'oldlace' : 'fdf5e6' , 'olive' : '808000' , 'olivedrab' : '6b8e23' , 'orange' : 'ffa500' , 'orangered' : 'ff4500' , 'orchid' : 'da70d6' , 'palegoldenrod' : 'eee8aa' , 'palegreen' : '98fb98' , 'paleturquoise' : 'afeeee' , 'palevioletred' : 'db7093' , 'papayawhip' : 'ffefd5' , 'peachpuff' : 'ffdab9' , 'peru' : 'cd853f' , 'pink' : 'ffc0cb' , 'plum' : 'dda0dd' , 'powderblue' : 'b0e0e6' , 'purple' : '800080' , 'red' : 'ff0000' , 'rosybrown' : 'bc8f8f' , 'royalblue' : '4169e1' , 'saddlebrown' : '8b4513' , 'salmon' : 'fa8072' , 'sandybrown' : 'f4a460' , 'seagreen' : '2e8b57' , 'seashell' : 'fff5ee' , 'sienna' : 'a0522d' , 'silver' : 'c0c0c0' , 'skyblue' : '87ceeb' , 'slateblue' : '6a5acd' , 'slategray' : '708090' , 'slategrey' : '708090' , 'snow' : 'fffafa' , 'springgreen' : '00ff7f' , 'steelblue' : '4682b4' , 'tan' : 'd2b48c' , 'teal' : '008080' , 'thistle' : 'd8bfd8' , 'turquoise' : '40e0d0' , 'violet' : 'ee82ee' , 'wheat' : 'f5deb3' , 'white' : 'ffffff' , 'whitesmoke' : 'f5f5f5' , 'yellow' : 'ffff00' , 'yellowgreen' : '9acd32' }
 if 91 - 91: I1Ii1I1 - i1I1
 def __new__ ( cls , label , subLabelColor , alfa = 'ff' ) :
  if not get_setting ( "conColor" ) and subLabelColor != 'LabelColor' :
   return label
   if 84 - 84: O000o % iI1iII1I1I1i - Ooo0Ooo
  if subLabelColor not in cls . colores :
   OoOOo = cls . COLOR_GOLD
   try :
    oo0 = localize ( get_setting ( subLabelColor ) )
    OoOOo = cls . COLOR_CSS [ re . findall ( r'\[COLOR\s+([^\]]+)' , oo0 ) [ 0 ] ]
   except Exception :
    pass
   cls . colores [ subLabelColor ] = alfa + OoOOo
   if 97 - 97: ii % ooo000 * Iii1i + IIiIIiIi11I1
  return '[COLOR %s]%s[/COLOR]' % ( cls . colores [ subLabelColor ] , label )
  if 42 - 42: I1I - IiIIii11Ii
  if 34 - 34: ii + ooOOO * O000o
class DialogImage ( xbmcgui . WindowXMLDialog ) :
 def __init__ ( self , heading , text ) :
  self . heading = heading
  if 2 - 2: i1i1i1111I / Ooo0Ooo / O000o - IIiIIiIi11I1 / IIiIIiIi11I1
  # Clean up any residual eduteamo / blogspot links from remote text
  text = re.sub(r'(?i)eduteamo(?:\.blogspot\S*)?', 'EduTeAmo', text)
  text = re.sub(r'(?i)eduteamo', 'EduTeAmo', text)
  oOo = re . findall ( r'(\[http[^\]]*])' , text )
  if oOo :
   text = text . replace ( str ( oOo [ 0 ] ) , '' , 1 )
   oOo = oOo [ 0 ] [ 1 : - 1 ]
  else :
   oOo = "special://home/addons/plugin.video.eduteamo/resources/media/icon.png"
   if 52 - 52: oOo0O00 / O0OO0OooooOo * IIiIIiIi11I1 + i1I1 % Ooo0Ooo + O000o
  text = text . replace ( r'\n' , '[CR]' )
  if 43 - 43: iI1iII1I1I1i * oOo0O00 + ooOOO
  self . text = text
  self . image = oOo
  self . doModal ( )
  if 30 - 30: I1I
 def __new__ ( cls , heading , text , image = None ) :
  return super ( DialogImage , cls ) . __new__ ( cls , "DialogImage.xml" , 'special://home/addons/plugin.video.eduteamo' )
  if 41 - 41: O000o
 def onInit ( self ) :
  self . getControl ( 10011 ) . setLabel ( self . heading )
  self . getControl ( 10014 ) . setText ( self . text )
  self . getControl ( 10013 ) . setImage ( self . image )
  self . setFocus ( self . getControl ( 10015 ) )
  if 98 - 98: I1I / IIiIIiIi11I1 / O0OO0OooooOo + ii % Oo + I1I
 def onClick ( self , controlID ) :
  if controlID in [ 10012 , 10015 ] :
   self . close ( )
