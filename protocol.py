import socket
class ProtocolGen():
    def getProtocolName(prtclNum):
        try:
            ip_proto={v:k[8:] for (k,v) in vars(socket).items() if k.startswith('IPPROTO')}
            return ip_proto[prtclNum].lower()
        except KeyError as e:
            print(f"ERROR: KeyError: {e}, for protocol_number input: {prtclNum}")
            return "UNKNOWN_PROTOCOL"
        except:
            print(f"ERROR: unknown error: {e}")
            return "UNKNOWN_ERROR"
