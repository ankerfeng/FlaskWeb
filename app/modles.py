#!/usr/bin/env python
#coding:utf-8

import random
import string
import datetime
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin, AnonymousUserMixin
from werkzeug.security import  generate_password_hash, check_password_hash

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = SQLAlchemy()
mysql_engine = create_engine('mysql://root:taiops@localhost:3306/taiops?charset=utf8', pool_recycle=100)
Session = sessionmaker(bind=mysql_engine)
session = Session()






