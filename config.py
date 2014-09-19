# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab fdm=marker:
"""
Small wrapper around the python ConfigParser module.
"""

import ConfigParser

CONFIG = ConfigParser.ConfigParser()

DEFAULTS = {
        'patterns': {
            'path' : '\w+ - \d{4}+ - \w+'
        }
}

def get_param(section, name):
    try:
        param = CONFIG.get(section, name)
    except ConfigParser.NoOptionError or ConfigParser.NoSectionError:
        param = None

    if not param:
        # Do a default lookup
        try:
            param = DEFAULTS[section][name]
        except KeyError:
            # Parameter is not in defaults
            LOG.error("Error: Parameter [%s][%s] does not exist", section, name)
            param = ""

    return param

