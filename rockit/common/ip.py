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
Directory of IP addresses
"""

# pylint: disable=too-few-public-methods


class IP:
    """List of computer / device IPs"""
    LocalHost = '127.0.0.1'

    # Warwick La Palma telescopes
    OneMetreDome = '10.2.6.202'
    OneMetreTCS = '10.2.6.203'
    OneMetreDomeAlert = '10.2.6.204'
    OneMetreRainSensors = '10.2.6.205'

    CLASPTCS = '10.2.6.181'
    CLASPDAS = '10.2.6.182'
    CLASPCMOSVM = '10.2.6.185'
    CLASPSWIRVM = '10.2.6.186'
    CLASPDomeAlert = '10.2.6.188'

    GOTOServer = '10.2.6.100'
    GOTOControl1 = '10.2.6.20'
    GOTOControl2 = '10.2.6.50'
    GOTODomeAlert1 = '10.2.6.18'
    GOTODomeAlert2 = '10.2.6.49'

    SWASPTCS = '10.2.6.160'
    SWASPCameraPi1 = '10.2.6.161'
    SWASPCameraPi2 = '10.2.6.162'
    SWASPCameraPi3 = '10.2.6.163'
    SWASPCameraPi4 = '10.2.6.164'
    SWASPCameraVM1 = '10.2.6.165'
    SWASPCameraVM2 = '10.2.6.166'
    SWASPCameraVM3 = '10.2.6.167'
    SWASPCameraVM4 = '10.2.6.168'
    SWASPDAS1 = '10.2.6.173'
    SWASPDAS2 = '10.2.6.175'

    HalfMetreTCS = '10.2.6.120'
    HalfMetreDomeAlert = '10.2.6.116'

    # Windmill Hill Observatory at Warwick University
    WarwickTCS = '172.19.0.160'
    WarwickDome = '172.19.0.161'

    # GOTO South (Siding Spring Observatory)
    GOTOSSO = '192.55.98.154'

    # NGTS CMOS test machine (Paranal Observatory)
    NGTSDASNUC = '10.2.5.115'
