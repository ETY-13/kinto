# -*- coding: utf-8 -*-

import re
from xkeysnail.transform import *

# [Global modemap] Change modifier keys as in xmodmap
define_conditional_modmap(lambda wm_class: wm_class not in ("Gnome-terminal","konsole","io.elementary.terminal","terminator","sakura","guake","tilda","xterm","eterm","kitty"),{
    # # Chromebook
    # Key.LEFT_ALT: Key.RIGHT_CTRL,   # Chromebook
    # Key.LEFT_CTRL: Key.LEFT_ALT,    # Chromebook
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,  # Chromebook
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,  # Chromebook

    # Default Mac/Win
    Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
    Key.LEFT_META: Key.LEFT_ALT,    # WinMac
    Key.LEFT_CTRL: Key.LEFT_META,   # WinMac
    Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac
    Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac
    Key.RIGHT_CTRL: Key.RIGHT_META, # WinMac

    # # Mac Only
    # Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
    # Key.LEFT_CTRL: Key.LEFT_META,   # Mac
    # Key.RIGHT_META: Key.RIGHT_CTRL, # Mac
    # Key.RIGHT_CTRL: Key.RIGHT_META, # Mac
})

# [Conditional modmap] Change modifier keys in certain applications
define_conditional_modmap(re.compile("Gnome-terminal|konsole|io.elementary.terminal|terminator|sakura|guake|tilda|xterm|eterm|kitty"), {
    # # Chromebook
    # Key.LEFT_ALT: Key.RIGHT_CTRL,
    # # Left Ctrl Stays Left Ctrl
    # Key.LEFT_META: Key.LEFT_ALT,
    # Key.RIGHT_ALT: Key.RIGHT_CTRL,
    # Key.RIGHT_CTRL: Key.RIGHT_ALT,
    # # Right Meta does not exist on chromebooks

    # Default Mac/Win
    Key.LEFT_ALT: Key.RIGHT_CTRL,   # WinMac
    Key.LEFT_META: Key.LEFT_ALT,    # WinMac
    Key.LEFT_CTRL: Key.LEFT_CTRL,   # WinMac
    Key.RIGHT_ALT: Key.RIGHT_CTRL,  # WinMac
    Key.RIGHT_META: Key.RIGHT_ALT,  # WinMac
    Key.RIGHT_CTRL: Key.LEFT_CTRL,  # WinMac

    # # Mac Only
    # Key.LEFT_META: Key.RIGHT_CTRL,  # Mac
    # # Left Ctrl Stays Left Ctrl
    # Key.RIGHT_META: Key.RIGHT_CTRL, # Mac
    # Key.RIGHT_CTRL: Key.LEFT_CTRL,  # Mac
})

