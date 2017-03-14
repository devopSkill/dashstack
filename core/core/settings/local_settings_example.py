# -*- coding: utf-8 -*-

from ConfigParser import RawConfigParserd
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE_ROOT = os.path.dirname(BASE_DIR)

config = RawConfigParser()
config.read(os.path.join(SITE_ROOT, 'etc', 'dashstack.ini'))

APP_OWNER = config.get('info', 'APP_OWNER')
APP_NAME = config.get('info', 'APP_NAME')
SITE_ID = config.getint('info', 'SITE_ID')

DBUSER = config.getint('database', 'DBUSER')
DBPASS = config.getint('database', 'DBPASS')
DBHOST = config.getint('database', 'DBHOST')
DBPORT = config.getint('database', 'DBPORT')
DBNAME = config.getint('database', 'DBNAME')
