#!/usr/bin/env python3
# Script for tree of file structure with indents returning
# Based on https://stackoverflow.com/a/9728478

import os
import argparse
from sys import argv


def list_files(startpath):
    TREE = ''
    for root,  dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        ROOT = str('{}{}/'.format(indent,  os.path.basename(root)))
        TREE += ROOT + '\n'
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            TREE += str('{}{}\n'.format(subindent, f))
    return TREE

def main():
    parser = argparse.ArgumentParser(prog='FileTree')
    parser.add_argument('--filename', '-f', help='Name of file for saving')
    parser.add_argument('--startpath', '-p', help='Start path for scanning')
    args = parser.parse_args()

    if args.filename:
        filename = args.filename
    else:
        filename = input('Type name for saving: ')

    if args.startpath:
        startpath = args.startpath
    else:
        startpath = input('Type start path for scanning: ')
        
    with open(filename, 'w') as f:
        f.write(list_files(str(startpath)))

if __name__ == '__main__':
    main()
