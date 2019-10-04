#!/usr/bin/env python

import argparse
import os
import sys
import base64

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

def four_bases_to_byte(four_bases):
    # TODO: generate the full version of this table:
    four_bases_to_byte_dict = {
        'TTTT': 0b00000000, # 0x00
        'TTTC': 0b00000001, # 0x01
        'TTTA': 0b00000010, # 0x02
        'TTTG': 0b00000011, # 0x03
        'TTCT': 0b00000100, # 0x04
        'TTCC': 0b00000101, # 0x05
        'TTCA': 0b00000110, # 0x06
        'TTCG': 0b00000110, # 0x07
        
        'GGGG': 0b11111111, # 0xff
    }
    try:
        output = four_bases_to_byte_dict[four_bases]
    except KeyError as e:
        output = None
    return output

def byte_to_four_bases(byte):
    byte_to_four_bases_dict = {
        0b00000000: 'TTTT',  # 0x00
        0b00000001: 'TTTC',  # 0x01
        0b00000010: 'TTTA',  # 0x02
        0b00000011: 'TTTG',  # 0x03
        0b00000100: 'TTCT',  # 0x04
        0b00000101: 'TTCC',  # 0x05
        0b00000110: 'TTCA',  # 0x06
        0b00000110: 'TTCG',  # 0x07
        
        0b11111111: 'GGGG', # 0xff
    }
    try:
        output = byte_to_four_bases_dict[byte]
    except KeyError as e:
        output = None
    return output

def chunks(l, n):
    """
    Yield successive n-sized chunks from l.
    https://stackoverflow.com/a/312464/780188
    """
    for i in range(0, len(l), n):
        yield l[i:i + n]

def main(args):
    seq = 'TTCGGGGGTTTGTTCCTTTAGGGG'
    chunked_seq = list(chunks(seq, 4))
    print(seq)
    pprint(chunked_seq)
    seq_bytearray = bytearray(map(four_bases_to_byte, chunked_seq))
    seq_base64_urlsafe = base64.urlsafe_b64encode(seq_bytearray)
    print(seq_base64_urlsafe.decode("utf-8"))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    #parser.add_argument("fasta", help="fasta file")
    args = parser.parse_args()
    main(args)
