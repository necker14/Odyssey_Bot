import os

import telebot

import config

TOKEN = os.environ.get('TOKEN') or config.TGBOT_TOKEN
bot = telebot.TeleBot(TOKEN)
logger = config.setup_log()


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_chat_action(message.chat.id, 'typing')
    bot.send_message(message.chat.id, '欢迎使用Odyssey_Bot 路易'
                                      '输入 /help 可以获得更多帮助',
                     '输入 /register 可以注册账号',
                     '输入 /status 可以查看服务器状态',
                     '输入 /reset 可以重置个人账号密码',
                     '输入 /delete 可以删除个人账号', )


if __name__ == '__main__':
    try:
        bot.polling(none_stop=True, timeout=600)
    except Exception as e:
        logger.exception("__main__ Telegram Bot运行异常，抛出信息:{}".format(e))
