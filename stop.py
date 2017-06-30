import subprocess, signal
import time
import os



os.system("taskkill /im vlc.exe")


"""
while True:
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()

	for line in out.splitlines():
		print(line)
		if 'vlc' in line:
			print('process vlc found ! waiting 6 seconds before kill !!!')
			time.sleep(6)
			pid = int(line.split(None, 1)[0])
			os.kill(pid, signal.SIGKILL)
"""