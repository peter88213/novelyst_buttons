#!/usr/bin/python3
"""Install the novelyst_buttons plugin. 

Version @release

Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst_buttons
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
import glob
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


def install(iconSize=16, disableHovertips=False):
    # Install the plugin.
    homePath = str(Path.home()).replace('\\', '/')
    novelystDir = f'{homePath}/.pywriter/novelyst'
    if os.path.isdir(novelystDir):
        if os.path.isfile(f'./{PLUGIN}'):
            pluginDir = f'{novelystDir}/plugin'
            os.makedirs(pluginDir, exist_ok=True)
            if disableHovertips:
                # Patch the code.
                with open(PLUGIN, 'r', encoding='utf-8') as f:
                    source = f.read()
                source = source.replace('ENABLE_HOVERTIPS = True', 'ENABLE_HOVERTIPS = False')
                with open(f'{pluginDir}/{PLUGIN}', 'w', encoding='utf-8') as f:
                    f.write(source)
            else:
                copyfile(PLUGIN, f'{pluginDir}/{PLUGIN}')
            output(f'Sucessfully installed "{PLUGIN}" at "{os.path.normpath(pluginDir)}"')
        else:
            output(f'ERROR: file "{PLUGIN}" not found.')

        try:
            from idlelib.tooltip import Hovertip
        except ModuleNotFoundError:
            output('\nThe idlelib module is missing.\nTo see the tooltips, please install the idle3 package for your python3 version.\n')

        # Install the localization files.
        output(f'Copying locale ...')
        copytree('locale', f'{novelystDir}/locale', dirs_exist_ok=True)

        # Install the icon files.
        output(f'Copying icons ...')
        copytree(f'icons/{iconSize}', f'{pluginDir}/icons', dirs_exist_ok=True)
        for f in os.listdir(f'{pluginDir}/icons'):
            print(f)
            if not f.endswith('.png'):
                output(f'Deleting {pluginDir}/icons/{f} ...')
                os.remove(f'{pluginDir}/icons/{f}')
    else:
        output(f'ERROR: Cannot find a novelyst installation at "{novelystDir}"')


if __name__ == '__main__':
    scriptPath = os.path.abspath(sys.argv[0])
    scriptDir = os.path.dirname(scriptPath)
    os.chdir(scriptDir)

    # Open a tk window.
    root.geometry("600x400")
    root.title(f'Install {PLUGIN}{VERSION}')
    header = Label(root, text='')
    header.pack(padx=5, pady=5)

    # Icon size selector.
    smallIcon = PhotoImage(file='icons/16/nb_save.png')
    bigIcon = PhotoImage(file='icons/24/nb_save.png')
    iconSize = IntVar(root, value=16)
    Label(root, image=smallIcon).pack()
    Radiobutton(root, text='Small icons', variable=iconSize, value=16).pack()
    Label(root, image=bigIcon).pack()
    Radiobutton(root, text='Big icons', variable=iconSize, value=24).pack()

    # Disable hovertips.
    disableHovertips = BooleanVar(root, value=False)
    Checkbutton(root, text='Disable the hovertips', variable=disableHovertips).pack()

    # Prepare the messaging area.
    processInfo.pack(padx=5, pady=5)

    Button(text="Install", height=1, width=30, command=lambda:install(iconSize.get(), disableHovertips.get())).pack()

    root.quitButton = Button(text="Quit", height=1, width=30, command=quit)
    root.quitButton.pack(padx=5, pady=5)
    root.mainloop()
