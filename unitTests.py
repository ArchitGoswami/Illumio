import unittest
import os
from protocol import ProtocolGen
from logReader import LogReader
import filecmp

class UnitTests(unittest.TestCase):
    def setUp(self):
        self.lineSep="_____________________________________________________________________________________________________________"
        self.ppcFile="PortProtocolCombinationCount"
        self.tcFile="tagCount"
############################################ PROTOCOL GEN TESTS #############################################################
    def test_protocolTestTCP(self):
        # Protocol number 6: TCP
        print("LOG: Running test_protocolTestTCP")
        self.assertEqual(ProtocolGen.getProtocolName(6), "tcp")
        print(self.lineSep)

    def test_protocolTestIPv4(self):
        # Protocol number 4: IPV4
        print("LOG: Running test_protocolTestIPv4")
        self.assertEqual(ProtocolGen.getProtocolName(4), "ipv4")
        print(self.lineSep)

    def test_protocolTestUDP(self):
        # Protocol number 17: UDP
        print("LOG: Running test_protocolTestUDP")
        self.assertEqual(ProtocolGen.getProtocolName(17), "udp")
        print(self.lineSep)

    def test_protocolTestICMP(self):
        # Protocol number 17: icmp
        print("LOG: Running test_protocolTestICMP")
        self.assertEqual(ProtocolGen.getProtocolName(1), "icmp")
        print(self.lineSep)

    def test_protocolTestUnknownInt(self):
        print("LOG: Running test_protocolTestUnknownInt")
        self.assertEqual(ProtocolGen.getProtocolName(207), "UNKNOWN_PROTOCOL")
        print(self.lineSep)

    def test_protocolTestUnknownStr(self):
        print("LOG: Running test_protocolTestUnknownStr")
        print(self.assertEqual(ProtocolGen.getProtocolName("abc"), "UNKNOWN_PROTOCOL"))
        print(self.lineSep)
    
#########################################################################################################################

############################################ LOG READER AND LOOKUP GEN TESTS ############################################


    def test_logReaderTestForDefaultInput(self):
        print("LOG: Running test_logReaderTestForDefaultInput")
        logG=LogReader("test/inputFiles/defaultLookupTable")
        logG.orchestrator("test/inputFiles/defaultFlowLogData","test/outputFiles/logReaderTestForDefaultInput/")
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForDefaultInput/"+self.ppcFile,"test/comparisonFiles/logReaderTestForDefaultInput/"+self.ppcFile, shallow=False))
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForDefaultInput/"+self.tcFile,"test/comparisonFiles/logReaderTestForDefaultInput/"+self.tcFile, shallow=False))
        print(self.lineSep)

    def test_logReaderTestForSingleInputWithDefaultLookupTable(self):
        print("LOG: Running test_logReaderTestForSingleInputWithDefaultLookupTable")
        logG=LogReader("test/inputFiles/defaultLookupTable")
        logG.orchestrator("test/inputFiles/singleFlowLogData","test/outputFiles/logReaderTestForSingleInputWithDefaultLookupTable/")
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForSingleInputWithDefaultLookupTable/"+self.ppcFile,"test/comparisonFiles/logReaderTestForSingleInputWithDefaultLookupTable/"+self.ppcFile, shallow=False))
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForSingleInputWithDefaultLookupTable/"+self.tcFile,"test/comparisonFiles/logReaderTestForSingleInputWithDefaultLookupTable/"+self.tcFile, shallow=False))
        print(self.lineSep)

    def test_logReaderTestForSingleInputWithEmptyLookupTable(self):
        print("LOG: Running test_logReaderTestForSingleInputWithEmptyLookupTable")
        logG=LogReader("test/inputFiles/emptyLookupTable")
        logG.orchestrator("test/inputFiles/singleFlowLogData","test/outputFiles/logReaderTestForSingleInputWithEmptyLookupTable/")
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForSingleInputWithEmptyLookupTable/"+self.ppcFile,"test/comparisonFiles/logReaderTestForSingleInputWithEmptyLookupTable/"+self.ppcFile, shallow=False))
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForSingleInputWithEmptyLookupTable/"+self.tcFile,"test/comparisonFiles/logReaderTestForSingleInputWithEmptyLookupTable/"+self.tcFile, shallow=False))
        print(self.lineSep)

    def test_logReaderTestForDefaultInputWithEmptyLookupTable(self):
        print("LOG: Running test_logReaderTestForDefaultInputWithEmptyLookupTable")
        logG=LogReader("test/inputFiles/emptyLookupTable")
        logG.orchestrator("test/inputFiles/defaultFlowLogData","test/outputFiles/logReaderTestForDefaultInputWithEmptyLookupTable/")
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForDefaultInputWithEmptyLookupTable/"+self.ppcFile,"test/comparisonFiles/logReaderTestForDefaultInputWithEmptyLookupTable/"+self.ppcFile, shallow=False))
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForDefaultInputWithEmptyLookupTable/"+self.tcFile,"test/comparisonFiles/logReaderTestForDefaultInputWithEmptyLookupTable/"+self.tcFile, shallow=False))
        print(self.lineSep)

    def test_logReaderTestForEmptyInputWithDefaultLookupTable(self):
        print("LOG: Running test_logReaderTestForEmptyInputWithDefaultLookupTable")
        logG=LogReader("test/inputFiles/defaultLookupTable")
        logG.orchestrator("test/inputFiles/EmptyFlowLogData","test/outputFiles/logReaderTestForEmptyInputWithDefaultLookupTable/")
        self.assertFalse(os.path.exists("test/outputFiles/logReaderTestForEmptyInputWithDefaultLookupTable/"+self.ppcFile))
        self.assertFalse(os.path.exists("test/outputFiles/logReaderTestForEmptyInputWithDefaultLookupTable/"+self.tcFile))
        print(self.lineSep)

    def test_logReaderTestForMaxLoadInput(self):
        print("LOG: Running test_logReaderTestForMaxLoadInput")
        logG=LogReader("test/inputFiles/maxLoadLookupTable")
        logG.orchestrator("test/inputFiles/MaxLoadFlowLogData","test/outputFiles/logReaderTestForMaxLoadInput/")
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForMaxLoadInput/"+self.ppcFile,"test/comparisonFiles/logReaderTestForMaxLoadInput/"+self.ppcFile, shallow=False))
        self.assertTrue(filecmp.cmp("test/outputFiles/logReaderTestForMaxLoadInput/"+self.tcFile,"test/comparisonFiles/logReaderTestForMaxLoadInput/"+self.tcFile, shallow=False))
        print(self.lineSep)

###########################################################################################################################
