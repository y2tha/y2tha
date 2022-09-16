from libqtile.bar import Bar
from libqtile.widget.clock import Clock
from libqtile.widget.cpu import CPU
from libqtile.widget.currentlayout import CurrentLayout
from libqtile.widget.groupbox import GroupBox
from libqtile.widget.memory import Memory
from libqtile.widget.net import Net
from libqtile.widget.spacer import Spacer
from libqtile.widget.systray import Systray
from libqtile.widget.window_count import WindowCount
from libqtile.widget.windowname import WindowName

from unicodes import right_arrow, left_arrow
import colors

colors, backgroundColor, foregroundColor, workspaceColor, foregroundColorTwo = colors.everforest()
bar = Bar([
    GroupBox(
        disable_drag=True,
        active=colors[2],
        inactive=colors[1],
        highlight_method='line',
        block_highlight_text_color=colors[7],
        borderwidth=0,
       # highlight_color=backgroundColor,
        highlight_color = [backgroundColor, workspaceColor],
        background=backgroundColor
    ),
    right_arrow(colors[0], backgroundColor),
    CurrentLayout(
        background=backgroundColor,
        foreground=foregroundColorTwo
    ),
    right_arrow(foregroundColorTwo, backgroundColor),

    WindowCount(
        text_format='缾 {num}',
        background=backgroundColor,
        foreground=foregroundColor,
        show_zero=True,
    ),

    right_arrow(foregroundColor, backgroundColor),
    WindowName(foreground=foregroundColorTwo),

    left_arrow(foregroundColor, backgroundColor),
    CPU(
        format=' {freq_current}GHz {load_percent}%',
        background=backgroundColor,
        foreground=foregroundColorTwo
    ),

    left_arrow(foregroundColor, foregroundColor),
    Memory(
        format=' {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
        background=backgroundColor,
        foreground=foregroundColorTwo
    ),

    left_arrow(foregroundColor, colors[6]),
    Net(
        background=backgroundColor,
        foreground=foregroundColorTwo
    ),

    left_arrow(foregroundColor, foregroundColor),
    Clock(
        background=backgroundColor,
        foreground=foregroundColor,
        # format=' %Y-%m-%d %a %I:%M %p'
        format=' %a %d %m %Y |  %I:%M %p',
    ),

    left_arrow(foregroundColor, backgroundColor),
    Systray(
        background=backgroundColor,
        foreground=foregroundColor
    ),

    Spacer(length=20, background=backgroundColor)
], background=backgroundColor, size=26, margin=9)
