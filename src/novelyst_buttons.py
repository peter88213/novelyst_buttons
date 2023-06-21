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

APPLICATION = 'Button bar plugin'


class Plugin:
    """Botton bar plugin class.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        on_close() -- Actions to be performed when a project is closed.       
        on_quit() -- Actions to be performed when novelyst is closed.               
    """
    VERSION = '@release'
    NOVELYST_API = '4.20'
    DESCRIPTION = 'Button bar plugin'
    URL = 'https://peter88213.github.io/novelyst'

    def install(self, ui):
        """Add a button bar.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        iconPath = f'{os.path.dirname(sys.argv[0])}/icons'.replace('\\', '/')

        # Add a button bar to the editor window.
        self._buttonBar = tk.Frame(self._ui.mainWindow)
        self._buttonBar.pack(expand=False, before=self._ui.appWindow, fill=tk.BOTH)

        saveIcon = tk.PhotoImage(file=f'{iconPath}/diskette.png')
        self._saveButton = ttk.Button(self._buttonBar, image=saveIcon, command=self._ui.save_project)
        self._saveButton.pack(side=tk.LEFT)
        self._saveButton.image = saveIcon

        lockIcon = tk.PhotoImage(file=f'{iconPath}/padlock.png')
        self._lockButton = ttk.Button(self._buttonBar, image=lockIcon, command=self._toggle_lock)
        self._lockButton.pack(side=tk.LEFT)
        self._lockButton.image = lockIcon

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        self._saveButton.config(state='disabled')
        self._lockButton.config(state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        self._saveButton.config(state='normal')
        self._lockButton.config(state='normal')

    def _toggle_lock(self):
        if self._ui.isLocked:
            self._ui.unlock()
        else:
            self._ui.lock()

