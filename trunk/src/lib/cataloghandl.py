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
    res = {}
    parser = etree.XMLParser(recover=True)
    for tag in etree.parse( open(catalogpath),parser ).findall('//Movie'):
        res[ int(tag.attrib['Number']) ] = tag.attrib['OriginalTitle']
    return res


def fetchMovieFor(title, number, catalogpath):
    '''
    Returns the details about the movie specified by its title, found in the .xml catalog
    file given as catalogpath, according to the passed number. It returns the details as
    a dictionary with.
    
    @param title: the title of the movie to search for
    @param number: the number that specifies the movie in the catalog.xml
    @param catalogpath: that identifies the catalog.xml from which to
                        fetch the details
    @return: a dictionary containing the relevant data.
    '''
    filtr_str = '//Movie[@Number="%s"]' % number
    parser = etree.XMLParser(recover=True)
    return etree.parse( open(catalogpath),parser ).find(filtr_str).attrib
