joinedFile = open("/joined.txt", "r")
joinedUser = set()
for line in joinedFile:
  joinedUsers.add(line.strip())
joinedFile.close()

@bot.message_hendler(commands=['start'])
def startJoin(massage):
  if not str(massage.chat.id) in joinedUsers:
    joinedFile=open("/joined.txt", "a")
    joinedFile.write(str(massage.chat.id) + "\n")
    joinedUsers.add(massage.chat.id)
    
@bot.message_hendler(commands=['special'])
def mess(massage):
  for user in joinedUsers:
    bot.send_massage(user, massage.text[massage.text.find(' '):])
                     
