#!/usr/bin/python
'''
Created on Jan 11, 2016

@author: y2joshi
'''
import getopt, sys
import csv

if __name__ == '__main__':
    eventsToNum={}
    eid = 1
    tLimit = None
    aLimit = None
    regExDim = None
    fileName = None
    outFileName = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], "f:t:a:o:")
        
    except getopt.GetoptError as err:
        # print help information and exit:
        print str(err) # will print something like "option -a not recognized"
        #usage()
        sys.exit(2)
        
    for o, a in opts:
        if o == "-f":
            fileName = a
        if o == "-t":
            tLimit = int(a)
        if o == "-o":
            outFileName = a    
        elif o == "-a":
            aLimit = int(a)
    
    if tLimit == None or aLimit == None or outFileName == None:
        print("Not all parameters supplied")
        sys.exit(2)    
                
    try:
        #print("Here")
        csvfile = open(fileName)
        rowCount = 0
        #outFileName = fileName.split(".")[0] + "out.txt"
        outFile = open(outFileName,"w")
        reader = csv.reader(csvfile)
        print "Writing Slice - " + outFileName
        linenum = 1
        for row in reader:
            if linenum == 1:
                linenum = linenum + 1
                continue   
            skip = False         
            keyIntr = str(row[2]) + str(row[3])  
                            
            if eventsToNum.has_key(keyIntr):
                evtNum =  eventsToNum.get(keyIntr)                        
            else:
                if eid > aLimit:
                    skip = True
                else:    
                    eventsToNum[keyIntr]  = eid   
                    evtNum = eid
                    eid = eid + 1
                    
            if not skip:          
                outFile.write(str(row[0]) + "," + str(evtNum) + "," + str(keyIntr) + "\n")    
                rowCount = rowCount + 1       
 
            if rowCount > tLimit:
                break   
    finally:
        print("Done")
        csvfile.close()   
        outFile.close() 