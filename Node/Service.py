#
#
#

import sys
import os

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

from Node.Arrange import Arrange
from Node.FlatModel import FlatModel
from Node.Http import WsgiHandler

class serviceConfig():
        
    def __init__(self, parent, path):
        self._Parent=parent
        self.Cfg = File.Output(path, mkdir=true)
        return
            
    def close(self):
        if self.Cfg is not None:
            self.skip()
            self.end()
            self.Cfg.close()
            self.Cfg=None            
        return self
        
    def __call__(self, var, *val):
        if self.Cfg is not None:
            if var is list:
                var = var.join("-")
            self._set(var, *val)
        return self
            
    def _set(self, var, *val):
        self.Cfg(var, "= ", *val)
        return self
           
    def skip(self):
        if self.Cfg is not None:
           self.Cfg()
        return self
           
    def remark(self, *s):
        if self.Cfg is not None:
            self.Cfg("# ", *s)
        return self
            
    def __enter__(self): 
        return self 
            
            
    def __exit__(self, type, value, tb): 
        self.Cfg.close()
        return
        
        
    def end(self):
        return self
            
    pass

class Service(FlatModel, Arrange, WsgiHandler):
    
    Config = serviceConfig
    
    def __init__(self, partition=_w.Default):
        WsgiHandler.__init__(self, partition)
        self._Partition=partition
        self.Cfg = None
        self._Instance = dict()
        return
        
    @property 
    def Partition(self):
        return self._Partition
        
    @property 
    def configSufix(self):
        return ".conf"
        
    @property 
    def socketSuffix(self):
        return ".socket"
                      
    def configPath(self, *args):
        return self.tempPath(self.Partition, *args)
                
    @property 
    def configFilePath(self):
        return (self.configPath() / self.Partition).with_suffix(self.configSuffix)
        
    def socketPath(self, *args):
        return self.runPath(self.Partition, *args)
       
    @property 
    def socketFilePath(self):
        return (self.socketPath() / self.Partition).with_suffix(self.socketSuffix)
        
        
    configFileClass = serviceConfig
           
    def begin(self):
        if self._Config is None:
            self._Config= configFileClass(self, self.configFilePath)
        return self._Config
                
    def end(self):
        if self._Config is not None:
            self._Config.close()
        return self    
        
    def start(self):
        self.stop()
        self.prepare()
        self.config()
        self.run()
        return self
        
    def run(self):
        return self
        
    def stop(self):
        return self
        
    def restart(self):
        return self
                
    def config(self):
        self.begin()
        
        self.end()                	
        return self

    def info(self):
        return
        
    def status(self):
        return False

    def Version(self, *args, **opts):
        return (0, 0, 0)
 
      
    pass


###