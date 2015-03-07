#!/bin/bash

cd /home/brycecaine/journalblog
rm -fr content
mkdir content
cp -r raw/* content

echo 'start'

for f in $(find /home/brycecaine/journalblog/content -name '*.md')
do
	# Remove comments at top of file
	sed -i '/<!---/d' $f
	sed -i '/-->/d' $f

	# Add {filename} prefix to image links
	sed -i 's/{filename}//g' $f
	sed -i 's/!\[image\](/!\[image\]({filename}/g' $f
done

echo 'done'
