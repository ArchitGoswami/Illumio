# from lookup import LookupGen
from logReader import LogReader
from test.unitTests import UnitTests
import unittest
import os
import shutil


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
    

print("___________________________________________________________________________________________________\n___________________________________________________________________________________________________")


# runs all unit tests
print("LOG: Running Tests")
unittest.main(exit=False)

##########################################################################
# generated lookupTable hash from csv file
# lg=LookupGen()
# lg.generateLookupTable()
##########################################################################



print("___________________________________________________________________________________________________\n___________________________________________________________________________________________________")
print("LOG: Running user files")

print("___________________________________________________________________________________________________\n___________________________________________________________________________________________________")
# calls log Reader
logG=LogReader()
logG.orchestrator()

print("___________________________________________________________________________________________________\n___________________________________________________________________________________________________")