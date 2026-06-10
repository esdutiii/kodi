# -*- coding: utf-8 -*-
if 82 - 82: Iii1i
if 87 - 87: Ii % i1i1i1111I . Oo / OooOoo * I1Ii1I1 - I1I
if 81 - 81: i1 + ooOOO / oOo0O00 * i1iiIII111 * IiIIii11Ii
import sys
import os
import xbmcvfs
import xbmcaddon
if 84 - 84: ooo000 - Ooo0Ooo + iI1iII1I1I1i . IIiIIiIi11I1
import builtins , base64
from types import ModuleType
from importlib import abc , machinery
if 99 - 98 : iI111iiIi11i = base64
OoOoo0o = __import__
def I1i ( name , locals = None , globals = None , fromlist = [ ] , level = 0 ) :
 class IiI11Ii111 ( abc . Loader ) :
  def __init__ ( self , modules ) :
   self . _modules = modules
  def has_module ( self , fullname ) :
   return ( fullname in self . _modules )
  def create_module ( self , spec ) :
   if self . has_module ( spec . name ) :
    I11II1Ii = ModuleType ( spec . name )
    exec ( self . _modules [ spec . name ] , I11II1Ii . __dict__ )
    return I11II1Ii
  def exec_module ( self , module ) :
   pass
 class iIi ( abc . MetaPathFinder ) :
  def __init__ ( self , loader ) :
   self . _loader = loader
  def find_spec ( self , fullname , path , target = None ) :
   if self . _loader . has_module ( fullname ) :
    return machinery . ModuleSpec ( fullname , self . _loader )
 if name not in sys . modules and name . startswith ( 'libs.' ) :
  ii = os . path . join ( xbmcvfs . translatePath ( xbmcaddon . Addon ( ) . getAddonInfo ( 'Path' ) ) , name . replace ( '.' , os . path . sep ) + ".md" )
  if os . path . isfile ( ii ) :
   with open ( ii , "rb" ) as iiI :
    i1Ii1i = iiI . read ( )
   oOooo0OOO = len ( i1Ii1i )
   Oo000ooO0Oooo = oOooo0OOO // 3
   IIiI = i1Ii1i [ oOooo0OOO - Oo000ooO0Oooo : ]
   i1Ii1i = i1Ii1i [ : oOooo0OOO - Oo000ooO0Oooo ]
   IIiI += i1Ii1i [ : Oo000ooO0Oooo ] + i1Ii1i [ Oo000ooO0Oooo : ] [ : : - 1 ]
   oO0 = { name : iI111iiIi11i ( IIiI ) . decode ( 'utf-8' ) }
   i1iiiiIIIiIi = iIi ( IiI11Ii111 ( oO0 ) )
   sys . meta_path . append ( i1iiiiIIIiIi )
 return OoOoo0o ( name , locals , globals , fromlist , level )
if 98 - 96 : iI111iiIi11i = iI111iiIi11i . b85decode
builtins . __import__ = I1i
from libs . ioOooOO import ContextMenu
if 22 - 22: OOO00000O . Ii111 / o0 . o0i1i
if 87 - 87: Oo - o0
if __name__ == '__main__' :
 ContextMenu ( ) . show ( )
 if 32 - 32: Ii % i1i1i1111I % o0 - OOO00000O % i1iiIII111
