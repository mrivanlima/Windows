#!/usr/bin/python

from configparser import ConfigParser


def config(filename):
    cf = ConfigParser()
    cf.read(filename)
    _database = cf.get("SQLSERVER", "database")
    _host = cf.get("SQLSERVER", 'host')
    _user = cf.get("SQLSERVER", 'user')
    _pwd = cf.get("SQLSERVER", 'pwd')
    return _database, _host, _user, _pwd
  
