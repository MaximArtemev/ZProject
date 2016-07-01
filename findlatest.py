import requests
from html.parser import HTMLParser
import log


class Latest(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self._ans = 0
        self._find = True
        log.debug("Latest initializated")

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'div' and attrs.get('class') == 'story'\
                and self._find and 'id' in attrs:
            try:
                self._ans = attrs.get('id')[6:]
                self._find = False
            except:
                self._ans = 0

    def parse(self, text):
        self.feed(text)
        return self._ans


def get_latest():
    ending = Latest()
    end = int(ending.parse(requests.get('http://zadolba.li/').text))
    if end == 0:
        log.error("Wrond latest thing")
        raise Exception
    return end