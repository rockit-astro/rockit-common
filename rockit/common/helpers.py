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
Common helper functions
"""

import socket
import Pyro4


def pyro_client_matches(ip_whitelist):
    """Returns true if the current pyro client IP is included in the given white list"""
    client_ip = Pyro4.current_context.client.sock.getpeername()[0]
    return client_ip in ip_whitelist


def key_for_current_ip(object_ips):
    """
    Returns the dictionary key that has a value array containing the current host IP
    object_ips should be a dictionary of key: [ips]
    returns None if the current IP is not in the dictionary
    """
    client_ip = socket.gethostbyname(socket.gethostname())
    for key, ip_list in object_ips.items():
        if client_ip in ip_list:
            return key
    return None
