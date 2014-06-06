#!/usr/bin/env python
# 
# ioutils.py
'''
Current version: 0.0.1


Created on 2014.06.05
@author CVirtue
'''
import os
import sys



def isModified(filepath, timestamp):
    '''
    Checks whether the given file has been modified since the last time it was
    checked as the passed timestamp indicates.
    
    @param filepath:  indicates the file to be checked
    @param timestamp: indicates the number of seconds since the epoch
    @return:          True if the given timestap is None or less than the seconds
                      obtained from os.path
    '''
    if not os.path.exists( filepath ):
        return False
    return timestamp == None and True or os.path.getmtime( filepath ) > timestamp
