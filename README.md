## Warwick common observatory code [![Travis CI build status](https://travis-ci.org/warwick-one-metre/warwick-observatory.svg?branch=master)](https://travis-ci.org/warwick-one-metre/warwick-observatory)

Python module that contains common backend code that is shared by the other python utilities.
The main components are:
* `warwick.observatory.common.daemons`: Pyro "phone book" specifying the IP and port for each daemon.
* `warwick.observatory.common.TryLock`: A helper class for taking locks that should fail instead of blocking.
* `warwick.observatory.common.log`: A helper class for writing to the dashboard log database.

See [Software Infrastructure](https://github.com/warwick-one-metre/docs/wiki/Software-Infrastructure) for an overview of the W1m software architecture and instructions for developing and deploying the code.
