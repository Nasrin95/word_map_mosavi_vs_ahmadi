#!/usr/bin/env python
# -*- coding: utf-8 -*-

from expiringdict import ExpiringDict

cnt = 0

WordMap = {}

file = open("ahmadinejadResult.txt", "w")

for line in open("ahmadinejad.txt"):

    for word in line.split(" "):
        cnt = cnt + 1

        size = word.__len__()

        if word is None:
            del word
            continue

        ################################################################################################################


        if (size <= 2):

            del word

        else:

            # print word[word.__len__() - 1:word.__len__() - 0]
            # if (size % 2 ==1 and size >=5 and word[word.__len__() - 2:word.__len__() - 1]=="."):
            #     wordt1 = word[0:word.__len__() - 1]
            #     print "inlaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            #
            # else:
            #     word1 = word
            # print word1.__len__()
            if (word[word.__len__() - 1:word.__len__()] == " "):
                word1 = word[0:word.__len__() - 1]
            else:
                word1 = word

            if (word1[0:2] == "»" or word1[0:2] == "«"):
                word2 = word[2:word1.__len__()]
            else:
                word2 = word1

            if (word2[word2.__len__() - 2:word2.__len__()] == "»" or word2[word2.__len__() - 2:word2.__len__()] == "«"):
                word3 = word2[0:word2.__len__() - 2]
            else:
                word3 = word2

            if (word3[word3.__len__() - 2:word3.__len__()] == "؟" or word3[word3.__len__() - 2:word3.__len__()] == "؛"):
                word4 = word3[0:word3.__len__() - 2]

            elif (word3[word3.__len__() - 1:word3.__len__()] == "!" or word3[
                                                                       word3.__len__() - 1:word3.__len__()] == "." or word3[
                                                                                                                      word3.__len__() - 1:word3.__len__()] == ":" or word3[
                                                                                                                                                                     word3.__len__() - 1:word3.__len__()] == "،" or word3[
                                                                                                                                                                                                                    word3.__len__() - 1:word3.__len__()] == "،"):
                word4 = word3[0:word3.__len__() - 1]

            elif (word3.__len__() % 2 == 1 and word3.__len__() >= 5 and word3[0:3]=="   "):
                word4 = word3[3:word.__len__()]


            elif (word3.__len__() % 2 == 0 and word3[word3.__len__() - 2:word3.__len__() - 1] == "."):
                word4 = word3[0:word3.__len__() - 2]



            else:
                word4 = word3







                ########################################################################################################################
            if( word4 == "به" or word4 == "چه"   or word4 == "را"  or word4 == "بر"  or word4 == "که" or word4 == "با" or word4 == "از" or word4 == "در" or word4 == "هر" or word4 == "ها" or word4 == "یا"  or word4 == "آن" or word4 == "این" ):
                continue
            else:
                print word4
                if (word4 in WordMap):

                    WordMap[word4] = WordMap[word4] + 1

                else:
                    WordMap[word4] = 1



########################################################################################################################
# file.write(word + '\n')
for k, v in WordMap.items():
    file.write(k +  '\t' + str(v) + '\n')

file.close()


