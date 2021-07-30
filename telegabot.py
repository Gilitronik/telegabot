from mytoken import token
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import ReplyKeyboardMarkup, replymarkup
from glob import glob
from emoji import emojize

import random

# создаём сущность mybot, которая будет получать сообщения
mybot = Updater(token, use_context=True) 
# заставляем mybot опрашивать телеграм по части сообщений

ne_alphavit = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
smiles = [':smile:', ':smiley:', ':laughing:', ':hugging_face:', ':zany_face:']
yasherica_smiles = [':turtle:', ':lizard:', ':crocodile:', ':snake:', ':sauropod:', ':t-rex:']
klava = [
    ['/start', '/help'],
    ['/img'],
    ['/is_word', '/call_me']
    ]

def give_knopka(update, context):
    update.message.reply_text('fggjhfgjgjh', reply_markup=ReplyKeyboardMarkup(klava))

def start(update, context):
    print('Вижу команду /start')
    if 'name' in context.user_data:
        iff = context.user_data['name']
    else:
        iff = update.message.from_user.name
    update.message.reply_text(f'Привет {iff}, я бот! ' + emojize(random.choice(smiles), use_aliases=True))
    #for x in smiles:
    #   update.message.reply_text(emojize(x, use_aliases=True))

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
    arr = context.args
    if arr == []:
        arr.append('')
    for elem in arr:
        imgs = glob(f'img\*{elem}*')
        if imgs:
            img = random.choice(imgs)
            id = update.effective_chat.id
            ph = open(img, 'rb')
            context.bot.send_photo(chat_id=id, photo=ph)
            ph.close()
            update.message.reply_text(emojize(random.choice(yasherica_smiles), use_aliases=True))


def is_word(update, context):
    arr = context.args
    for i in arr:
        for j in i:
            if j not in ne_alphavit:
                update.message.reply_text(f'Слова {i} нет')
                break
        else:
            update.message.reply_text(f'Слово {i} возмножно')


def call_me(update, context):
    a = context.args
    a = ' '.join(a)
    update.message.reply_text(f'Я буду звать тебя {a}')
    context.user_data['name'] = a

mybot.dispatcher.add_handler(CommandHandler('give_knopka', give_knopka))
mybot.dispatcher.add_handler(CommandHandler('start', start))
mybot.dispatcher.add_handler(CommandHandler('help', info))
mybot.dispatcher.add_handler(CommandHandler('img', img))
mybot.dispatcher.add_handler(CommandHandler('is_word', is_word))
mybot.dispatcher.add_handler(CommandHandler('call_me', call_me))
# связываем функцию talk_to_me с исключительно текстовыми сообщениями
mybot.dispatcher.add_handler(MessageHandler(Filters.text, talk_to_me))
print('Я запустился!')


mybot.start_polling()
# запускаем обработчик
mybot.idle()