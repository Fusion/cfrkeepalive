#!/usr/bin/python

from os import remove
from sys import exit
from time import time

maxpossumtime = 300
filename = '/home/clicdev/public_html/tmp/cfrkeepalive.txt'
hostname = 'tvhub1'
retcode = 0
retmsg = ('%s says: Everything is shiny!' % hostname)

try:
    with open(filename) as f:
        s = f.read()
        if time() - int(s) > maxpossumtime:
            retcode = 1
            retmsg = ("%s says: It's been too long, son!" % hostname)
    #remove(filename)
except IOError:
    retcode = 1
    retmsg = ('%s says: Nothing! This is quite alarming.' % hostname)

print retmsg
exit(retcode)
