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
observatory_environment = PyroDaemon('observatory_environment_daemon', IP.GOTOServer, 9028, 5)
observatory_ephemeris = PyroDaemon('observatory_environment_daemon', IP.GOTOServer, 9029, 5)

superwasp_log = PyroDaemon('superwasp_daemon', IP.GOTOServer, 9007, 5)
tng_log = PyroDaemon('tng_daemon', IP.GOTOServer, 9011, 5)
eumetsat_opacity = PyroDaemon('eumetsat_daemon', IP.GOTOServer, 9013, 5)
goto_roomalert = PyroDaemon('goto_roomalert_daemon', IP.GOTOServer, 9020, 5)
goto_ups = PyroDaemon('goto_ups_daemon', IP.GOTOServer, 9021, 5)
goto_vaisala = PyroDaemon('goto_vaisala_daemon', IP.GOTOServer, 9022, 5)
ing_robodimm = PyroDaemon('ing_robodimm_daemon', IP.GOTOServer, 9026, 5)

superwasp_roomalert = PyroDaemon('superwasp_roomalert_daemon', IP.GOTOServer, 9023, 5)
superwasp_roofbattery = PyroDaemon('superwasp_roofbattery_daemon', IP.GOTOServer, 9024, 5)
superwasp_preview = PyroDaemon('superwasp_preview', IP.GOTOServer, 9025, 5)
superwasp_power = PyroDaemon('superwasp_power_daemon', IP.GOTOServer, 9027, 5)
superwasp_aircon = PyroDaemon('superwasp_aircon_daemon', IP.GOTOServer, 9030, 5)
superwasp_aurora = PyroDaemon('superwasp_aurora_daemon', IP.GOTOServer, 9031, 5)
superwasp_leo_observer = PyroDaemon('superwasp_leo_observer', IP.SWASPGPSPi, 9001, 5)

onemetre_operations = PyroDaemon('operations_daemon', IP.OneMetreDome, 9015, 5)
onemetre_environment = PyroDaemon('environment_daemon', IP.OneMetreDome, 9002, 5)
onemetre_vaisala = PyroDaemon('onemetre_vaisala_daemon', IP.OneMetreDome, 9001, 5)
onemetre_roomalert = PyroDaemon('onemetre_roomalert_daemon', IP.OneMetreDomeAlert, 9008, 5)
onemetre_power = PyroDaemon('onemetre_power_daemon', IP.OneMetreDome, 9009, 5)
onemetre_rain = PyroDaemon('onemetre_rain_daemon', IP.OneMetreRainSensors, 9017, 5)
onemetre_dome = PyroDaemon('dome_daemon', IP.OneMetreDome, 9004, 5)

onemetre_telescope = PyroDaemon('telescope_daemon', IP.OneMetreTCS, 9003, 5)
onemetre_tcs_diskspace = PyroDaemon('onemetre_diskspace_daemon', IP.OneMetreTCS, 9008, 5)
onemetre_blue_camera = PyroDaemon('blue_camera_daemon', IP.OneMetreTCS, 9011, 5)
onemetre_red_camera = PyroDaemon('red_camera_daemon', IP.OneMetreTCS, 9010, 5)
onemetre_pipeline = PyroDaemon('pipeline_daemon', IP.OneMetreTCS, 9012, 5)

nites_roomalert = PyroDaemon('nites_roomalert_daemon', IP.NitesMain, 9008, 5)
nites_dome = PyroDaemon('nites_dome_daemon', IP.NitesMain, 9009, 5)
nites_environment = PyroDaemon('nites_environment', IP.NitesMain, 9010, 5)

goto_gtecs_mnt = PyroDaemon('mnt', IP.GOTOControl, 9001, 5)
goto_gtecs_filt = PyroDaemon('filt', IP.GOTOControl, 9002, 5)
goto_gtecs_foc = PyroDaemon('foc', IP.GOTOControl, 9003, 5)
goto_gtecs_cam = PyroDaemon('cam', IP.GOTOControl, 9004, 5)
goto_gtecs_exq = PyroDaemon('exq', IP.GOTOControl, 9005, 5)
goto_gtecs_power = PyroDaemon('power', IP.GOTOControl, 9006, 5)
goto_gtecs_dome = PyroDaemon('dome', IP.GOTOControl, 9007, 5)
goto_gtecs_ota = PyroDaemon('ota', IP.GOTOControl, 9008, 5)
goto_gtecs_conditions = PyroDaemon('conditions', IP.GOTOControl, 9030, 5)

rasa_operations = PyroDaemon('rasa_operations_daemon', IP.RASAMain, 9030, 5)
rasa_environment = PyroDaemon('rasa_environment_daemon', IP.RASAMain, 9031, 5)
rasa_pipeline = PyroDaemon('rasa_pipeline_daemon', IP.RASAMain, 9032, 5)
rasa_power = PyroDaemon('rasa_power_daemon', IP.RASAMain, 9033, 5)
rasa_dome = PyroDaemon('rasa_dome_daemon', IP.RASAMain, 9034, 5)
rasa_telescope = PyroDaemon('rasa_telescope_daemon', IP.RASAWindowsVM, 9035, 5)
rasa_focus = PyroDaemon('rasa_focus_daemon', IP.RASAMain, 9036, 5)
rasa_camera = PyroDaemon('rasa_camera_daemon', IP.RASAMain, 9037, 5)
rasa_diskspace = PyroDaemon('rasa_diskspace_daemon', IP.RASAMain, 9039, 5)
rasa_internal_environment = PyroDaemon('rasa_internal_environment', IP.RASAPi, 9040, 5)

localhost_test = PyroDaemon('localhost_test_daemon', IP.LocalHost, 9000, 5)

# pylint: enable=invalid-name
