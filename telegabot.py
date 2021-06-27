from mytoken import token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from glob import glob

import random

# создаём сущность mybot, которая будет получать сообщения
mybot = Updater(token, use_context=True) 
# заставляем mybot опрашивать телеграм по части сообщений



def greet(update, context):
    print('Вижу команду /start')
    update.message.reply_text('Привет, я бот!')

def info(update, context):
    print('Вижу команду /help')
    update.message.reply_text('Я не оказываю помощи и знаю команды /start /help')

def talk_to_me(update, context):
    user_text = update.message.text        
    print(f'Получен текст: {user_text}') 
    if '?' in user_text:
        update.message.reply_text(f'Не знаю!!')
    else:
        update.message.reply_text(f'Ты написал: {user_text}!')
    
def img(update, context):
    if not context.args:
        imgs = glob('img\*')
        if imgs:    
            img = random.choice(imgs)
            id = update.effective_chat.id
            ph = open(img, 'rb')
            context.bot.send_photo(chat_id=id, photo=ph)
            ph.close()
        else:
            update.message.reply_text(f'Нужно найти вора картинок')
        return
    for elem in context.args:
        imgs = glob(f'img\*{elem}*')
        if imgs:    
            img = random.choice(imgs)
            id = update.effective_chat.id
            ph = open(img, 'rb')
            context.bot.send_photo(chat_id=id, photo=ph)
            ph.close()
            break
    else:
        update.message.reply_text(f'Таких картинок нету')



mybot.dispatcher.add_handler(CommandHandler('start', greet))
mybot.dispatcher.add_handler(CommandHandler('help', info))
mybot.dispatcher.add_handler(CommandHandler('img', img))
# связываем функцию talk_to_me с исключительно текстовыми сообщениями
mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))
print('Я запустился!')



mybot.start_polling()
# запускаем обработчик
mybot.idle()