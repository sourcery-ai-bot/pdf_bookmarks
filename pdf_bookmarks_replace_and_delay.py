#!/usr/bin/python

BM_Info = open('info_bm.txt').read().split('|')
BM_Info_After = open('info_bm_after.txt','a')
d   = int(raw_input('Page delay:      '))
pg1 = int(raw_input('Delay from page: '))
pg2 = int(raw_input('Delay to page:   '))

for i in range(len(BM_Info)):
	j = i % 3
	if(j == 0):
		if(i != 0):
			BM_Info_After.write('|')
		BM_Info_After.write(BM_Info[i].decode('utf-8').encode('ascii', 'xmlcharrefreplace'))
	elif(j == 1):
		BM_Info_After.write('|' + BM_Info[i])
	elif(j == 2):
		if((int(BM_Info[i]) >= pg1) and (int(BM_Info[i]) <= pg2)):
			BM_Info_After.write('|' + str(int(BM_Info[i]) + d))
		else:
			BM_Info_After.write('|' + BM_Info[i])

BM_Info_After.close()