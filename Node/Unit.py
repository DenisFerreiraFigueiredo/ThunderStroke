#
#
#

import sys
import os
import subprocess
from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)


from Node import Words as _w

_w.Unit = _w._i("Unit")

	
from Node.File import Output
from Node.System import System
from Node.Memcached import Memcached 
from Node.Service import Service
from Node.Document import Document
from Node import Node

import hashlib
import json

class unitConfig(Service.Config):
        
    def _set(self, var, *val):
       self.Cfg(var, "= ", *val)
       return self
           
    def segment(self, seg):
       self.Cfg("[", seg, "]")
       return self
           
    def end(self):
        self.Cfg.remark("##")
        return self
           
    pass
    
class UnitClient():
    
    
    _socketpath = "/var/run/control.unit.sock"
    
    def __init__(self, parent):
        self._Parent=parent
        if Syste.isDevelop():
            pass
        else:
            self 
        return
        
    def getConfig(self, key, val):
        r=request("http://127.0.0.0.1")
        return
        
    def putConfig(self ):
       return
        
    def Listener(self, port=None): ## get/set listener
        cc["listeners"]= {
                        "127.0.0.1:"+str(self._PORT): {
                                            "pass": "routes"
                                            }
                         }
        r=requests()
        return
        
    def Application(): ## get/set applications
        cc["applications"]= { 
            	            "wiki-dev": { 
            	        	                "type": "python", 
            	        	                "module": "wsgi", 
            	        	                "user": "www-wiki", 
            	        	                "group": "www-wiki", 
            	        	                "path": "/www/wiki-dev/" },
            	            	"wiki-prod": { "type": "python", 
            	        	                    "processes": 5,
            	        	                    "module": "wsgi", 
            	        	                    "user": "www-wiki", 
            	        	                    "group": "www-wiki", 
            	        	                    "path": "/www/wiki/" 
            	        	                } 
            	        	        }
        return
    
    def Route(self, rt): ## get/set routes
        cc["routes"]= [
                        { 
                        	"match": { 
                        		        "uri": "/development/*" 
                        		        }, 
                        	"action": { 
                        			        "pass": "applications/wiki-dev"     
                        			        } 
                        },
                        {
                        "action": {
                                    "share": "/www/data$uri"
                                   }
                        }
                        ]
        return
    
    
    pass

class Unit(Service):    

    _PORT = 5100
        
    configFileClass = unitConfig
    
    Client = UnitClient    
    
    
    @property 
    def configSufix(self):
        return ".json"
        
    def begin(self):
        cc = {}
         	    
        
        cfg=Service.begin()
        cfg.remark()
        cfg.remark()
        cfg.remark()
        cfg.skip()
        cfg.segment("uwsgi")
        cfg("uid", "zimbra")
        cfg("gid", "zimbra")
        cfg(_socket, '"/tmp/%n.socket"')
        cfg("processes", 4)
        cfg(_master, True)
        cfg(("enable","threads"), True)
        cfg("chdir", "/opt/Zimbra")
        cfg("arakiri", 30)
        cfg(("offload", "threads"), 2)
        cfg(("procname","prefix","-spaced"), "Zimbra")
        cfg(_route, ".*", "addheader:Server: Zimbra")
        cfg(("manage","script","name"), True)
        cfg.skip()
        return cfg      
        
    def run(self):     
        if System.isDevelop():
            pass
        else:
            System.exec("/usr/bin/unitd", "--control", "unix::/var/run/control-unit.sock")
        return self
        
    def Stop(self):
        return self
                
    def Config(self):
        cfg=self.begin()
                	
      
        
        self.end()
        return self
        

    def handler(self, env, begin_response):
        print("--- hander start")
        begin_response("200 OK", [("Content-Type", Mime.ApplicationJson+"; charset=utf-8")]) 
        print("--- body") 
       
        r = Document()
    
        r["message"] = "Unit reporting"
        r["agent"] = "NGINX Unit 1.30.0" 
    
        r["headers"] = {} 
        for header in env.keys(): 
            if header.startswith("HTTP_"):
                r["headers"][header] = env[header] 
    
        bytes = env["wsgi.input"].read() 
        r["body"] = bytes.decode("utf-8") 
        r["sha256"] = hashlib.sha256(bytes).hexdigest() 
        
        print("--- end")
        
        rs = json.dumps(r, indent=4).encode("utf-8") 
    
        return [rs]


    pass

if __name__ == "__main__":
    from Node.EmulateWsgi import EmulateWsgi 
      
    UNIT = Unit()
    
    EmulateWsgi.Start(_w.Unit, handler=UNIT)    
    
    pass



###