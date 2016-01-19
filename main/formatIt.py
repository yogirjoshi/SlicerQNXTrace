#!/usr/bin/python
'''
Created on Jan 11, 2016

@author: y2joshi
'''

import sys
import csv
if __name__ == '__main__':

    offset = 0
    currOffset = 0
    notEOF = True
    sliceCount = 0
    while notEOF == True:
        eventsToNum={}
        eid = 1
        try:
            with open(sys.argv[1]) as csvfile:
                rowCount = 0
                csvfile.seek(currOffset)
                #print currOffset
                reader = csv.reader(csvfile)
                notEOF = False
                for row in reader:
                    notEOF = True
                    if row[2] == "INT_ENTR" or row[2] == "INT_EXIT" or row[2] == "INT_HANDLER_ENTR" or row[2] == "INTR_HANDLER_EXIT":   
                        keyIntr = str(row[2]) + str(row[3]) + str(row[8])                  
                        if eventsToNum.has_key(keyIntr):
                            evtNum =  eventsToNum.get(keyIntr)
                        else:
                            eventsToNum[keyIntr]  = eid   
                            eid = eid + 1  
                    rowCount = rowCount + 1
                    offset = offset + sys.getsizeof(row)               
                    if rowCount > int(sys.argv[2]):
                        break   
        finally:
            csvfile.close()   
             
        linenum = 1
        try:
            with open(sys.argv[1]) as csvfile:
                rowCount = 0
                csvfile.seek(currOffset)
                reader = csv.reader(csvfile)
                outFileName = sys.argv[1].split(".")[0] + str(sliceCount) + ".txt"
                print "Writing Slice - " + outFileName
                outFile = open(outFileName,"w")
                for row in reader:
                    if linenum == 1:
                        outFile.write("time, traceEvent, eventName")
                        #print "time, traceEvent, eventName"
                        linenum = linenum + 1
                        continue
                    
                    if row[2] == "INT_ENTR" or row[2] == "INT_EXIT" or row[2] == "INT_HANDLER_ENTR" or row[2] == "INTR_HANDLER_EXIT":   
                        keyIntr = str(row[2]) + str(row[3]) + str(row[8])                  
                        if eventsToNum.has_key(keyIntr):
                            evtNum =  eventsToNum.get(keyIntr)
                            outFile.write(str(row[0]) + "," + str(evtNum) + "," + str(keyIntr) + "\n")
                            #print(str(row[0]) + "," + str(evtNum) + "," + str(keyIntr))
                            
                    else:    
                        outFile.write(str(row[0]) + "," + str(eid) + "," + "NA" + "\n")   
                        #print(str(row[0]) + "," + str(eid) + "," + "NA")   
                    rowCount = rowCount + 1   
                    if rowCount > int(sys.argv[2]):
                        break        
                    
        finally:
            csvfile.close()  
            outFile.close()
            
        currOffset = offset     
        sliceCount = sliceCount + 1       
