'''
Provides a simple UI to the reader package

@author: ArchKudo
'''
import sys
import reader

try:
    file = reader.Reader(sys.argv[1])
    print(file.read())
    file.close()
except:
    print('Could not read file')
