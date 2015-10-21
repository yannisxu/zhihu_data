#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: yannisxu
# @Date:   2015-09-14 01:17:38
# @Last Modified by:   xuyannis
# @Last Modified time: 2015-10-21 11:51:25

from mongoengine import *
from ConfigParser import ConfigParser
from datetime import datetime
import os

cf = ConfigParser()
config_file = "config.ini"

if os.path.exists(config_file) and os.path.isfile(config_file):
    print "正在加载 mongo 配置文件 ..."
    cf.read(config_file)
    name = cf.get("mongo", "name")
    password = cf.get("mongo", "password")
    host = cf.get("mongo", "host")
    port = cf.get("mongo", "port")
    database = cf.get("mongo", "database")
else :
	print "无法加载 mongo 配置文件"

mongo_url = "mongodb://" + name + ":" + password + "@" + host + ":" + port + "/" + database 
connect_zhihu = connect('zhihu', host=mongo_url)

class Users(Document):
    user_id = StringField()
    data_id = StringField(unique = True)
    name = StringField()
    followers_num = IntField()
    followees_num = IntField()
    asks_num = IntField()
    answers_num = IntField()
    collections_num = IntField()
    agree_num = IntField()
    thanks_num = IntField()
    url = StringField()
    create_time = DateTimeField(default = datetime.utcnow())
    modify_time = DateTimeField()

class Queue(Document):
    url = StringField(unique = True)
    create_time = DateTimeField(default = datetime.utcnow())
    modify_time = DateTimeField()
    is_traversal = BooleanField(default = False)

# user = Users(_id = 22222312, name = "asdad")
# user.followees_num = 12313
# print user._id
# print user.followees_num
# user.save()
