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

import inspect 

class Out():
    
    def __init__(self, fd, prefix=None):
        self._Fd=fd
        self._Prefix=sys.intern(prefix.upper()) if prefix is not None else None 
        self._Break=False
        self._Enable = True
        return
        
    def Enable(self, f=True):
        self._Enable=f
        return self
    
    def Disable(self):
        self._Enable=False
        return self
    
    def write(self, s):
        self._Fd.write(s)
        return
        
    def nl(self):
        self.write("\n")
        self._Break=False
        return self
        
    def writeout(self, e):
        if self._Enable:
            if not self._Break:
                if self._Prefix is not None:
                    self.write(self._Prefix)
                    self.write(": ")     
        
            if e is None:
                self.write("None")
            elif isinstance(e, str):
                self.write(e)
            elif isinstance(e, int):
                self.write(str(e))
            elif isinstance(e, float):
                self.write(str(e))
            elif isinstance(e, (list, tuple)):
                self.write(e)
            elif isinstance(e, dict):
                self.write(str(e))
            elif isinstance(e, bool):
                self.write("True" if e else "False")
            elif inspect.isclass(e):
                s=inspect.getmodule(e).__name__ 
                self.write("<Class "+s+":"+e.__name__+">")
            elif inspect.ismethod(e):
                s=inspect.getmodule(e).__name__ 
                self.write("<Method "+s+":"+e.__name__+">")
            elif inspect.ismodule(e):
                self.write("<Module "+e.__name__+">")
            elif inspect.isfunction(e):
                s=inspect.getmodule(e).__name__ 
                self.write("<Function "+s+":"+e.__qualname__+">")
            elif inspect.istraceback(e):
                self.write("<Traceback "+str(e)+">")
            else:
                self.write(str(e))
            self._Break=True
        return self
        
    def __call__(self, *args, **opts):
        if self._Enable:
            ff=False
            for e in args:
                if ff:
                    self._Fd.write(" ")
                self.writeout(e)
                ff=True
            return self.nl()      
        return self   
        
    def _(self):
        
        return self
        
    def __add__(self, v):
        return self.writeout(v)
    
    def __lshift__(self, v):
        return self.writeout(v)
    
    def __rshift__(self, v):
        return self.writeout(v).nl()
        
    def __radd__(self, v):
        return self.writeout(v)
        
    def __rlshift__(self, v):
        return self.writeout(v)
        
    def __rrlshift__(self, v):
        return self.writeout(v).nl()
                
    def __iadd__(self, v):
        return self.writeout(v)
        
    def __ilshift__(self, v):
        return self.writeout(v)
        
    def __irshift__(self, v):
        return self.writeout(v).nl()
    
    def __bool__(self):
        if self._Fd is None:
            return False
        return True
    
    pass


STDOUT = Out(sys.stdout)

STDERR = Out(sys.stderr)

DEBUG = Out(sys.stderr, prefix="Debug")
WARNIG = Out(sys.stderr, prefix="Warning")
INFO = Out(sys.stderr, prefix="Info")
FAIL = Out(sys.stderr, prefix="Fail")
CRITICAL = Out(sys.stderr, prefix="Critical")

class Io():
    
   
    
    pass
    
if __name__ =="__main__":
    
    STDERR("Error", Io, Out, Out.write)
    
    DEBUG.Enable()("code", 1)
    DEBUG << "XXX"

###