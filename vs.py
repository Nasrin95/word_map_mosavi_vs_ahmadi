#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expiringdict import ExpiringDict




file = open("InAhmadiNotMosavi.txt","w")

mosavi = {}
for line in open("mosaviwords.txt"):
    cnt = 0
    for word in line.split("\t"):
        cnt = cnt + 1
        if(cnt % 2 == 1):
            if(word is None):
                continue
            else:
                key = word

        else:
            value = int(word)

    mosavi[key] = value

ahmadi = {}
for line in open("ahmadinejadwords.txt"):
    cnt = 0
    for word in line.split("\t"):
        cnt = cnt + 1
        if(cnt % 2 == 1):
            if(word is None):
                continue
            else:
                key = word

        else:
            value = int(word)

    ahmadi[key] = value






diff = {}

for  k in ahmadi:
        if((k in mosavi) == False):
            diff[k] = ahmadi[k]



for k, v in diff.items():

        file.write(k + '\t' + str(int(v)) +  '\n')

file.close()


###########################################################################################







