# from __future__ import unicode_literals
# from threading import Timer
# import requests
# import wxpy
#
# bot = None
#
#
# def get_news():
#     url = 'http://open.iciba.com/dsapi'
#     r = requests.get(url)
#     print(r.json())
#     contents = r.json()['content']
#     translation = r.json()['translation']
#     return contents, translation
#
#
# def login_wechat():
#     global bot
#     bot = wxpy.Bot()
#
#
# def send_msg():
#     if None == bot:
#         login_wechat()
#     try:
#         my_friend = bot.friends().serach(u'弟弟')[0]
#         my_friend.send(get_news()[0])
#         my_friend.send(get_news()[1][5:])
#         my_friend.send(u'咦？我是机器人')
#         t = Timer(5, send_msg)
#     except:
#         print(u'失败')
#
#
# if __name__ == '__main__':
#     send_msg()
#     print(get_news()[0])

import wxpy


def send():
    bot = wxpy.Bot()
    guys = bot.friends()
    for guy in guys:
        print(guy)


if __name__ == '__main__':
    send()
