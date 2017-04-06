#coding=utf-8
import json
from wxpy import *

bot = Bot()

groups = {} 

logger = get_wechat_logger()
logger.warning(u'這是一條WARNING等級的日志，你收到了嗎？')

@bot.register([my_friend, Group], TEXT)
def auto_reply_text(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return 
    else:
        return '收到信息: {} ({})'.format(msg.text, msg.type)

@bot.register([my_friend, Group], PICTURE)
def auto_reply_pic(msg):
    if isinstance(msg.chat, Group) and not msg.is_at:
        return
    else:
        send_image('./QR.png',media_id=None)

@bot.register(msg_types=FRIENDS)
def add_friend(msg):
    if 'Algorithm' in msg.text.lower():
        new_friend = bot.accept_friend(msg.card)
        new_friend.send(u'每日一题微信机器人为您服务', msg.sender)

bot.start()

#embed()
bot.join()
