# from lookup import LookupGen
from logReader import LogReader
from unitTests import UnitTests
import unittest
import os
import shutil
import argparse

def fileClear():
    # deletes folders containing old output files
    folders = ["test/outputFiles","outputFiles"] 
    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder) # For non-empty folders
                print("LOG: Folder '",folder,"' deleted successfully.")
            except OSError as e:
                print("LOG: Error deleting folder '",folder,"':",e)
        else:
            print("LOG: Folder '",folder,"' does not exist.")

if __name__=="__main__":
    
    s="_"*110
    lineSep=s+"\n"+s

    parser = argparse.ArgumentParser(description="Flags to see unit tests and to take custom filepaths for flowLogSource read, write, and lookupTableSource read")
    parser.add_argument("-u", action='store_true')
    parser.add_argument("--lookupTableSource", required=False, type=str)
    parser.add_argument("--flowLogSource", required=False, type=str)
    parser.add_argument("--writeSource", required=False, type=str)
    args = parser.parse_args()
    lookupTableSource = args.lookupTableSource
    flowLogSource     = args.flowLogSource       
    writeSource       = args.writeSource       
    runUnitTests      = args.u

    fileClear()
    print(lineSep)
    if runUnitTests:
        print("LOG: Running Tests")
        unittest.main(argv=[__file__])      # runs all unit tests
        print(lineSep)

    else:
        if lookupTableSource is None:  
            lookupTableSource="inputFiles/lookupTable"
        if flowLogSource is None:  
            flowLogSource="inputFiles/flowLogData"
        if writeSource is None:  
            writeSource="outputFiles/"
        print("LOG: Running user files")
        print(lineSep)

        logG=LogReader(lookupTableSource)
        logG.orchestrator(flowLogSource, writeSource) # calls log Reader orchestrator
        print(lineSep) 