import telebot
from telebot import types
from classValuteConvert import Exchange, Value_Open_courses
from TOKEN import token

value_open_current = Value_Open_courses()
bot = telebot.TeleBot(token())

keys = {
    f"🇧🇾 БелорусскийРубль": "BYN",
    f"🇺🇸 Доллар": 'USD',
    f"🇪🇺 Евро": 'EUR',
    f"🇨🇳 Юань": 'CNY',
    f"🇷🇺 Рубль": "RUB",
    f"🇹🇷 ЛираТурецкая": "TRY"
}

value_1 = None
value_2 = None
amount_sum = None


@bot.message_handler(commands=['start'])
def handle_start_welcome(message: telebot.types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("💵 Доступные Вам валюты.")
    item2 = types.KeyboardButton("✅ Обмен Валют.")
    item3 = types.KeyboardButton("🆕 Узнать Актуальный курс валют.")
    item4 = types.KeyboardButton("🆘 Помощь!")
    markup.add(item1, item2, item3, item4)
    if message.text == '/start':
        bot.send_message(message.chat.id, f"⭐️ Добро пожаловать в конвектор валют, {message.chat.first_name}! ⭐️",
                         reply_markup=markup)
    else:
        bot.send_message(message.chat.id, "✨ Основное меню", reply_markup=markup)


@bot.message_handler(content_types=['photo', 'document'])
def handle_photo(message: telebot.types.Message):
    bot.send_message(message.chat.id, "Очень Мило!")
    bot.send_sticker(message.chat.id, "CAACAgIAAxkBAAELzs1mBSiC6a7iDghK20aeCiIRY5aEWQACBhUAArDdqUgY5a-GuC48gzQE")
    pass


@bot.message_handler(content_types=['voice'])
def handle_voice(message: telebot.types.Message):
    bot.reply_to(message, "К сожалению, я не умею слушать ваш прекрасный голос 🙃")
    pass


@bot.message_handler(commands=['help'])
def handle_help_comand(message: telebot.types.Message):
    text_help_user = "Для того, чтобы конвертировать валюту вам нужно:\n" \
                     "1.Перейти на кнопочку '✅ Обмен Валют.'\n" \
                     "2.Сначала нажать на валюту, которую хотите перевести.\n" \
                     "3.После указать валюту, НА которую хотите перевести средства\n" \
                     "4.Указать сумму для перевода, и всё!🥰\n" \
                     "\n" \
                     "Список валют можно увидеть по команде - /values или нажать на кнопку '💵 Доступные Вам валюты.'\n" \
                     "Посмотреть акутуальные курсы валют на рубли - /current или нажать на кнопку '🆕 Узнать Актуальный курс валют.'"

    bot.reply_to(message, text_help_user)
    pass


@bot.message_handler(commands=['values'])
def handle_open_value(message: telebot.types.Message):
    Open_value = "Доступные валюты 💵:"
    for key in keys.keys():
        Open_value = "\n".join((Open_value, key,))
    bot.reply_to(message, Open_value)
    pass


@bot.message_handler(commands=['current'])
def handle_current_currencies(message: telebot.types.Message):
    current = f"""
    📣Актуальный Курс валют:
        Белорусский Рубль - {value_open_current.BYN_to_RUB()}РУБ.
        Доллар - {value_open_current.USD_to_RUB()}РУБ.
        Евро - {value_open_current.EUR_to_RUB()}РУБ. 
        Юань - {value_open_current.CNY_to_RUB()} РУБ.
        Лира Турецкая - {value_open_current.TRY_to_RUB()}РУБ.

"""

    bot.reply_to(message, current)


@bot.message_handler(content_types=['text'], )
def bot_items(message: telebot.types.Message):
    if message.text == "🆘 Помощь!":
        return handle_help_comand(message)
    elif message.text == "💵 Доступные Вам валюты.":
        handle_open_value(message)
    elif message.text == "🔙 Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("💵 Доступные Вам валюты.")
        item2 = types.KeyboardButton("✅ Обмен Валют.")
        item3 = types.KeyboardButton("🆕 Узнать Актуальный курс валют.")
        item4 = types.KeyboardButton("🆘 Помощь!")
        markup.add(item1, item2, item3, item4)
        bot.reply_to(message, "✨ Основное меню", reply_markup=markup)
    elif message.text == "🆕 Узнать Актуальный курс валют.":
        handle_current_currencies(message)
    elif message.text == "✅ Обмен Валют.":
        start_exchange(message)
    else:
        bot.send_message(message.chat.id, f"❓ Ой, я такого не знают.")


def start_exchange(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        telebot.types.KeyboardButton("🇺🇸 USD"),
        telebot.types.KeyboardButton("🇪🇺 EUR"),
        telebot.types.KeyboardButton("🇨🇳 CNY"),
        telebot.types.KeyboardButton("🇹🇷 TRY"),
        telebot.types.KeyboardButton("🇷🇺 RUB"),
        telebot.types.KeyboardButton("🇧🇾 BYN"),
        telebot.types.KeyboardButton("🔙 Назад")
    ]
    markup.add(*buttons)

    bot.send_message(message.chat.id, "💸Выберите валюту для перевода.", reply_markup=markup)
    bot.register_next_step_handler(message, select_first_currency)


def select_first_currency(message):
    global valute_1

    valute_1 = message.text
    if message.text == "🔙 Назад":
        return handle_start_welcome(message)
    if valute_1 not in ["🇺🇸 USD", "🇪🇺 EUR", "🇨🇳 CNY", "🇹🇷 TRY", "🇷🇺 RUB", "🇧🇾 BYN"]:
        bot.send_message(message.chat.id, "❌ Неопознанная валюта, выберите другую!")
        return bot.register_next_step_handler(message, start_exchange)

    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(*[
        telebot.types.KeyboardButton("🇺🇸 USD"),
        telebot.types.KeyboardButton("🇪🇺 EUR"),
        telebot.types.KeyboardButton("🇨🇳 CNY"),
        telebot.types.KeyboardButton("🇹🇷 TRY"),
        telebot.types.KeyboardButton("🇷🇺 RUB"),
        telebot.types.KeyboardButton("🇧🇾 BYN")
    ], telebot.types.KeyboardButton("🔙 Назад"))

    bot.send_message(message.chat.id, "💸Выберите в какую валюту желаете перевести.", reply_markup=markup)
    bot.register_next_step_handler(message, select_second_currency)


def select_second_currency(message):
    global valute_2
    global amount_sum
    if message.text == "🔙 Назад":
        return start_exchange(message)

    valute_2 = message.text
    if valute_2 not in ["🇺🇸 USD", "🇪🇺 EUR", "🇨🇳 CNY", "🇹🇷 TRY", "🇷🇺 RUB", "🇧🇾 BYN"]:
        bot.send_message(message.chat.id, "❌ Неопознанная валюта, выберите другую!")
        return bot.register_next_step_handler(message, select_first_currency)
    bot.send_message(message.chat.id, "💰 Введите Вашу сумму:")
    bot.register_next_step_handler(message, get_amount)


def get_amount(message):
    global amount_sum
    if message.text == "🔙 Назад":
        bot.send_message(message.chat.id, "💸Выберите в какую валюту желаете перевести.")
        return bot.register_next_step_handler(message, select_second_currency)

    amount_sum = message.text

    if len(amount_sum) >= 7:
        bot.send_message(message.chat.id, f"❌ Сумма не может быть больше 1000000 {valute_2[:3]}")
        return handle_start_welcome(message)
    try:
        amount_sum = int(amount_sum)
    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Ошибка конвертации суммы!")
        return bot.register_next_step_handler(message, select_second_currency)

    if amount_sum == int(amount_sum):
        print(True)
    else:
        print(False)
    exchange = Exchange(amount_sum, valute_1[3:], valute_2[3:])
    finaly = exchange.exchange()
    bot.send_message(message.chat.id, f"⚡️ Ваша сумма состовляет = {finaly} {valute_2[:3]}")
    return handle_start_welcome(message)


bot.polling(none_stop=True)
