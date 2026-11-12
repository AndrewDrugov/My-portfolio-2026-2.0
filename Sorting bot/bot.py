import telebot
from telebot.types import Message, ReplyKeyboardMarkup
from cfg import cfg
from Sort.sorting import selection_sort, bingo, blinchiki
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

bot = telebot.TeleBot(cfg)
user_state = {}
SORTS = {'Sort choice':selection_sort,
         'Bingo':bingo,
         'Blinchiki':blinchiki}

def pars_input(text):
    text = text.strip()
    if text.startswith('['):
        text = text.replace('[','').replace('[','')
        numbers = list(map(int, text.replace(',','').split()))
    else:
        numbers = list(map(int, text.split()))
    return numbers

@bot.message_handler(commands=['start'])
def start(msg: Message):
    bot.send_message(msg.chat.id, 'Welcome to Module 4 Bot')
    kb = ReplyKeyboardMarkup(True, True)
    kb.row('Sort choice')
    kb.row('Bingo')
    kb.row('Blinchiki')
    bot.send_message(msg.chat.id, 'Chose one variant of sorting', reply_markup=kb)

@bot.message_handler(content_types=['text'])
def start_handler(msg: Message):
    if msg.text in SORTS:
        bot.send_message(msg.chat.id,
                    f"Chose: {msg.text}\n\nEnter numbers with one of the variants:\n"
                         f"• Space: 5 3 -1 8 2\n"
                         f"• List: [5, 3, -1, 8, 2]")
        user_state[msg.chat.id]=msg.text
    elif msg.chat.id in user_state:
        numbers = pars_input(text=f'{msg.text}')
        sort_name = user_state[msg.chat.id]
        sort_func = SORTS[sort_name]
        result = sort_func(numbers)
        bot.send_message(msg.chat.id, f'result:{result}OMG🤯' )




bot.infinity_polling()
