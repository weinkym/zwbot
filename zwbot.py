import itchat
import os
from itchat.content import *
import time
import ocr_baidu as OCRBD

zw_group_name='TT123456'
zw_group_obj={}

ZW_IMAGE_TYPE_INVOICE='invoice'
ZW_IMAGE_TYPE_NORMAL='normal'
zw_image_type='normal'

def get_save_root_path():
    d = os.path.dirname(__file__)
    d = os.path.join(d,'TEMP')
    if not os.path.exists(d):
        os.mkdir(d)
    return d

def get_save_path_pictrue(fileName):
    d = get_save_root_path()
    d = os.path.join(d,'PICTRUE')
    if not os.path.exists(d):
        os.mkdir(d)
    return os.path.join(d,fileName)

def isGroupMessage(msg,group_obj):
    if type(group_obj) is not dict:
        print("group_obj is not dict type={}".format(type(group_obj)))
        return False

    if type(msg) is not dict:
        print("msg is not dict type={}".format(type(msg)))
        return False

    # print(group_obj.keys)
    if 'UserName' not in group_obj:
        print("group_obj is not has {}".format('UserName'))
        return False
    
    if 'FromUserName' not in msg:
        print("msg is not has {}".format('FromUserName'))
        return False

    from_name=msg['FromUserName']
    g_name=group_obj['UserName']
    if from_name in g_name and (len(from_name) == len(g_name)):
        return True
    return False

@itchat.msg_register(TEXT,isGroupChat=True)
def do_group_text_reply(msg):
    global zw_image_type
    if isGroupMessage(msg,zw_group_obj):
        print(msg)
        text=msg['Text']
        if type(text) is str:
            if text == ZW_IMAGE_TYPE_INVOICE and not(zw_image_type == ZW_IMAGE_TYPE_INVOICE):
                itchat.send("changed {} to {}".format(zw_image_type,ZW_IMAGE_TYPE_INVOICE),msg['FromUserName'])
                zw_image_type = ZW_IMAGE_TYPE_INVOICE
            if text == ZW_IMAGE_TYPE_NORMAL and not(zw_image_type == ZW_IMAGE_TYPE_NORMAL):
                itchat.send("changed {} to {}".format(zw_image_type,ZW_IMAGE_TYPE_NORMAL),msg['FromUserName'])
                zw_image_type = ZW_IMAGE_TYPE_NORMAL 
    else:
        print("msg is ignore id={},name={},Text={}".format(msg['MsgId'],msg['ActualNickName'],msg['Text']))
    # msg.user.send("{}:{}".format(msg.type,msg.text))

@itchat.msg_register(PICTURE,isGroupChat=True)
def do_group_picture_reply(msg):
    if isGroupMessage(msg,zw_group_obj):
        print(msg)
        fileName='{}_{}_{}'.format(msg['Type'], int(time.time()),msg['FileName'])
        fileDir = get_save_path_pictrue(fileName)
        msg['Text'](fileDir)
        if zw_image_type == ZW_IMAGE_TYPE_INVOICE:
            content=OCRBD.get_image_ocr_vatInvoice(fileDir)
            itchat.send(str(content),msg['FromUserName'])

        if zw_image_type == ZW_IMAGE_TYPE_NORMAL:
            contents=OCRBD.get_image_ocr_path(fileDir)
            content=''.join('{}\n'.format(str(i)) for i in contents)
            itchat.send(content,msg['FromUserName'])

    else:
        print("msg is ignore id={},name={},Text={}".format(msg['MsgId'],msg['ActualNickName'],msg['Text']))

itchat.auto_login(enableCmdQR=2,hotReload=True)

zw_group_obj=itchat.search_chatrooms(name=zw_group_name)[0]
# print(zw_group_obj)
print("zw_group_obj={}".format(zw_group_obj))

itchat.send('Hello, filehelper', toUserName='filehelper')

# friends=itchat.get_friends(update=True)[0:]
# print("first friend")
# print(friends[0])
# for obj in friends:
    # print("NickName({})===>Sex({})==>UniFriend({})".format(obj["NickName"],obj["Sex"],obj['UniFriend']))
    
# itchat.send_msg()
itchat.run(True)
# itchat.logout()
