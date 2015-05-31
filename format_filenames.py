import glob
import os
import re
import shutil

TAG_LIST = (
    'kathy', 'elina', 'aaron', 'emmett', 'daven', 'lora', 'tom', 'jeremy', 'jeralyn',
    'mom', 'dad', 'grandma', 'grandpa', 'aunt', 'uncle', 'cousin', 'nephew', 'niece',
    'love', 'faith', 'happy', 'smile', 'family', 'marriage', 'children', 'work', 'play',
    'eat', 'ate', 'run', 'ran', 'drive', 'drove', 'read', 'book', 'breakfast', 'lunch', 'dinner'
)

# Clear out all files from pelican source folder
files = glob.glob('content_myjournal/*')
for f in files:
    os.remove(f)

# Add groomed md files to pelican source folder from journal txt files
indir = 'content/journals/bryce_caine'
for root, dirs, filenames in os.walk(indir):
    i = 0
    for filename in sorted(filenames):
        if re.match(r'.*\.txt', filename):
            i += 1
            with open(os.path.join(root, filename), 'r') as f:
                # Derive tags from file content
                content = f.read().replace(',', '').replace('.', '').replace('\n', ' ').replace('\'s', '').lower()
                word_list = content.split(' ')
                tags = list(set(word_list).intersection(TAG_LIST))
                tags_str = 'Tags: %s' % ', '.join(tags)

                # Get date string from existing filename and use it to name
                # the new file
                date_str = re.search(r'(\d{2}_\d{2}_\d{4})', filename).group().replace('_', '.')
                new_filename = 'Journal Entry %s%s.md' % (i, date_str)

                with open(os.path.join('content_myjournal', new_filename), 'w') as file_to_tag:
                    file_to_tag.write(tags_str + '\n\n')
                    f.seek(0, 0)
                    file_to_tag.write(f.read())

# Add all other files
for root, dirs, filenames in os.walk(indir):
    for filename in filenames:
        if not re.match(r'.*\.txt', filename):
            shutil.copy2(os.path.join(root, filename), 'content_myjournal')