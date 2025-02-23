from protocol import ProtocolGen
from lookup import LookupGen
from collections import defaultdict
import os

class LogReader():
    def __init__(self,lookupTableSource: str="inputFiles/lookupTable"):
        lg=LookupGen()
        # TODO: don't hardcode?
        self.lookupHash=lg.generateLookupTable(lookupTableSource)
        self.tagCount=defaultdict(int)
        self.protocolCount=defaultdict(int)
        
    def orchestrator(self,readSource: str="inputFiles/flowLogData", writeSource: str="outputFiles/"):
        print("LOG: Reading From:",readSource)
        readSuccessFul=self.readFile(readSource)
        if readSuccessFul:
            self.writeFile(writeSource)
        else:
            print("ERROR: reading was not possible")


    def readFile(self,source):
        readSuccessFul=False
        with open(source, "r") as file:
            for line in file:
                line=line.strip()
                dataCols = line.split(" ")
                if len(dataCols)==14 and int(dataCols[0])==2:
                    if not dataCols[7].isdigit():
                        print("ERROR: Protocol input in log file is not valid.")
                        return "UNKNOWN_ERROR"
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
        return readSuccessFul

    def writeFile(self,writeSource:str="outputFiles/"):
        # write to both files
        print("LOG: Writing to txt files")
        tagCountSource=writeSource+"tagCount"
        os.makedirs(os.path.dirname(tagCountSource), exist_ok=True)
        file = open(tagCountSource, "w")
        file.write("Tag Counts: \n\nTag,Count \n\n")
        for tag,count in self.tagCount.items():
            writeVal=tag+","+str(count)+"\n"+"\n"
            file.write(writeVal)
        file.close()
        print("LOG: Finished Writing to:",tagCountSource)

        PortProtocolCombinationCountSource=writeSource+"PortProtocolCombinationCount"
        os.makedirs(os.path.dirname(PortProtocolCombinationCountSource), exist_ok=True)
        file = open(PortProtocolCombinationCountSource, "w")
        file.write("Port/Protocol Combination Counts: \n\nPort,Protocol,Count \n\n")
        for key,count in self.protocolCount.items():
            port=key[0]
            protocol=key[1]
            writeVal=port+","+protocol+","+str(count)+"\n"+"\n"
            file.write(writeVal)
        file.close()
        print("LOG: Finished Writing to:",PortProtocolCombinationCountSource)