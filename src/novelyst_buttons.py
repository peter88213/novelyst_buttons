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
import locale
import gettext
import webbrowser

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

ENABLE_HOVERTIPS = True


class Plugin:
    """Button bar plugin class.
    
    Public methods:
        disable_menu() -- disable menu entries when no project is open.
        enable_menu() -- enable menu entries when a project is open.
        on_close() -- Actions to be performed when a project is closed.       
        on_quit() -- Actions to be performed when novelyst is closed.               
    """
    VERSION = '@release'
    NOVELYST_API = '4.35'
    DESCRIPTION = 'A button bar'
    URL = 'https://peter88213.github.io/novelyst_buttons'
    _HELP_URL = 'https://peter88213.github.io/novelyst_buttons/usage'

    def install(self, ui):
        """Add a button bar.
        
        Positional arguments:
            ui -- reference to the NovelystTk instance of the application.
        """
        self._ui = ui

        # Add an entry to the Help menu.
        self._ui.helpMenu.add_command(label=_('Buttonbar plugin Online help'),
                                      command=lambda: webbrowser.open(self._HELP_URL))

        iconPath = f'{os.path.dirname(sys.argv[0])}/plugin/icons'.replace('\\', '/')

        # Add a button bar to the editor window.
        self._buttonBar = tk.Frame(self._ui.mainWindow)
        self._buttonBar.pack(expand=False, before=self._ui.appWindow, fill='both')

        # "Go back" button.
        goBackIcon = tk.PhotoImage(file=f'{iconPath}/nb_goBack.png')
        self._goBackButton = ttk.Button(self._buttonBar,
                                            image=goBackIcon,
                                            command=self._ui.tv.go_back)
        self._goBackButton.pack(side='left')
        self._goBackButton.image = goBackIcon

        # "Go forward" button.
        goForwardIcon = tk.PhotoImage(file=f'{iconPath}/nb_goForward.png')
        self._goForwardButton = ttk.Button(self._buttonBar,
                                            image=goForwardIcon,
                                            command=self._ui.tv.go_forward)
        self._goForwardButton.pack(side='left')
        self._goForwardButton.image = goForwardIcon

        # Separator.
        tk.Frame(self._buttonBar, bg='light gray', width=1).pack(side='left', fill='y', padx=4)

        # "View Book" button.
        viewBookIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewBook.png')
        self._viewBookButton = ttk.Button(self._buttonBar,
                                            image=viewBookIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.NV_ROOT))
        self._viewBookButton.pack(side='left')
        self._viewBookButton.image = viewBookIcon

        # "View Characters" button.
        viewCharactersIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewCharacters.png')
        self._viewCharactersButton = ttk.Button(self._buttonBar,
                                            image=viewCharactersIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.CR_ROOT))
        self._viewCharactersButton.pack(side='left')
        self._viewCharactersButton.image = viewCharactersIcon

        # "View Locations" button.
        viewLocationsIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewLocations.png')
        self._viewLocationsButton = ttk.Button(self._buttonBar,
                                            image=viewLocationsIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.LC_ROOT))
        self._viewLocationsButton.pack(side='left')
        self._viewLocationsButton.image = viewLocationsIcon

        # "View Items" button.
        viewItemsIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewItems.png')
        self._viewItemsButton = ttk.Button(self._buttonBar,
                                            image=viewItemsIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.IT_ROOT))
        self._viewItemsButton.pack(side='left')
        self._viewItemsButton.image = viewItemsIcon

        # "View Research" button.
        viewResearchIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewResearch.png')
        self._viewResearchButton = ttk.Button(self._buttonBar,
                                            image=viewResearchIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.RS_ROOT))
        self._viewResearchButton.pack(side='left')
        self._viewResearchButton.image = viewResearchIcon

        # "View Planning" button.
        viewPlanningIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewPlanning.png')
        self._viewPlanningButton = ttk.Button(self._buttonBar,
                                            image=viewPlanningIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.PL_ROOT))
        self._viewPlanningButton.pack(side='left')
        self._viewPlanningButton.image = viewPlanningIcon

        # "View Projectnotes" button.
        viewProjectnotesIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewProjectnotes.png')
        self._viewProjectnotesButton = ttk.Button(self._buttonBar,
                                            image=viewProjectnotesIcon,
                                            command=lambda: self._ui.tv.show_branch(self._ui.tv.PN_ROOT))
        self._viewProjectnotesButton.pack(side='left')
        self._viewProjectnotesButton.image = viewProjectnotesIcon

        # Separator.
        tk.Frame(self._buttonBar, bg='light gray', width=1).pack(side='left', fill='y', padx=4)

        # "Save" button.
        saveIcon = tk.PhotoImage(file=f'{iconPath}/nb_save.png')
        self._saveButton = ttk.Button(self._buttonBar,
                                      image=saveIcon,
                                      command=self._ui.save_project)
        self._saveButton.pack(side='left')
        self._saveButton.image = saveIcon

        # "Reload" button.
        reloadIcon = tk.PhotoImage(file=f'{iconPath}/nb_reload.png')
        self._reloadButton = ttk.Button(self._buttonBar,
                                        image=reloadIcon,
                                        command=self._ui.reload_project)
        self._reloadButton.pack(side='left')
        self._reloadButton.image = reloadIcon

        # "Lock/Unlock" button.
        lockIcon = tk.PhotoImage(file=f'{iconPath}/nb_lock.png')
        self._lockButton = ttk.Button(self._buttonBar,
                                      image=lockIcon,
                                      command=self._ui.toggle_lock)
        self._lockButton.pack(side='left')
        self._lockButton.image = lockIcon

        # "Discard manuscript" button.
        discardIcon = tk.PhotoImage(file=f'{iconPath}/nb_discard.png')
        self._discardButton = ttk.Button(self._buttonBar,
                                            image=discardIcon,
                                            command=self._ui.discard_manuscript)
        self._discardButton.pack(side='left')
        self._discardButton.image = discardIcon

        # "Manuscript" button.
        manuscriptIcon = tk.PhotoImage(file=f'{iconPath}/nb_manuscript.png')
        self._manuscriptButton = ttk.Button(self._buttonBar,
                                            image=manuscriptIcon,
                                            command=lambda:self._ui.export_document('_manuscript'))
        self._manuscriptButton.pack(side='left')
        self._manuscriptButton.image = manuscriptIcon

        # Reverse order (side='right').

        # "Toggle properties" button.
        propertiesIcon = tk.PhotoImage(file=f'{iconPath}/nb_properties.png')
        self._propertiesButton = ttk.Button(self._buttonBar,
                                            image=propertiesIcon,
                                            command=self._ui.toggle_properties)
        self._propertiesButton.pack(side='right')
        self._propertiesButton.image = propertiesIcon

        # "Toggle content viewer" button.
        viewerIcon = tk.PhotoImage(file=f'{iconPath}/nb_viewer.png')
        self._viewerButton = ttk.Button(self._buttonBar,
                                        image=viewerIcon,
                                        command=self._ui.toggle_viewer)
        self._viewerButton.pack(side='right')
        self._viewerButton.image = viewerIcon

        if ENABLE_HOVERTIPS:
            try:
                from idlelib.tooltip import Hovertip
            except ModuleNotFoundError:
                pass
            else:
                Hovertip(self._saveButton, _('Save'))
                Hovertip(self._reloadButton, _('Reload'))
                Hovertip(self._lockButton, _('Lock/unlock'))
                Hovertip(self._discardButton, _('Discard manuscript'))
                Hovertip(self._manuscriptButton, _('Export Manuscript for editing'))
                Hovertip(self._viewBookButton, _('Show Book'))
                Hovertip(self._viewCharactersButton, _('Show Characters'))
                Hovertip(self._viewLocationsButton, _('Show Locations'))
                Hovertip(self._viewItemsButton, _('Show Items'))
                Hovertip(self._viewResearchButton, _('Show Research'))
                Hovertip(self._viewPlanningButton, _('Show Planning'))
                Hovertip(self._viewProjectnotesButton, _('Show Project notes'))
                Hovertip(self._goBackButton, _('Go back in the browsing history'))
                Hovertip(self._goForwardButton, _('Go forward in the browsing history'))
                Hovertip(self._propertiesButton, _('Toggle Properties'))
                Hovertip(self._viewerButton, _('Toggle Text viewer'))

    def disable_menu(self):
        """Disable menu entries when no project is open."""
        self._saveButton.config(state='disabled')
        self._reloadButton.config(state='disabled')
        self._lockButton.config(state='disabled')
        self._discardButton.config(state='disabled')
        self._manuscriptButton.config(state='disabled')
        self._viewBookButton.config(state='disabled')
        self._viewCharactersButton.config(state='disabled')
        self._viewLocationsButton.config(state='disabled')
        self._viewItemsButton.config(state='disabled')
        self._viewResearchButton.config(state='disabled')
        self._viewPlanningButton.config(state='disabled')
        self._viewProjectnotesButton.config(state='disabled')
        self._goBackButton.config(state='disabled')
        self._goForwardButton.config(state='disabled')
        self._propertiesButton.config(state='disabled')
        self._viewerButton.config(state='disabled')

    def enable_menu(self):
        """Enable menu entries when a project is open."""
        self._saveButton.config(state='normal')
        self._reloadButton.config(state='normal')
        self._lockButton.config(state='normal')
        self._discardButton.config(state='normal')
        self._manuscriptButton.config(state='normal')
        self._viewBookButton.config(state='normal')
        self._viewCharactersButton.config(state='normal')
        self._viewLocationsButton.config(state='normal')
        self._viewItemsButton.config(state='normal')
        self._viewResearchButton.config(state='normal')
        self._viewPlanningButton.config(state='normal')
        self._viewProjectnotesButton.config(state='normal')
        self._goBackButton.config(state='normal')
        self._goForwardButton.config(state='normal')
        self._propertiesButton.config(state='normal')
        self._viewerButton.config(state='normal')

