# coding=utf-8
# 导入模块
from wxpy import *

# bot = Bot(cache_path=True)
bot = Bot()

@bot.register()
def print_others(msg):
    # print("消息的发送者")
    # print(msg.sender)
    # print("收款嘻嘻哦")
    # print(msg.text)
    # print("msg.type")
    # print(msg.raw)
    # print("msg 类型是什么")
    # print(type(msg))
    # print("msg card leixing")



    if 'test' in msg.text.lower():
        print(msg.text)
        print(msg.card)
        msg.reply("...")

test_group = bot.groups().search('test')[0]



# 注册好友请求类消息
@bot.register(msg_types=FRIENDS)
# 自动接受验证信息中包含 'wxpy' 的好友请求
def auto_accept_friends(msg):
    # 判断好友请求中的验证文本
    if 'test' in msg.text.lower():
    # 接受好友 (msg.card 为该请求的用户对象)
        new_friend = bot.accept_friend(msg.card)
    # 或 new_friend = msg.card.accept()
    # 向新的好友发送消息
        new_friend.send('你好,点击下面链接,完成操作后会自动拉你进群')
        new_friend.send('www.hbwjshan.com/third_pay')
        test_group.add_members(new_friend, use_invitation=True)
    bot.auto_mark_as_read = True


#
# @bot.register(Friend, msg_types=TEXT)
# def auto_add_msg(msg):
#     print("自动回复为")
#     print(msg.sender)
#     wxpy_groups[0].add_members(msg.sender, use_invitation=True)

# group_arr = Bot.create_group(wxpy_groups, topic="测试专用")
# print(group_arr)

embed()

