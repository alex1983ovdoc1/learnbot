# импорт нужных компонентов
from glob import glob
import logging
from random import choice

from emoji import emojize
import telegram
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram.ext.callbackcontext import CallbackContext
# from telegram.ext.filters import Filters
from telegram.update import Update

import settings123



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

bot = telegram.Bot(settings123.API_KEY)
user_data = {}
# user_data['emo'] = ''
# user_data['emo'] = emojize(choice(settings123.USER_EMOJI))

def greet_user(update: Update, context: CallbackContext):
	text = 'Command: /start'
	print('--------------')
	print(text)
	print('--------------')
	logging.info(text)
	# update.message.reply_text(text)
	# emo = emojize(choice(settings123.USER_EMOJI))
	# user_data['emo'] = emo
	# bot.send_message(chat_id=update.message.chat.id, text = f'Hello {emo}')
	
	# my_keyboard = ReplyKeyboardMarkup([['/start', '/cat']])
	# contact_button = KeyboardButton('Send contacts', request_contact=True)
	# location_button = KeyboardButton('Send location', request_location=True)
	# my_keyboard = ReplyKeyboardMarkup(
	# 	[
	# 	['/start', 'Send a cat', 'Change avatar'],
	# 	[contact_button, location_button]
	# 	])
	# bot.send_message(chat_id=update.message.chat.id, text =f'Hello {emo}', reply_markup = my_keyboard)
	# user_data['emo'] = emo
	# emo = get_user_emo(user_data)
	bot.send_message(chat_id=update.message.chat.id, text =f'Hello {get_user_emo(user_data)}', reply_markup = get_keyboard())
	# update.message.reply_text(f'Hello {emo}', reply_markup = my_keyboard)
	bot.send_message(chat_id=update.message.chat.id, text = "Please write:\
	\n -/start\
	\n -/cat\
	\n -/any_text\
	\n -/planet")
	# update.message.reply_text(
    #     "Please write:\
	# \n -/start\
	# \n -/cat\
	# \n -/any_text\
	# \n -/planet")
	
	
def talk_to_me(update: Update, context: CallbackContext):
	user_text = update.message.text
	print('+++++++++++++++')
	# text_print = f'Message User: {user_text}'
	print(user_data)
	emo = get_user_emo(user_data)
	text_print = f'Hello {update.message.chat.first_name} {emo}! You wroute: {user_text}'
	print('--------------')
	print(text_print)
	print('--------------')
	# print(update.message)
	logging.info(f'User:{update.message.chat.first_name},\
	Chat id:{update.message.chat.id},\
	Message:{update.message.text}')
	# update.message.reply_text(text_print)
	bot.send_message(chat_id=update.message.chat.id, text = text_print, reply_markup = get_keyboard())


def planet_list(update: Update, context: CallbackContext):
	# update.message.reply_text(
    #     "Please select object:\
	# \n -/Sun\n -/Moon\n -/Mercury\n -/Venus\n -/Mars\n -/Jupiter\n -/Saturn\n -/Uranus\n -/Neptune\n -/Pluto")
	bot.send_message(chat_id=update.message.chat.id, text="Please select object:\
	\n -/Sun\n -/Moon\n -/Mercury\n -/Venus\n -/Mars\n -/Jupiter\n -/Saturn\n -/Uranus\n -/Neptune\n -/Pluto", reply_markup = get_keyboard())
	logging.info('Command: /planet')


def send_cat_picture(update: Update, context: CallbackContext):
# def send_cat_picture(bot, update):
	# bot = telegram.Bot(settings123.API_KEY)
	logging.info('Command: /cat')
	bot.send_message(chat_id=update.message.chat.id, text="From Telegram Bot", reply_markup = get_keyboard())
	cat_list = glob('images\cat*.jp*g')
	cat_pic = choice(cat_list)
	print(cat_pic)
	bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))
	


def planet_user(update: Update, context: CallbackContext):
	import planet_object
	# print(planet_object.planet1)
	Message_pl = update.message.text
	# print(Message_pl)
	select_planet=Message_pl.replace('/','')
	# print(select_planet)
	select_date = planet_object.time_in
	select_coordinat = planet_object.planet1[select_planet]
	print('--------------')
	print(f'Planet	: {select_planet}')
	print(f'Date	: {select_date}')
	print(f'Location: {select_coordinat}')
	print('--------------')
	# update.message.reply_text(\
	# 	f' Select planet\t\t\t\t\t\t: \t"{select_planet}"\
	# 	\nToday date\t\t\t\t\t\t\t\t\t: \t"{select_date}"\
	# 	\nLocation planet: \t"{select_coordinat}" 		')
	bot.send_message(chat_id=update.message.chat.id, text=\
		f' Select planet\t\t\t\t\t\t: \t"{select_planet}"\
		\nToday date\t\t\t\t\t\t\t\t\t: \t"{select_date}"\
		\nLocation planet: \t"{select_coordinat}" 		', reply_markup = get_keyboard())	
	logging.info(f'User:{update.message.chat.first_name},\
	Chat id:{update.message.chat.id},\
	Planet :{select_planet},\
	Date   :{select_date},\
	Location: {select_coordinat} ')


def get_user_emo(user_data):
	if 'emo' in user_data:
		return user_data['emo']
	else:
		user_data['emo'] = emojize(choice(settings123.USER_EMOJI))
		return user_data['emo']


def change_avatar(update: Update, context: CallbackContext):
	if 'emo' in user_data:
		del user_data['emo']
	emo = get_user_emo(user_data)
	bot.send_message(chat_id=update.message.chat.id, text=f'Ready, your avatar: {emo}', reply_markup = get_keyboard())


def get_contact(update: Update, context: CallbackContext):
	print(update.message.contact)
	bot.send_message(chat_id=update.message.chat.id, text=f'Ready: {get_user_emo(user_data)}', reply_markup = get_keyboard())


def get_location(update: Update, context: CallbackContext):
	print(update.message.location)
	bot.send_message(chat_id=update.message.chat.id, text=f'Ready: {get_user_emo(user_data)}', reply_markup = get_keyboard())


def get_keyboard():
	contact_button = KeyboardButton('Send contacts', request_contact=True)
	location_button = KeyboardButton('Send location', request_location=True)
	my_keyboard = ReplyKeyboardMarkup(
		[
		['/start', 'Send a cat', 'Change avatar'],
		[contact_button, location_button]
		], resize_keyboard=True
		)
	return my_keyboard


# Функция, которая соединяется с платформой Telegram, тело нашего бота
def main():
		# mybot = Updater((API_KEY, request_kwargs = PROXY)
		mybot = Updater(settings123.API_KEY)
		dp = mybot.dispatcher

		logging.info('Bot starting')
		print('--------------')
		print('Bot starting')
		print('--------------')
		
		dp.add_handler(CommandHandler('start', greet_user))
		dp.add_handler(CommandHandler('planet', planet_list))
		dp.add_handler(CommandHandler('cat', send_cat_picture))
		dp.add_handler(MessageHandler(Filters.text('(Send a cat)'), send_cat_picture))
		dp.add_handler(MessageHandler(Filters.text('(Change avatar)'), change_avatar))
		dp.add_handler(MessageHandler(Filters.contact, get_contact))
		dp.add_handler(MessageHandler(Filters.location, get_location))
	
		
		dp.add_handler(CommandHandler(['Sun','Moon','Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'], planet_user))
		
		dp.add_handler(MessageHandler(Filters.text, talk_to_me))

		mybot.start_polling()
		mybot.idle()
		
		
# Вызываем функцию - эта строчка запускает бот
main()

