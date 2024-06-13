#
# This file is part of the Robotic Observatory Control Kit (rockit)
#
# rockit is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# rockit is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with rockit.  If not, see <http://www.gnu.org/licenses/>.

"""
Terminal formatting helpers
"""

_console = None


class TFmt:
    Green = u'\033[92m'
    Red = u'\033[91m'
    Cyan = u'\033[96m'
    Yellow = u'\033[93m'
    Bold = u'\033[1m'
    Clear = u'\033[0m'


def print(*objects, sep=" ", end="\n", file=None, flush=False):
    """
    Replacement for the builtin print function using the rich module
    with a custom theme
    """
    from rich.console import Console
    global _console
    if _console is None:
        from rich.console import Theme
        _console = Console(theme=Theme(inherit=False, styles={
            'green': 'bright_green',
            'red': 'bright_red',
            'cyan': 'bright_cyan',
            'yellow': 'bright_yellow'
        }))

    console = _console if file is None else Console(file=file)
    return console.print(*objects, sep=sep, end=end)

