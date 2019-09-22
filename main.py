from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot
import config

bot = TeleBot(config.token)

user_dict = {}


class User:

    def __init__(self, name):
        self.name = name


@bot.message_handler(commands=['start'])
def start_message(message):

    keyboard = InlineKeyboardMarkup()
    yes_bottom = InlineKeyboardButton (text='Да' , callback_data='a')
    no_bottom = InlineKeyboardButton (text= "Нет", callback_data='b')
    some_bottom = InlineKeyboardButton (text= "Ты в каком это тоне со мной разговариваешь???", callback_data='c')
    
    keyboard.add (yes_bottom, no_bottom,)
    keyboard.add (some_bottom) 

    bot.send_message(message.chat.id, 'Ну здравствуй! Лампа не сильно в глаза светит? Наручники не трут? Ну ничего, привыкнешь.\n Я бот - специалист по извлечению резюме из таких как ты. И вопросы здесь задаю я. \n Это понятно?', reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ('a', 'b', 'c'))
def callback_inline(call):
    if call.data == 'a':
        msg = bot.reply_to(call.message, 'Отлично! Тогда давай приступим, как тебя зовут?')
    elif call.data == 'b':
        msg = bot.reply_to(call.message, 'Ну чтож, значит сейчас разберешься. Как тебя зовут?')
    else:
        msg = bot.reply_to(call.message, 'Ну все, развезло. А я еще только начал. Вот, держи водички. А я перейду к вопросам. Как тебя зовут?')
    bot.register_next_step_handler(msg, process_name_step)


def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        bot.send_message(chat_id, 'Nice to meet you ' + user.name + '\nGrats!')
    except Exception as e:
        bot.reply_to(message, 'oops')
	


if __name__ == '__main__':
    bot.polling(none_stop=True)
