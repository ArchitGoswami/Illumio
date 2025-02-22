import socket
class LogReader():
    def fileReader(fileLocation,mode):
        with open(fileLocation, mode) as file:
            for line in file:
                print(line.strip())


if __name__=="__main__":
    LogReader.fileReader("flowLogData.log","r")