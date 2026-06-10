# -*- coding: utf-8 -*-
import sys
import os

# Add libs to sys.path to resolve absolute imports inside the folder
addon_dir = os.path.dirname(os.path.abspath(__file__))
libs_dir = os.path.join(addon_dir, 'libs')
if libs_dir not in sys.path:
    sys.path.insert(0, libs_dir)

from libs.ioOooOO import ContextMenu

if __name__ == '__main__':
    ContextMenu().show()
