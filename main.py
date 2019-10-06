from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from telebot import TeleBot
import config
import re

bot = TeleBot(config.token)

user_dict = {}


class User:

    def __init__(self, name):
        self.name = name
        self.surname = None
        self.second_name = None
        self.data_birth = None
        self.country = None
        self.city = None
        self.education = None
        self.work = None # выбранная профессия(пункт 8)
        self.math = None
        self.knowledge_web = None
        self.target = None
        self.knowledge_it = None
        self.experience = None
        self.reason = None


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
        bot.send_message(call.message.chat.id, 'Превосходно! Я тоже не люблю долго ждать.')
    elif call.data == 'b':
        bot.send_message(call.message.chat.id, 'НЕТ??? Ну чтож, тогда продолжай сидеть и ждать у моря погоды. Можешь своими делами заняться. Ой, погоди, так у тебя же наручники на руках Наверно, тебе будет не очень удобно')
        return
    else:
        bot.send_message(call.message.chat.id, 'Ага, не любишь такие шутки. Принял, давай хотя бы сниму наручники. В следующий раз буду умнее.')
    msg = bot.reply_to(call.message, 'Ты там писать то сможешь? Надеюсь, что да. Прежде всего мне нужно знать, как называть тебя. Скажи мне только своё имя.')
    bot.register_next_step_handler(msg, process_name_step)



def process_name_step(message):
    try:
        chat_id = message.chat.id
        name = message.text
        user = User(name)
        user_dict[chat_id] = user
        msg = bot.reply_to(message, 'Прогресс, {}. Теперь мне нужна твоя фамилия'.format(name))
        # bot.register_next_step_handler(msg, process_surname_step)
        bot.register_next_step_handler(msg, process_education_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_surname_step(message):
    try:
        chat_id = message.chat.id
        surname = message.text
        user = user_dict[chat_id]
        user.surname = surname
        msg = bot.reply_to(message, 'Есть отчество? Тогда оно мне тоже пригодится. Если нет, напиши просто “–“ (Без кавычек)')
        bot.register_next_step_handler(msg, process_secondname_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_secondname_step(message):
    try:
        chat_id = message.chat.id
        secondname = message.text
        user = user_dict[chat_id]
        if not secondname == '-':
            user.secondname = secondname
        else:
            user.secondname = ''
        msg = bot.reply_to(message, 'Отлично! Теперь посмотрим, насколько ты старик. Укажи свою дату рождения в формате ДД.ММ.ГГ')
        bot.register_next_step_handler(msg, process_data_birth_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_data_birth_step(message):
    try:
        chat_id = message.chat.id
        data_birth = message.text
        user = user_dict[chat_id]
        for i in data_birth.split('.'):
            if not i.isdigit():
                msg = bot.reply_to(message, 'Неверный ввод, попробуй ещё раз)')
                bot.register_next_step_handler(msg, process_data_birth_step)
                return
        user.data_birth = data_birth
        msg = bot.reply_to(message, 'Слушай, а ты, собственно, откуда? Напиши страну, в которой ты живёшь?')
        bot.register_next_step_handler(msg, process_country_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_country_step(message):
    try:
        chat_id = message.chat.id
        country = message.text
        user = user_dict[chat_id]
        user.country = country
        msg = bot.reply_to(message, 'Ага, {} значит. Давай чуть подробнее, а то на карте это довольно большая точка. Напиши город, в котором проживаешь'.format(country))
        bot.register_next_step_handler(msg, process_city_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_city_step(message):
    try:
        chat_id = message.chat.id
        city = message.text
        user = user_dict[chat_id]
        user.city = city
        msg = bot.reply_to(message, 'Уже неплохо. Как видишь, это не так уж и сложно. Перейдём на более профессиональную тему. У тебя есть высшее образование?  (Да/Нет)')
        bot.register_next_step_handler(msg, process_education_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_education_step(message):
    try:
        chat_id = message.chat.id
        education = message.text
        user = user_dict[chat_id]
        user.education = education

        markup = InlineKeyboardMarkup()
        programmer = InlineKeyboardButton(text='Программист', callback_data='programmer')
        marketer   = InlineKeyboardButton(text='Маркетолог', callback_data='marketer')
        designer   = InlineKeyboardButton(text='Дизайнер', callback_data='designer')
        manager    = InlineKeyboardButton(text='Менеджер по продажам', callback_data='manager')
        other      = InlineKeyboardButton(text='Другое', callback_data='other')
        markup.add(programmer, marketer, designer, manager, other)

        msg = bot.reply_to(message, 'Теперь посмотрим, какой именно потенциальной угрозой ты являешься для общества. Мне нужно знать, кем ты являешься по образованию'
                , reply_markup=markup)
        bot.register_next_step_handler(msg, process_education_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


@bot.callback_query_handler(func=lambda call: call.data in ('programmer', 'marketer', 'designer', 'manager', 'other'))
def process_work_step(call):
    print(call.text)
    try:
        if call.data == 'other':
            msg = bot.reply_to(call.message, 'Я вижу, ты не простой орешек. Ну тогда отвечай сам, что это там за такая профессия.')
            bot.register_next_step_handler(msg, process_other_work_step)
        else:
            chat_id = call.message.chat.id
            print('Yep')
            work = call.message.text
            user = user_dict[chat_id]
            user.work = education
            msg = bot.reply_to(call.message, 'Теперь давай углубимся в твои знания. Как у тебя дела с математикой? Любишь ли ты этот предмет? Оцени свою искренние чувства по пятибалльной шкале, где 5 – люблю и уважаю, а 1 – терпеть не могу.')
            bot.register_next_step_handler(msg, process_math_step)
    except Exception as e:
        bot.reply_to(call.message, 'oops')


def process_other_work_step(message):
    try:
        chat_id = message.chat.id
        work = message.text
        user = user_dict[chat_id]
        user.work = work
        msg = bot.reply_to(message, 'Теперь давай углубимся в твои знания. Как у тебя дела с математикой? Любишь ли ты этот предмет? Оцени свою искренние чувства по пятибалльной шкале, где 5 – люблю и уважаю, а 1 – терпеть не могу.')
        bot.register_next_step_handler(msg, process_math_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


def process_math_step(message):
    try:
        chat_id = message.chat.id
        city = message.text
        user = user_dict[chat_id]
        user.city = city
        msg = bot.reply_to(message, 'Меня радуют твои успехи. Не устал? Тогда давай посмотрим, с какими знаниями IT ты пришёл ко мне. Для начала очевидное. Тебе известно понятия Frontend и Backend. Ты понимаешь их отличия? Если не понимаешь, не молчи, я расскажу тебе об этом.')
        bot.register_next_step_handler(msg, process_education_step)
    except Exception as e:
        bot.reply_to(message, 'oops')


if __name__ == '__main__':
    bot.polling(none_stop=True)
