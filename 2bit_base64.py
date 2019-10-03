#!/usr/bin/env python

import argparse
import os
import sys

from pprint import pprint


def char_to_bits(char):
    char_to_bits_dict = {
        'T': 0b00,
        'C': 0b01,
        'A': 0b10,
        'G': 0b11,
    }
    try:
        output = char_to_bits_dict[char]
    except KeyError as e:
        output = None
    return output

def main(args):
    seq = 'ACGATGCAT'
    
    output = list(map(char_to_bits, list(seq)))
    pprint(output)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("fasta", help="fasta file")
    args = parser.parse_args()
    main(args)
