import os
dir = os.path.dirname(os.path.abspath(__file__))
file_full_name = os.path.join(dir, "last_message_ts")
def getLastMessageTs():
    try:
        file = open(file_full_name, "r")
        return file.readline()
    except FileNotFoundError:
        setLastMessageTs("0")
        return getLastMessageTs()


def setLastMessageTs(ts):
    file = open(file_full_name, "w")
    file.write(ts)
