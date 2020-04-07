#!/usr/bin/bash

STARTTIMETOTAL=$(date +%s)

python pdf_bookmarks_replace_and_delay.py

x=0
y=true

while [ "$y" = true ]
do
	if [ -f info_bm"$x".txt ]
	then
   		x=$(( $x + 1 ))
   	else
   		cp info_bm.txt info_bm"$x".txt
   		rm info_bm.txt
   		cp info_bm_after.txt info_bm.txt
   		rm info_bm_after.txt
   		y=false
	fi
done

ENDTIMETOTAL=$(date +%s)
echo "Total execution time: $(($ENDTIMETOTAL - $STARTTIMETOTAL)) seconds"
