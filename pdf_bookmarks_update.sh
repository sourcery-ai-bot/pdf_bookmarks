#!/usr/bin/bash

STARTTIMETOTAL=$(date +%s)

pdftk "$1" dump_data output info_pdf_old.txt

echo -n "Generate Info? (y=1/n=0) "
read choice1
if [ $choice1 -eq 1 ] ; then
	rm info_bm.txt
	python pdf_bookmarks_info_gen.py
fi

python pdf_bookmarks_format.py
rm info_pdf_old.txt
pdftk "$1" update_info info_pdf_updated.txt output "${1%%.pdf}_out.pdf"
rm info_pdf_updated.txt

#echo -n "Replace original pdf file? (y=1/n=0) "
#read choice3
#if [ $choice3 -eq 1 ] ; then
	pid=$(pidof evince)
	kill $pid
	rm "$1"
	cp "${1%%.pdf}_out.pdf" "$1"
	rm "${1%%.pdf}_out.pdf"
#fi

ENDTIMETOTAL=$(date +%s)
echo "Total execution time: $(($ENDTIMETOTAL - $STARTTIMETOTAL)) seconds"
