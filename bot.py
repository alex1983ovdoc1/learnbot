# импорт нужных компонентов
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import settings123
from handlersBot import *


logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')
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

		dp.add_handler(MessageHandler(Filters.text('(Send a cat)'), send_cat_picture))
		dp.add_handler(MessageHandler(Filters.text('(Change avatar)'), change_avatar))
		dp.add_handler(MessageHandler(Filters.text('(calculatorV1_0)'), start_calculator))
		dp.add_handler(MessageHandler(Filters.contact, get_contact))
		dp.add_handler(MessageHandler(Filters.location, get_location))	
		dp.add_handler(MessageHandler(Filters.text, talk_to_me))

		mybot.start_polling()
		mybot.idle()
		
	
# Вызываем функцию - эта строчка запускает бот
if __name__ == '__main__':
	main()

