import messages
import requests
import sqlite3
import telegram
import logging
from telegram import ext
from functools import wraps

updater = ext.Updater('<TOKEN>')
dp = updater.dispatcher


def authenticated(func):
    @wraps(func)
    def wrapped(bot, update, *args, **kwargs):
        conn = sqlite3.connect('content.sqlite')
        cur = conn.cursor()
        if len(cur.execute('''SELECT id FROM userdata WHERE id = ?        
            ''', (update.message.from_user.id,)).fetchall()) > 0:
            return func(bot, update, *args, **kwargs)
        bot.send_message(chat_id=update.message.chat_id,
                         text="Silahkan Registrasi Terlebih dahulu : \n/start",
                         parse_mode=telegram.ParseMode.HTML)
        conn.commit()
        conn.close()
    return wrapped


#### SQLITE BRANCH ####
def loadDB():
    # Creates SQLite database to store info.
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    cur.executescript('''CREATE TABLE IF NOT EXISTS userdata
    (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE, 
    firstname TEXT, 
    Nama TEXT,
    NIM_or_NIP TEXT,
    EMAIL TEXT,
    Status TEXT DEFAULT 'Dosen');'''
                      )
    conn.commit()
    conn.close()


def checkUser(update, user_data):
    # Checks if user has visited the bot before
    # If yes, load data of user
    # If no, then create a new entry in database
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    if len(cur.execute('''SELECT id FROM userdata WHERE id = ?        
            ''', (update.message.from_user.id,)).fetchall()) > 0:
        c = cur.execute('''SELECT Nama FROM userdata WHERE id = ?''',
                        (update.message.from_user.id,)).fetchone()
        user_data['Nama'] = c[0]
        c = cur.execute('''SELECT NIM_or_NIP FROM userdata WHERE id = ?''',
                        (update.message.from_user.id,)).fetchone()
        user_data['NIM_or_NIP'] = c[0]
        c = cur.execute('''SELECT Email FROM userdata WHERE id = ?''',
                        (update.message.from_user.id,)).fetchone()
        user_data['Email'] = c[0]
        c = cur.execute('''SELECT Status FROM userdata WHERE id = ?''',
                        (update.message.from_user.id,)).fetchone()
        user_data['Status'] = c[0]
        print("Pass user")
    else:
        cur.execute('''INSERT OR IGNORE INTO userdata (id, firstname) VALUES (?, ?)''',
                    (update.message.from_user.id, update.message.from_user.first_name,))
        print("New user")
    conn.commit()
    conn.close()


def updateUser(category, text, update):
    # Updates user info as inputted.
    conn = sqlite3.connect('content.sqlite')
    cur = conn.cursor()
    conn.text_factory = str
    # Update SQLite database as needed.
    cur.execute('''UPDATE OR IGNORE userdata SET {} = ? WHERE id = ?'''.format(category),
                (text, update.message.from_user.id,))
    conn.commit()
    conn.close()


#### Python Telegram Bot Branch ####
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

CHOOSING, TYPING_REPLY, TYPING_CHOICE = range(3)

reply_keyboard = [['Nama', 'NIM_or_NIP'],
                  ['Email'],
                  ['Done']]
markup = telegram.ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)


def facts_to_str(user_data):
    facts = list()

    for key, value in user_data.items():
        facts.append('{} - {}'.format(key, value))

    return "\n".join(facts).join(['\n', '\n'])


def regular_choice(bot, update, user_data):
    text = update.message.text
    user_data['choice'] = text
    update.message.reply_text(
        'Silahkan masukkan {} anda'.format(text.lower()))
    return TYPING_REPLY


def received_information(bot, update, user_data):
    text = update.message.text
    category = user_data['choice']
    user_data[category] = text
    updateUser(category, text, update)
    del user_data['choice']

    update.message.reply_text("Data anda :"
                              "{}"
                              "Silahkan isi data lainnya".format(
                                  facts_to_str(user_data)), reply_markup=markup)
    return CHOOSING


def done(bot, update, user_data):
    if 'choice' in user_data:
        del user_data['choice']

    update.message.reply_text("Anda sudah terdaftar dengan data : "
                              "{}"
                              "Anda sudah bisa mengakses Layanan yang sudah disediakan"
                              " di /home"
                              "\nSelamat Menikmati".format(facts_to_str(user_data)))

    user_data.clear()
    return ext.ConversationHandler.END


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


###Layanan Informasi###
# Start Handler
def start(bot, update, user_data):
    reply_keyboard = [['Nama', 'NIM_or_NIP'],
                      ['Email'],
                      ['Done']]
    markup = telegram.ReplyKeyboardMarkup(
        reply_keyboard, one_time_keyboard=True)
    update.message.reply_text(messages.start.format(
        first_name=update.message.from_user.first_name),
        parse_mode=telegram.ParseMode.HTML,
        reply_markup=markup)
    checkUser(update, user_data)
    return CHOOSING


# Home Handler
@authenticated
def home(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=messages.home,
                     parse_mode=telegram.ParseMode.HTML)
    # checkUser(update, user_data)


# Handler Layanan PKL
@authenticated
def layananpkl(bot, update):
    button_list = [
        telegram.InlineKeyboardButton(
            'Pendaftaran', callback_data='pendaftaranpkl'),
        telegram.InlineKeyboardButton(
            'Seminar', callback_data='seminarpkl'),
        telegram.InlineKeyboardButton(
            'Pembukuan', callback_data='pembukuanpkl'),
    ]
    reply_markup = telegram.InlineKeyboardMarkup(
        build_menu(button_list, n_cols=2))
    bot.send_message(chat_id=update.message.chat_id,
                     text='Pilih Informasi Terkait Praktek Kerja Lapangan :',
                     reply_markup=reply_markup)


