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
Helper object for use with `with` statements
"""

class TryLock:
    """Helper object for use with `with` statements"""
    def __init__(self, lock):
        self._lock = lock
        self._locked = False

    def __enter__(self):
        self._locked = self._lock.acquire(False)
        return self._locked

    def __exit__(self, *args):
        if self._locked:
            self._lock.release()
            self._locked = False
