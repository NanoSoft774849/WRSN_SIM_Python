
import socket
import threading
from ns_core.ns_node import *
from ns_com.conn_status import *
import asyncio

class ns_clientNode :

    def __init__(self, sock:socket.socket, node:ns_node):
        self.sock = sock
        self.node = node 
        self.buffer_size = 1024
        self.client_id = node.id
        self.rx_packet_count = 0
        self.tx_packet_count = 0
        self.port = 50000
        self.is_connected = False
        self.OnReceivePacketHandler = None
        self.OnDisConnectedHandler = None

    def connect(self, ip_addr : str , port : int) -> ConnStatus:
       #socket(family=AF_INET, type=SOCK_STREAM, proto=0, fileno=None
        try :
            if( self.sock == None):
                self.sock = socket.socket(family= socket.AddressFamily.AF_INET, type=socket.SOCK_STREAM)
                #return ConnStatus.Error
            self.sock.connect((ip_addr, port))
        except Exception as ex:
            print("Error {0} in Connection in node {1}".format(ex,self.client_id))
            return ConnStatus.Error
        print("{0} connected".format(self.client_id))
        self.is_connected = True
        return ConnStatus.Connected
    def SetHandlers(self, OnRxHandlerFx, OnDisconnectHandlerFx):
        self.OnReceivePacketHandler = OnRxHandlerFx
        self.OnDisConnectedHandler = OnDisconnectHandlerFx
        return self
    def send_data(self, data: str)->bool:
        if(self.sock._closed or self.sock == None or data == None):
            return False
        try :
            self.sock.sendall(bytes(data,"utf-8"))
        except Exception as ex:
            print("Exception in sending {0} -> {1}".format(ex, self.client_id))
            return False
        self.tx_packet_count = self.tx_packet_count+1
        return True
    def IsClosed(self):
        return self.sock._closed | self.sock==None
    async def Run(self):
        #if self.IsClosed():
        #   return
        
        count = self.buffer_size
        buffer = bytearray(count)
        try :

            while True:
                read, addr = self.sock.recvfrom_into(buffer,count)
                if read == 0:
                    self.OnDisConnectedHandler(self)
                    break
                self.OnReceivePacketHandler(self, addr, buffer, read)

        except Exception as ex:
            print("Exception in Run-> {0}".format(ex))
            return
        return 
                
    def Start (self):
        try:
           # asyncio.run(self.Run())
            asyncio.run(self.Run())
        except Exception as ex:
            print("Exception in start:", ex)
            pass
    
        return self
    def Stop(self):
        try:
            self.sock.close()
        except Exception as ex:
            print("Exception in Stop:", ex)
        return self

        

    