# Keybindings for Sublime Text
define_keymap(re.compile("Sublime_text"),{
    K("C-Super-up"): K("M-o"),                  # Switch file
    K("C-M-f"): K("f11"),                       # toggle_full_screen
    K("C-M-v"): [K("C-k"), K("C-v")],           # paste_from_history
    K("C-up"): pass_through_key,                # cancel scroll_lines up
    K("Super-M-up"): K("C-up"),                 # scroll_lines up
    K("C-down"): pass_through_key,              # cancel scroll_lines down
    K("Super-M-down"): K("C-down"),             # scroll_lines down
    K("C-PAGE_DOWN"): pass_through_key,         # cancel next_view
    K("C-PAGE_UP"): pass_through_key,           # cancel prev_view
    K("C-Shift-left_brace"): K("C-PAGE_DOWN"),  # next_view
    K("C-Shift-right_brace"): K("C-PAGE_UP"),   # prev_view
    K("C-M-right"): K("C-PAGE_DOWN"),           # next_view
    K("C-M-left"): K("C-PAGE_UP"),              # prev_view
    K("insert"): pass_through_key,              # cancel toggle_overwrite
    K("C-M-o"): K("insert"),                    # toggle_overwrite
    K("M-c"): pass_through_key,                 # cancel toggle_case_sensitive
    K("C-M-c"): K("M-c"),                       # toggle_case_sensitive
    K("C-h"): pass_through_key,                 # cancel replace
    K("C-M-f"): K("C-h"),                       # replace
    K("C-Shift-h"): pass_through_key,           # cancel replace_next
    K("C-M-e"): K("C-Shift-h"),                 # replace_next
    K("f3"): pass_through_key,                  # cancel find_next
    K("C-g"): K("f3"),                          # find_next
    K("Shift-f3"): pass_through_key,            # cancel find_prev
    K("C-Shift-g"): K("Shift-f3"),              # find_prev
    K("C-f3"): pass_through_key,                # cancel find_under
    K("Super-M-g"): K("C-f3"),                  # find_under
    K("C-Shift-f3"): pass_through_key,          # cancel find_under_prev
    K("Super-M-Shift-g"): K("C-Shift-f3"),      # find_under_prev
    K("M-f3"): pass_through_key,                # Default - cancel find_all_under
    # K("M-Refresh"): pass_through_key,           # Chromebook - cancel find_all_under
    # K("M-C-g"): K("M-Refresh"),                 # Chromebook - find_all_under
    K("Super-C-g"): K("M-f3"),                  # Default - find_all_under
    K("C-Shift-up"): pass_through_key,          # cancel swap_line_up
    K("Super-C-up"): K("C-Shift-up"),           # swap_line_up
    K("C-Shift-down"): pass_through_key,        # cancel swap_line_down
    K("Super-C-down"): K("C-Shift-down"),       # swap_line_down
    K("C-Pause"): pass_through_key,             # cancel cancel_build
    K("Super-c"): K("C-Pause"),                 # cancel_build
    K("f9"): pass_through_key,                  # cancel sort_lines case_s false
    K("f5"): K("f9"),                           # sort_lines case_s false
    K("Super-f9"): pass_through_key,            # cancel sort_lines case_s true
    K("Super-f5"): K("Super-f9"),               # sort_lines case_s true
    K("M-Shift-Key_1"): pass_through_key,       # cancel set_layout
    K("C-M-Key_1"): K("M-Shift-Key_1"),         # set_layout
    K("M-Shift-Key_2"): pass_through_key,       # cancel set_layout
    K("C-M-Key_2"): K("M-Shift-Key_2"),         # set_layout
    K("M-Shift-Key_3"): pass_through_key,       # cancel set_layout
    K("C-M-Key_3"): K("M-Shift-Key_3"),         # set_layout
    K("M-Shift-Key_4"): pass_through_key,       # cancel set_layout
    K("C-M-Key_4"): K("M-Shift-Key_4"),         # set_layout
    K("M-Shift-Key_8"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_2"): K("M-Shift-Key_8"),   # set_layout
    K("M-Shift-Key_9"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_3"): K("M-Shift-Key_9"),   # set_layout
    K("M-Shift-Key_5"): pass_through_key,       # cancel set_layout
    K("C-M-Shift-Key_5"): K("M-Shift-Key_5"),   # set_layout
    # K(""): pass_through_key,                    # cancel
    # K(""): K(""),                               #
}, "Sublime Text")

define_keymap(None,{
    # Cmd Tab - App Switching Default
    K("RC-Tab"): K("RC-F13"),
    K("RC-Shift-Tab"): K("RC-Shift-F13"),
    K("RC-Grave"): K("RC-Shift-F13"),
    # In-App Tab switching
    # K("M-Tab"): K("C-Tab"),                   # Chromebook
    # K("M-Shift-Tab"): K("C-Shift-Tab"),       # Chromebook
    K("Super-Tab"): K("LC-Tab"),                # Default
    K("Super-Shift-Tab"): K("LC-Shift-Tab"),    # Default
    K("LC-Grave") : K("LC-Shift-Tab"),          # Default

    # Wordwise
    K("RC-Left"): K("Home"),        # Beginning of Line
    K("RC-Right"): K("End"),        # End of Line
    K("M-Left"): K("C-Left"),       # Left of Word
    K("M-Right"): K("C-Right"),     # Right of Word
    K("RC-Up"): K("C-Home"),        # Beginning of File
    K("RC-Down"): K("C-End"),       # End of File
    K("M-Backspace"): K("Delete"),  # Delete
    # K(""): pass_through_key,        # cancel
    # K(""): K(""),                   #
})

# define_keymap(re.compile("Gnome-terminal|io.elementary.terminal|terminator|sakura|guake|tilda|xterm|eterm|kitty"),{
#     # Ctrl Tab - In App Tab Switching
#     # LC is already set
#     K("LC-Grave") : K("LC-Shift-Tab"),
# }, "Terminals tab switching")

define_keymap(re.compile("konsole"),{
    # Ctrl Tab - In App Tab Switching
    K("LC-Tab") : K("Shift-Right"),
    K("LC-Shift-Tab") : K("Shift-Left"),
    K("LC-Grave") : K("Shift-Left"),

}, "Konsole tab switching")



define_keymap(re.compile("Gnome-terminal|konsole|io.elementary.terminal|terminator|sakura|guake|tilda|xterm|eterm|kitty"),{
    # Ctrl Tab - In App Tab Switching
    K("LC-Tab") : K("LC-PAGE_DOWN"),
    K("LC-Shift-Tab") : K("LC-PAGE_UP"),
    K("LC-Grave") : K("LC-PAGE_UP"),
    # Converts Cmd to use Ctrl-Shift
    K("RC-Tab"): K("RC-F13"),
    K("RC-Shift-Tab"): K("RC-Shift-F13"),
    K("RC-V"): K("C-Shift-V"),
    K("RC-MINUS"): K("C-Shift-MINUS"),
    K("RC-EQUAL"): K("C-Shift-EQUAL"),
    K("RC-BACKSPACE"): K("C-Shift-BACKSPACE"),
    K("RC-Q"): K("C-Shift-Q"),
    K("RC-W"): K("C-Shift-W"),
    K("RC-E"): K("C-Shift-E"),
    K("RC-R"): K("C-Shift-R"),
    K("RC-T"): K("C-Shift-t"),
    K("RC-Y"): K("C-Shift-Y"),
    K("RC-U"): K("C-Shift-U"),
    K("RC-I"): K("C-Shift-I"),
    K("RC-O"): K("C-Shift-O"),
    K("RC-P"): K("C-Shift-P"),
    K("RC-LEFT_BRACE"): K("C-Shift-LEFT_BRACE"),
    K("RC-RIGHT_BRACE"): K("C-Shift-RIGHT_BRACE"),
    K("RC-A"): K("C-Shift-A"),
    K("RC-S"): K("C-Shift-S"),
    K("RC-D"): K("C-Shift-D"),
    K("RC-F"): K("C-Shift-F"),
    K("RC-G"): K("C-Shift-G"),
    K("RC-H"): K("C-Shift-H"),
    K("RC-J"): K("C-Shift-J"),
    K("RC-K"): K("C-Shift-K"),
    K("RC-L"): K("C-Shift-L"),
    K("RC-SEMICOLON"): K("C-Shift-SEMICOLON"),
    K("RC-APOSTROPHE"): K("C-Shift-APOSTROPHE"),
    K("RC-GRAVE"): K("C-Shift-GRAVE"),
    K("RC-BACKSLASH"): K("C-Shift-BACKSLASH"),
    K("RC-Z"): K("C-Shift-Z"),
    K("RC-X"): K("C-Shift-X"),
    K("RC-C"): K("C-Shift-C"),
    K("RC-V"): K("C-Shift-V"),
    K("RC-B"): K("C-Shift-B"),
    K("RC-N"): K("C-Shift-N"),
    K("RC-M"): K("C-Shift-M"),
    K("RC-COMMA"): K("C-Shift-COMMA"),
    K("RC-DOT"): K("C-Shift-DOT"),
    K("RC-SLASH"): K("C-Shift-SLASH"),
    K("RC-KPASTERISK"): K("C-Shift-KPASTERISK"),
}, "terminals")

# define_keymap(re.compile("Chromium-browser"),{
#     # K("RC-Tab"): K("C-F13"),
#     # K("RC-Shift-Tab"): K("C-f1"),
# }, "Chromium-browser")
