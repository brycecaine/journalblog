from pelican.contents import Page
from pelican.readers import MarkdownReader

class TxtReader(MarkdownReader):
    file_extensions = ['txt']
