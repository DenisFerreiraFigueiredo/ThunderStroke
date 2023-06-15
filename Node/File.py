#
#
#

import sys
import os

import json
import yaml
import xml
import inspect

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w
from Node.Types import Types

class _File():
    
    @staticmethod 
    def asPath(p, pwd=None, suffix=None):
        if pwd is not None:
            if inspect.isclass(pwd):
                pwd=inspect.getfile(pwd)
            pwd=Path(pwd)
            if not pwd.is_dir():
                pwd=pwd.parent
                
        if isinstance(p, Path):
            pass
        elif isinstance(p, str):
            p=Path(p)
        elif isinstance(p, (list, tuple)):
            rr=None
            for e in p: 
                if rr is None:
                    rr=Path(e)
                else:
                    rr /= e
            p=rr
        else:
            ValueError()
        if pwd is not None:
            p = pwd / p
        if p.suffix in (None, "") and suffix is not None:
            p = p.with_suffix(suffix)
        return p
    
    
    def __init__(self, path, pwd=None, suffix=None):
        self.Path = File.asPath(path, pwd=pwd, suffix=suffix)
        self.Fd = None
        self.open()
        return    
        
    def open(self):
        return
        
    def close(self):
        if self.Fd is not None:
            self.Fd.close()
            self.Fd = None
        return self
    
    def __enter__(self):
        return self.open()

    def __exit__(self, exc_type, exc_val, tb=None):
        if tb is None:
            self.close()
            pass # no exception
        else:
            # Exception occurred, so rollback.
            pass
        return False
    
    pass

class _Input(_File):
   
   
    def __init__(self, path, pwd=None, suffix=None):
        super().__init__(path, pwd=pwd, suffix=suffix)
        return
                
    def open(self):
        if self.Fd is None:
            #self.close()
            self.Fd = open(self.Path, "r")
        else:
            self.Fd.seek(0)
        return self 
               
    def read(self, n=None):
        if self.Fd is not None:
            return self.Fd.read(n)
        return None
                   
    pass
    
        
class Bin(_Input):
        
    @staticmethod 
    def Load(path, pwd=None, suffix=None): 
        fi=Input.Bin(path, pwd=pwd, suffix=suffix)
        s=fi.read()
        fi.close()
        return s
        
    def open(self):
        if self.Fd is None:
            #self.close()
            self.Fd = open(self.Path, "rb")
        else:
            self.Fd.seek(0)
        return self 
       
    pass
    
class YAML(_Input):
        
    @classmethod 
    def Load(cls, path, pwd=None, suffix=None):
        r=Types.Dict()            
        fi=Input.YAML(path, pwd=pwd, suffix=suffix)
        s=fi.read()
        fi.close()
        r.update(s)
        return r
        
    def __init__(self, path, pwd=None, suffix=None):
        super().__init__(path, pwd=pwd, suffix=".yaml")
        return
            
    def read(self):
        r = None
        if self.Fd is not None:
            r= yaml.load(self.Fd, Loader=yaml.SafeLoader)
        return r
               
    pass
    
    
class Macro(_Input):
    
    @classmethod 
    def Load(cls, path, pwd=None, suffix=None):       
        fi=Input(path, pwd=pwd, suffix=suffix)
        s=fi.read()
        fi.close()
        return s   
    
    pass
    
class Input(_Input):
    
    
    Yaml = YAML
    YAML = YAML
    Bin = Bin      
    Macro = Macro    
           
    @classmethod 
    def Load(self, path, pwd=None, suffix=None):
        #print("Load File", path)
        with Input(path, pwd=pwd, suffix=suffix) as ff:
            r=ff.read()
        return r
        
    pass    

class _Output(_File):
    
    def __init__(self, path, pwd=None, suffix=None, makedir=False, append=False):
        super().__init__(path, pwd=pwd, suffix=suffix)
       # self.Path = path
       # self.Fd = None
        if makedir is True:
            self.Path.makedirs(exits_ok=true)
        if append:
            self.append()
        else:
            self.create()
        return     
        
    def append(self):
        self.close()
        self.Fd = open(self.Path, "a")
        return self      
        
    def create(self):
        self.close()
        self.Fd = open(self.Path, "w")        
        return self
        
    def flush(self):
        if self.Fd is not None:
            self.Fd.flush()
        return self
    
    def __call__(self, *s):
        if self.Fd is not None:
            ff = False
            for e in s:
                if ff:
                    self.Fd.write(" ")
                ff = True
                self.Fd.write(e)
            self.Fd.write("\n")
        return self
    
    def WriteYAML(self, w):
        if w is dict:
            s = yaml.dumpa (w)
            self.Fd.write(s)
            self.Fd.write("\n")
        
        return self
        
    def WriteJSON(self, w):
        if w is dict:
            s = json.dumps(w)
            self.Fd.write(s)
            self.Fd.write("\n")
        return self
    
    pass
    
    
class Output(_Output):

    
    @classmethod 
    def Save(cls, path, pwd=None, suffix=None):
        return
    	
    pass
    
    
class File(_File):
    
    Input = Input
    Output = Output
    
    
    pass
    
    
if __name__ =="__main__":
    
    s = Input.Load("Styles/Node.css", pwd=__file__)
    print(s)
    
    b = Input.Bin.Load("Images/Icons/Docker", suffix=".png", pwd=__file__)
    print(b)
    b = Input.Bin.Load(("Images","Icons","Docker.png"), pwd=__file__)
    print(b)
    pass
  
###