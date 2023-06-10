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


class Arrange(): ## Interface of    
      
     
    @classmethod
    def asPath(cls, radix, *args, mkdir=False):
        p=Path("/") 
        if isinstance(radix, str):
            p /= radix
        elif isinstance(radix, (list, tuple)):
            for e in radix:
                p /= e
        else:
            raise ValueError()         
        if len(args)>0:
            for e in args:
                p = p / e    
        p /= cls.__name__
        if mkdir and not p.is_dir():
            p.mkdir(mode=0o777, parents=True, exist_ok=True)     
        return p      
      
    @classmethod
    def tempPath(cls, *args, mkdir=False):
        return cls.asPath("tmp", *args, mkdir=mkdir)      
        
    @classmethod
    def runPath(cls, *args, mkdir=False):
        return cls.asPath(("var" / "run"), *args, mkdir=mkdir)
        	      
    @classmethod 
    def workPath(cls, *args, mkdir=False):
        return cls.asPath(_w.WORK, *args, mkdir=mkdir)
        
        
    _BasePath = None
    
    @classmethod 
    def basePath(cls, *s):
        if cls._BasePath is None:
            p=Path(inspect.getfile(cls)).parent
            cls._BasePath = p
        if len(s)>0:
            p = self._BasePath
            for e in s:
                p /= e
            return e
        return self._BasePath
        
    @classmethod 
    def configPath(cls, *args, mkdir=False):
        return cls.tempPath(*args, mkdir=mkdir)
        
        
    pass


###