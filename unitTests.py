import unittest
from protocol import ProtocolGen
class UnitTests(unittest.TestCase):
    def test_protocolTestTCP(self):
        # Protocol number 6: TCP
        self.assertEqual(ProtocolGen.getProtocolName(6), "TCP")

    def test_protocolTestIPv4(self):
        # Protocol number 4: IPV4
        self.assertEqual(ProtocolGen.getProtocolName(4), "IPV4")

    def test_protocolTestIPv4LowerCasev(self):
        self.assertNotEqual(ProtocolGen.getProtocolName(4), "IPv4")

    def test_protocolTestUDP(self):
        # Protocol number 17: UDP
        self.assertEqual(ProtocolGen.getProtocolName(17), "UDP")

    # def test_protocolTestUnknown(self):
    #     self.assertEqual(ProtocolGen.getProtocolName(207), "UNKNOWN_PROTOCOL")

    # def test_protocolTestUnknown(self):
    #     self.assertEqual(ProtocolGen.getProtocolName("abc"), "UNKNOWN_PROTOCOL")

if __name__ == '__main__':
        unittest.main()