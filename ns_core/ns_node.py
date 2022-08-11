
from ns_core.ns_point import *
from ns_core.ns_nodeConfig import *
import enum
import time
class ns_nodeType(enum.Enum):
    Sensor = 1,
    BS = 2,
    MCV = 3
    Drone = 4

class ns_node:
    ###
    def __init__(self, id, loc = ns_point()):
        self.id = id
        self.location = loc
        self.neighbors = dict()
        self.nodeConfig = ns_nodeConfig()
        self.NodeTye = ns_nodeType.Sensor
    ### 
    def __init__(self, id , x=0.0, y=0.0):
        self.id = id
        self.location = ns_point(x,y)
        self.neighbors = dict()
        self.nodeConfig = ns_nodeConfig()
        self.NodeTye = ns_nodeType.Sensor

    ### 
    def getLocation(self):
        return self.location
    ###
    def getId(self):
        return self.id
    ###
    def __str__(self):
        return self.id + "\t loc:"+ self.location.__str__()
    ## neighbor alrready exists:
    def conatins_node(self, neighbor):
        return self.neighbors
    ###
    def addlink(self, neighbor):
        self.neighbors[neighbor.id] = neighbor
        return self

    ###
    def connectTo(self, node):
        self.addlink(node)
        return self
    
    #### Start the node
    def start(self):
        self.startTime = time.ctime()
        return self