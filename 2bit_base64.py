#!/usr/bin/env python

import argparse
import os
import sys
import twobitreader

from pprint import pprint

def main(args):
    twobitfile = twobitreader.TwoBitFile(args.twobit)
    for twobitseq in twobitfile:
        print(twobitfile[twobitseq])


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("twobit", help="2bit file")
    args = parser.parse_args()
    main(args)
