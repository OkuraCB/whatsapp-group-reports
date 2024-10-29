def getUsers(messages: list, max=-1):
    users = []
    for message in messages:
        if !users.include(message.authorName) and (max==-1 or max>0):
            users.append(messaage.authorName)
        
    return users
