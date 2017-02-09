'''
The compressed subpackage
@author: ArchKudo
'''
from ..compressed.bzipped import opener as bz2_opener
from ..compressed.gzipped import opener as gz2_opener

__all__ = ['bz2_opener', 'gz2_opener']

print('Importing compressed package...')
