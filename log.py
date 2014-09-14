"""
Logging configuration for MCVerify.
"""

import logging

LOG = logging.getLogger("mcverify")
LOG_HANDLER = logging.StreamHandler()
LOG_FORMAT = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
LOG_HANDLER.setFormatter(LOG_FORMAT)
LOG.addHandler(LOG_HANDLER)
LOG.setLevel(logging.DEBUG)

