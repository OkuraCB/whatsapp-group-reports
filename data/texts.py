import utils.py

def messagesPerUser(textMessages: list):
    users = utils.getUsers()

    messagesPerUser = []
    for user in users:
        messagesPerUser.append({name: user, count: len(textMessages.filter(user))})

    return messagesPerUser

def wordsPerMessage(textMessages):
    messageCount = len(textMessages)
    wordCount = 0
    for message in textMessages:
        wordCount+=len(message.body.split(" "))

    return wordCount/messageCount

def wordsPerMessagePerUser(textMessages):
    users = utils.getUsers()
    wordsPerMessagePerUser = []
    for user in users:
        userMessages = textMessages.filter(user)
        wordsPerMessage = wordsPerMessage(userMessages)
        wordsPerMessagePerUser.append({name: user, wordsPerMessage: wordsPerMessage})

    return wordsPerMessagePerUser

def wordOccurrence(textMessages):
    words = []
    wordCount = []
    for message in textMessages:
        messageWords = message.body.split(" ")
        for word in messageWords:
            if !words.include(word):
                words.append(word)
                wordCount.append(1)
            else:
                index = words.indexOf(word)
                wordCount[index]+=1
            users = []
            for message in textMessages:
                if !users.includes(message.authorName
                    users.append(message.authorName)
