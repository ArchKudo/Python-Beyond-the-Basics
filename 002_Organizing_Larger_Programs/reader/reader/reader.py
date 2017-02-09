'''
Read from text or compressed files
@author: ArchKudo
'''
import os

# Using relative imports
# .compressed is the same as reader.compressed
from .compressed import bzipped, gzipped

EXT_DICT = {'.bz2': bzipped.opener,
            '.gz2': gzipped.opener
            }


class Reader:
    '''Reader Class -- Read contens from text/bzip/gzip files'''

    def __init__(self, filename):
        '''Opening a supported file'''
        # Get .Extension
        extension = os.path.splitext(filename)[1]

        # OPENER is extension.OPENER or equal to open function
        opener = EXT_DICT.get(extension, open)

        # Substitutes with bzip2.OPENER/gzip2.OPENER/open
        self.file = opener(filename, 'rt')

    def close(self):
        ''' Close a file '''
        self.file.close()

    def read(self):
        ''' Read a file '''
        return self.file.read()
