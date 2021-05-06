
joinedFile = open("https://github.com/AnastasiaNik98/bot/blob/main/joined.txt", "r")
joinedUsers = set()
for line in joinedFile:
  joinedUsers.add(line.strip())
  joinedFile.close()
  

  def startJoin(message):
    if not str(chat_id) in joinedUsers:
      joinedFile = open("https://github.com/AnastasiaNik98/bot/blob/main/joined.txt", "a")
      joinedFile.write(str(chat_id)+"\n")
      joinedUsers.add(chat_id)

def mess(message):
  for user in joinedUsers:
    update.send_message(user, message.text[message.text.find(' '):])
