"""Button bar plugin for novelyst.

Adds a button bar.

Requires Python 3.6+
Copyright (c) 2023 Peter Triesberger
For further information see https://github.com/peter88213/novelyst/novelyst_buttons
License: GNU GPLv3 (https://www.gnu.org/licenses/gpl-3.0.en.html)
"""
import os
import sys
import tkinter as tk
from tkinter import ttk
from idlelib.tooltip import Hovertip
import locale
import gettext

APPLICATION = 'Button bar plugin'

# Initialize localization.
LOCALE_PATH = f'{os.path.dirname(sys.argv[0])}/locale/'
try:
    CURRENT_LANGUAGE = locale.getlocale()[0][:2]
except:
    # Fallback for old Windows versions.
    CURRENT_LANGUAGE = locale.getdefaultlocale()[0][:2]
try:
    t = gettext.translation('novelyst_buttons', LOCALE_PATH, languages=[CURRENT_LANGUAGE])
    _ = t.gettext
except:

    def _(message):
        return message


class Plugin:
    """Botton bar plugin class.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        on_close() -- Actions to be performed when a project is closed.       
        on_quit() -- Actions to be performed when novelyst is closed.               
    """
    VERSION = '@release'
    NOVELYST_API = '4.29'
    DESCRIPTION = 'Button bar plugin'
    URL = 'https://peter88213.github.io/novelyst_buttons'

    def install(self, ui):
        """Add a button bar.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        iconPath = f'{os.path.dirname(sys.argv[0])}/plugin/icons'.replace('\\', '/')

        # Add a button bar to the editor window.
        self._buttonBar = tk.Frame(self._ui.mainWindow)
        self._buttonBar.pack(expand=False, before=self._ui.appWindow, fill=tk.BOTH)

        # "Save" button.
        saveIcon = tk.PhotoImage(file=f'{iconPath}/diskette.png')
        self._saveButton = ttk.Button(self._buttonBar, image=saveIcon, command=self._ui.save_project)
        self._saveButton.pack(side=tk.LEFT)
        self._saveButton.image = saveIcon
        Hovertip(self._saveButton, _('Save'))

        # "Reload" button.
        reloadIcon = tk.PhotoImage(file=f'{iconPath}/refresh.png')
        self._reloadButton = ttk.Button(self._buttonBar, image=reloadIcon, command=self._ui.reload_project)
        self._reloadButton.pack(side=tk.LEFT)
        self._reloadButton.image = reloadIcon
        Hovertip(self._reloadButton, _('Reload'))

        # "Lock/Unlock" button.
        lockIcon = tk.PhotoImage(file=f'{iconPath}/padlock.png')
        self._lockButton = ttk.Button(self._buttonBar, image=lockIcon, command=self._ui.toggle_lock)
        self._lockButton.pack(side=tk.LEFT)
        self._lockButton.image = lockIcon
        Hovertip(self._lockButton, _('Lock/unlock'))

        # "Manuscript" button.
        manuscriptIcon = tk.PhotoImage(file=f'{iconPath}/manuscript.png')
        self._manuscriptButton = ttk.Button(self._buttonBar, image=manuscriptIcon, command=self._ui.export_manuscript)
        self._manuscriptButton.pack(side=tk.LEFT)
        self._manuscriptButton.image = manuscriptIcon
        Hovertip(self._manuscriptButton, _('Export Manuscript for editing'))

        # "Toggle properties" button.
        propertiesIcon = tk.PhotoImage(file=f'{iconPath}/info.png')
        self._propertiesButton = ttk.Button(self._buttonBar, image=propertiesIcon, command=self._ui.toggle_properties)
        self._propertiesButton.pack(side=tk.RIGHT)
        self._propertiesButton.image = propertiesIcon
        Hovertip(self._propertiesButton, _('Toggle Properties'))

        # "Toggle content viewer" button.
        viewerIcon = tk.PhotoImage(file=f'{iconPath}/file.png')
        self._viewerButton = ttk.Button(self._buttonBar, image=viewerIcon, command=self._ui.toggle_viewer)
        self._viewerButton.pack(side=tk.RIGHT)
        self._viewerButton.image = viewerIcon
        Hovertip(self._viewerButton, _('Toggle Text viewer'))

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        self._saveButton.config(state='disabled')
        self._reloadButton.config(state='disabled')
        self._lockButton.config(state='disabled')
        self._manuscriptButton.config(state='disabled')
        self._propertiesButton.config(state='disabled')
        self._viewerButton.config(state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        self._saveButton.config(state='normal')
        self._reloadButton.config(state='normal')
        self._lockButton.config(state='normal')
        self._manuscriptButton.config(state='normal')
        self._propertiesButton.config(state='normal')
        self._viewerButton.config(state='normal')

