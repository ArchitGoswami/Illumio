class LookupGen():
    def __init__(self):
        self.lookupHash={}

    def generateLookupTable(self,source):
        print("LOG: Generating Lookup Table from source:",source)
        with open(source, "r") as file:
            for line in file:
                line=line.strip()
                dataCols = line.split(",")
                if len(dataCols)==3:
                    self.lookupHash[(dataCols[0],dataCols[1])]=dataCols[2]
        return self.lookupHash