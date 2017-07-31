#!/usr/bin/env python

import hashlib
import sys
import os

def sha256_checksum(filename, block_size=65536):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        for block in iter(lambda: f.read(block_size), b''):
            sha256.update(block)
    return sha256.hexdigest()

def main():
    numfiles = len(sys.argv) # how many files are we expecting?
    print("Creating HASHes for " + str(numfiles) + " Files...")
    for f in sys.argv[1:]:
        checksum = sha256_checksum(f)
        dir,file = os.path.split(f)
        #print(f + '\t' + checksum)
        #print(os.path.dirname(f))
        #print(dir)
        #print(file)
        try:
            # We are opening the file in APPEND mode, so if it already exists we will delete it
            # so that we do not append to old data. 
            try:
                os.remove(os.path.join(dir,'hash.txt'))
            except OSError:
                pass
            fh = open((os.path.join(dir,'hash.txt')),'a')
            #info = str(dir) + "\" + str(file) + "  " + checksum + '\t'
            info = str(file) + "  |  " + checksum + ' [SHA256]\n\n'
            print(info)
            fh.write(info)
            fh.close
            pass
        except IOError:
            print("File IOError!")
 
    os.system("pause")

if __name__ == '__main__':
    main()