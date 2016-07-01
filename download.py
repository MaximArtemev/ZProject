from concurrent.futures import ThreadPoolExecutor
from os import listdir
from time import time

import requests

import findlatest
import log

HTML = '/home/max/PycharmProjects/FULL_DATA/HTML_DATA'
BASE = 'http://zadolba.li/story/'


def lost_packages():
    downloaded = set(
        map(lambda name: int(name.rstrip('.txt')),
            listdir(HTML))
    )
    lost = set(i for i in range(1, findlatest.get_latest()) if i not in downloaded)
    try:
        len_n = len(lost)
        thr = 40
        if len_n < 1000:
            thr = len_n/20
        start_working(lost, threads=thr)
    except:
        log.error("Some error occurred while downloading least")
    log.debug("Base finished with updating")


def start_working(files, threads=40):
    start_time = time()
    log.debug("Download started")
    with ThreadPoolExecutor(threads) as executor:
        executor.map(run, files)
    log.debug("Program ends at " + str(time() - start_time))


def nonthreadingSlave(data):
    try:
        text = requests.get(BASE + str(data)).text
    except:
        log.error(" can't open link " + str(data))
        log.error("Error code is " + requests.get(BASE + str(data)).status_code)
    else:
        with open(HTML + '/' + str(data) + '.txt', 'w') as file:
            file.write(text)
            log.debug(' saved ' + str(data))


def run(data):
    try:
        nonthreadingSlave(data)
    except KeyboardInterrupt:
        log.debug("Forsed to stop")
    else:
        log.debug("Finished")


