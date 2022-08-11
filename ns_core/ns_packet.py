
import enum
### Enum for Packet Type
class ns_packet_Type(enum.Enum):
    Data  = 1
    ChargeRequest = 2 
    AssignThreshold = 3
    AssignImportance = 4
    Forward = 5
    Command = 6

### packet 
class ns_packet:
    def __init__(self, src, dst, ptype= ns_packet_Type.Data):
        self.src = src 
        self.dst = dst 
        self.Type = ptype
        self.data = str()
    
    

