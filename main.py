from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot

bot = TeleBot("922442502:AAGH0X59pX7HSjH7XJD-uJTdc_2fO9Ptdbs")


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
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Отлично! Тогда давай приступим', reply_markup=None)
    elif call.data == 'b':
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ну что ж. Значит, сейчас разберешься', reply_markup=None)
    else:
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text='Ну все, развезло. А я еще только начал. Вот, держи водички. А я перейду к вопросам.', reply_markup=None)
	


if __name__ == '__main__':
    bot.polling(none_stop=True)