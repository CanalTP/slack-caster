import os
dir = os.path.dirname(os.path.abspath(__file__))
file_full_name = os.path.join(dir, "last_message_ts")
def getLastMessageTs(suffix = ''):
    try:
        file = open(file_full_name + suffix, "r")
        return file.readline()
    except FileNotFoundError:
        setLastMessageTs("0", suffix)
        return getLastMessageTs(suffix)


def setLastMessageTs(ts, suffix = ''):
    file = open(file_full_name + suffix, "w")
    file.write(ts)
