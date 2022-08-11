
import math

class ns_point:

    def __init__(self, x:float()=0, y:float() =0):
        self.x = x
        self.y = y

    def __str__ (self):

        return "("+ str(self.x)+","+str(self.y)+")"
    
    # """ Add two points """
    def Add(self, p):

        return ns_point(self.x + p.x ,  self.y +p.y)
    ####--------
   
# Multiply point by a factor f
    def Mul( self , f:float()):
        self.x = self.x * f
        self.y = self.y *f
        return self

    """ multiply ... """
    def __mul__(self , f:float()):
        return self.Mul(f)
    
    """ substract """

    def sub(self, p):
        return ns_point(self.x-p.x, self.y - p.y)
    
    # calc euclidian distance between two points
    """ euclidean distance """
    def edistance(self, p):
        
        p = self.sub(p)
        return math.sqrt(p.x*p.x + p.y*pi.y)

    """ manhatan distance """
    def mdistance( self , p):

        p = self.sub(p)
        return abs(p.x) + abs(p.y)
    # linea intero.
    """ linear intero  """
    def lerp( self , p,  tao ):
        if tao > 1:
            return p
        pass
        

    def toStr(self):
        return __str__() 
