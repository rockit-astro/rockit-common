#!/usr/bin/env python3
#
# This file is part of warwick.observatory.
#
# warwick.observatory is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# warwick.observatory is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with warwick.observatory.  If not, see <http://www.gnu.org/licenses/>.

"""
Directory of Pyro daemons
"""

# pylint: disable=too-few-public-methods

import datetime
import Pyro4

from .ip import IP

class PyroDaemon(object):
    """Encodes a reference to a remote Pyro4 daemon"""
    def __init__(self, name, host, port, default_timeout):
        self.name = name
        self.host = host
        self.port = port
        self.default_timeout = default_timeout
        self.uri = 'PYRO:' + name + '@' + host + ':' + str(port)

    def connect(self, timeout=None):
        """Returns a Pyro4 proxy to the remote daemon"""
        proxy = Pyro4.Proxy('PYRO:' + self.name + '@' + self.host + ':' + str(self.port))

        # pylint: disable=protected-access
        if timeout is None:
            proxy._pyroTimeout = self.default_timeout
        elif timeout > 0:
            proxy._pyroTimeout = timeout
        # pylint: enable=protected-access

        return proxy

    def launch(self, daemon):
        """Launches a daemon with the given server object"""
        Pyro4.config.DETAILED_TRACEBACK = True
        Pyro4.config.REQUIRE_EXPOSE = True

        pyro = Pyro4.Daemon(host=self.host, port=self.port)
        uri = pyro.register(daemon, objectId=self.name)

        print('{} MESSAGE: Starting daemon {}'.format(datetime.datetime.utcnow(), uri))
        pyro.requestLoop()
        print('{} MESSAGE: Exiting daemon {}'.format(datetime.datetime.utcnow(), uri))

# pylint: disable=invalid-name
observatory_log = PyroDaemon('observatory_log_daemon', IP.GOTOServer, 9016, 5)
observatory_network_ping = PyroDaemon('observatory_netping_daemon', IP.GOTOServer, 9012, 5)
superwasp_log = PyroDaemon('superwasp_daemon', IP.GOTOServer, 9007, 5)
tng_log = PyroDaemon('tng_daemon', IP.GOTOServer, 9011, 5)
goto_roomalert = PyroDaemon('goto_roomalert_daemon', IP.GOTOServer, 9020, 5)
goto_ups = PyroDaemon('goto_ups_daemon', IP.GOTOServer, 9021, 5)
goto_vaisala = PyroDaemon('goto_vaisala_daemon', IP.GOTOServer, 9022, 5)
superwasp_roomalert = PyroDaemon('superwasp_roomalert_daemon', IP.GOTOServer, 9023, 5)

onemetre_operations = PyroDaemon('operations_daemon', IP.OneMetreDome, 9015, 5)
onemetre_environment = PyroDaemon('environment_daemon', IP.OneMetreDome, 9002, 5)
onemetre_vaisala = PyroDaemon('onemetre_vaisala_daemon', IP.OneMetreDome, 9001, 5)
onemetre_roomalert = PyroDaemon('onemetre_roomalert_daemon', IP.OneMetreDome, 9008, 5)
onemetre_power = PyroDaemon('onemetre_power_daemon', IP.OneMetreDome, 9009, 5)
onemetre_rain = PyroDaemon('onemetre_rain_daemon', IP.OneMetreDome, 9017, 5)
onemetre_dome = PyroDaemon('dome_daemon', IP.OneMetreDome, 9004, 5)

onemetre_telescope = PyroDaemon('telescope_daemon', IP.OneMetreTCS, 9003, 5)
onemetre_tcs_diskspace = PyroDaemon('onemetre_diskspace_daemon', IP.OneMetreTCS, 9008, 5)
onemetre_blue_camera = PyroDaemon('blue_camera_daemon', IP.OneMetreTCS, 9011, 5)
onemetre_red_camera = PyroDaemon('red_camera_daemon', IP.OneMetreTCS, 9010, 5)
onemetre_pipeline = PyroDaemon('pipeline_daemon', IP.OneMetreTCS, 9012, 5)

nites_roomalert = PyroDaemon('nites_roomalert_daemon', IP.NitesMain, 9008, 5)
nites_dome = PyroDaemon('nites_dome_daemon', IP.NitesMain, 9009, 5)
nites_environment = PyroDaemon('nites_environment', IP.NitesMain, 9010, 5)

goto_gtecs_mnt = PyroDaemon('mnt', IP.GOTORackLeft, 9001, 5)
goto_gtecs_filt = PyroDaemon('filt', IP.GOTORackLeft, 9002, 5)
goto_gtecs_foc = PyroDaemon('foc', IP.GOTORackLeft, 9003, 5)
goto_gtecs_cam = PyroDaemon('cam', IP.GOTORackLeft, 9004, 5)
goto_gtecs_exq = PyroDaemon('exq', IP.GOTORackLeft, 9005, 5)
goto_gtecs_power = PyroDaemon('power', IP.GOTORackLeft, 9006, 5)
goto_gtecs_conditions = PyroDaemon('conditions', IP.GOTORackLeft, 9031, 5)

rasa_operations = PyroDaemon('rasa_operations_daemon', IP.RASAMain, 9030, 5)
rasa_environment = PyroDaemon('rasa_environment_daemon', IP.RASAMain, 9031, 5)
rasa_pipeline = PyroDaemon('rasa_pipeline_daemon', IP.RASAMain, 9032, 5)
rasa_power = PyroDaemon('rasa_power_daemon', IP.RASAMain, 9033, 5)
rasa_dome = PyroDaemon('rasa_dome_daemon', IP.RASAMain, 9034, 5)
rasa_telescope = PyroDaemon('rasa_telescope_daemon', IP.RASAMain, 9035, 5)
rasa_focus = PyroDaemon('rasa_focus_daemon', IP.RASAMain, 9036, 5)
rasa_camera = PyroDaemon('rasa_camera_daemon', IP.RASAMain, 9037, 5)
rasa_diskspace = PyroDaemon('rasa_diskspace_daemon', IP.RASAMain, 9039, 5)

# pylint: enable=invalid-name
