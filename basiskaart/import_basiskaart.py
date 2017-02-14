"""
All commands to create a basiskaart
"""

import argparse
import logging

from bk2 import basiskaartbuild as bkb

LOG = logging.getLogger(__name__)

parser = argparse.ArgumentParser(
    description='Process import of basiskaart 10/50')
parser.add_argument(
    '--basiskaart',
    action='store',
    default='all',
    help='Select which basiskaart to import',
    choices=['all', 'kbk10', 'kbk50', 'bgt'])
args = parser.parse_args()

bkb.process_bk(args.basiskaart)
