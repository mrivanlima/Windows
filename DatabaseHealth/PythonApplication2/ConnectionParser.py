#!/usr/bin/python

from configparser import ConfigParser


def config(filename):
    cf = ConfigParser()
    cf.read(filename)
    _database = cf.get("SQLSERVERWINDOWS", "database")
    _host = cf.get("SQLSERVERWINDOWS", 'host')
    _user = cf.get("SQLSERVERWINDOWS", 'user')
    _pwd = cf.get("SQLSERVERWINDOWS", 'pwd')
    return _database, _host, _user, _pwd
  
