#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuyannis
# @Date:   2015-09-26 09:26:01
# @Last Modified by:   xuyannis
# @Last Modified time: 2015-10-21 09:48:02

from zhihu import User
from mongo import Users
from datetime import datetime
import threading
import logging
import time
import csv

logging.basicConfig(filename='followee_grab.log', format = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s", level=logging.INFO)


#查找出需要遍历的用户
user_list = Users.objects[0:100]

def grab(url, threadID):
    print url
    user_grab = User(url)
    followees = user_grab.get_followees()

    for i, user_grab in enumerate(followees):
        user = Users()
        flag = True
        while True:
            try:
                if Users.objects(data_id = user_grab.get_data_id()).count():
                    user = Users.objects(data_id = user_grab.get_data_id()).first()
                break
            except Exception, e:
                flag = False
                logging.error("========error1")
                logging.error(e)
                time.sleep(300)
                break
        try:
            user.user_id = user_grab.get_user_id()
            user.data_id = user_grab.get_data_id()
            user.followees_num = user_grab.get_followees_num()
            user.followers_num = user_grab.get_followers_num()
            user.asks_num = user_grab.get_asks_num()
            user.answers_num = user_grab.get_answers_num()
            user.collections_num = user_grab.get_collections_num()
            user.agree_num = user_grab.get_agree_num()
            user.thanks_num = user_grab.get_thanks_num()
            user.url = user_grab.get_user_url()
            user.modify_time = datetime.utcnow()
        except Exception, e:
            logging.error("========error2")
            logging.error(e)
            logging.debug(user_grab.get_user_url())
        if flag:
            user.save()
        logging.info("followers:" + str(i) + "threadID:" + str(threadID))
        logging.info(str(datetime.now()))
    logging.info(url + "##########" + "finish")

for i, url in enumerate(url_list):
     grab(url, i)
        


# for url in url_list:
#     user_grab = User(url)
#     followees = user_grab.get_followees()

#     for i, user_grab in enumerate(followees):
#         user = Users()
#         while True:
#             try:
#                 if Users.objects(data_id = user_grab.get_data_id()).count():
#                     user = Users.objects(data_id = user_grab.get_data_id()).first()
#                 break
#             except Exception, e:
#                 print e
#                 time.sleep(300)
#                 break
#         try:
#             user.user_id = user_grab.get_user_id()
#             user.data_id = user_grab.get_data_id()
#             user.followees_num = user_grab.get_followees_num()
#             user.followers_num = user_grab.get_followers_num()
#             user.agree_num = user_grab.get_agree_num()
#             user.thanks_num = user_grab.get_thanks_num()
#             user.url = user_grab.get_user_url()
#             user.modify_time = datetime.utcnow()

#             user.asks_num = user_grab.get_asks_num()
#             user.answers_num = user_grab.get_answers_num()
#             user.collections_num = user_grab.get_collections_num()
#         except Exception, e:
#             print e
        
#         user.save()
#         logging.info("followees:" + str(i))
#         logging.info(str(datetime.now()))
#     logging.info(url + ": finish")
