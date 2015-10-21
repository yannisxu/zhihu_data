#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuyannis
# @Date:   2015-09-05 23:26:10
# @Last Modified by:   xuyannis
# @Last Modified time: 2015-10-03 20:07:56

from zhihu import User
from mongo import Users
from datetime import datetime
import threading
import logging
import time

logging.basicConfig(filename='example.log', format = "%(levelname) -10s %(asctime)s %(module)s:%(lineno)s %(funcName)s %(message)s", level=logging.INFO)

# user_url = "http://www.zhihu.com/people/kaifulee"
# user_grab = User(user_url)
# user = Users()

# if Users.objects(data_id = user_grab.get_data_id()).count():
#     user = Users.objects(data_id = user_grab.get_data_id()).first()

# user.user_id = user_grab.get_user_id()
# user.data_id = user_grab.get_data_id()
# user.followees_num = user_grab.get_followees_num()
# user.followers_num = user_grab.get_followers_num()
# user.asks_num = user_grab.get_asks_num()
# user.answers_num = user_grab.get_answers_num()
# user.collections_num = user_grab.get_collections_num()
# user.agree_num = user_grab.get_agree_num()
# user.thanks_num = user_grab.get_thanks_num()
# user.thanks_num = user_grab.get_thanks_num()
# user.url = user_grab.get_user_url()
# user.modify_time = datetime.utcnow()

# user.save()

# followees = user_grab.get_followees()
# followers = user_grab.get_followers()

# for i, user_grab in enumerate(followees):
#   if i%100 == 0:
#       time.sleep(200)
#       logging.info("sleep 200")
#   else:
#       time.sleep(1)
#   user = Users()
#   if Users.objects(data_id = user_grab.get_data_id()).count():
#       user = Users.objects(data_id = user_grab.get_data_id()).first()

#   user.user_id = user_grab.get_user_id()
#   user.data_id = user_grab.get_data_id()
#   user.followees_num = user_grab.get_followees_num()
#   user.followers_num = user_grab.get_followers_num()
#   user.asks_num = user_grab.get_asks_num()
#   user.answers_num = user_grab.get_answers_num()
#   user.collections_num = user_grab.get_collections_num()
#   user.agree_num = user_grab.get_agree_num()
#   user.thanks_num = user_grab.get_thanks_num()
#   user.url = user_grab.get_user_url()
#   user.modify_time = datetime.utcnow()

#   user.save()
#   logging.info("followees:" + str(i))

# for i, user_grab in enumerate(followers):
#     user = Users()
#     while True:
#         try:
#             if Users.objects(data_id = user_grab.get_data_id()).count():
#                 user = Users.objects(data_id = user_grab.get_data_id()).first()
#             break
#         except Exception, e:
#             print e
#             time.sleep(300)
#     user.user_id = user_grab.get_user_id()
#     user.data_id = user_grab.get_data_id()
#     user.followees_num = user_grab.get_followees_num()
#     user.followers_num = user_grab.get_followers_num()
#     try:
#         user.asks_num = user_grab.get_asks_num()
#         user.answers_num = user_grab.get_answers_num()
#         user.collections_num = user_grab.get_collections_num()
#     except Exception, e:
#         print e
#         print user_grab.get_user_url()
    
#     user.agree_num = user_grab.get_agree_num()
#     user.thanks_num = user_grab.get_thanks_num()
#     user.url = user_grab.get_user_url()
#     user.modify_time = datetime.utcnow()

#     user.save()
#     logging.info("followers:" + str(i))
#     logging.info(str(datetime.now()))


class myThread(threading.Thread):
    """docstring for myThread"""
    def __init__(self, threadID, name, counter, url):
        super(myThread, self).__init__()
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.url = url

    def run(self):
        logging.info("Starting" + self.name)
        grab(self.url, self.threadID)
        logging.info("Ending" + self.name)

def grab(url, threadID):
    print url
    user_grab = User(url)
    followers = user_grab.get_followers()

    for i, user_grab in enumerate(followers):
        user = Users()
        while True:
            try:
                if Users.objects(data_id = user_grab.get_data_id()).count():
                    user = Users.objects(data_id = user_grab.get_data_id()).first()
                break
            except Exception, e:
                logging.error("========error1")
                logging.error(e)
                time.sleep(300)
        user.user_id = user_grab.get_user_id()
        user.data_id = user_grab.get_data_id()
        user.followees_num = user_grab.get_followees_num()
        user.followers_num = user_grab.get_followers_num()
        try:
            user.asks_num = user_grab.get_asks_num()
            user.answers_num = user_grab.get_answers_num()
            user.collections_num = user_grab.get_collections_num()
        except Exception, e:
            logging.error("========error2")
            logging.error(e)
            logging.debug(user_grab.get_user_url())
    
        user.agree_num = user_grab.get_agree_num()
        user.thanks_num = user_grab.get_thanks_num()
        user.url = user_grab.get_user_url()
        user.modify_time = datetime.utcnow()

        user.save()
        logging.info("followers:" + str(i) + "threadID:" + str(threadID))
        logging.info(str(datetime.now()))

    
        
#thread1 = myThread(1, "线程1", 5, "http://www.zhihu.com/people/zeng-kai-87")
#thread2 = myThread(2, "线程2", 5, "http://www.zhihu.com/people/wangxiaofeng")
#thread3 = myThread(3, "线程3", 6, "http://www.zhihu.com/people/zhouyuan")
# thread4 = myThread(4, "线程4", 6, "http://www.zhihu.com/people/xiepanda")
# thread5 = myThread(5, "线程5", 6, "http://www.zhihu.com/people/feifeimao")


#thread1.start()
#thread2.start()
#thread3.start()
# thread4.start()
# thread5.start()

grab("http://www.zhihu.com/people/zhouyuan", 3)

logging.info("finish")
