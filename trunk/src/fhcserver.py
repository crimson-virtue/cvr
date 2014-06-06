#!/usr/bin/env python
# 
# fhcserver.py
'''
Current version: 0.0.1


Created on 2014.05.31
@author CVirtue
'''
import os
import sys
import flask
import logging

sys.path.append( './lib' )

import cataloghandl
from logging import Formatter
from ioutils import isModified
from logging.handlers import RotatingFileHandler
from flask import Flask, request, render_template, session, redirect, g



# Global Space
app     = Flask(__name__)
environ = {
    'SECRETKEY': 'gw\xbdv<\xeah>\xbf\x9d\x1a\xe3\xfe\xa72\x90\xe5:a\xa9A\xbe\x82"',
    'LOGFILE': 'static/log/srv.log',
    'CATALOGROOT':'static/ctlgs/',
    'CATALOGFILE':'DVD_katalogus.xml'
} 



# Routing Space
@app.route( '/',methods=['GET'] )
def root():
    app.logger.debug('root reached..')
    return render_template('fhc_index.html')


@app.route( '/movies',methods=['GET'] )
def movies():
    catalogpath = '/'.join( [environ['CATALOGROOT'],environ['CATALOGFILE']] )
    '''
    if not session.get('movies') or isModified( catalogpath,session.get('lastmod_ts') ):
        session['movies'] = flask.jsonify(cataloghandl.fetchMovies( catalogpath ))
        session['lastmod_ts'] = os.path.getmtime( catalogpath )'''
    session['movies'] = cataloghandl.fetchMovies( catalogpath )
    app.logger.debug( 'movies: %s' % session['movies'] )
    return render_template( 'fhc_movies.html',movies=session['movies'] )



# Inner Mechanisms Space
def __setEnvironFor__(applic, environmap):
    '''
    Sets the environment specific properties of the Flask instance given as applic
    according to the passed environmap dictionary. It requires that environmap contains
    a key SECRETKEY, otherwise a KeyError is thrown.
    
    @param applic: the Flask instance
    @param environmap: the dict containing the filepath to the logfile
    '''
    applic.secret_key = environmap['SECRETKEY']


def __setLoggersFor__(applic, environmap):
    '''
    Appends a logging.handler.RotatingFileHandler instance to the Flask instance
    given as applic, sets its logging file according to the environmap parameter.
    It requires that the environmap contains a key LOGFILE, otherwise a KeyError is thrown.
    
    @param applic: the Flask instance
    @param environmap: the dict containing the filepath to the logfile
    '''
    filehandl = RotatingFileHandler( environmap['LOGFILE'],backupCount=2 )
    filehandl.setLevel( logging.DEBUG )
    filehandl.setFormatter( Formatter('%(asctime)s %(levelname)s %(message)s '
                                      '[in %(pathname)s:%(lineno)d]'))
    applic.logger.addHandler(filehandl)



if __name__=='__main__':
    __setLoggersFor__( app,environ )
    __setEnvironFor__( app,environ )
    app.run( host='0.0.0.0',debug=True )
