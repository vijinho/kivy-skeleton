# -*- coding: utf-8 -*-
'''
Skeleton Database Models
========================

Models to handle data
'''

import click
from peewee import *
from datetime import datetime
import json
import kivy
kivy.require('1.8.0')
from kivy import platform


def get_database():
    if platform == 'android':
        file = '/sdcard/skeleton/skeleton.db'
    else:
        import ConfigParser
        config = ConfigParser.RawConfigParser()
        config.read('config.ini')
        file = config.get('database', 'file')
    return SqliteDatabase(file)


class BaseModel(Model):

    """(Peewee) Base Database model for Aphorisms App"""
    class Meta:
        database = get_database()

if __name__ == "__main__":
    pass
