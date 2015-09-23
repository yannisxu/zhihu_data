#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuyannis
# @Date:   2015-09-05 23:26:10
# @Last Modified by:   xuyannis
# @Last Modified time: 2015-09-24 03:40:15

from zhihu import User
from mongo import Users
from datetime import datetime
import logging
import time

logging.basicConfig(filename='example.log', level=logging.INFO)

user_url = "http://www.zhihu.com/people/kaifulee"
user_grab = User(user_url)
user = Users()

if Users.objects(data_id = user_grab.get_data_id()).count():
	user = Users.objects(data_id = user_grab.get_data_id()).first()

user.user_id = user_grab.get_user_id()
user.data_id = user_grab.get_data_id()
user.followees_num = user_grab.get_followees_num()
user.followers_num = user_grab.get_followers_num()
user.asks_num = user_grab.get_asks_num()
user.answers_num = user_grab.get_answers_num()
user.collections_num = user_grab.get_collections_num()
user.agree_num = user_grab.get_agree_num()
user.thanks_num = user_grab.get_thanks_num()
user.thanks_num = user_grab.get_thanks_num()
user.url = user_grab.get_user_url()
user.modify_time = datetime.utcnow()

user.save()

followees = user_grab.get_followees()
followers = user_grab.get_followers()

# for i, user_grab in enumerate(followees):
# 	if i%100 == 0:
# 		time.sleep(200)
# 		logging.info("sleep 200")
# 	else:
# 		time.sleep(1)
# 	user = Users()
# 	if Users.objects(data_id = user_grab.get_data_id()).count():
# 		user = Users.objects(data_id = user_grab.get_data_id()).first()

# 	user.user_id = user_grab.get_user_id()
# 	user.data_id = user_grab.get_data_id()
# 	user.followees_num = user_grab.get_followees_num()
# 	user.followers_num = user_grab.get_followers_num()
# 	user.asks_num = user_grab.get_asks_num()
# 	user.answers_num = user_grab.get_answers_num()
# 	user.collections_num = user_grab.get_collections_num()
# 	user.agree_num = user_grab.get_agree_num()
# 	user.thanks_num = user_grab.get_thanks_num()
# 	user.url = user_grab.get_user_url()
# 	user.modify_time = datetime.utcnow()

# 	user.save()
# 	logging.info("followees:" + str(i))

for i, user_grab in enumerate(followers):
	user = Users()
	while True:
		try:
			if Users.objects(data_id = user_grab.get_data_id()).count():
				user = Users.objects(data_id = user_grab.get_data_id()).first()
			break
		except Exception, e:
			print e
			sleep(300)
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

	user.save()
	logging.info("followers:" + str(i))

logging.info("finish")