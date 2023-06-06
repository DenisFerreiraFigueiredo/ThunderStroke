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


from Node.Uuid import Uuid
from Node.Types import Types

import json

class Document(Types.Dict):
    
    def __init__(self, *args, **kvargs):
        self._Id=kvargs.pop("Id", None)
        #print("args", args)
        #print("kvargs", kvargs)
        super().__init__(**kvargs)
        for e in args:
            if isinstance(e, dict):
                self.update(e)
            elif isinstance(e, (list, tuple)):
                p=0
                c=len(e)
                while p<c:
                    i=e[p]
                    p+=1
                    if p<c:
                        d=e[p]
                        p+=1
                    else:
                        d=None
                    self[i]=d
                pass
            else:
                raise ValueError
                
        return
        
    #def As(self, id):
    #    self.set_Id(id)
    #    return self
        
    def loadFrom(self, *args, **kvargs):
        for e in args:
            if isinstance(e, dict):
                self.update(e)
            elif isinstance(e, (list, tuple)):
                p=0
                c=len(e)
                while p<c:
                    i=e[p]
                    p+=1
                    if p<c:
                        d=e[p]
                        p+=1
                    else:
                        d=None
                    self[i]=d
                pass
            else:
                raise ValueError
                
        for e in kvargs:
            v=kvargs.get(e)
            if e == "Id":
                self.Id(v)
            else:
                self[e]=v
            
        return self
        
    def copy(self):
        r = Document(self)
        r._Id=self._Id        
        return r
       
    #def get_Id(self):
    #    if self.__Id is None:
    #        self.__Id = Uuid.SID(Uuid.new())
    #    return self.__Id
        
    #def set_Id(self, id):
    #    self.__Id=id
    #    return self
        
    #Id = property( get_Id, set_Id)
    
    def Id(self, id=None):
        r = self._Id
        if id is not None:
            self._Id=id
        return r
                
    def __call__(self, *args, **kvargs):
        for e in args:
            if isinstance(e, dict):
                self.update(e)
        for e in kvargs:
            v=kvargs.get(e)
            self[e]=v
        return self
           
    def Json(self):
        s = json.dumps(self)
        return s       
        
    @property 
    def Contents(self):
        r={ '_id': self._Id }
        r.update(self)
        return r
        
    def __getattr__(self, n):
        print("---getattr", n, self.__dict__)
        if n==n.upper():
           n=sys.intern(n.capitalize())
           return self.get(n, None)
        else:
           if n in self.__dict__:
               return self.__dict__[n]
           else:
               raise AttributeError(n)
        return None
        
    def __setattr__(self, n, v):
        print("--- setattr", n, v, self.__dict__ )
        if n==n.upper():
            n= sys.intern(n.capitalize())
            self[n]= v  
        else:
            self.__dict__[n]= v
        return
    
            
    pass

if __name__ =="__main__":
    r = Document()    
    print(r, r.Id(), r.Contents)
    r.Id("z.o")
    print(r, r.Id(), r.Contents)
    r({"z" : 4}, n={"val":"aaa"})
    print(r)
    print(r.Json())
    r=Document(['a', 3], Id="zzz")
    print(r.Contents)
    e=r.copy()
    print("XOP=", e.XOP)
    e.DUP="dddd"
    print(r, e)
###