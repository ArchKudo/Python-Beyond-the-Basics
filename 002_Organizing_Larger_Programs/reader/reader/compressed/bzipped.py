'''
bzipped module provides two functionality
* Open bzip2 files
* Compress files to bzip2

@author: ArchKudo
'''
import bz2
import sys

opener = bz2.open

'''If file is opened as the main file rather than imported'''
if __name__ == '__main__':
    file = bz2.open(sys.argv[1], mode='wt')
    file.write(''.join(sys.argv[2:]))
