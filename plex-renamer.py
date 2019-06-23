#!/usr/bin/python3

# This is a magical program that reformats all of the file names in a directory
# It is used for formatting flac albums to work with a plex server
# Author: Brendan Russell 6/23/2019

import sys
import os

def main():
    i = 0

    if (len(sys.argv) < 2):
        print("Please specify directory")
        sys.exit(1)
    else:
        print("Changing files in: %s\n" % sys.argv[1])

    for filename in os.listdir(sys.argv[1]):
        dst = filename.lower()
        dst = dst.replace(" ", "_")
        dst = dst.replace(",", "_")
        dst = dst.replace("'", "")
        dst = dst.replace(".", "")
        dst = dst.replace("!", "")
        dst = dst.replace("?", "")
        dst = dst.replace("_-_", "_")
        dst = dst.replace("___", "_")
        dst = dst.replace("flac", ".flac")
        print("Renaming: %s as %s" % (filename, dst))
        if sys.argv[1][len(sys.argv[1]) - 1] != '/':
            src = sys.argv[1] + "/" + filename
            dst = sys.argv[1] + "/" + dst
        else:
            src = sys.argv[1] + filename
            dst = sys.argv[1] + dst
        os.rename(src, dst)



if __name__ == '__main__':
    
    main()

