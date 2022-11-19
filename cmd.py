import os
command = input('pycmd >')

if 'cmd' in command:
	tmp0 = command.split(sep=' ')
	os.system(tmp0[1 - 10])
	#
elif 'java' in command:
	tmp0 = command.split(sep=' ')
	os.system('java -jar ', tmp0[1])
	#
elif 'py' in command:
	tmp0 = command.split(sep=' ')
	os.system('py ', tmp0[1])
	#
elif command == 'close':
	exit()
	#
elif command == 'update':
	os.system('py update.py')
elif 'port' in command:
	tmp0 = command.split(sep=' ')
	if 'open' in command:
		os.system(f'ngrok tcp {tmp0[2]}')
	else:
		os.system('ngrok ', tmp0[1])
else:
	print ('Неизвестная или неполная команда')
	
os.system('call cmd.py')
