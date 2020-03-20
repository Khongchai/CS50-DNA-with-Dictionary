# CS50-DNA-with-Dictionary

from sys import argv
import re
import csv

if len(argv) != 3:
    print("Error: incorrect command line")
    exit(1)

with open(argv[2], "r") as filesequence:
    FiveTemp = 0
    FourTemp = 0
    EightTemp = 0
    FourSTR = {
            "AATG": 0,
            "GATA": 0,
            "TATC": 0,
            "GAAA": 0,
            "TCTG": 0
        }
    FiveSTR = {
        "AGATC": 0,
        "TCTAG": 0
        }

    EightSTR = {"TTTTTTCT": 0}
    sequence = filesequence.read() #copy text to sequence
    sequenceLength = len(sequence)
    for i in range(sequenceLength - 4): #keep going until last four values (min val for STR length)

        FivecharFromi = ""
        FourcharFromi = ""
        FivecharFromfive = ""
        FourcharFromfour = ""
        EightcharFromi = ""
        EightcharFromeight = ""


        for j in range(8):
            if ((i+j) > sequenceLength):
                break
            else:
                if (i+8+j < sequenceLength): #if the next eight char is still not out of range:
                    EightcharFromeight += sequence[i+8+j]
                    EightcharFromi += sequence[i+j]

                if j < 5:
                    FivecharFromi += sequence[i+j]
                    if (i+5+j < sequenceLength):   #if still not out of range
                        FivecharFromfive += sequence[i+5+j]

                        if j < 4: #only when j is four
                            FourcharFromi += sequence[i+j]
                            if (i+4+j < sequenceLength):   #if still not out of range
                                FourcharFromfour += sequence[i+4+j]
        #--------------------------------------------------------------------------------------------------------------------
        for STR in FiveSTR:
            if (FivecharFromi == STR):
                FiveTemp += 1

                if (FivecharFromfive == STR):     #Check if five char from five is the matched string
                    if (FiveTemp > FiveSTR[STR]): #if current is more than max; if max is no longer max,
                        FiveSTR[STR] = FiveTemp   # current value to max(continuous) value.
                else:                             #If Fivecharfromfive is not the matched string; reach the end of the combo,
                    if (FiveTemp > FiveSTR[STR]): #then, still check if current is more than max,
                        FiveSTR[STR] = FiveTemp   #but after copy the value, to max,
                    FiveTemp = 0                  #then set current value to 0
                break

        #--------------------------------------------------------------------------------------------------------------------
        for STR in FourSTR:
            if (FourcharFromi == STR):
                FourTemp += 1
                if (FourcharFromfour == STR):     #Check if five char from five is the matched string
                    if (FourTemp > FourSTR[STR]): #if current is more than max; if max is no longer max,
                        FourSTR[STR] = FourTemp   # current value to max(continuous) value.
                else:                             #If Fivecharfromfive is not the matched string; reach the end of the combo,
                    if (FourTemp > FourSTR[STR]): #then, still check if current is more than max,
                        FourSTR[STR] = FourTemp   #but after copy the value, to max,
                    FourTemp = 0                  #then set current value to 0
                break
        #---------------------------------------------------------------------------------------------------------------------
        for STR in EightSTR:
            if (EightcharFromi == STR):
                EightTemp += 1
                if (EightcharFromeight == STR):     #Check if five char from five is the matched string
                    if (EightTemp > EightSTR[STR]): #if current is more than max; if max is no longer max,
                        EightSTR[STR] = EightTemp   # current value to max(continuous) value.
                else:                             #If Fivecharfromfive is not the matched string; reach the end of the combo,
                    if (EightTemp > EightSTR[STR]): #then, still check if current is more than max,
                        EightSTR[STR] = EightTemp   #but after copy the value, to max,
                    EightTemp = 0                  #then set current value to 0
                break

    #print(FourSTR, FiveSTR, EightSTR)

    with open(argv[1], 'r') as filePeople:
        reader = csv.reader(filePeople)
        header = next(reader)
        #Empty Dict for people
        People = {}


        #get values from the STR dict
        IndexedDict = {
            "AGATC": FiveSTR["AGATC"],
            "TTTTTTCT": EightSTR["TTTTTTCT"],
            "AATG": FourSTR["AATG"],
            "TCTAG": FiveSTR["TCTAG"],
            "GATA": FourSTR["GATA"],
            "TATC": FourSTR["TATC"],
            "GAAA": FourSTR["GAAA"],
            "TCTG": FourSTR["TCTG"]
        }
        print(f"IndexedDict = {IndexedDict}")

        for row in reader:
            People[row[0]] = {
                "AGATC": int(row[1]),
                "TTTTTTCT":int(row[2]),
                "AATG": int(row[3]),
                "TCTAG": int(row[4]),
                "GATA": int(row[5]),
                "TATC": int(row[6]),
                "GAAA": int(row[7]),
                "TCTG": int(row[8])
            }
            if People[row[0]] == IndexedDict:
                print(f"Found! It's {row[0]}")
                exit(0)

print("Not found")

