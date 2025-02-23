import unittest
from protocol import ProtocolGen
from logReader import LogReader

class UnitTests(unittest.TestCase):
    
############################################ PROTOCOL TESTS ############################################
    def test_protocolTestTCP(self):
        # Protocol number 6: TCP
        print("LOG: Running test_protocolTestTCP")
        self.assertEqual(ProtocolGen.getProtocolName(6), "tcp")
        print("________________________________________________________________________________________________________")

    def test_protocolTestIPv4(self):
        # Protocol number 4: IPV4
        print("LOG: Running test_protocolTestIPv4")
        self.assertEqual(ProtocolGen.getProtocolName(4), "ipv4")
        print("________________________________________________________________________________________________________")

    def test_protocolTestUDP(self):
        # Protocol number 17: UDP
        print("LOG: Running test_protocolTestUDP")
        self.assertEqual(ProtocolGen.getProtocolName(17), "udp")
        print("________________________________________________________________________________________________________")

    def test_protocolTestICMP(self):
        # Protocol number 17: icmp
        print("LOG: Running test_protocolTestICMP")
        self.assertEqual(ProtocolGen.getProtocolName(1), "icmp")
        print("________________________________________________________________________________________________________")

    # def test_protocolTestUnknown(self):
    #     self.assertEqual(ProtocolGen.getProtocolName(207), "UNKNOWN_PROTOCOL")

    # def test_protocolTestUnknown(self):
    #     self.assertEqual(ProtocolGen.getProtocolName("abc"), "UNKNOWN_PROTOCOL")
    
########################################################################################################

############################################ LOG READER TESTS ############################################


    def test_logReaderTestForDefaultInput(self):
        print("LOG: Running test_logReaderTestForDefaultInput")
        logG=LogReader("test/inputFiles/defaultLookupTable.csv")
        logG.orchestrator("test/inputFiles/defaultFlowLogData.log","test/outputFiles/logReaderTestForDefaultInput/")
        print("________________________________________________________________________________________________________")

    def test_logReaderTestForSingleInputWithDefaultLookupTable(self):
        print("LOG: Running test_logReaderTestForSingleInputWithDefaultLookupTable")
        logG=LogReader("test/inputFiles/defaultLookupTable.csv")
        logG.orchestrator("test/inputFiles/singleFlowLogData.log","test/outputFiles/logReaderTestForSingleInputWithDefaultLookupTable/")
        print("________________________________________________________________________________________________________")

    def test_logReaderTestForSingleInputWithEmptyLookupTable(self):
        print("LOG: Running test_logReaderTestForSingleInputWithEmptyLookupTable")
        logG=LogReader("test/inputFiles/emptyLookupTable.csv")
        logG.orchestrator("test/inputFiles/singleFlowLogData.log","test/outputFiles/logReaderTestForSingleInputWithEmptyLookupTable/")
        print("________________________________________________________________________________________________________")

    def test_logReaderTestForDefaultInputWithEmptyLookupTable(self):
        print("LOG: Running test_logReaderTestForDefaultInputWithEmptyLookupTable")
        logG=LogReader("test/inputFiles/emptyLookupTable.csv")
        logG.orchestrator("test/inputFiles/defaultFlowLogData.log","test/outputFiles/logReaderTestForDefaultInputWithEmptyLookupTable/")
        print("________________________________________________________________________________________________________")

    def test_logReaderTestForEmptyInputWithDefaultLookupTable(self):
        print("LOG: Running test_logReaderTestForEmptyInputWithDefaultLookupTable")
        logG=LogReader("test/inputFiles/defaultLookupTable.csv")
        logG.orchestrator("test/inputFiles/EmptyFlowLogData.log","test/outputFiles/logReaderTestForEmptyInputWithDefaultLookupTable/")
        print("________________________________________________________________________________________________________")


########################################################################################################

############################################ LOG READER TESTS ############################################

    def test_protocolTestICMP(self):
        # Protocol number 17: icmp
        print("LOG: Running test_protocolTestICMP")
        self.assertEqual(ProtocolGen.getProtocolName(1), "icmp")