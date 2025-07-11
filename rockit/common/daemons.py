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
Directory of Pyro daemons
"""

import datetime
import Pyro4

from .ip import IP

class PyroDaemon:
    """Encodes a reference to a remote Pyro4 daemon"""
    def __init__(self, name, host, port, default_timeout=5, default_retries=0):
        self.name = name
        self.host = host
        self.port = port
        self.default_timeout = default_timeout
        self.default_retries = default_retries
        self.uri = 'PYRO:' + name + '@' + host + ':' + str(port)

    def connect(self, timeout=None, retries=None):
        """Returns a Pyro4 proxy to the remote daemon"""
        proxy = Pyro4.Proxy('PYRO:' + self.name + '@' + self.host + ':' + str(self.port))

        # pylint: disable=protected-access
        if timeout is None:
            proxy._pyroTimeout = self.default_timeout
        elif timeout > 0:
            proxy._pyroTimeout = timeout

        if retries is None:
            proxy._pyroMaxRetries = self.default_retries
        elif retries > 0:
            proxy._pyroMaxRetries = retries
        # pylint: enable=protected-access

        return proxy

    def launch(self, daemon):
        """Launches a daemon with the given server object"""
        Pyro4.config.DETAILED_TRACEBACK = True
        Pyro4.config.REQUIRE_EXPOSE = True

        pyro = Pyro4.Daemon(host=self.host, port=self.port)
        uri = pyro.register(daemon, objectId=self.name)

        print(f'{datetime.datetime.utcnow()} MESSAGE: Starting daemon {uri}')
        pyro.requestLoop()
        print(f'{datetime.datetime.utcnow()} MESSAGE: Exiting daemon {uri}')


# pylint: disable=invalid-name
observatory_log = PyroDaemon('observatory_log_daemon', IP.GOTOServer, 9016)
observatory_network_ping = PyroDaemon('observatory_netping_daemon', IP.GOTOServer, 9012)
observatory_environment = PyroDaemon('observatory_environment_daemon', IP.GOTOServer, 9028)
observatory_ephemeris = PyroDaemon('observatory_ephemeris_daemon', IP.GOTOServer, 9029)

tng_log = PyroDaemon('tng_daemon', IP.GOTOServer, 9011)
eumetsat_opacity = PyroDaemon('eumetsat_daemon', IP.GOTOServer, 9013)
goto_dome1_domealert = PyroDaemon('goto1_domealert_daemon', IP.GOTODomeAlert1, 9008)
goto_dome2_domealert = PyroDaemon('goto2_domealert_daemon', IP.GOTODomeAlert2, 9008)
goto_ups = PyroDaemon('goto_ups_daemon', IP.GOTOServer, 9021)
goto_vaisala = PyroDaemon('goto_vaisala_daemon', IP.GOTOServer, 9022)
ing_robodimm = PyroDaemon('ing_robodimm_daemon', IP.GOTOServer, 9026)

sting_power = PyroDaemon('sting_power_daemon', IP.STINGTCS, 9027)
sting_telescope = PyroDaemon('sting_telescope_daemon', IP.STINGTCS, 9003)
sting_dome = PyroDaemon('sting_dome_daemon', IP.STINGTCS, 9004)
sting_dehumidifier = PyroDaemon('sting_dehumidifier_daemon', IP.STINGTCS, 9041)
sting_operations = PyroDaemon('sting_operations_daemon', IP.STINGTCS, 9015)
sting_lensheater = PyroDaemon('sting_lensheater_daemon', IP.STINGTCS, 9050)
sting_pipeline = PyroDaemon('sting_pipeline', IP.STINGTCS, 9032)
sting_power_relay = PyroDaemon('sting_powerrelay_daemon', IP.STINGTCS, 9033)

sting_cam1 = PyroDaemon('sting_camera_daemon_1', IP.STINGCameraVM1, 9040)
sting_pipeline_cam1 = PyroDaemon('sting_pipeline_cam1', IP.STINGCameraVM1, 9033)
sting_cam2 = PyroDaemon('sting_camera_daemon_2', IP.STINGCameraVM2, 9041)
sting_pipeline_cam2 = PyroDaemon('sting_pipeline_cam2', IP.STINGCameraVM2, 9034)
sting_cam3 = PyroDaemon('sting_camera_daemon_3', IP.STINGCameraVM3, 9042)
sting_pipeline_cam3 = PyroDaemon('sting_pipeline_cam3', IP.STINGCameraVM3, 9035)
sting_cam4 = PyroDaemon('sting_camera_daemon_4', IP.STINGCameraVM4, 9043)
sting_pipeline_cam4 = PyroDaemon('sting_pipeline_cam4', IP.STINGCameraVM4, 9036)
sting_diskspace_das1 = PyroDaemon('sting_diskspace_das1', IP.STINGDAS1, 9008)
sting_diskspace_das2 = PyroDaemon('sting_diskspace_das2', IP.STINGDAS2, 9009)
sting_pipeline_astrometry_das1 = PyroDaemon('sting_pipeline_astrometry_das1', IP.STINGDAS1, 9010)
sting_pipeline_astrometry_das2 = PyroDaemon('sting_pipeline_astrometry_das2', IP.STINGDAS2, 9011)
sting_camvirt_das1 = PyroDaemon('sting_camvirt_daemon_das1', IP.STINGDAS1, 9012)
sting_camvirt_das2 = PyroDaemon('sting_camvirt_daemon_das2', IP.STINGDAS2, 9013)

sting_swreduce_1 = PyroDaemon('sting_swreduce_1', IP.STINGDAS1, 9050)
sting_swreduce_2 = PyroDaemon('sting_swreduce_2', IP.STINGDAS2, 9050)

onemetre_operations = PyroDaemon('operations_daemon', IP.OneMetreDome, 9015)
onemetre_vaisala = PyroDaemon('onemetre_vaisala_daemon', IP.OneMetreDome, 9001)
onemetre_domealert = PyroDaemon('onemetre_domealert_daemon', IP.OneMetreDomeAlert, 9008)
onemetre_power = PyroDaemon('onemetre_power_daemon', IP.OneMetreDome, 9009)
onemetre_dome = PyroDaemon('dome_daemon', IP.OneMetreDome, 9004)
onemetre_dehumidifier = PyroDaemon('onemetre_dehumidifier_daemon', IP.OneMetreDome, 9041)

onemetre_telescope = PyroDaemon('telescope_daemon', IP.OneMetreTCS, 9003)
onemetre_covers = PyroDaemon('onemetre_covers_daemon', IP.OneMetreTCS, 9005)

onemetre_red_focuser = PyroDaemon('onemetre_red_focuser_daemon', IP.OneMetreDAS, 9004)
onemetre_diskspace = PyroDaemon('onemetre_diskspace_daemon', IP.OneMetreDAS, 9008)
onemetre_blue_camera = PyroDaemon('onemetre_camera_blue', IP.OneMetreDAS, 9011)
onemetre_red_camera = PyroDaemon('onemetre_camera_red', IP.OneMetreDAS, 9010)
onemetre_pipeline = PyroDaemon('onemetre_pipeline', IP.OneMetreDAS, 9012)
onemetre_pipeline_blue = PyroDaemon('onemetre_pipeline_blue', IP.OneMetreDAS, 9013)
onemetre_pipeline_red = PyroDaemon('onemetre_pipeline_red', IP.OneMetreDAS, 9014)

goto_dome1_gtecs_mnt = PyroDaemon('mnt', IP.GOTOControl1, 9001)
goto_dome1_gtecs_filt = PyroDaemon('filt', IP.GOTOControl1, 9002)
goto_dome1_gtecs_foc = PyroDaemon('foc', IP.GOTOControl1, 9003)
goto_dome1_gtecs_cam = PyroDaemon('cam', IP.GOTOControl1, 9004)
goto_dome1_gtecs_exq = PyroDaemon('exq', IP.GOTOControl1, 9005)
goto_dome1_gtecs_power = PyroDaemon('power', IP.GOTOControl1, 9006)
goto_dome1_gtecs_dome = PyroDaemon('dome', IP.GOTOControl1, 9007)
goto_dome1_gtecs_ota = PyroDaemon('ota', IP.GOTOControl1, 9008)
goto_dome1_gtecs_conditions = PyroDaemon('conditions', IP.GOTOControl1, 9030)

goto_dome2_gtecs_mnt = PyroDaemon('mnt', IP.GOTOControl2, 9001)
goto_dome2_gtecs_filt = PyroDaemon('filt', IP.GOTOControl2, 9002)
goto_dome2_gtecs_foc = PyroDaemon('foc', IP.GOTOControl2, 9003)
goto_dome2_gtecs_cam = PyroDaemon('cam', IP.GOTOControl2, 9004)
goto_dome2_gtecs_exq = PyroDaemon('exq', IP.GOTOControl2, 9005)
goto_dome2_gtecs_power = PyroDaemon('power', IP.GOTOControl2, 9006)
goto_dome2_gtecs_dome = PyroDaemon('dome', IP.GOTOControl2, 9007)
goto_dome2_gtecs_ota = PyroDaemon('ota', IP.GOTOControl2, 9008)
goto_dome2_gtecs_conditions = PyroDaemon('conditions', IP.GOTOControl2, 9030)

halfmetre_domealert = PyroDaemon('halfmetre_domealert_daemon', IP.HalfMetreDomeAlert, 9008)
halfmetre_aircon = PyroDaemon('halfmetre_aircon_daemon', IP.HalfMetreTCS, 9030)
halfmetre_roof = PyroDaemon('halfmetre_roof_daemon', IP.HalfMetreTCS, 9004)
halfmetre_power = PyroDaemon('halfmetre_power_daemon', IP.HalfMetreTCS, 9027)
halfmetre_telescope = PyroDaemon('halfmetre_telescope_daemon', IP.HalfMetreTCS, 9003)
halfmetre_operations = PyroDaemon('halfmetre_operations_daemon', IP.HalfMetreTCS, 9015)
halfmetre_cam = PyroDaemon('halfmetre_camera_daemon', IP.HalfMetreTCS, 9040)
halfmetre_focuser = PyroDaemon('halfmetre_focuser_daemon', IP.HalfMetreTCS, 9041)
halfmetre_pipeline = PyroDaemon('halfmetre_pipeline_daemon', IP.HalfMetreTCS, 9032)
halfmetre_pipeline_cam = PyroDaemon('halfmetre_pipeline_daemon_cam', IP.HalfMetreTCS, 9033)
halfmetre_diskspace = PyroDaemon('halfmetre_diskspace_daemon', IP.HalfMetreTCS, 9008)
halfmetre_vaisala = PyroDaemon('halfmetre_vaisala_daemon', IP.CLASPCMOS, 9020)
halfmetre_cloudwatcher = PyroDaemon('halfmetre_cloudwatcher_daemon', IP.CLASPCMOS, 9021)

clasp_operations = PyroDaemon('clasp_operations_daemon', IP.CLASPTCS, 9030)
clasp_power = PyroDaemon('clasp_power_daemon', IP.CLASPTCS, 9033)
clasp_dome = PyroDaemon('clasp_dome_daemon', IP.CLASPTCS, 9034)
clasp_telescope = PyroDaemon('clasp_telescope_daemon', IP.CLASPTCS, 9035)
clasp_focus = PyroDaemon('clasp_focus_daemon', IP.CLASPTCS, 9036)
clasp_pipeline = PyroDaemon('clasp_pipeline_daemon', IP.CLASPTCS, 9032)
clasp_camera_cmos = PyroDaemon('clasp_camera_cmos_daemon', IP.CLASPCMOSVM, 9037)
clasp_camera_swir = PyroDaemon('clasp_camera_swir_daemon', IP.CLASPSWIRVM, 9038)
clasp_pipeline_cmos = PyroDaemon('clasp_pipeline_cmos_daemon', IP.CLASPCMOSVM, 9031)
clasp_pipeline_swir = PyroDaemon('clasp_pipeline_swir_daemon', IP.CLASPSWIR, 9031)
clasp_pipeline_astrometry = PyroDaemon('clasp_pipeline_astrometry_daemon', IP.CLASPCMOS, 9032)
clasp_diskspace_cmos = PyroDaemon('clasp_diskspace_cmos_daemon', IP.CLASPCMOS, 9039)
clasp_diskspace_swir = PyroDaemon('clasp_diskspace_swir_daemon', IP.CLASPSWIR, 9039)
clasp_domealert = PyroDaemon('clasp_domealert_daemon', IP.CLASPDomeAlert, 9008)
clasp_dehumidifier = PyroDaemon('clasp_dehumidifier_daemon', IP.CLASPTCS, 9041)
clasp_chiller = PyroDaemon('clasp_chiller_daemon', IP.CLASPTCS, 9042)

clasp_swreduce = PyroDaemon('clasp_swreduce', IP.CLASPCMOS, 9050)
clasp_camvirt_cmos = PyroDaemon('clasp_camvirt_cmos_daemon', IP.CLASPCMOS, 9040)
clasp_camvirt_swir = PyroDaemon('clasp_camvirt_swir_daemon', IP.CLASPSWIR, 9040)

portable_operations = PyroDaemon('portable_operations_daemon', IP.PortableTCS, 9030)
portable_telescope = PyroDaemon('portable_telescope_daemon', IP.PortableTCS, 9035)
portable_focus = PyroDaemon('portable_focus_daemon', IP.PortableTCS, 9036)
portable_pipeline = PyroDaemon('portable_pipeline_daemon', IP.PortableTCS, 9032)
portable_camera = PyroDaemon('portable_camera_daemon', IP.PortableTCS, 9037)
portable_pipeline_cam = PyroDaemon('portable_pipeline_daemon_cam', IP.PortableTCS, 9031)
portable_pipeline_astrometry = PyroDaemon('portable_pipeline_astrometry', IP.PortableTCS, 9032)
portable_diskspace = PyroDaemon('portable_diskspace_daemon', IP.PortableTCS, 9039)
portable_environment = PyroDaemon('portable_environment_daemon', IP.PortableTCS, 9010)

warwick_dome = PyroDaemon('warwick_dome_daemon', IP.WarwickTCS, 9000)
warwick_power = PyroDaemon('warwick_power_daemon', IP.WarwickTCS, 9001)
warwick_telescope = PyroDaemon('warwick_telescope_daemon', IP.WarwickTCS, 9002)
warwick_camera = PyroDaemon('warwick_camera_daemon', IP.WarwickTCS, 9003)
warwick_focuser = PyroDaemon('warwick_focuser_daemon', IP.WarwickTCS, 9004)
warwick_filterwheel = PyroDaemon('warwick_filterwheel_daemon', IP.WarwickTCS, 9005)
warwick_pipeline = PyroDaemon('warwick_pipeline_daemon', IP.WarwickTCS, 9006)
warwick_pipeline_cam = PyroDaemon('warwick_pipeline_daemon_cam', IP.WarwickTCS, 9007)
warwick_diskspace = PyroDaemon('warwick_diskspace_daemon', IP.WarwickTCS, 9008)
warwick_vaisala = PyroDaemon('warwick_vaisala_daemon', IP.WarwickTCS, 9009)
warwick_cloudwatcher = PyroDaemon('warwick_cloudwatcher_daemon', IP.WarwickTCS, 9010)
warwick_rain = PyroDaemon('warwick_rain_daemon', IP.WarwickTCS, 9011)
warwick_ephemeris = PyroDaemon('warwick_ephemeris_daemon', IP.WarwickTCS, 9012)
warwick_environment = PyroDaemon('warwick_environment_daemon', IP.WarwickTCS, 9013)
warwick_operations = PyroDaemon('warwick_operations_daemon', IP.WarwickTCS, 9014)
warwick_log = PyroDaemon('warwick_operations_daemon', IP.WarwickTCS, 9015)
warwick_dome_shtstick = PyroDaemon('warwick_dome_shtstick_daemon', IP.WarwickTCS, 9016)

warwick_heliostat_dome = PyroDaemon('warwick_heliostat_dome_daemon', IP.WarwickHeliostatDome, 9000)
warwick_heliostat_shtstick = PyroDaemon('warwick_heliostat_shtstick_daemon', IP.WarwickHeliostatDome, 9001)

goto_south_vaisala = PyroDaemon('goto_south_vaisala_daemon', IP.GOTOSSO, 9022)
goto_south_cloudwatcher = PyroDaemon('goto_south_cloudwatcher_daemon', IP.GOTOSSO, 9021)

ngts_m06_power = PyroDaemon('ngts_m06_power_daemon', IP.NGTSDASNUC, 9000)
ngts_m06_telescope = PyroDaemon('ngts_m06_telescope_daemon', IP.NGTSDASNUC, 9001)
ngts_m06_focuser = PyroDaemon('ngts_m06_focuser_daemon', IP.NGTSDASNUC, 9002)
ngts_m06_camera = PyroDaemon('ngts_m06_camera_daemon', IP.NGTSDASNUC, 9003)
ngts_m06_pipeline = PyroDaemon('ngts_m06_pipeline_daemon', IP.NGTSDASNUC, 9004)
ngts_m06_pipeline_cam = PyroDaemon('ngts_m06_pipeline_daemon_cam', IP.NGTSDASNUC, 9005)
ngts_m06_diskspace = PyroDaemon('ngts_m06_diskspace_daemon', IP.NGTSDASNUC, 9006)
ngts_m06_operations = PyroDaemon('ngts_m06_operations_daemon', IP.NGTSDASNUC, 9007)
ngts_sentinel = PyroDaemon('ngts_sentinel_daemon', IP.NGTSDASNUC, 9008)
ngts_ephemeris = PyroDaemon('ngts_ephemeris_daemon', IP.NGTSDASNUC, 9009)
ngts_environment = PyroDaemon('ngts_environment_daemon', IP.NGTSDASNUC, 9010)

pdt_pipeline = PyroDaemon('pdt_pipeline', IP.LocalHost, 9000)
pdt_cam1 = PyroDaemon('pdt_camera_daemon_cam1', IP.LocalHost, 9001)
pdt_pipeline_cam1 = PyroDaemon('pdt_pipeline_cam1', IP.LocalHost, 9002)
pdt_cam2 = PyroDaemon('pdt_camera_daemon_cam2', IP.LocalHost, 9003)
pdt_pipeline_cam2 = PyroDaemon('pdt_pipeline_cam2', IP.LocalHost, 9004)
pdt_focuser = PyroDaemon('pdt_focuser_daemon', IP.LocalHost, 9005)
pdt_operations = PyroDaemon('pdt_operations_daemon', IP.LocalHost, 9006)
pdt_environment = PyroDaemon('pdt_environment_daemon', IP.LocalHost, 9007)
pdt_diskspace = PyroDaemon('pdt_diskspace_daemon', IP.LocalHost, 9008)

localhost_test = PyroDaemon('localhost_test_daemon', IP.LocalHost, 9000)
localhost_test2 = PyroDaemon('localhost_test_daemon2', IP.LocalHost, 9001)
localhost_test3 = PyroDaemon('localhost_test_daemon3', IP.LocalHost, 9002)
localhost_test4 = PyroDaemon('localhost_test_daemon4', IP.LocalHost, 9003)
localhost_test5 = PyroDaemon('localhost_test_daemon5', IP.LocalHost, 9004)

# pylint: enable=invalid-name
