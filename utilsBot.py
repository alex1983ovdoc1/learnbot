from emoji import emojize
from random import choice

from telegram import ReplyKeyboardMarkup, KeyboardButton

import settings123



def get_user_emo(user_data):
	if 'emo' in user_data:
		return user_data['emo']
	else:
		user_data['emo'] = emojize(choice(settings123.USER_EMOJI))
		return user_data['emo']


def get_keyboard():
	contact_button = KeyboardButton('Send contacts', request_contact=True)
	location_button = KeyboardButton('Send location', request_location=True)
	my_keyboard = ReplyKeyboardMarkup(
		[
		['/start', 'Send a cat', 'Change avatar'],
		[contact_button, location_button, 'calculatorV1_0']
		], resize_keyboard=True
		)
	return my_keyboard

