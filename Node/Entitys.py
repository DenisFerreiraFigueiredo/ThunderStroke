#
#
# Domain Node

import sys
import os
import syslog

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w
from Node.File import Input
from Node.Http import Request, Response
from Node import Node

from Node import Words as _w

_w.Entity = _w._i("Entity")
_w.Entities = _w._i("Entities")

from Node.Uuid import Uuid

from Node.Mongodb import Mongodb


class Test():
      	
    _Client = None
    _Db = None        	
     
    @classmethod 
    def Client(cls):
        if cls._Client is None:
            cls._Client = Mongodb.Client()
        
        return cls._Client
        
    @classmethod 
    def Db(cls):
        if cls._Db is None:
            cls._Db = cls.Client()[_w.Test]
        return cls._Db
   	
    pass
    
class Entity():
    
    
    
    pass
  
class Entitys():
    
    Entity = Entity
    
    def __init__(self, rootclass=Test, name=_w.Entities):
        self._Root=rootclass
        self._Name=name
        self._Collection=None
        self.Prepare()
        return
        
    def Prepare(self):
        return
        
    def Collection(self):
        if self._Collection== None:
            self._Collection=self._Root.Db()[self._Name]
        return self._Collection
        
    def Find(self, _id):          	
        r = self.Collection().find_one({"_id": _id})
        if r is dict:            
            return r        
        return None
        
    def newId(self):
        r = Uuid.SID(Uuid.new(), crc=True)        
        return r
        
    def create(self, _id):
        r = {
        	  "_id": _id,
        	  _w.Name: "xxx"
        	    }
        self.Collection().Insert(r) 

        return False       
        
    def EnsureLoad(self, key, path, pwd=None):
        rr = Input.YAML.Load(path, pwd=pwd)
        self.Collection().loadFrom(key, rr, True)       
        return
        
    def _Test(self):
        print(self.__class__.__name__,"=", self.newId())
     
        rr=self.Collection().Find()
        if rr is not None:
            for r in rr:
                print(r)
    
        a = self.create("12345678901B")
      
        
        
        return
            
    pass
    
    
def handler(env, begin_response):
    return Domain.handler(env, begin_resoonse)
    

if __name__ =="__main__":  
   Entitys()._Test()
      
###   