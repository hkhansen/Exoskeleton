import sys
from cx_Freeze import setup, Executable

includefiles = ['guide.jpg',]
includes = []
excludes = []
packages = []

# base="Win32GUI" should be used only for Windows GUI app
base = "Win32GUI" if sys.platform == "win32" else None

setup(
    name='Exoskeleton configurator',
    description='Program for generating user-specific exoskeletons',
    version='1.0',
    options = {'build_exe': {'excludes':excludes,'packages':packages,'include_files':includefiles}},
    executables=[Executable('Configurator_UI.py', 
			    target_name='Exoskeleton_configurator.exe', 
			    icon='icon.ico', 
			    copyright='Copyright (C) Hans Kristian Bech Hansen 2023', 
			    base=base)],
)
