# from lookup import LookupGen
from logReader import LogReader
from test.unitTests import UnitTests
import unittest
import os
import shutil

def fileClear():
    # deletes folders containing old output files
    folders = ["test/outputFiles","outputFiles"] 
    for folder in folders:
        if os.path.exists(folder):
            try:
                shutil.rmtree(folder) # For non-empty folders
                print("LOG: Folder '",folder,"' deleted successfully.")
            except OSError as e:
                print(f"LOG: Error deleting folder '{folder}': {e}")
        else:
            print("LOG: Folder '",folder,"' does not exist.")

if __name__=="__main__":
    lineSep="_____________________________________________________________________________________________________________\n_____________________________________________________________________________________________________________"
    print(lineSep)
    print("LOG: Running Tests")
    unittest.main(exit=False)      # runs all unit tests

    print(lineSep)
    print("LOG: Running user files")
    print(lineSep)

    logG=LogReader()
    logG.orchestrator()            # calls log Reader orchestrator
    print(lineSep) 