#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expiringdict import ExpiringDict

def cln(word):
    word1 = "("
    word11 = ")"

    word2 = "،"
    word21 = ","

    word3 = "ست"

    word4 = "‌ي"
    word41 = "ی"

    word5 = "‌ها"
    word51 = "های"
    word52 = "هایی"

    word6 = "‌اي"
    word61 = "ای"

    if (word[0:1] == word1):
        temp1 = word[1:word.__len__()]
    else:
        temp1 = word

    if (temp1[temp1.__len__() - 1:temp1.__len__()] == word11):
        temp = temp1[0:temp1.__len__() - 1]
    else:
        temp = temp1

    if (temp[temp.__len__() - 2:temp.__len__()] == word2):
        temp2 = temp[0:word.__len__() - 2]

    elif (temp[temp.__len__() - 1:temp.__len__()] == word21):
        temp2 = temp[0:temp.__len__() - 1]
    else:
        temp2 = temp

    if (temp2[temp2.__len__() - 4:temp2.__len__()] == word3):
        temp3 = temp2[0:temp2.__len__() - 4]
    else:
        temp3 = temp2

    if (temp3[temp3.__len__() - 5:temp3.__len__()] == word4):
        temp4 = temp3[0:temp3.__len__() - 5]

    elif (temp3[temp3.__len__() - 2:temp3.__len__()] == word41):
        temp4 = temp3[0:temp3.__len__() - 2]

    else:
        temp4 = temp3

    if (temp4[temp4.__len__() - 8:temp4.__len__()] == word52):
        temp5 = temp4[0:temp4.__len__() - 8]


    elif (temp4[temp4.__len__() - 7:temp4.__len__()] == word5):
        temp5 = temp4[0:temp4.__len__() - 7]

    elif (temp4[temp4.__len__() - 6:temp4.__len__()] == word51):
        temp5 = temp4[0:temp4.__len__() - 6]

    else:
        temp5 = temp4

    if (temp[temp.__len__() - 7:temp.__len__()] == word6):
        temp6 = temp[0:temp.__len__() - 7]
    elif (temp[temp.__len__() - 4:temp.__len__()] == word61):
        temp6 = temp[0:temp.__len__() - 4]
    elif (temp5[temp5.__len__() - 7:temp5.__len__()] == word6):
        temp6 = temp5[0:temp5.__len__() - 7]
    elif (temp5[temp5.__len__() - 4:temp5.__len__()] == word61):
        temp6 = temp5[0:temp5.__len__() - 4]
    else:
        temp6 = temp5

    return temp6



clean = {}
file = open("aresult.txt","w")

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

    clean[key] = value
sum =0
for k in clean:

    if(cln(k) in clean and cln(k) != k ):
        clean[cln(k)] = clean[cln(k)] + clean[k] +1
        clean[k] = 0
        sum = sum + clean[cln(k)]

    else:
        clean[k] = clean[k] +1
        sum = sum + clean[k]






for k, v in clean.items():

    if(v  != 0):

        file.write(k + '\t' + str(float(v)/float(44315)) +  '\t' + str(v) +  '\n')

file.close()


###########################################################################################







