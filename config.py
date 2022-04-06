import subprocess, os, json

#Pywal Colors
colors = os.path.expanduser('~/.cache/wal/colors.json')
colordict = json.load(open(colors))
ColorZ=(colordict['colors']['color0'])
ColorA=(colordict['colors']['color1'])
ColorB=(colordict['colors']['color2'])
ColorC=(colordict['colors']['color3'])
ColorD=(colordict['colors']['color4'])
ColorE=(colordict['colors']['color5'])
ColorF=(colordict['colors']['color6'])
ColorG=(colordict['colors']['color7'])
ColorH=(colordict['colors']['color8'])
ColorI=(colordict['colors']['color9'])


#Bindings from DT (https://gitlab.com/dwt1/dotfiles/-/blob/master/.config/qutebrowser/config.py)
config.bind('M', 'hint links spawn mpv {hint-url}')
config.bind('xb', 'config-cycle statusbar.show always never')
config.bind('xt', 'config-cycle tabs.show always never')

config.load_autoconfig(False)
c.url.start_pages = ["file:///home/user/.local/share/start-page/min.html"]
c.url.default_page = "file:///home/user/.local/share/start-page/min.html"

# Adblock list from nephitejnf (https://gist.github.com/nephitejnf/3457258c0c4d444c33f562444e7b795c)
c.content.blocking.method = 'both'
c.content.blocking.adblock.lists = [
        "https://easylist.to/easylist/easylist.txt",
        "https://easylist.to/easylist/easyprivacy.txt",
        "https://easylist.to/easylist/fanboy-social.txt",
        "https://secure.fanboy.co.nz/fanboy-annoyance.txt",
        "https://easylist-downloads.adblockplus.org/abp-filters-anti-cv.txt",
        "https://pgl.yoyo.org/adservers/serverlist.php?showintro=0;hostformat=hosts",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/legacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2020.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/filters-2021.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badware.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/privacy.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/badlists.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/annoyances.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/resource-abuse.txt",
        "https://www.i-dont-care-about-cookies.eu/abp/",
        "https://secure.fanboy.co.nz/fanboy-cookiemonster.txt",
        "https://github.com/uBlockOrigin/uAssets/raw/master/filters/unbreak.txt"]

# Modified Font settings from Ape (https://gist.github.com/Ape/d0c48b3f7ec9c8efaecf48eaa1e75d0d)
monospace = "12px 'JetBrains Mono'"
sans = "bold 12px 'Noto sans'"
# Font used in the completion categories.
c.fonts.completion.category = "bold 12px 'JetBrains Mono'"

# Font used in the completion widget.
c.fonts.completion.entry = monospace

# Font used for the debugging console.
c.fonts.debug_console = monospace

# Font used for the downloadbar.
c.fonts.downloads = monospace

# Font used in the keyhint widget.
c.fonts.keyhint = monospace

# Font used for error messages.
c.fonts.messages.error = monospace

# Font used for info messages.
c.fonts.messages.info = monospace

# Font used for warning messages.
c.fonts.messages.warning = monospace

# Font used for prompts.
c.fonts.prompts = monospace

# Font used in the statusbar.
c.fonts.statusbar = monospace

# Font used in the tab bar.
c.fonts.tabs.selected = sans 
c.fonts.tabs.unselected = sans

# Font used for the hints.
c.fonts.hints = "bold 13px 'JetBrains Mono'"
# 
# Modified gruvbox dark hard qutebrowser theme 
#
# Originally based on:
#   gruvbox dark hard qutebrowser theme by Florian Bruhin <me@the-compiler.org>
#   base16-qutebrowser (https://github.com/theova/base16-qutebrowser)
#   Base16 qutebrowser template by theova and Daniel Mulford
#   Gruvbox dark, hard scheme by Dawid Kurek (dawikur@gmail.com), morhetz (https://github.com/morhetz/gruvbox)

bg0_hard = "#1d2021"
bg0_soft = '#32302f'
bg0_normal = '#282828'

bg0 = bg0_normal
bg1 = "#3c3836"
bg2 = "#504945"
bg3 = "#665c54"
bg4 = "#7c6f64" 

fg0 = "#fbf1c7"
fg1 = "#ebdbb2"
fg2 = ColorG
fg3 = "#bdae93"
fg4 = "#a89984"

bright_red = "#fb4934"
bright_green = "#b8bb26"
bright_yellow = "#fabd2f"
bright_blue = "#83a598"
bright_purple = "#d3869b"
bright_aqua = "#8ec07c"
bright_gray = "#928374"
bright_orange = "#fe8019"

