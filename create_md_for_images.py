from datetime import datetime
from dateutil.parser import parse
import os
import re

for image_filename_full in os.listdir('.'):
    if re.match(r'.*\.jpg', image_filename_full):
        # ---------------------------------------------------------------------
        # Rename image files
        new_image_filename_full = image_filename_full.replace(' ', '_')
        os.rename(image_filename_full, new_image_filename_full)

        # ---------------------------------------------------------------------
        # Create markdown file for each image
        # Get the date and create the file
        try:
            possible_date_str = re.search(r'(\d+[.-_]?\d+[.-_]?\d+)', image_filename_full)
            file_date = parse(possible_date_str.group())
            md_filename = os.path.splitext(new_image_filename_full)[0]
        except (ValueError, AttributeError):
            file_date = datetime.fromtimestamp(os.path.getctime(image_filename_full))
            md_filename = '%s_%s' % (os.path.splitext(new_image_filename_full)[0], file_date.strftime('%Y.%m.%d'))

        print file_date

        md_file = open('%s.md' % md_filename, 'w+')

        # Populate content
        md_content = (
            '<!--- HEADER\n'
            '$notedate %s -->\n\n'
            '![image](%s)' % (file_date, image_filename_full)
        )

        md_file.write(md_content)
