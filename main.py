#!/usr/bin/python3
#coding=utf-8
import json
from wxpy import *


# 声明成员

bot = Bot()
# Friends_test = bot.friends().search('东东')[0]
group_geek = bot.groups().search('算法第6群')[0]

#  logger = get_wechat_logger()
#  logger.warning('這是一條WARNING等級的日志，你收到了嗎？')


# 回复群里@到和好友信息

@bot.register([Friend, Group], TEXT)
def auto_reply_text(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return 
    else:
        return '收到信息: {} ({})'.format(msg.text, msg.type)
        if '加群' in msg.text.lower():
            add_members(msg.sender,use_invitation=True)


# 发送图片

@bot.register([Friend, Group], PICTURE)
def auto_reply_pic(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        msg.reply_image('./th.jpg', media_id=None)


# 自动添加好友

@bot.register(msg_types=FRIENDS)
def add_friend(msg):
    if '我要加群' in msg.text.lower():
        new_friend = bot.accept_friend(msg.card)
        new_friend.send('每日一题微信机器人为您服务', msg.sender)
        group_geek.add_members(msg.sender, use_invitation=True)

# 自动拉人进群

@bot.register(Friend, TEXT)
def add_group_member(msg):
    if '申请入群' in msg.text.lower():
        group_geek.add_members(msg.sender, use_invitation=True)

bot.start()

#embed()
bot.join()  # 堵塞线程
