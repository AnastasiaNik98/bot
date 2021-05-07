
import telebot
from telegram.ext import Updater
updater = Updater(TELEGRAM_TOKEN)
joinedFile = open("/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
  joinedUsers.add(line.strip())
  joinedFile.close()
  
@bot.message_handler(commands=['start'])
  def startJoin(message):
    if not str(message.chat.id) in joinedUsers:
      joinedFile = open("/joined.txt", "a")
      joinedFile.write(str(chat_id)+"\n")
      joinedUsers.add(message.chat.id)
@bot.message_handler(commands=['info'])
def mess(message):
  for user in joinedUsers:
    update.send_message(user, message.text[message.text.find(' '):])
