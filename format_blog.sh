# Replace spaces in filenames with hyphens
find -name "* *" -type f | rename 's/ /-/g'

for file in *.txt; do
  # Split filename by hyphen
  var="${file}"
  parts=(${var//-/ })

  # Assign date, title, and name variables
  dat=${parts[3]:0:10}
  ttl="${parts[0]} ${parts[1]} ${parts[2]} $dat"
  nam="${parts[1]} ${parts[2]}"

  # Insert front matter into file
  sed -i "1iTitle: $ttl\nDate: $dat\nAuthor: $nam\n" $file

  # Change file extension from txt to md
  mv "$file" "${file%.txt}.md"
done
