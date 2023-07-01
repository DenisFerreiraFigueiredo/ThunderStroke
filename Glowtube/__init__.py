#
#
# Glowtube Node

import sys
import os
import syslog

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

_w.Glowtube = _w._i("Glowtube")



from Node.File import Input
from Node.Http import Request, Response
from Node import Node
from Node.Document import Document
from Node.Http import Http

from Node.Mongodb import Mongodb

from Node.Html import Html

from Node.Unit import Unit
from Node.FlatAPI import FlatAPI
from Node import Node_Db

class Glowtube(Node_Db):
    
    _PORT = 9000
    _VERSION = (1, 3, 0)
    _LOGO = "/Image/Logo/Glowtube.png"
    
      
    @classmethod     
    def cmdStart(cls, *args, **opts):
        return
        
    @classmethod            
    def cmdConfig(cls, *args, **opts):
        super().Config(*args, **opts)        
        return self
        
    @classmethod         
    def Prepare(cls, *args, **opts):
        super().Prepare(*args, **opts)        
              
      
        return None
        
    @staticmethod 
    def cmdStop(cls, *args, **opts):
        return None
      
    @classmethod 
    def Buildup(cls):
        serv=cls.Services()
        
        
        
        return
   
   
    @classmethod 
    def findInstance(cls, ins):
        r=cls._Accounts.Find(ins)
        if r is None:
            return None
        return r
         
     
        
      
    pass
    
class Glowtube(Glowtube):
    
    _API = FlatAPI(None, _w.Glowtube, api=Glowtube)
    
    pass
    
       
def handler(env, begin_response):
    return Glowtube.API(env, begin_response)
    
    
if __name__=="__main__":

    from Node.EmulateWsgi import EmulateWsgi 
    #Domain.Buildup()
    EmulateWsgi.Start(_w.Glowtube, handler=handler)

    