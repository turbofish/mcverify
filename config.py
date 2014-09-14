# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab fdm=marker:
"""
Small wrapper around the python ConfigParser module.
"""

import ConfigParser

# pylint: disable=R0903
class Config(ConfigParser):
    """
    A small extension for the ConfigParser class to simplify parsing a
    configuration file.
    """

    def __init__(self):
        # {{{
        pass
        # }}}

