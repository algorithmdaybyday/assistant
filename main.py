#coding=utf-8
import itchat
import json
from itchat.content import *

groups = {}

@itchat.msg_register(TEXT, isGroupChat=True)
def group_reply_text(msg):
    fromUserName = msg['FromUserName']
    source = msg['ToUserName']
    if msg['Content'] == 'Hi':
        groups[source] = source 
    if groups.has_key(fromUserName):
        for item in groups.keys():
            if not item == fromUserName:
                itchat.send(' %s say:\n%s' % (msg['ActualNickName'], msg['Content']), item)

@itchat.msg_register(PICTURE, isGroupChat=True)
def group_reply_media(msg):
    source = msg['FromUserName']
    msg['Text'](msg['FileName'])
    if groups.has_key(source):
        for item in groups.keys():
            if not item == source:
                itchat.send('@%s@%s'%('img' if msg['Type'] == 'Picture' else 'fil', msg['FileName']), item)

@itchat.msg_register(PICTURE, isGroupChat=False)
def download_png(msg):
    source = msg['FromUserName']
    msg['Text'](msg['FileName'])
    itchat.send(msg['FileName'], source)

itchat.auto_login(True)
itchat.run()
