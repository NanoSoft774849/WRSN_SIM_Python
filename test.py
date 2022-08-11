
import sys

from ns_core.ns_point import *
from ns_core.ns_node import *
from ns_com.ns_clientNode import *

test_ip = "172.20.10.2"
test_port = 20001

p = ns_point(10,10)
print(p) 

#p = p + ns_point(10,20);

#print(p)
n1 = ns_node(id= "S_1", x=10, y=20)
n2 = ns_node("S_2", 20 , 30)
n3 = ns_node("S_3", 50,100)

n1.addlink(n2)
n2.addlink(n3)
n1.addlink(n3)
def OnRx(cn , fromx, buffer, count):
    strx = str(buffer[:count],"utf-8")
    print("{0} from {1} -count:{2}".format(strx, fromx, count))
    cn.send_data("Hello,man I am here!")

def OnDisc(cn):
    print("{0} disconnected :".format(cn.client_id))
nodes = dict()
nodes["n1"] = n1
nodes["n2"] = n2
nodes["n3"] = n3
for node in nodes.values():
    client = ns_clientNode(None, node)
    client.SetHandlers(OnRx, OnDisc)
    client.connect(test_ip, test_port)
    client.Start()






