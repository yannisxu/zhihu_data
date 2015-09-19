#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuyannis
# @Date:   2015-09-05 23:26:10
# @Last Modified by:   yannisxu
# @Last Modified time: 2015-09-19 11:11:00

from zhihu import User
from mongo import Users
import logging

logging.basicConfig(filename='example.log', level=logging.INFO)

user_url = "http://www.zhihu.com/people/jixin"


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
user.thanks_num = 123456
user.url = user_url

user.save()



followees = user_grab.get_followees()
followers = user_grab.get_followers()

for i, user_grab in enumerate(followees):
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
	user.url = user_url

	user.save()
	logging.info("followees:" + str(i))

for i, user_grab in enumerate(followers):
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
	user.url = user_url

	user.save()
	logging.info("followers:" + str(i))

logging.info("finish")