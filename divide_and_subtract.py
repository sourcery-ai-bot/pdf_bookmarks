#!/usr/bin/python

for i in range(150):

	# GENERAL
	#p = int(raw_input('Page :            '))
	#d = int(raw_input('Page delay:       '))
	#t =     raw_input('(e)ven/(o)dd 1st: ')

	# SPECIFIC
	p = int(raw_input('Page : '))
	d = 8
	t = 'E'

	if((t == 'E') or (t == 'e')):
		if(p % 2 == 0):
			print((p/2) + d)
		else:
			print(((p - 1)/2) + d)
	elif ((t == 'O') or (t == 'o')):
		if(p % 2 == 0):
			print((p/2) + d)
		else:
			print(((p + 1)/2) + d)