
def getLastMessageTs():
	file = open("last_message_ts", "r")
	return file.readline()

def setLastMessageTs(ts):
	file = open("last_message_ts", "r+")
	file.write(ts)





#ts = "456"
#last_ts = getLastMessageTs()
#print(last_ts)

#setLastMessageTs(ts)

#last_ts = getLastMessageTs()
#print(last_ts)


#print('end')



