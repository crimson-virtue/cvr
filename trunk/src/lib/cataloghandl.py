#!/usr/bin/env python
# 
# cataloghandl.py
'''
Current version: 0.0.1


Created on 2014.05.31
@author CVirtue
'''
from lxml import etree



def fetchMovies(catalogpath):
    '''
    Parses the movie titles found in the specified .xml file given as
    catalogpath, then returns them as a list of strings.
    
    @param catalogpath: a string representing the path to the catalog.xml
    @return: the movie titles represented as a list of strings 
    '''
    return [ 'NO Strings Attached','Fight Club' ] #etree.parse( catalogpath ).find('//')
