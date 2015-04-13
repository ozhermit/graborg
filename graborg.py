#!/usr/bin/env python
'''
Used to download samples and keep track of them over
time allowing for files with the same name etc.
'''

import os
import hashlib
from datetime import datetime
import shutil
import urllib2
import argparse


def parse_args():
    '''
    parse the in-line arguments.
    '''
    parser = argparse.ArgumentParser(description="garborg: file analysis tool")
    parser.add_argument("-u", "--url", required=True, type=str)
    args = parser.parse_args()

    return args


def grab(url, filename):
    '''
    download sample
    '''
    opener = urllib2.build_opener()
    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
    file = opener.open('%s' % url)
    filed = file.read()
    f = open("samples/%s" % filename, 'wb')
    f.write(filed)
    f.close()


def org(NAME, sample):
    '''
    Md5 downloaded file, write details to log file and rename ot md5 hash.
    '''
    md5 = hashlib.md5(open('samples/%s' % NAME).read()).hexdigest()
    logf = open("graborg-log.csv", "a+")
    fsize = os.stat('samples/%s' % NAME).st_size
    entry = '{0},{1},{2},{3},{4}'.format(
        md5, NAME, fsize, datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        sample
    )
    logf.write(entry + '\n')
    logf.close()
    shutil.move('samples/%s' % NAME, 'samples/%s' % md5)


def reqcheck():
    '''
    Check the logging file and samples directory exists
    '''
    filedir = "samples/"
    filelog = "graborg-log.csv"

    if not os.path.exists('%s' % filedir):
        os.mkdir('%s' % filedir)
    if not os.path.isfile('%s' % filelog):
        shutil.copyfile('graborg-log.csv-template', 'graborg-log.csv')


def main():
    '''
    main graborg process
    '''

    # validate that the command line arguments are correct
    args = parse_args()

    # sample becomes a arg namespace
    sample = args.url
    NAME = sample.split('/')[-1]
    reqcheck()
    grab(sample, NAME)
    org(NAME, sample)


if __name__ == "__main__":
    main()