dark_red = "#cc241d"
dark_green = "#98971a"
dark_yellow = "#d79921"
dark_blue = "#458588"
dark_purple = "#b16286"
dark_aqua = "#689d6a"
dark_gray = "#a89984"
dark_orange = "#d65d0e"

### Completion

# Text color of the completion widget. May be a single color to use for
# all columns or a list of three colors, one for each column.
c.colors.completion.fg = [fg1, bright_aqua, bright_yellow]

# Background color of the completion widget for odd rows.
c.colors.completion.odd.bg = bg0

# Background color of the completion widget for even rows.
c.colors.completion.even.bg = c.colors.completion.odd.bg

# Foreground color of completion widget category headers.
c.colors.completion.category.fg = bright_blue

# Background color of the completion widget category headers.
c.colors.completion.category.bg = bg1

# Top border color of the completion widget category headers.
c.colors.completion.category.border.top = c.colors.completion.category.bg

# Bottom border color of the completion widget category headers.
c.colors.completion.category.border.bottom = c.colors.completion.category.bg

# Foreground color of the selected completion item.
c.colors.completion.item.selected.fg = fg0

# Background color of the selected completion item.
c.colors.completion.item.selected.bg = bg4

# Top border color of the selected completion item.
c.colors.completion.item.selected.border.top = bg2

# Bottom border color of the selected completion item.
c.colors.completion.item.selected.border.bottom = c.colors.completion.item.selected.border.top

# Foreground color of the matched text in the selected completion item.
c.colors.completion.item.selected.match.fg = bright_orange

# Foreground color of the matched text in the completion.
c.colors.completion.match.fg = c.colors.completion.item.selected.match.fg

# Color of the scrollbar handle in the completion view.
c.colors.completion.scrollbar.fg = c.colors.completion.item.selected.fg

# Color of the scrollbar in the completion view.
c.colors.completion.scrollbar.bg = c.colors.completion.category.bg

### Context menu

# Background color of disabled items in the context menu.
c.colors.contextmenu.disabled.bg = bg3

# Foreground color of disabled items in the context menu.
c.colors.contextmenu.disabled.fg = fg3

# Background color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.bg = bg0

# Foreground color of the context menu. If set to null, the Qt default is used.
c.colors.contextmenu.menu.fg =  fg2

# Background color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.bg = bg2

#Foreground color of the context menu’s selected item. If set to null, the Qt default is used.
c.colors.contextmenu.selected.fg = c.colors.contextmenu.menu.fg

### Downloads

# Background color for the download bar.
c.colors.downloads.bar.bg = bg0

# Color gradient start for download text.
c.colors.downloads.start.fg = bg0

# Color gradient start for download backgrounds.
c.colors.downloads.start.bg = bright_blue

# Color gradient end for download text.
c.colors.downloads.stop.fg = c.colors.downloads.start.fg

# Color gradient stop for download backgrounds.
c.colors.downloads.stop.bg = bright_aqua

# Foreground color for downloads with errors.
c.colors.downloads.error.fg = bright_red

### Hints

# Font color for hints.
c.colors.hints.fg = bg0

# Background color for hints.
c.colors.hints.bg = 'rgba(250, 191, 47, 200)'  # bright_yellow

# Font color for the matched part of hints.
c.colors.hints.match.fg = bg4

### Keyhint widget

# Text color for the keyhint widget.
c.colors.keyhint.fg = fg4

# Highlight color for keys to complete the current keychain.
c.colors.keyhint.suffix.fg = fg0

# Background color of the keyhint widget.
c.colors.keyhint.bg = bg0

### Messages

# Foreground color of an error message.
c.colors.messages.error.fg = bg0

# Background color of an error message.
c.colors.messages.error.bg = bright_red

# Border color of an error message.
c.colors.messages.error.border = c.colors.messages.error.bg

# Foreground color of a warning message.
c.colors.messages.warning.fg = bg0

# Background color of a warning message.
c.colors.messages.warning.bg = bright_purple

# Border color of a warning message.
c.colors.messages.warning.border = c.colors.messages.warning.bg

# Foreground color of an info message.
c.colors.messages.info.fg = fg2

# Background color of an info message.
c.colors.messages.info.bg = bg0

# Border color of an info message.
c.colors.messages.info.border = c.colors.messages.info.bg

### Prompts

# Foreground color for prompts.
c.colors.prompts.fg = fg2

