## Warwick common observatory code

Python module that contains common backend code that is shared by the other python utilities.
The main components are:
* `warwick.observatory.common.IP`: List of IP addresses used by daemons
* `warwick.observatory.common.daemons`: Pyro "phone book" specifying the IP and port for each daemon.
* `warwick.observatory.common.pyro_client_matches`: Pyro helper for white listing priviledged commands.
* `warwick.observatory.common.key_for_current_ip`: Helper to return the dictionary key that has a value matching the host IP.
* `warwick.observatory.common.TryLock`: A helper class for taking locks that should fail instead of blocking.
* `warwick.observatory.common.log`: A helper class for writing to the dashboard log database.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.
