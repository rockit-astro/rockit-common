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
Interface with the central log database
"""

import socket
import sys
import Pyro4
from . import daemons

sys.excepthook = Pyro4.util.excepthook

# pylint: disable=broad-except
# pylint: disable=invalid-name


def info(table, message):
    """Write an info message to the given table"""
    print('INFO {}: {}'.format(table, message))
    try:
        if socket.gethostbyname(socket.gethostname()).startswith('10.2.6.'):
            with daemons.observatory_log.connect() as log:
                log.log_info(table, message)
    except Exception as e:
        print('Failed to log info message with exception: ' + str(e))
        print('Original message was: (' + table + ') ' + message)


def warning(table, message):
    """Write a warning message to the given table"""
    print('WARN {}: {}'.format(table, message))
    try:
        if socket.gethostbyname(socket.gethostname()).startswith('10.2.6.'):
            with daemons.observatory_log.connect() as log:
                log.log_warning(table, message)
    except Exception as e:
        print('Failed to log warning message with exception: ' + str(e))
        print('Original message was: (' + table + ') ' + message)


def error(table, message):
    """Write an error message to the given table"""
    print('ERROR {}: {}'.format(table, message))
    try:
        if socket.gethostbyname(socket.gethostname()).startswith('10.2.6.'):
            with daemons.observatory_log.connect() as log:
                log.log_error(table, message)
    except Exception as e:
        print('Failed to log error message with exception: ' + str(e))
        print('Original message was: (' + table + ') ' + message)