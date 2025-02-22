class LookupGen():
    def __init__(self):
        self.lookupHash={}

    def generateLookupTable(self):
        with open("lookupTable.csv", "r") as file:
            for line in file:
                line=line.strip()
                dataCols = line.split(",")
                if len(dataCols)==3:
                    self.lookupHash[(dataCols[0],dataCols[1])]=dataCols[2]
        return self.lookupHash

if __name__=="__main__":
    lg=LookupGen()
    lg.generateLookupTable()