from protocol import ProtocolGen
from lookup import LookupGen
from collections import defaultdict
import os

class LogReader():
    def __init__(self):
        lg=LookupGen()
        self.lookupHash=lg.generateLookupTable()
        self.tagCount=defaultdict(int)
        self.protocolCount=defaultdict(int)

    def fileReader(self,fileLocation: str, mode: str):
        # print("self.lookupHash:",self.lookupHash)
        readSuccessFul=False
        with open(fileLocation, mode) as file:
            for line in file:
                line=line.strip()
                # print(line)
                dataCols = line.split(" ")
                if len(dataCols)==14 and int(dataCols[0])==2:
                    if not dataCols[7].isdigit():
                        print("Protocol input in log file is not valid.")
                        return "UNKNOWN_ERROR"
                    # print("dstport:",dataCols[6],", protocolName:",ProtocolGen.getProtocolName(int(dataCols[7])))
                    currDstPortProtoColTuple=(dataCols[6],ProtocolGen.getProtocolName(int(dataCols[7])))

                    # creating tagCount
                    if currDstPortProtoColTuple in self.lookupHash:
                        self.tagCount[self.lookupHash[currDstPortProtoColTuple]]=self.tagCount[self.lookupHash[currDstPortProtoColTuple]]+1
                    else:
                        self.tagCount["Untagged"]=self.tagCount["Untagged"]+1

                    
                    # creating protocolCount
                    if currDstPortProtoColTuple in self.lookupHash:
                        self.protocolCount[currDstPortProtoColTuple]=self.protocolCount[currDstPortProtoColTuple]+1

                    readSuccessFul=True

        if readSuccessFul:
            # write to both files
            print("Writing")
            os.makedirs(os.path.dirname("outputFiles/my_file1.txt"), exist_ok=True)
            os.makedirs(os.path.dirname("outputFiles/my_file2.txt"), exist_ok=True)
            file = open("outputFiles/my_file1.txt", "w")
            for tag,count in self.tagCount.items():
                writeVal=tag+","+str(count)+"\n"+"\n"
                file.write(writeVal)
            file.close()
            file = open("outputFiles/my_file2.txt", "w")
            for key,count in self.protocolCount.items():
                port=key[0]
                protocol=key[1]
                writeVal=port+","+protocol+","+str(count)+"\n"+"\n"
                file.write(writeVal)
            file.close()
        else:
            print("ERROR: reading was not possible")

if __name__=="__main__":
    logG=LogReader()
    logG.fileReader("flowLogData.log","r")