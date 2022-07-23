# импорт нужных компонентов
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
import settings123

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s',
					level=logging.INFO,
					filename='bot.log')

def greet_user(update: Update, context: CallbackContext):
	text = 'Command: /start'
	print('--------------')
	print(text)
	print('--------------')
	logging.info(text)
	# update.message.reply_text(text)
	
def talk_to_me(update: Update, context: CallbackContext):
	user_text = update.message.text
	# text_print = f'Message User: {user_text}'
	text_print = f'Hello {update.message.chat.first_name}! Yuo wroute: {user_text}'
	
	print('--------------')
	print(text_print)
	print('--------------')
	# logging.info('--------------')
	# logging.info(text_print)
	logging.info('--------------')
	# print(update.message)
	logging.info(f'User: {update.message.chat.first_name}, \
				Chat id: {update.message.chat.id}, \
				Message: {update.message.text}')
	logging.info('--------------')
	update.message.reply_text(text_print)

# Функция, которая соединяется с платформой Telegram, тело нашего бота
def main():
	# mybot = Updater((API_KEY, request_kwargs = PROXY)
	mybot = Updater(settings123.API_KEY)

	logging.info('Bot starting')
	print('--------------')
	print('Bot starting')
	print('--------------')

	dp = mybot.dispatcher
	dp.add_handler(CommandHandler('start', greet_user))
	dp.add_handler(MessageHandler(Filters.text, talk_to_me))

	mybot.start_polling()
	mybot.idle()
# Вызываем функцию - эта строчка запускает бот
main()