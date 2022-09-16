from libqtile.bar import Bar
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName
from libqtile.widget.cpu import CPU
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.systray import Systray
from libqtile.widget.clock import Clock
from libqtile.widget.spacer import Spacer
from libqtile.widget.volume import Volume
from libqtile.widget.keyboardlayout import KeyboardLayout
from libqtile.widget.prompt import Prompt
from libqtile.widget.chord import Chord

from unicodes import left_half_circle, right_half_circle
import colors

colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colors.dracula()
bar = Bar([
    left_half_circle(colors[1]),
    WindowCount(
        text_format='缾 {num}',
        background=backgroundColor,
        foreground=foregroundColor,
        show_zero=True,
    ),
    right_half_circle(colors[1]),

    left_half_circle(colors[8]),
    CurrentLayout(
        background=colors[8],
        ),
    right_half_circle(colors[8]),

    Spacer(length=2),

    left_half_circle(colors[6]),
    GroupBox(
                background=colors[6],
        ),
    right_half_circle(colors[6]),

    Spacer(length=2),

    Prompt(),
    left_half_circle(colors[8]),
    WindowName(
                background=colors[8],
        ),
    right_half_circle(colors[8]),
    Chord(
       chords_colors={
      "launch": ("#ff0000", "#ffffff"),
       },
   name_transform=lambda name: name.upper(),
   ),
#    TextBox("default config", name="default"),
#    TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
#    Volume(fontsize=10, update_interval=2),

Spacer(length=2),

    # left_half_circle(colors[2]),
    # Volume(
    #     foreground = colors[1],
    #     background = colors[2],
    #     fmt = 'Vol: {}',
    #     padding = 5
    # ),
    # right_half_circle(colors[2]),

    Spacer(length=2),

    left_half_circle(colors[10]),
    Net(
        interface = "wlp1s0",
        format = ' {down} ↓↑ {up}',
        foreground = colors[1],
        background = colors[10],
        padding = 5
    ),
    right_half_circle(colors[10]),
    Spacer(length=2),

    left_half_circle(colors[4]),

    Clock(
        foreground = colors[1],
        background = colors[4],
        format = "%a, %d%b > %I:%M %p "
    ),
	       #Clock(format="%Y-%m-%d %a %I:%M %p"),
    right_half_circle(colors[4]),
    Spacer(length=2),
    left_half_circle(colors[5]),

   KeyboardLayout(
        foreground = colors[1],
        background = colors[5],
        fmt = 'KB: {}',
        padding = 5
    ),

    right_half_circle(colors[5]),
    Spacer(length=2),
    left_half_circle(colors[6]),

    Memory(
        foreground = colors[1],
        background = colors[6],
        mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
        # fmt = 'Mem: {}',
         format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
         padding = 5
    ),

    right_half_circle(colors[6]),
    Spacer(length=2),
    left_half_circle(colors[1]),

    Systray(
        background = colors[1],
        padding = 5
    ),
    right_half_circle(colors[1]),
                # QuickExit(),
],
    24,
    margin=[12,15,5,15],
   # background=["#0000ffff"],
   background="#00000000",
    opacity=1,
    border_color="#00000000",
    border_width=[2,0,2,0],
    # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
)
# 	bottom=bar.Gap(1),
# 	left=bar.Gap(1),
# 	right=bar.Gap(1),
#     ),
# ]

