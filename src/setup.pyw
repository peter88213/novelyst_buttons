#!/usr/bin/python3
"""Install the novelyst_buttons plugin. 

Version @release

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_buttons
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
from shutil import copytree
from shutil import copyfile
from pathlib import Path
try:
    from tkinter import *
except ModuleNotFoundError:
    print('The tkinter module is missing. Please install the tk support package for your python3 version.')
    sys.exit(1)

PLUGIN = 'novelyst_buttons.py'
VERSION = ' @release'

root = Tk()
processInfo = Label(root, text='')
message = []


def output(text):
    message.append(text)
    processInfo.config(text=('\n').join(message))


if __name__ == '__main__':
    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    # Open a tk window.
    root.geometry("600x200")
    root.title(f'Install {PLUGIN}{VERSION}')
    header = Label(root, text='')
    header.pack(padx=5, pady=5)

    # Prepare the messaging area.
    processInfo.pack(padx=5, pady=5)

    # Install the plugin.
    homePath = str(Path.home()).replace('\\', '/')
    novelystDir = f'{homePath}/.pywriter/novelyst'
    if os.path.isdir(novelystDir):
        if os.path.isfile(f'./{PLUGIN}'):
            pluginDir = f'{novelystDir}/plugin'
            os.makedirs(pluginDir, exist_ok=True)
            copyfile(PLUGIN, f'{pluginDir}/{PLUGIN}')
            output(f'Sucessfully installed "{PLUGIN}" at "{os.path.normpath(pluginDir)}"')
        else:
            output(f'ERROR: file "{PLUGIN}" not found.')

        try:
            from idlelib.tooltip import Hovertip
        except ModuleNotFoundError:
            output('\nThe idlelib module is missing.\nTo see the tooltips, please install the idle3 package for your python3 version.\n')

        # Install the localization files.
        copytree('locale', f'{novelystDir}/locale', dirs_exist_ok=True)
        output(f'Copying "locale"')

        # Install the icon files.
        copytree('icons', f'{pluginDir}/icons', dirs_exist_ok=True)
        output(f'Copying "icons"')
    else:
        output(f'ERROR: Cannot find a novelyst installation at "{novelystDir}"')

    root.quitButton = Button(text="Quit", command=quit)
    root.quitButton.config(height=1, width=30)
    root.quitButton.pack(padx=5, pady=5)
    root.mainloop()
