import logging
from glob import glob
from random import choice

import telegram
from telegram.ext.callbackcontext import CallbackContext
from telegram.update import Update
from utilsBot import get_user_emo, get_keyboard

import settings123
import planet_object
import extended_calculator
# import os


bot = telegram.Bot(settings123.API_KEY)
user_data = {}


def greet_user(update: Update, context: CallbackContext):
	text = 'Command: /start'
	print('--------------')
	print(text)
	print('--------------')
	logging.info(text)
	# update.message.reply_text(text)
	bot.send_message(chat_id=update.message.chat.id, text =f'Hello {get_user_emo(user_data)}', reply_markup = get_keyboard())
	bot.send_message(chat_id=update.message.chat.id, text = "Please write:\
	\n -/start\
	\n -/cat\
	\n -/any_text\
	\n -/planet")
	
	
def talk_to_me(update: Update, context: CallbackContext):
	user_text = update.message.text	
	if user_text[:5] == '/calc':
		string_r = user_text[5:]
		result_r = extended_calculator.calculator(string_r)
		print(result_r)
		bot.send_message(chat_id=update.message.chat.id, text = f'Your result: {result_r}', reply_markup = get_keyboard())		
	else:
		emo = get_user_emo(user_data)
		text_print = f'Hello {update.message.chat.first_name} {emo}! You wroute: {user_text}'
		print('--------------')
		print(text_print)
		print('--------------')
		logging.info(f'User:{update.message.chat.first_name},\
		Chat id:{update.message.chat.id},\
		Message:{update.message.text}')
		bot.send_message(chat_id=update.message.chat.id, text = text_print, reply_markup = get_keyboard())


def planet_list(update: Update, context: CallbackContext):
	bot.send_message(chat_id=update.message.chat.id, text="Please select object:\
	\n -/Sun\n -/Moon\n -/Mercury\n -/Venus\n -/Mars\n -/Jupiter\n -/Saturn\n -/Uranus\n -/Neptune\n -/Pluto", reply_markup = get_keyboard())
	logging.info('Command: /planet')


def send_cat_picture(update: Update, context: CallbackContext):
	logging.info('Command: /cat')
	bot.send_message(chat_id=update.message.chat.id, text="From Telegram Bot", reply_markup = get_keyboard())
	cat_list = glob('images\cat*.jp*g')
	cat_pic = choice(cat_list)
	print(cat_pic)
	bot.send_photo(chat_id=update.message.chat.id, photo=open(cat_pic, 'rb'))
	


def planet_user(update: Update, context: CallbackContext):
	Message_pl = update.message.text
	select_planet=Message_pl.replace('/','')	
	select_date = planet_object.time_in
	select_coordinat = planet_object.planet1[select_planet]
	print('--------------')
	print(f'Planet	: {select_planet}')
	print(f'Date	: {select_date}')
	print(f'Location: {select_coordinat}')
	print('--------------')
	bot.send_message(chat_id=update.message.chat.id, text=\
		f' Select planet\t\t\t\t\t\t: \t"{select_planet}"\
		\nToday date\t\t\t\t\t\t\t\t\t: \t"{select_date}"\
		\nLocation planet: \t"{select_coordinat}" 		', reply_markup = get_keyboard())	
	logging.info(f'User:{update.message.chat.first_name},\
	Chat id:{update.message.chat.id},\
	Planet :{select_planet},\
	Date   :{select_date},\
	Location: {select_coordinat} ')


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


def start_calculator(update: Update, context: CallbackContext):
	bot.send_message(chat_id=update.message.chat.id, text='Please enter "/calc" and a string of numbers separated by symbols "+,-,*,/", \n Example: /calc 2+5-9*8/3', reply_markup = get_keyboard())
	
