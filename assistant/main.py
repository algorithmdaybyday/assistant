#!/usr/bin/python3
#coding=utf-8
import json
from wxpy import *
import threading
import time


# 声明成员
bot = Bot(cache_path=True, console_qr=True)

# 定义同步消息的groups
global groups
global group
global group2
global group3
global group4
groups = bot.groups().search('算法')
group = bot.groups().search("每日一题算法7群")[0]
group2 = bot.groups().search("每日一题中转站")[0]
group3 = bot.groups().search("每日一题灌水群")[0]
group4 = bot.groups().search("清单")[0]

#  logger = get_wechat_logger()
#  logger.warning('這是一條WARNING等級的日志，你收到了嗎？')

# 同步微信群的消息
# @bot.register(groups, except_self=False)
# def sync_my_groups(msg):
    # sync_message_in_groups(msg, groups)

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
        msg.reply_image('./assets/th.jpg', media_id=None)

# 自动添加好友
@bot.register(msg_types=FRIENDS)
def add_friend(msg):
    message = '''
欢迎加入每日一题群，我是加群助手小雪。
每日一题群是每天练习一道算法题的算法学习群。
历史题目和总结见公众号「每日一道算法题」, 或者搜索 myhuyanluanyu 。
        '''
    new_friend = bot.accept_friend(msg.card)
    new_friend.send(message, msg.sender)
    group.add_members(msg.sender, use_invitation=True)

# 自动拉人进群
@bot.register(Friend, TEXT)
def add_group_member(msg):
    if '刷题' in msg.text.lower() or '加群' in msg.text.lower():
        group.add_members(msg.sender, use_invitation=True)
    if '灌水' in msg.text.lower():
        group3.add_members(msg.sender, use_invitation=True)
    if '清单' in msg.text.lower():
        group4.add_members(msg.sender, use_invitation=True)

def send_message_to_group():
    message = '''@所有人:
大家好，我是群助手机器人小雪。
没进入算法主群的伙伴请加我微信，并发送我要加群的消息给我，我拉你们进主群。
已经进主群的伙伴麻烦退出该群，谢谢。
没有收到邀请的伙伴请发如下信息给我：我要刷题
    '''
    group2.send(message)
    global timer
    timer = threading.Timer(20800, send_message_to_group)
    timer.start()

timer = threading.Timer(7200, send_message_to_group)
timer.start()

bot.start()
# embed()
bot.join()  # 堵塞线程
