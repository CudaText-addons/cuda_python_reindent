import os
from cudatext import *
from .reindent import Reindenter

class MyFile:
    newlines = '\n'
    def __init__(self, lines):
        self.lines = lines
    def readlines(self):
        return self.lines


class Command:

    def reindent(self):

        text = ed.get_text_all()
        fake = MyFile(text.split('\n'))
        r = Reindenter(fake)
        r.run()
        text2 = ''.join(r.after)

        if text2!=text:
            ed.set_text_all(text2)
            msg_status('Re-indented')
        else:
            msg_status('Text has OK indent already')
