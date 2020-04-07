#!/usr/bin/bash

STARTTIMETOTAL=$(date +%s)

cd "$1"
for f in *.pdf
do
	echo "$f" >> ~/Downloads/PDFPages.txt
	pdfinfo "$f" | grep Pages >> ~/Downloads/PDFPages.txt
done

ENDTIMETOTAL=$(date +%s)
echo "Total execution time: $(($ENDTIMETOTAL - $STARTTIMETOTAL)) seconds"