import os
import subprocess
from typing import Callable, List  # noqa: F401

from libqtile import hook

from libqtile.extension.dmenu import DmenuRun
from libqtile.extension.window_list import WindowList
from libqtile.extension.command_set import CommandSet

# import layout objects
from libqtile.layout.columns import Columns
from libqtile.layout.xmonad import MonadTall, MonadWide
from libqtile.layout.stack import Stack
from libqtile.layout.floating import Floating

# import widgets and bar

from libqtile.config import Click, Drag, DropDown, Group, Key, Match, ScratchPad, Screen
from libqtile.lazy import lazy
# from libqtile.utils import guess_terminal

#from colors import gruvbox
import colors

from bar3 import bar

colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colors.dracula()

mod = "mod4"
terminal = "alacritty"
myAppMenu="rofi -show drun"

# terminal = guess_terminal()

keys = [
    Key([mod, "control"], "1", lazy.to_screen(0)),
    Key([mod, "control"], "2", lazy.to_screen(1)),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),

  Key([mod], "d", lazy.spawn(myAppMenu), desc="Launch rofi"),

    # DmenuRun
    Key([mod,"shift"], 'd', lazy.run_extension(DmenuRun(
        font="TerminessTTF Nerd Font",
        fontsize="13",
        dmenu_command="dmenu_run",
        dmenu_prompt=" ",
        dmenu_height=10,
        dmenu_lines=15,
        background=backgroundColor,
        foreground=foregroundColor,
        selected_foreground=colors[2],
        selected_background=foregroundColorTwo,
    ))),

    Key([mod, "shift"], 'w', lazy.run_extension(WindowList(
        all_groups=True,
        font="TerminessTTF Nerd Font",
        fontsize="13",
        dmenu_prompt=" ",
        dmenu_height=10,
        # dmenu_lines=15,
        background=backgroundColor,
        foreground=foregroundColor,
        selected_foreground=colors[2],
        selected_background=foregroundColorTwo,
    ))),

    # Key([mod, "control"], 'n', lazy.run_extension(CommandSet(
    #     commands={
    #         'Thesis notes': 'kitty nvim Neorg/Notes/Thesis/index.norg',
    #         'Dev notes': 'kitty nvim Neorg/Notes/Dev/index.norg',
    #         'JWL notes': 'kitty nvim Neorg/Notes/JWL/index.norg',
    #         'YouTube notes': 'kitty nvim Neorg/YT/index.norg',
    #     },
    #     background=gruvbox['bg'],
    #     foreground=gruvbox['fg'],
    #     dmenu_prompt=' ',
    #     dmenu_lines=10,
    #     dmenu_height=10,
    #     selected_foreground=gruvbox['blue'],
    #     selected_background=gruvbox['bg'],
    # ))),

    # Toggle floating and fullscreen
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen mode"),
    Key([mod, "shift"], "space", lazy.window.toggle_floating(),
        desc="Toggle fullscreen mode"),

    # Keybindings for resizing windows in MonadTall layout
    Key([mod], "i", lazy.layout.grow()),
    Key([mod], "m", lazy.layout.shrink()),
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "o", lazy.layout.maximize()),
    Key([mod, "control"], "space", lazy.layout.flip()),

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
]

#groups = [Group(i) for i in "123456789"]
groups = [
    Group('1', label="𑑑", matches=[
          Match(wm_class='firefox'), Match(wm_class='brave'), Match(wm_class='qutebrowser')], layout="stack"),
    Group('2', label="𑑒", layout="monadtall"),
    Group('3', label="𑑓 ", layout="columns"),
    Group('4', label="𑑔", matches=[
          Match(wm_class='discord'), Match(wm_class='zoom'), Match(wm_class="teams-for-linux")], layout="stack"),
    Group('5', label="𑑕", matches=[Match(wm_class="Spotify")], layout="stack"),
    Group('6', label="𑑖", layout="monadtall"),
    Group('7', label="𑑗 ", layout="monadtall"),
    Group('8', label="𑑘 ", layout="monadtall"),
    Group('9', label="𑑙", layout="monadtall"),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # Key([mod], i.name, lazy.function(go_to_group(i.name))),

        # Or, use below if you prefer not to switch to that group.
        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            desc="move focused window to group {}".format(i.name)),
    ])

# Append scratchpad with dropdowns to groups
groups.append(ScratchPad('scratchpad', [
    DropDown('term', 'alacritty', width=0.8, height=0.5, x=0.1, y=0.1, opacity=1),
    DropDown('mixer', 'pavucontrol', width=0.4,
             height=0.6, x=0.3, y=0.1, opacity=1),
    DropDown('pomo', 'pomotroid', x=0.4, y=0.2, opacity=1),
    DropDown('bitwarden', 'bitwarden-desktop',
             width=0.4, height=0.6, x=0.3, y=0.1, opacity=1),
]))
# extend keys list with keybinding for scratchpad
keys.extend([
    Key(["control"], "1", lazy.group['scratchpad'].dropdown_toggle('term')),
    Key(["control"], "2", lazy.group['scratchpad'].dropdown_toggle('mixer')),
    Key(["control"], "3", lazy.group['scratchpad'].dropdown_toggle('pomo')),
    Key(["control"], "4", lazy.group['scratchpad'].dropdown_toggle('bitwarden')),
])




layouts = [
    Stack(
        border_normal=colors[2],
        border_focus=colors[4],
        border_width=2,
        num_stacks=1,
        margin=8,
    ),
    MonadTall(
        border_normal=colors[2],
        border_focus=colors[4],
        margin=8,
        border_width=2,
        single_border_width=1,
        single_margin=8,
    ),
    Columns(
        border_normal=colors[2],
        border_focus=colors[4],
        border_width=2,
        border_normal_stack=colors [3],
        border_focus_stack=colors[5],
        border_on_single=2,
        margin=8,
        margin_on_single=8,
    )
]

floating_layout = Floating(
    border_normal=colors[2],
    border_focus=colors[4],
    border_width=4,
    float_rules=[
        *Floating.default_float_rules,
        Match(wm_class='confirmreset'),  # gitk
        Match(wm_class='makebranch'),  # gitk
        Match(wm_class='maketag'),  # gitk
        Match(wm_class='ssh-askpass'),  # ssh-askpass
        Match(title='branchdialog'),  # gitk
        Match(title='pinentry'),  # GPG key password entry

        Match(title="Android Emulator - pixel5:5554"),
        Match(wm_class="Genymotion Player"),
        Match(title="AICOMS"),
        Match(wm_class="blueman-manager"),
        Match(wm_class="pavucontrol"),
        Match(wm_class="zoom "),
        Match(wm_class="bitwarden"),
        Match(wm_class="nemo"),
        Match(wm_class="xarchiver"),
    ])

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]
widget_defaults = dict(
    font='TerminessTTF Nerd Font',
    fontsize=13,
    padding=2,
    foreground=colors[1]
)

extension_defaults = widget_defaults.copy()

screens = [
    Screen(top=bar)
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True
auto_minimize = True
wmname = "LG3D"


@ hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.run([home])
