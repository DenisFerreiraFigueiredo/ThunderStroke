#
#
#

import sys
import os

import json
import yaml

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

class Macro(str):
    
    def __call__(self, **args):
        if getattr(self, "_Arfument", None) is None:
          self._Arguments=dict()
        self._Arguments.update(args)
        for e, v in args.items():
            e=e.capitalize()
            self._Arguments[e]=v
        return self
        
    def __str__(self):
        print(bytes(self, "utf-8"))
        if getattr(self, "_Arguments", None) is not None:
            s=self.split("${{")
            if len(s)>1:
                r=list()
                for e in s:
                    if "}}" in e:
                        e=e.split("}}",2)
                        a=e[0].strip().capitalize()
                        va=self._Arguments[a]
                        vv=va+e[1]
                        r.append(vv)
                    else:
                        r.append(e)
                print("r=", r)
                return "".join(r)
        return self
    
    pass
    
class List(list):
    
    def fromYaml(self, y):
        ss = yaml.load(y, Loader=yaml.FullLoader)
        if ss is list:
            self.extends(ss)
        return self             
        
    def loadFromYaml(self, path, pwd=None):
        path=File.asPath(path, pwd=pwd, suffix=".yaml")
        with open(path, "r") as fd:
            r= yaml.load(fd, Loader=yaml.SafeLoader)
        self.update(r)
        return self            
    
    
    def isEmpty(self):
        return len(self)==0
    
    pass

class Dict(dict):
                
    @staticmethod 
    def From(s):
        if isinstance(s, Dict):
            return s
        elif isinstance(s, dict):
            return Dict(s)
        return None
                
    def fromYaml(self, y):
        ss = yaml.load(y, Loader=yaml.FullLoader)
        if ss is dict:
            self.update(ss)
        return self 
            
        
    def loadFromYaml(self, path, pwd=None):
        if pwd is not None:
           path=os.path.dirname(pwd)+"/"+path+".yaml"
        with open(path, "r") as fd:
            r= yaml.load(fd, Loader=yaml.SafeLoader)
        self.update(r)
        return self            
            
    def __setattr__(self, item, v):
        if isinstance(item, str):
           if item.isupper():
              item = item.replace('_', '-')
              item = sys.intern(item.title())
              if isinstance(v, dict):
                  v = Dict.From(v)
              self[item] = v
              return
#        raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__setattr__(item, v)
        
    def zzzz__setattr__(self, n, v):
        print("--- setattr", n, v, self.__dict__ )
        if n.isupper():
            n= sys.intern(n.capitalize())
            self[n]= v  
        else:
            self.__dict__[n]= v
        return
    
        
    def __getattr__(self, item):
        if isinstance(item, str):
            if item == item.upper():
                i = item.replace('_', '-')
                i = sys.intern(i.title())
                return self[i]
        raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

        return super().__getattr__(item)
        
    

    def __getitem__(self, i):
        
        return super().__getitem__(i)
        
    def __setitem__(self, i, v):
        return super().__setitem__(i, v)


    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, tb=None):
        if tb is None:
            pass # no exception
        else:
            # Exception occurred, so rollback.
            pass
        return False
            
    pass

class Types():
    
    Macro = Macro
    Dict = Dict
    
         
    pass
    
    
if __name__ =="__main__":
    d = Types.Dict()
    d.EEEE = 3
    print("d=", d)
    print(d.EEEE)
    d.ZZZ = {'a': "###"}
    a=d.ZZZ
    print(d.ZZZ, a, type(a))
    
    ss = Macro("esse e uma ${{V1}} macro")
    ss(v1="xxxxccxxx")
    print(ss)
  
###