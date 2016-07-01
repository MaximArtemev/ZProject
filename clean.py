from html.parser import HTMLParser
from time import time
import log
from os import listdir
from collections import namedtuple
from marking import clean_by_words

CLEAN = '/home/max/PycharmProjects/FULL_DATA/CLEAN_DATA'
HTML = '/home/max/PycharmProjects/FULL_DATA/HTML_DATA'
RESULT = namedtuple("Result", ['title', 'span'])


class Cleaner(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._title = ''
        self._span = ''
        self._in_title = False
        self._in_span = False

    def handle_starttag(self, tag, attrs):
        if tag == 'h1':
            self._in_title = True
        if tag == 'p':
            self._span += '\n\n'
        if tag == 'br':
            self._span += '\n'
        if dict(attrs).get('class') == 'text':
            self._in_span = True

    def handle_endtag(self, tag):
        if tag == 'h1':
            self._in_title = False
        if tag == 'div':
            self._in_span = False

    def handle_data(self, data):
        if self._in_title:
            self._title += data
        if self._in_span:
            self._span += data

    def parse(self, _text):
        self.feed(_text)
        return RESULT(self._title, self._span)


def start_working(files):
    start_time = time()
    try:
        for num in files:
            process(num)
            log.debug(str(num) + " is cleared")
    except:
        log.error('Some error occurred while processing')
    clean_by_words()
    log.debug("Finished in " + str(time() - start_time))


def process(num):
    with open(HTML + '/' + num, 'r') as file:
        store(CLEAN + '/' + num,
              parse(file.read()))


def store(file, text):
    with open(file, 'w') as out:
        out.write(text)
    log.debug('Stored ' + file)


def parse(text):
    ans = Cleaner().parse(text)
    return ans.title + '\n\n' + ans.span


def lost_packages():
    downloaded = set(
        map(lambda name: name,
            listdir(CLEAN))
    )
    lost = set(i for i in listdir(HTML) if i not in downloaded)
    start_working(lost)
    log.debug("Least finished")