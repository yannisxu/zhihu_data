#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: xuyannis
# @Date:   2015-09-05 23:26:10
# @Last Modified by:   xuyannis
# @Last Modified time: 2015-09-13 01:04:08

from zhihu import User

user_url = "http://www.zhihu.com/people/jixin"
user = User(user_url)
# 获取用户ID
user_id = user.get_user_id()
# 获取该用户的关注者人数
followers_num = user.get_followers_num()
# 获取该用户关注的人数
followees_num =user.get_followees_num()
# 获取该用户提问的个数
asks_num = user.get_asks_num()
# 获取该用户回答的个数
answers_num = user.get_answers_num()
# 获取该用户收藏夹个数
collections_num = user.get_collections_num()
# 获取该用户获得的赞同数
agree_num = user.get_agree_num()
# 获取该用户获得的感谢数
thanks_num = user.get_thanks_num()

# 获取该用户关注的人
followees = user.get_followees()
# 获取关注该用户的人
followers = user.get_followers()
# 获取该用户提的问题
asks = user.get_asks()
# 获取该用户回答的问题的答案
answers = user.get_answers()
# 获取该用户的收藏夹
collections = user.get_collections()

print user_id # 黄继新
print followers_num # 614840
print followees_num # 8408
print asks_num # 1323
print answers_num # 786
print collections_num # 44
print agree_num # 46387
print thanks_num # 11477


print followees
# follow = list(followees)
# for x in follow:
# 	print x
# <generator object get_followee at 0x7ffcac3af050>
# 代表所有该用户关注的人的生成器对象
print followers

next(followers)
# <generator object get_follower at 0x7ffcac3af0f0>
# 代表所有关注该用户的人的生成器对象
print asks
# <generator object get_ask at 0x7ffcab9db780>
# 代表该用户提的所有问题的生成器对象
print answers
# <generator object get_answer at 0x7ffcab9db7d0>
# 代表该用户回答的所有问题的答案的生成器对象
print collections
# <generator object get_collection at 0x7ffcab9db820>
# 代表该用户收藏夹的生成器对象