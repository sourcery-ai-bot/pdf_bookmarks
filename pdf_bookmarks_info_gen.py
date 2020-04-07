#!/usr/bin/python

d = int(raw_input('Page delay: '))
q = raw_input('All levels = 1? (y/n) ')

f = open('info_bm.txt','a')

i = 1
test = 'OK'
while (True):
	print(str(i) + ') ')
	
	test = raw_input('TITLE: ')
	if((test == 'END') or (test == 'ENDC')):
		break
	
	if(i != 1):
		f.write('|')

	f.write(test.decode('utf-8').encode('ascii', 'xmlcharrefreplace') + '|')
	
	if((q == 'y') or (q == 'Y')):
		f.write('1|')
	else:
		f.write(raw_input('LEVEL: ') + '|')
	
	f.write(str(int(raw_input('PAGE:  ')) + d))
	i += 1

f.close()

if(test == 'ENDC'):
	raw_input('OK?');