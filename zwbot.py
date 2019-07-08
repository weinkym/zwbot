import itchat
from itchat.content import *

zw_group_name='TT123456'
zw_group_obj={}

@itchat.msg_register(TEXT,isGroupChat=True)
def do_group_text_reply(msg):
    FromUserName=msg['FromUserName']
    if 'UserName' not in zw_group_obj.keys:
        print("zw_group_obj is not has UserName")
        return
    g_name=zw_group_obj['UserName']
    # print('g_name={}'.format(g_name))
    # print('msg={}'.format(msg))
    # print('FromUserName={}'.format(FromUserName))
    if FromUserName in g_name:
        print(msg)
    else:
        print("msg is ignore id={},name={},Text={}".format(msg['MsgId'],msg['ActualNickName'],msg['Text']))
    # msg.user.send("{}:{}".format(msg.type,msg.text))

itchat.auto_login(enableCmdQR=2,hotReload=True)

zw_group_obj=itchat.search_chatrooms(name=zw_group_name)[0]
# print(zw_group_obj)

print("zw_group_obj={}".format(zw_group_obj))

friends=itchat.get_friends(update=True)[0:]


# print("first friend")
# print(friends[0])

# for obj in friends:
    # print("NickName({})===>Sex({})==>UniFriend({})".format(obj["NickName"],obj["Sex"],obj['UniFriend']))
    

# itchat.send_msg()
itchat.run(True)
# itchat.logout()
