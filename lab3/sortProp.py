#!/usr/bin/python

import sys,locale,string

#find all objects and propositions
def find_old_obj_prop():
    with open("oldObjNProp","w") as outFile:
        for i in range(469):
            with open("./sentence-completed/%s.instenv" % i,"r") as inFile:
                outFile.write('\n' + inFile.readline() + '\nProposition: ');
                #find all the propositions
                prop = set(inFile.read().replace('\n',',').split(','));
                for elem in prop:
                   # if(elem.count("state") != 0):
                        outFile.write(elem );
                outFile.write('\n\n\n');

#find all propositions involving 2 objects
def find_2_prop():
    with open("2ObjProp","w") as outFile:
        for i in range(469):
            with open("./sentence-completed/%s.instenv" % i,"r") as inFile:
                outFile.write('\n' + inFile.readline() + '\n');
                #find all the propositions
                prop = set(inFile.read().replace('\n',',').split(','));
                for elem in prop:
                    if(elem.count(' ') ==2):
                        outFile.write(elem);
                outFile.write('\n');

#find all propositions has "states"
def find_state_prop():
    prop = set();
    with open("stateProp","w") as outFile:
        for i in range(469):
            with open("./sentence-completed/%s.instenv" % i,"r") as inFile:
               # outFile.write('\n' + inFile.readline() + '\n');
                inFile.readline();
                #find all the propositions
                prop = prop | set(inFile.read().replace('\n',',').split(','));
                
        for elem in prop:
            if(elem.count("state") != 0):
                outFile.write(elem);

            

def main():
    if len(sys.argv) != 2:
        print("Please specify an option!");
        exit(1);
    
    if sys.argv[1] == "old":
        find_old_obj_prop();
    elif sys.argv[1] == "2prop":
        find_2_prop();
    elif sys.argv[1] == "stateprop":
        find_state_prop();
    else:
        print("cannot recognize the command!");
        exit(1);
        
if __name__ == "__main__":
    main();
