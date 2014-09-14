# vim: set fileencoding=utf-8 ts=4 sw=4 expandtab fdm=marker:
"""
Main file for MCVerify. Parses the config, options to the file and
executes the line of checkers.
"""
import os
import logging
import sys
import checkers

LOG = logging.getLogger("mcverify")

def usage():
    print "fnord"

if len(sys.argv) <= 1:
    usage()
    sys.exit(1)

for root, dirs, files in os.walk(sys.argv[1]):
    if not dirs:
        LOG.debug("Reached bottom @ '%s'" % root)
        LOG.debug("Running checkers")

        for c in checkers.CHECKERS:
            c.check(root, files)

