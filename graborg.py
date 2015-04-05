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
LOGF = open("graborg-log.csv", "a+")
FNAME = SAMPLE.split('/')
NAME = FNAME[-1]
os.system('curl -o /security/samples/sort/%s -A "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.115 Safari/537.36" %s ' %(NAME, SAMPLE))
MD5 = hashlib.md5(open('/security/samples/sort/%s' %NAME).read()).hexdigest()
NOW = (time.strftime("%d/%m/%Y %H:%M:%S"))
ENTRY = "%s,%s,%s,%s" % (MD5, NAME, NOW, SAMPLE)
LOGF.write(ENTRY + '\n')
os.system('mv /security/samples/sort/%s /security/samples/sort/%s' % (NAME, MD5))
print "MD5 = %s  ||  FILNAME = %s  ||  Time Retrieved = %s  || Source = %s" % (MD5, NAME, NOW, SAMPLE)