# Border used around UI elements in prompts.
c.colors.prompts.border = f'1px solid {bg1}'

# Background color for prompts.
c.colors.prompts.bg = bg3

# Background color for the selected item in filename prompts.
c.colors.prompts.selected.bg = bg2

### Statusbar

# Foreground color of the statusbar.
c.colors.statusbar.normal.fg = fg2

# Background color of the statusbar.
c.colors.statusbar.normal.bg = bg0

# Foreground color of the statusbar in insert mode.
c.colors.statusbar.insert.fg = fg2

# Background color of the statusbar in insert mode.
c.colors.statusbar.insert.bg = bg4

# Foreground color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.fg = bg0

# Background color of the statusbar in passthrough mode.
c.colors.statusbar.passthrough.bg = dark_blue

# Foreground color of the statusbar in private browsing mode.
c.colors.statusbar.private.fg = bright_purple

# Background color of the statusbar in private browsing mode.
c.colors.statusbar.private.bg = bg0

# Foreground color of the statusbar in command mode.
c.colors.statusbar.command.fg = fg3

# Background color of the statusbar in command mode.
c.colors.statusbar.command.bg = bg1

# Foreground color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.fg = c.colors.statusbar.private.fg

# Background color of the statusbar in private browsing + command mode.
c.colors.statusbar.command.private.bg = c.colors.statusbar.command.bg

# Foreground color of the statusbar in caret mode.
c.colors.statusbar.caret.fg = bg0

# Background color of the statusbar in caret mode.
c.colors.statusbar.caret.bg = dark_purple

# Foreground color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.fg = c.colors.statusbar.caret.fg

# Background color of the statusbar in caret mode with a selection.
c.colors.statusbar.caret.selection.bg = bright_purple

# Background color of the progress bar.
c.colors.statusbar.progress.bg = bright_blue

# Default foreground color of the URL in the statusbar.
c.colors.statusbar.url.fg = fg4

# Foreground color of the URL in the statusbar on error.
c.colors.statusbar.url.error.fg = dark_red

# Foreground color of the URL in the statusbar for hovered links.
c.colors.statusbar.url.hover.fg = bright_aqua

# Foreground color of the URL in the statusbar on successful load
# (http).
c.colors.statusbar.url.success.http.fg = fg2

# Foreground color of the URL in the statusbar on successful load
# (https).
c.colors.statusbar.url.success.https.fg = fg2

# Foreground color of the URL in the statusbar when there's a warning.
c.colors.statusbar.url.warn.fg = bright_purple

### tabs

# Background color of the tab bar.
c.colors.tabs.bar.bg = bg0

# Color gradient start for the tab indicator.
c.colors.tabs.indicator.start = bright_blue

# Color gradient end for the tab indicator.
c.colors.tabs.indicator.stop = fg2

# Color for the tab indicator on errors.
c.colors.tabs.indicator.error = bright_red

# Foreground color of unselected odd tabs.
c.colors.tabs.odd.fg = fg2

# Background color of unselected odd tabs.
c.colors.tabs.odd.bg = bg2

# Foreground color of unselected even tabs.
c.colors.tabs.even.fg = c.colors.tabs.odd.fg

# Background color of unselected even tabs.
c.colors.tabs.even.bg = bg3

# Foreground color of selected odd tabs.
c.colors.tabs.selected.odd.fg = fg2

# Background color of selected odd tabs.
c.colors.tabs.selected.odd.bg = bg0

# Foreground color of selected even tabs.
c.colors.tabs.selected.even.fg = c.colors.tabs.selected.odd.fg

# Background color of selected even tabs.
c.colors.tabs.selected.even.bg = bg0

# Background color of pinned unselected even tabs.
c.colors.tabs.pinned.even.bg = bright_green

# Foreground color of pinned unselected even tabs.
c.colors.tabs.pinned.even.fg = bg2

# Background color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.bg = bright_green

# Foreground color of pinned unselected odd tabs.
c.colors.tabs.pinned.odd.fg = c.colors.tabs.pinned.even.fg

# Background color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.bg = bg0

# Foreground color of pinned selected even tabs.
c.colors.tabs.pinned.selected.even.fg = c.colors.tabs.selected.odd.fg

# Background color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.bg = c.colors.tabs.pinned.selected.even.bg

# Foreground color of pinned selected odd tabs.
c.colors.tabs.pinned.selected.odd.fg = c.colors.tabs.selected.odd.fg

# Background color for webpages if unset (or empty to use the theme's
# color).
c.colors.webpage.bg = bg4
