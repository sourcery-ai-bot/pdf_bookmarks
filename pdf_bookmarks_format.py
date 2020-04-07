#!/usr/bin/python

BM_Info = open('info_bm.txt').read().split('|')
BM_Info_formated = ''

for i in range(len(BM_Info)):
	j = i % 3
	if(j == 0):
		BM_Info_formated += 'BookmarkBegin\nBookmarkTitle: '
	elif(j == 1):
		BM_Info_formated += 'BookmarkLevel: '	
	elif(j == 2):
		BM_Info_formated += 'BookmarkPageNumber: '
		#BM_Info[i] = str(int(BM_Info[i]) - 24) #EMERGENCY DELAY
	BM_Info_formated += BM_Info[i].decode('utf-8').encode('ascii', 'xmlcharrefreplace') + '\n'

PDF_Info_1 = open('info_pdf_old.txt')
PDF_Info_2 = open('info_pdf_updated.txt','a')

while(True):
	line = PDF_Info_1.readline()
	if(line.find('Bookmark') == -1):
		PDF_Info_2.write(line)
	if(line.find('NumberOfPages') != -1):
		PDF_Info_2.write(BM_Info_formated)
	if(line == ''):
		break

PDF_Info_1.close()
PDF_Info_2.close()

