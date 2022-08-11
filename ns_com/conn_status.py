

import enum 

class ConnStatus(enum.Enum):
    Error = -1
    Disconnected = 0
    Connected = 1
    Closed = 2