# Handler Layanan TA
@authenticated
def layananta(bot, update):
    button_list = [
        telegram.InlineKeyboardButton('Tugas Akhir 1', callback_data='ta1'),
        telegram.InlineKeyboardButton('Tugas Akhir 2', callback_data='ta2'),
    ]
    reply_markup = telegram.InlineKeyboardMarkup(
        build_menu(button_list, n_cols=1))
    bot.send_message(chat_id=update.message.chat_id,
                     text='Pilih Tugas Akhir :',
                     reply_markup=reply_markup)


# Handler Tata Tulis
@authenticated
def tatatulis(bot, update):
    button_list = [
        telegram.InlineKeyboardButton(
            'Tata Tulis Laporan PKL', callback_data='tatatulispkl'),
        telegram.InlineKeyboardButton(
            'Tata Tulis Laporan TA', callback_data='tatatulista'),
    ]
    reply_markup = telegram.InlineKeyboardMarkup(
        build_menu(button_list, n_cols=1))
    bot.send_message(chat_id=update.message.chat_id,
                     text='Pilih Informasi Terkait Tata Tulis Penulisan Laporan :',
                     reply_markup=reply_markup)


# UnknownCommand Handler
def unknowncommand(bot, update):
    bot.send_message(chat_id=update.message.chat_id,
                     text=messages.unknown,
                     parse_mode=telegram.ParseMode.HTML)


####Handler####
# Layout Menu Button
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


# Handler Button
def button(bot, update):
    query = update.callback_query

    # views PKL Menu
    if query.data == 'pendaftaranpkl':
        bot.send_message(text=messages.pendaftaranpkl,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'seminarpkl':
        bot.send_message(text=messages.seminarpkl,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'pembukuanpkl':
        bot.send_message(text=messages.pembukuanpkl,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)

    # views TA Menu
    if query.data == 'ta1':
        button_list = [
            telegram.InlineKeyboardButton(
                'Pendaftaran', callback_data='pendaftaranta1'),
            telegram.InlineKeyboardButton(
                'Seminar', callback_data='seminarta1'),
            telegram.InlineKeyboardButton(
                'Pembukuan', callback_data='pembukuanta1'),
        ]
        reply_markup = telegram.InlineKeyboardMarkup(
            build_menu(button_list, n_cols=2))
        bot.send_message(chat_id=query.message.chat_id,
                         text='Pilih Informasi Tugas Akhir 1 :',
                         reply_markup=reply_markup)
    if query.data == 'ta2':
        button_list = [
            telegram.InlineKeyboardButton(
                'Pendaftaran', callback_data='pendaftaranta2'),
            telegram.InlineKeyboardButton(
                'Seminar', callback_data='seminarta2'),
            telegram.InlineKeyboardButton(
                'Pembukuan', callback_data='pembukuanta2'),
        ]
        reply_markup = telegram.InlineKeyboardMarkup(
            build_menu(button_list, n_cols=2))
        bot.send_message(chat_id=query.message.chat_id,
                         text='Pilih Informasi Terkait Tugas Akhir 2 :',
                         reply_markup=reply_markup)

    # views TA1 Menu
    if query.data == 'pendaftaranta1':
        bot.send_message(text=messages.pendaftaranta1,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'seminarta1':
        bot.send_message(text=messages.seminarta1,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'pembukuanta1':
        bot.send_message(text=messages.pembukuanta1,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)

    # views TA2 Menu
    if query.data == 'pendaftaranta2':
        bot.send_message(text=messages.pendaftaranta2,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'seminarta2':
        bot.send_message(text=messages.seminarta2,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'pembukuanta2':
        bot.send_message(text=messages.pembukuanta2,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)

    # views Tata Tulis Menu
    if query.data == 'tatatulispkl':
        bot.send_message(text=messages.tatatulispkl,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)
    if query.data == 'tatatulista':
        bot.send_message(text=messages.tatatulista,
                         chat_id=query.message.chat_id,
                         message_id=query.message.message_id,
                         parse_mode=telegram.ParseMode.HTML)


def main():
    print("Connection to Telegram established; starting bot.")

    conv_handler = ext.ConversationHandler(
        entry_points=[ext.CommandHandler('start', start, pass_user_data=True)],
        states={
            CHOOSING: [ext.RegexHandler(
                '^(Nama|NIM_or_NIP|Email)$', regular_choice, pass_user_data=True),
            ],
            TYPING_CHOICE: [ext.MessageHandler(
                ext.Filters.text, regular_choice, pass_user_data=True),
            ],
            TYPING_REPLY: [ext.MessageHandler(
                ext.Filters.text, received_information, pass_user_data=True),
            ],
        },
        fallbacks=[ext.RegexHandler('^Done$', done, pass_user_data=True)]
    )

    dp.add_handler(conv_handler)

    # log all errors
    dp.add_error_handler(error)

    # Start command
    # dp.add_handler(ext.CommandHandler(
    #     ('start'), start))

    # Home command
    dp.add_handler(ext.CommandHandler(
        ('home'), home))

    # Tata Tulis PKL dan TA
    dp.add_handler(ext.CommandHandler(
        ('tatatulis'), tatatulis))

    # Layanan TA
    dp.add_handler(ext.CommandHandler(
        ('layananta'), layananta))

    # Layanan PKL
    dp.add_handler(ext.CommandHandler(
        ('layananpkl'), layananpkl))

    # Button Handler
    dp.add_handler(ext.CallbackQueryHandler(button))

    # Filter Command
    dp.add_handler(ext.MessageHandler(
        (ext.Filters.command), unknowncommand))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    loadDB()
    main()
