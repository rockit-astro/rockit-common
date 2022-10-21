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
    OneMetreBlueCamera = '10.2.6.216'
    OneMetreRedCamera = '10.2.6.217'

    CLASPTCS = '10.2.6.181'
    CLASPDAS1 = '10.2.6.182'
    CLASPDAS2 = '10.2.6.181'
    CLASPDomeAlert = '10.2.6.188'

    GOTOServer = '10.2.6.100'
    GOTOControl1 = '10.2.6.20'
    GOTOControl2 = '10.2.6.50'
    GOTODomeAlert1 = '10.2.6.18'
    GOTODomeAlert2 = '10.2.6.49'

    SWASPTCS = '10.2.6.124'
    SWASPCameraPi1 = '10.2.6.120'
    SWASPCameraPi2 = '10.2.6.121'
    SWASPCameraPi3 = '10.2.6.122'
    SWASPCameraPi4 = '10.2.6.123'

    # Windmill Hill Observatory at Warwick University
    # TODO: Assign final IPs from ITS
    WarwickDome = '10.2.7.1'
    WarwickTCS = '10.2.7.2'
