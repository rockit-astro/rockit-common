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
Configuration file validation helpers
"""

import jsonschema
import os.path
import sys
import traceback
from warwick.observatory.common import daemons, IP


class ConfigSchemaViolationError(Exception):
    """Exception used to report schema violations"""
    def __init__(self, errors):
        message = 'Invalid configuration:\n\t' + '\n\t'.join(errors)
        super(ConfigSchemaViolationError, self).__init__(message)


# pylint: disable=unused-argument
def daemon_name_validator(validator, value, instance, schema):
    """Validate a string as a daemon name from warwick.observatory.common.daemons"""
    try:
        getattr(daemons, instance)
    except Exception:
        yield jsonschema.ValidationError('{} is not a valid daemon name'.format(instance))


def machine_name_validator(validator, value, instance, schema):
    """Validate a string as a machine name from warwick.observatory.common.IP"""
    try:
        getattr(IP, instance)
    except Exception:
        yield jsonschema.ValidationError('{} is not a valid machine name'.format(instance))


def directory_path_validator(validator, value, instance, schema):
    """Validate a string as an existing directory path"""
    if not os.path.isdir(instance):
        yield jsonschema.ValidationError('{} is not a valid directory path'.format(instance))
# pylint: enable=unused-argument


def validate_config(json, schema, custom_validators=None, print_exception=False):
    """Tests whether a json object defines a valid environment config file
       Raises SchemaViolationError on error
    """
    errors = []
    try:
        validators = dict(jsonschema.Draft4Validator.VALIDATORS)
        if custom_validators:
            validators.update(custom_validators)

        validator = jsonschema.validators.create(
            meta_schema=jsonschema.Draft4Validator.META_SCHEMA,
            validators=validators)

        for error in sorted(validator(schema).iter_errors(json),
                            key=lambda e: e.path):
            if error.path:
                path = '->'.join([str(p) for p in error.path])
                message = path + ': ' + error.message
            else:
                message = error.message
            errors.append(message)
    except Exception:
        if print_exception:
            traceback.print_exc(file=sys.stdout)
        errors = ['exception while validating']

    if errors:
        raise ConfigSchemaViolationError(errors)
