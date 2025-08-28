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
    OneMetreTCS = '10.2.6.201'
    OneMetreDome = '10.2.6.202'
    OneMetreDAS = '10.2.6.203'
    OneMetreDomeAlert = '10.2.6.204'

    CLASPTCS = '10.2.6.181'
    CLASPCMOS = '10.2.6.182'
    CLASPSWIR = '10.2.6.187'
    CLASPCMOSVM = '10.2.6.185'
    CLASPSWIRVM = '10.2.6.186'
    CLASPDomeAlert = '10.2.6.188'
    CLASPCompute = '10.2.6.194'

    GOTOServer = '10.2.6.100'
    GOTOControl1 = '10.2.6.20'
    GOTOControl2 = '10.2.6.50'
    GOTODomeAlert1 = '10.2.6.18'
    GOTODomeAlert2 = '10.2.6.49'

    STINGTCS = '10.2.6.160'
    STINGDAS1 = '10.2.6.173'
    STINGDAS2 = '10.2.6.175'
    STINGCameraVM1 = '10.2.6.165'
    STINGCameraVM2 = '10.2.6.166'
    STINGCameraVM3 = '10.2.6.167'
    STINGCameraVM4 = '10.2.6.168'

    HalfMetreTCS = '10.2.6.120'
    HalfMetreDomeAlert = '10.2.6.116'

    PortableTCS = '127.0.0.1'

    # Windmill Hill Observatory at Warwick University
    WarwickTCS = '172.19.0.160'
    WarwickHeliostatDome = '172.19.0.166'

    # GOTO South (Siding Spring Observatory)
    GOTOSSO = '192.55.98.154'

    # NGTS CMOS test machine (Paranal Observatory)
    NGTSDASNUC = '10.2.5.115'
