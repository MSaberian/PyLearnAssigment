import os
import random
import qrcode
import gtts
import telebot
from telebot import types
from datetime import date, datetime
from khayyam import JalaliDate, jalali_datetime

bot = telebot.TeleBot("5858795730:AAFRhu3XzmQBs48DqvGvCL1-q-aQVHiKD_8", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

newgame_keyboard = types.ReplyKeyboardMarkup(row_width=1)
keynewgame = types.KeyboardButton("new game")
keyleavegame = types.KeyboardButton("leave game")
newgame_keyboard.add(keynewgame,keyleavegame)

def update_status(new_status):
	if not 'status' in globals():
		global status
		status = ''
	status = new_status

def read_status():
	if not 'status' in globals():
		global status
		status = ''
	return status

def my_max(array):
	maximum = int(array[0])
	for num in array:
		if int(num) > maximum:
			maximum = int(num)
	return maximum
	
def my_argmax(array):
	maximum = int(array[0])
	ind = -1
	index = 0
	for num in array:
		ind += 1
		if int(num) > maximum:
			maximum = int(num)
			index = ind
	return index

@bot.message_handler(commands=['start'])
def send_welcome(message):
	update_status('welcome')
	user_first_name = str(message.chat.first_name) 
	bot.reply_to(message, f"Hey! {user_first_name} \n Welcome to the MoSa Bot\npress /help for help")

@bot.message_handler(commands=['game'])
def start_game(message):
	update_status('game')
	if not 'game_number' in globals():
		global game_number
	game_number = random.randint(1, 50)
	bot.send_message(message.chat.id, f'guess a number between 1 to 50',reply_markup=newgame_keyboard)

@bot.message_handler(commands=['age'])
def start_game(message):
	update_status('agey')
	if not 'age_y' in globals():
		global age_y
		global age_m
		global age_d
	age_y = 1
	age_m = 1
	age_d = 1
	bot.send_message(message.chat.id, 'Enter your birth year (four-digit)', reply_markup = telebot.types.ReplyKeyboardRemove())
	
@bot.message_handler(commands=['voice'])
def start_game(message):
	update_status('voice')
	bot.send_message(message.chat.id, 'Enter your text to convert to voice')

@bot.message_handler(commands=['max'])
def start_game(message):
	update_status('max')
	bot.send_message(message.chat.id, 'Enter your array to find the maximum\nFor example: 45,26,3,489')
	
@bot.message_handler(commands=['argmax'])
def start_game(message):
	update_status('argmax')
	bot.send_message(message.chat.id, 'Enter your array to find index of the maximum\nFor example: 45,26,3,489')
	
@bot.message_handler(commands=['qrcode'])
def start_game(message):
	update_status('qrcode')
	bot.send_message(message.chat.id, 'Enter your text to convert to QrCode')
	
@bot.message_handler(commands=['help'])
def start_game(message):
	help_massage = """List of the commands:
	/start: Telling Welcome
	/game: Number guessing game
	/age: Telling your age
	/voice: Convert text to voice
	/qrcode: Convert text to QrCode
	/max: Find maximum of the array
	/argmax: Find index of maximum of the array
	/help: commands list (this massage!)
	"""
	bot.send_message(message.chat.id, help_massage)

@bot.message_handler(func=lambda m:True)
def plsy_game(message):

	if read_status() == 'game':
		if message.text.isdigit() and 0 < int(message.text) < 51:
			if int(message.text) == game_number:
				bot.send_message(message.chat.id, 'congratulations, you win', reply_markup = telebot.types.ReplyKeyboardRemove())
				bot.send_message(message.chat.id, '🎉')
				update_status('')
			elif int(message.text) > game_number:
				bot.send_message(message.chat.id, 'go down ⏬')
			else:
				bot.send_message(message.chat.id, 'go up ⏫')
		elif message.text == 'new game':
			start_game(message)
		elif message.text == 'leave game':
			update_status('')
			bot.send_message(message.chat.id, 'You leave game', reply_markup = telebot.types.ReplyKeyboardRemove())
		else:
			bot.send_message(message.chat.id, 'You have to enter number between 1 to 50! ⚠')

	elif read_status() == 'agey':
		yearnow = int(str(JalaliDate.today()).split('-')[0])
		if message.text.isdigit() and 0 <= int(message.text) <= yearnow:
			update_status('agem')
			global age_y
			age_y = int(message.text)
			bot.send_message(message.chat.id, 'Enter your birth month')
		else:
			bot.send_message(message.chat.id, f'You have to enter number between 1 to {yearnow}! ⚠')

	elif read_status() == 'agem':
		if message.text.isdigit() and 1 <= int(message.text) <= 12:
			update_status('aged')
			global age_m
			age_m = int(message.text)
			bot.send_message(message.chat.id, f'Enter your birth day')
		else:
			bot.send_message(message.chat.id, 'you have to enter number between 1 to 12 ! ⚠')

	elif read_status() == 'aged':
		if message.text.isdigit() and 1 <= int(message.text) <= 31:
			update_status('')
			age_d = int(message.text)
			difference = JalaliDate.today() - JalaliDate(age_y, age_m, age_d)
			bot.send_message(message.chat.id, 'You are ' + str(int(str(difference).split(' ')[0])//365) + ' years old')
		else:
			bot.send_message(message.chat.id, 'You have to enter number between 1 to 31 ! ⚠')
			
	elif read_status() == 'voice':
		voice_file = message.text.split(' ')[0] + '.mp3' 
		gtts.gTTS(message.text, lang='en', slow=False).save(voice_file)
		bot.send_audio(message.chat.id, open(voice_file,'rb'))
		os.remove(voice_file)
		update_status('')
		
	elif read_status() == 'max':
		array = message.text.split(',') 
		maximum = my_max(array)
		update_status('')
		bot.send_message(message.chat.id, f'Maximum of your array is {maximum}')
		
	elif read_status() == 'argmax':
		array = message.text.split(',') 
		argmaximum = my_argmax(array)
		update_status('')
		bot.send_message(message.chat.id, f'Index of maximum of your array is {argmaximum}')
		
	elif read_status() == 'qrcode':
		qrcode_file = message.text.split(' ')[0] + '.png' 
		QRcode = qrcode.make(message.text).save(qrcode_file)
		update_status('')
		bot.send_photo(message.chat.id, open(qrcode_file,'rb'), message.text)
		os.remove(qrcode_file)
		
	else:
		bot.send_message(message.chat.id, 'No status')
		help_massage = """List of the commands:
		/start: Telling Welcome
		/game: Number guessing game
		/age: Telling your age
		/voice: Convert text to voice
		/qrcode: Convert text to QrCode
		/max: Find maximum of the array
		/argmax: Find index of maximum of the array
		/help: commands list (this massage!)
		"""
		bot.send_message(message.chat.id, help_massage)


bot.infinity_polling()