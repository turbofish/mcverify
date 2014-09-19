#!/bin/python
# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab fdm=marker:
"""
Main file for MCVerify. Parses the config, options to the file and
executes the line of checkers.
"""
import os
from os.path import expandvars, expanduser
import logging
import sys
import checkers
import argparse
from config import CONFIG
from log import LOG

# Path to default configuration
DEFAULT_CONFIG = "~/.mcverifyrc"

def parse_arguments():
    """
    Fnord
    """
    # {{{
    LOG.debug("Parsing arguments...")
    parser = argparse.ArgumentParser()

    parser.add_argument("directory", type=str,
            help="Directory to be scanned")
    parser.add_argument("-c", "--config", type=str,
            help="Configuration file")

    args = parser.parse_args()

    return args
    # }}}

def parse_config(filename):
    """
    Fnord
    """
    # {{{
    filename = expanduser(expandvars(filename))
    LOG.debug("Parsing configuration in file '%s'",filename)
    CONFIG.read(filename)
    # }}}

if __name__ == '__main__':
    args = parse_arguments()

    if args.config:
        parse_config(args.config)
    else:
        parse_config(DEFAULT_CONFIG)

    LOG.debug("Starting walking directory %s",args.directory)
    for root, dirs, files in os.walk(args.directory):
        if not dirs:
            LOG.debug("Reached bottom @ '%s'" % root)
            LOG.debug("Running checkers")

            for c in checkers.CHECKERS:
                c.check(root, files)

