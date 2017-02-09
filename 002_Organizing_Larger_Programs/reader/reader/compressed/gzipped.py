'''
gzipped module provides two functionality
* Open gzip2 files
* Compress files to gzip2

@author: ArchKudo
'''
import gzip
import sys

opener = gzip.open

'''If file is opened as the main file rather than imported'''
if __name__ == '__main__':
    f = gzip.open(sys.argv[1], mode='wt')
    f.write(''.join(sys.argv[2:]))
    f.close()
