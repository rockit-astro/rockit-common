Python module that contains common backend code that is shared by the other python utilities.
The main components are:
* `rockit.common.IP`: List of IP addresses used by daemons
* `rockit.common.daemons`: Pyro "phone book" specifying the IP and port for each daemon.
* `rockit.common.helpers.pyro_client_matches`: Pyro helper for white listing privileged commands.
* `rockit.common.helpers.key_for_current_ip`: Helper to return the dictionary key that has a value matching the host IP.
* `rockit.common.TryLock`: A helper class for taking locks that should fail instead of blocking.
* `rockit.common.log`: A helper class for writing to the dashboard log database.
