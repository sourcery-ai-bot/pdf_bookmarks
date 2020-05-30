#!/usr/bin/python

d = 8
t = 'E'

for _ in range(150):

	# GENERAL
	#p = int(raw_input('Page :            '))
	#d = int(raw_input('Page delay:       '))
	#t =     raw_input('(e)ven/(o)dd 1st: ')

	# SPECIFIC
	p = int(raw_input('Page : '))
	if (t in ['E', 'e'] and (p % 2 == 0)
	    or t != 'E' and t != 'e' and t in ['O', 'o'] and (p % 2 == 0)):
		print((p/2) + d)
	elif t in ['E', 'e']:
		print(((p - 1)/2) + d)
	elif t in ['O', 'o']:
		print(((p + 1)/2) + d)