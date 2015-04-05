#!/usr/bin/env python
'''
Used to download samples and keep track of them over
time allowing for files with the same name etc.
'''

import os
import sys
import hashlib
import time

SAMPLE = sys.argv[1]

#Check the csv to log results to has been moved from the template
if not os.path.exists('graborg-log.csv'):
    os.system('cp graborg-log.csv-template graborg-log.csv')

#Directory downloaded files are saved to
FILEDIR = "samples/"
if not os.path.exists('%s' % FILEDIR):
    os.system('mkdir %s' % FILEDIR)

LOGF = open("graborg-log.csv", "a+")
FNAME = SAMPLE.split('/')
NAME = FNAME[-1]
os.system('curl -o %s%s -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36" %s ' %(FILEDIR, NAME, SAMPLE))
MD5 = hashlib.md5(open('%s%s' %(FILEDIR, NAME)).read()).hexdigest()
NOW = (time.strftime("%d/%m/%Y %H:%M:%S"))
ENTRY = "%s,%s,%s,%s" % (MD5, NAME, NOW, SAMPLE)
LOGF.write(ENTRY + '\n')
os.system('mv %s%s %s%s' % (FILEDIR, NAME, FILEDIR, MD5))
print "MD5 = %s  ||  FILNAME = %s  ||  Time Retrieved = %s  || Source = %s" % (MD5, NAME, NOW, SAMPLE)
