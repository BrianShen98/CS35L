#!/usr/bin/python

import sys, locale, string
from optparse import OptionParser


def cmpFile(name1, name2,op1,op2,op3,unsorted):

    file1 = sys.stdin if name1 == '-' else  open(name1,'r')
    file2 = sys.stdin if name2 == '-' else  open(name2,'r')
    content1 = file1.read().splitlines()
    content2 = file2.read().splitlines()

    length1 = len(content1)
    length2 = len(content2)
    if not unsorted:
        length = length1 if length1 > length2 else length2

        for index in range(length):
            if index<length1 and index < length2:
                if content1[index] == content2[index]:
                    if not op3:
                        print('\t' * (2 - op1 - op2) + content1[index])
          
                elif content1[index] < content2[index]:
                    if not op1:
                        print(content1[index])
                    if not op2:
                        print('\t' * (1-op1)+ content2[index])
           
                else:
                    if not op2:
                        print('\t' * (1-op1)+ content2[index])
                    if not op1:
                        print(content1[index])
            else:
                if index < length1:
                    if not op1:
                        print(content1[index])
                else:
                    if not op2:
                        print('\t' * (1-op1) + content2[index])
    
    else:
        sameObj = []
        for index in range(length1):
            for num in range(length2):
                if(content1[index] == content2[num]):
                    #store the same object to check unique word in file2 later
                    sameObj.append(content1[index])
                    if not op3:
                        print('\t' * (2-op1-op2) + content1[index])
        
        unique2A = [x for x in content1 if x not in sameObj]
        for index in range(len(unique2A)):
            if not op1:
                print(unique2A[index])

        unique2B = [x for x in content2 if x not in sameObj]
        for index in range(len(unique2B)):
            if not op2:
                print('\t' * (1-op1) + unique2B[index])

    file1.close()
    file2.close()

def main():
    version_msg = "%prog Beta"
    usage_msg = "%prog [OPTION] file1 file2"

    parser = OptionParser(version=version_msg,usage=usage_msg)

    parser.add_option("-1", action = "store_true", dest = "op1",
                      default = False, help = "Suppress the output column of lines unique to file1")
    parser.add_option("-2", action = "store_true", dest = "op2",
                      default = False, help = "Suppress the output column of lines unique to file2")
    parser.add_option("-3", action = "store_true", dest = "op3",
                      default = False, help = "Suppress the output column of lines duplicated in file1 and file2")
    parser.add_option("-u", action = "store_true",dest = "unsorted",
                      default = False, help = "compare two unsorted files")

    option,args = parser.parse_args(sys.argv[1:])

    if len(args) != 2:
        parser.error("wrong number of operands")

    cmpFile(args[0],args[1],option.op1,option.op2,option.op3,option.unsorted)

    

if __name__ == "__main__":
    main()
        
