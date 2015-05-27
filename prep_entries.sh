#!/bin/bash

cd /home/brycecaine/workspace/journalblog
rm -fr content
mkdir content
cp -r raw/* content

echo 'Start'

for file in $(find /home/brycecaine/workspace/journalblog/content -name '*.md')
do
    echo "Begin: $file"
    # -------------------------------------------------------------------------
    # Generate front matter

    # Get parent directory name to assign as author
    path=$(dirname $file)
    path_els=(${path//// })
    name_el="${path_els[5]}"
    name=$(echo "$name_el" | tr _ " " | sed 's/[^ ]\+/\L\u&/g')

    # Get datetime of file
    date_str=$(sed -n 's/\$notedate \(.*\) -->/\1/p' $file)
    date=$(date -d $date_str +"%Y-%m-%d %H:%M")
    file_date=$(date -d $date_str +"%Y.%m.%d.%H.%M")

    # Get title
    title="Journal of $name $date"

    # Get tags
    tags_str=$(sed -n 's/\(:.*:\s\)/\1/p' $file)
    tags_els=(${tags_str//:/ })

    tags=""
    for i in "${tags_els[@]}"
    do
        :
        if [ -z "$tags" ]; then
            tags="$i"
        else
            tags="$tags, $i"
        fi
    done

    # Insert front matter into file
    sed -i "1iTitle: $title\nTags: $tags\n" $file

    # -------------------------------------------------------------------------
    # Moddify syntax for images

    # Add {filename} prefix to image links
    sed -i 's/{filename}//g' $file
    sed -i 's/!\[image\](/!\[image\]({filename}/g' $file

    # -------------------------------------------------------------------------
    # Change filename
    mv "$file" "$path/journal_${name_el}_$file_date.md"
    echo "End: $file"
done

echo 'Done'
