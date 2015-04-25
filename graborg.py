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
    parser = argparse.ArgumentParser(description="graborg: file analysis tool")
    parser.add_argument("-u", "--url", required=True, type=str, \
    help="Set URL address to retrieve file from")
    parser.add_argument("-p", "--proxy", nargs='?', const="127.0.0.1:8118",
    type=str, help="Used to set proxy set by default address. Eg. \
    192.168.0.254:8080. Localhost Privoxy set by default")
    args = parser.parse_args()

    return args


def grab(url, filename, proxy):
    '''
    download sample
    '''

    # Check samples directory exists. If not make it.
    filedir = "samples/"
    if not os.path.exists('%s' % filedir):
        os.mkdir('%s' % filedir)


    opener = urllib2.build_opener()
    if proxy == True:
        proxyh = urllib2.ProxyHandler({'http': '127.0.0.1:8118'})
        opener = urllib2.build_opener(proxyh)

    opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36')]
    urllib2.install_opener(opener)
    filed = opener.open('%s' % url).read()
    fout = open("samples/%s" % filename, 'wb')
    fout.write(filed)
    fout.close()


def org(NAME, sample):
    '''
    Md5 downloaded file, write details to log file and rename ot md5 hash.
    '''

    filedir = "samples/"
    logfile_name = "graborg-log.csv"

    if not os.path.isfile('%s' % logfile_name):
        shutil.copyfile('%s-template' % logfile_name, logfile_name)

    # Generate File MD5
    md5 = hashlib.md5(open('samples/%s' % NAME).read()).hexdigest()

    #Add file details to CSV file
    logf = open("graborg-log.csv", "a+")
    fsize = os.stat(os.path.join(filedir, NAME)).st_size
    entry = '{0},{1},{2},{3},{4}'.format(
        md5, NAME, fsize, datetime.now().strftime("%d/%m/%Y %H:%M:%S"), sample)

    logf.write(entry + '\n')
    logf.close()
    print entry
    shutil.move(os.path.join(filedir, NAME), os.path.join(filedir, md5))



def main():
    '''
    main graborg process
    '''

    # validate that the command line arguments are correct
    args = parse_args()

    # Set variables and call run program
    sample = args.url
    NAME = sample.split('/')[-1]
    proxy = args.proxy
    grab(sample, NAME, proxy)
    org(NAME, sample)


if __name__ == "__main__":
    main()
