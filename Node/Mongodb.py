#
#
#

import sys
import os
import subprocess
from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if  ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

_w.Tiny = _w._i("Tiny")
_w.Small = _w._i("Small")
_w.Medium = _w._i("Medium")
_w.Default = _w._i("Default")
_w.Big = _w._i("Big")
_w.Huge = _w._i("Huge")
	
from Node.File import Output
from Node.System import System
from Node.Memcached import Memcached 
from Node.Service import Service
from Node.Document import Document
from Node.Uuid import Uuid
from Node.Io import DEBUG
from Node.Types import Types

import pymongo

class Mongodb(Service):
    
    Errors = pymongo.errors
    
    
    class Cursor(pymongo.cursor.Cursor):
        
        @classmethod 
        def From(cls, s):
            if type(s)==pymongo.cursor.Cursor:
                s.__class__= cls
                return s
            elif isinstance(s, cls):
                return s
            return None
        
        def __next__(self):
            r=super().__next__()
            if type(r)==dict:
                r=Document.From(r)
            return r
        
        pass
    
    class Database(pymongo.database.Database):
        
        def __getitem__(self, i):
            if isinstance(i, str):
                r= super().__getitem__(i)
                if r is not None:
                    r.__class__=Mongodb.Collection
                    return r                
            return None
            
        def Collection(self, name, size=None, maxsize=None):
            if maxsize is None    :
                if size is None:
                    r= self.create_collection(name)
                else:
                    ms=int(size)
                    r= self.create_collection(name, size=ms)
            else:
                ms=max(int(size), int(maxsize))
                r= self.create_collection(name, capped=True, maxsize=ms)
            return
            
        def RemoveUser(self, user):
            return
            
        def AddUser(self, user):
            return
            
        def ValidateCollection(self, name):
            return
            
        def EachCollection(self):
            return
            
        def List(self):
           
            return
            
        pass
        
        
    class Collection(pymongo.collection.Collection):
                
        def __getitem__(self, i):
            if isinstance(i, str):
                r= super().__getitem__(i)
                if r is not None:
                    r.__class__=Mongodb.Collection
                    return r                
            return None
            
        def loadFrom(self, prefix, data, childs=False):
            DEBUG.PREFIX(prefix, data, childs)
            if isinstance(data, dict):
                for d in data:
                    v = data.get(d, None)
                    DEBUG.ITEM("-->", d, "=",v)                                           
                    if childs and d[0]=='.':       
                        k = prefix+d    
                        DEBUG._("kk", k)                                                                 
                        self.loadFrom(k, v, childs=childs)
                    else:
                        k = prefix+'.'+d    
                        DEBUG._("k", k) 
                        r = Document(Id=prefix+"."+d)   
                        r(v)
                        self.Ensure(r)                             
            else:
                r=Document(Id=prefix)
                r(Value=data)
                self.Ensure(r)  
                
            return           
            
            
        def Rename(self, name):
            return
            
        def Validate(self, scandata=False, full=False):
            return self.database.validate_collection(self, scandata, full)
            
            
        def _StructureVal(self, val, *args, id=None, **kvargs):
            DEBUG("val=", val, type(val), id)
            
            if isinstance(val, Document):
                #DEBUG("orig val=", val.Contents)
                val=val.copy()
                #DEBUG("copy val=", val.Contents)               
                if id is None:
                    if val.Id is None:
                        val.Id=Uuid.new()
                else:
                    val.Id=id
                DEBUG.DOCUMENT(val)
            else:
                if id is None:
                    id = Uuid.SID(Uuid.new())
                if isinstance(val, dict):
                    val= Document(val)
                    val.Id(id)                    	
                elif isinstance(val, (list, tuple)):
                    val = Document(val)
                    val.Id(id)
                else:
                    val = { "_id": id , "_data": val }  
               
            for e in args:
                if isinstance(e, Document):
                    pass
                elif isinstance(e, dict):
                    pass
                elif isinstance(e, (list, tupple)):
                    pass
                else:
                    pass  
            
            for e in kvargs:
                v=kvargs.get(e)      
                if e.upper()=="ID":
                    val.Id(v)
                else:  
                    val[e]=v
                
            DEBUG("structureval -->",val, val.Contents)
            
            return val
            
        def Insert(self, val, *args, id=None, **kvargs):
            val=self._StructureVal(val, *args, id=id, **kvargs)
            
            if val.Id() is None:
                val.Id(Uuid.SID(Uuid.new()))
                DEBUG("new id=", val.Contents)
                
            DEBUG("insert -->", val.Contents)
            
            try:
                r=self.insert_one(val.Contents)
                DEBUG._("r", r.inserted_id)
            except pymongo.errors.DuplicateKeyError:
                return False
                
            return True
            
        def Ensure(self, val, *args, id=None, **kvargs):
            val=self._StructureVal(val, *args, id=id, **kvargs)
            
            if val.Id() is None:
                val.Id(Uuid.SID(Uuid.new()))
                DEBUG("new id=", val.Contents)
                
            DEBUG.ENSURE("-->", val.Contents)            
                
            try:
               r= self.insert_one(val.Contents)
               DEBUG._("r", r.inserted_id)
            except pymongo.errors.DuplicateKeyError:
                if len(val)>0:
                    _id = { "_id": val.Id() }
                    rs = { "$set": val }
                
                    r=self.update_one(_id, rs, upsert=False)    
                
            return True
            
        def Update(self, val, *args, id=None, **kvargs):
            val=self._StructureVal(val, *args, id=id, **kvargs)
            
            if val.Id() is None:
                val.Id(Uuid.SID(Uuid.new()))
                DEBUG("new id=", val.Contents)
                
            DEBUG.UPDATE("-->", val.Contents)
                
            if len(val )>0:
                _id = { "_id": val.Id() }
                rs = { "$set": val }
                self.update_one(_id, rs, upsert=False)    
                            
            return True
            
        def UpdateWhere(self):
            return
            
        def Replace(self):
            return
            
        def Delete(self):
            return
            
        def Remove(self):
            return 
            
        def Copy(self):
            return
            
        def Find(self, id=None, limit=None):
            if id is None:
                r=self.find_one()
            else:
                r=self.find_one({ "_id": id })
            return Document.From(r)
            
        def FindAll(self, limit=None):
            r=self.find()
            DEBUG.FINDALL(r)
            return Mongodb.Cursor.From(r)
            
        def FindWhere(self, cond, limit=None):
            return          
            
            
        def Drop(self):
            self.drop()
            return  
        
        def Count(self):
            r= self.count()
            return r
            
        pass
    
    class Client(pymongo.MongoClient):
        
        _Version = None
        
        @classmethod 
        def Version(cls):
            if cls._Version is None:
                r=pymongo.version.split('.')
                cls._Version = tuple(map(int, r))
            return cls._Version
        
        def __init__(self, host="localhost", port=27017):
            #if self..socketFilePath.is_file():
            #    pass
            super().__init__("mongodb://"+host+":"+str(port)+"/")
        
            return
            
        def __getitem__(self, i):
            if isinstance(i, str):
                r= super().__getitem__(i)
                if r is not None:
                    r.__class__=Mongodb.Database
                    return r
                
            return None
        
    pass
        
    class Utils():
    
        pass
    
    _Sizes = {
    	        _w.Tiny:    {},
    	        _w.Small:   {},
    	        _w.Medium:  {},
    	        _w.Default: {},
    	        _w.Big:     {},
    	        _w.Huge:    {}
    	         }
        
    def __init__(self, partition="MongoDb", _size=_w.Small):
        super().__init__(partition)
        self._Size = _size
        if not (_size in Mongodb._Sizes):
           raise ValueError() 
        return
               
    @property 
    def configPath(self):
        return Node.tempPath(_w._Mongodb)
        
    @property 
    def configFile(self):
        return self.configPath / (self.instance+".yaml")
    
    def config(self):
        cfg=File(self.configFile, makedir=True)
        cfg("#", "auto generated")
        cc = {}
        
        cc["systemLog"] = {
        	    	            _w._verbosity: 3,
        	    	            "quiet": True,
        	    	            "traceAllExceptions": True,
        	    	            "sysligFacility": "local0",
        	    	            "destination": "syslog",
        	    	            "component": {
        	    	            	    "accessControl": {
        	    	            	    	                _w._verbosity:1,
        	    	            	    	                },
        	    	                 "command": {
        	    	                 	            _w._verbosity: 1
        	    	                 	            }
        	    	                 	        },
        	    	            "processManagement": {
        	    	            	                    }
        	    	            }
        	    	            
        cc["storage"]= {
        	    		            "dbPath": "/WORKSPACE/MongoDb",
        	    		            "directiryPerDB": True,
        	    		            "syncPeriodSecs": 60,
        	    		            "engine": "wiredTiger",
        	    		            "journal": {
        	    		            	            "enabled": True,
        	    		            	            "commitIntervalMs": 2000
        	    			                       },
        	    			           "wireďTiger": {
        	    			           	            "cacheSizeGB": 0.25,
        	    			           	            "journalCompressor": "snappy",
        	    			           	            "directoryForIndexes": True,        	    			           	        
        	    			           	            "collectionConfig": {
        	    			           	            	                    "blockCompressor": "snappy",
        	    			           	            	                    },
        	    			           	            	"indexConfig": {
        	    			           	            		                "prefixCompression": True,
        	    			           	            		                }
        	    			           	            }        	    			           
        	    		            }
        	    		            
        cc["processManagement"]= {
        	    	                    "fork": True
        	    	                    }
        	    	                    
        cc["net"] ={
        	    	        "bindIp": "127.0.0.1",
        	    	        "port": 27017,
        	    	        "unixDomainSocket" : {
        	    	        	                    "enabled": True
        	    	        	                    }
        	    	        }
        	    	        
        cc["setParameter"]= {
        	    		                "enableLocalhostAuthBypass": True
        	    		                }
        	    
        	    
        im = {
        		"inMemory": {
        	    			       "engineConfig": {
        	    			           		          "inMemoryGB": 0.25, 
        	    			           		           }        		           
                    	}
              }
              
        cfg.writeYAML(cc)
        
        cfg.close()
        
        return
    
    def run(self, *args):
        System.exec("/usr/bin/mongod", 
        	            "--config", self.configFile,
        	            "--quiet",
        	            
        	            )
        return self
    
    def start(self, *args ):
        return self
        
    pass
    
    
if __name__ == "__main__":  
    DEBUG(Mongodb.Client.Version())
    c = Mongodb.Client()
    d = c["Domain"]
    t = d["test"]
    DEBUG("validate=", t.Validate())
    if t.Count()>10:
        t.Drop()
        
    DEBUG._("c", type(c))
    DEBUG("d=", type(d))
    DEBUG("t=", type(t), t.name, t.full_name)
    
    #t.insert_one({ "x": 2 })
    
    r = Document()
    t.Insert(r)
    
    t.Insert({'_id': 'sss', 'a': 34})
    
    r.Id("zap")
    r["xxx"]=45
    t.Update(r)
    
    t.Ensure(r)
    
    t.loadFrom("test", { 'z': 1, '.x': 25, 'd': { 'w': 'fff'} }, childs=True)
    DEBUG(t.Count())
    
    for e in t.FindAll():
        DEBUG(e)
    
###