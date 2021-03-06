# -*- coding:utf-8 -*-
'''
creation time: 2020-6-26
last_modify: 2020-10-24
'''

def Uptime(bot, message):

    chat_id = message["chat"]["id"]
    message_id = message["message_id"]
    text = message["text"]
    prefix = "uptime"

    if text[1:len(prefix)+1] == prefix:
        time_format = bot.uptime(time_format="format")
        time_second = bot.uptime(time_format="second")
        response_times = bot.response_times()
        status = bot.sendChatAction(chat_id, "typing")
        inlineKeyboard = [
                    [
                        {"text": "详细信息", "url": "https://t.me/teelebot_channel/6"}
                    ]
                ]
        reply_markup = {
            "inline_keyboard": inlineKeyboard
        }
        msg = "感谢您的关心 <b>(￣ε ￣)</b> %0A%0A我已经运行 <b>" +  str(time_second) + "</b> 秒%0A" +\
                "即：<b>" + str(time_format) + "</b>%0A%0A" +\
                "在此期间累计响应指令 <b>" + str(response_times) + "</b> 次%0A%0A"
        status = bot.sendMessage(chat_id=chat_id, text=msg, parse_mode="HTML", reply_to_message_id=message_id, reply_markup=reply_markup)
        bot.message_deletor(15, chat_id, status["message_id"])