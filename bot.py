# импорт нужных компонентов
from glob import glob
import logging
from random import choice

from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

import settings123



logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

bot = telegram.Bot(settings123.API_KEY)

def greet_user(update: Update, context: CallbackContext):
	text = 'Command: /start'
	print('--------------')
	print(text)
	print('--------------')
	logging.info(text)
	# update.message.reply_text(text)
	update.message.reply_text(
        "Please write:\
	\n -/start\
	\n -/cat\
	\n -/any_text\
	\n -/planet")
	
	
def talk_to_me(update: Update, context: CallbackContext):
	user_text = update.message.text
	# text_print = f'Message User: {user_text}'
	text_print = f'Hello {update.message.chat.first_name}! You wroute: {user_text}'
	
	print('--------------')
	print(text_print)
	print('--------------')

	# print(update.message)
	logging.info(f'User:{update.message.chat.first_name},\
	Chat id:{update.message.chat.id},\
	Message:{update.message.text}')
	# update.message.reply_text(text_print)
	bot.send_message(chat_id=update.message.chat.id, text = text_print)


def planet_list(update: Update, context: CallbackContext):
	# update.message.reply_text(
    #     "Please select object:\
	# \n -/Sun\n -/Moon\n -/Mercury\n -/Venus\n -/Mars\n -/Jupiter\n -/Saturn\n -/Uranus\n -/Neptune\n -/Pluto")
	bot.send_message(chat_id=update.message.chat.id, text="Please select object:\
	\n -/Sun\n -/Moon\n -/Mercury\n -/Venus\n -/Mars\n -/Jupiter\n -/Saturn\n -/Uranus\n -/Neptune\n -/Pluto")
	logging.info('Command: /planet')


def send_cat_picture(update: Update, context: CallbackContext):
# def send_cat_picture(bot, update):
	# bot = telegram.Bot(settings123.API_KEY)
	logging.info('Command: /cat')
	bot.send_message(chat_id=update.message.chat.id, text="From Telegram Bot")
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
		\nLocation planet: \t"{select_coordinat}" 		')
	
	logging.info(f'User:{update.message.chat.first_name},\
	Chat id:{update.message.chat.id},\
	Planet :{select_planet},\
	Date   :{select_date},\
	Location: {select_coordinat} ')



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
		dp.add_handler(CommandHandler(['Sun','Moon','Mercury','Venus','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto'], planet_user))
		
		dp.add_handler(MessageHandler(Filters.text, talk_to_me))

		
		mybot.start_polling()
		mybot.idle()
		
		
# Вызываем функцию - эта строчка запускает бот
main()

