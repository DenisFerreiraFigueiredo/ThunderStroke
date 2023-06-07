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
	
from Node.File import Input

class Mime():
    
    Any = sys.intern("*/*")
   
    @classmethod 
    def Load(cls):
        m = Input.YAML.Load("Data/Mime", pwd=__file__)
        
        for e in m:
            mm = m[e]
            ec=sys.intern(e.capitalize())
            #print("-", e, ec)
            for ee in mm:
                t = mm[ee]
                eec=sys.intern(ee.title().replace("-", "").replace(".", "").replace("+",""))
                #print("--", ee, eec)
                mimename = sys.intern(ec+eec)
                mimedef = sys.intern(ec.title()+'/'+ee.title())
                setattr(cls, mimename, mimedef)
                #for tt in t:
                #    print("---", tt)
                setattr(cls, '_'+mimename+'_', t)
                for tt in t:
                    if tt[0]=='.':
                        tt=tt[1:]
                    setattr(cls, "__"+ tt.capitalize(), mimedef )
        
        return
        
    @classmethod 
    def Validate(cls, ct, dflt=None):
        if ct==cls.Any:
            return cls.Any
        for e in cls.__dict__:
            if not(e.startswith("_")):
                v = getattr(cls, e, None )                    
                if isinstance(v, str):
                        if ct.lower()==v.lower():                    
                            return v
                        
        if dflt is not None:
            return dflt
            
        return ct
    
    @classmethod 
    def Find(cls, ext, dflt=None):
        if ext[0]=='.':
            ext=ext[1:]
        ss="__"+ext.capitalize()
        e=getattr(cls, ss, None)
        if e is not None:
           #print(ext, e)
           return e
        return dflt
    
    pass
    
    
Mime.Load()

if __name__ =="__main__":
    print(Mime.__dict__)
    print(Mime.Find(".pdf"))

###