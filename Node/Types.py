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

class Types():
    
    class Dict(dict):
                
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
               if item == item.upper():
                  item = item.replace('_', '-')
                  item = sys.intern(item.title())
                  self[item] = v
                  return
#        raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

            return super().__setattr__(item, v)
        
        def __getattr__(self, item):
            if isinstance(item, str):
                if item == item.upper():
                    i = item.replace('_', '-')
                    i = sys.intern(i.title())
                    return self[i]
            raise AttributeError("attibute not found %s in %s" % (item, self.__class__.__name__))

            return super().__getattr__(item)

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
         
    pass
    
    
if __name__ =="__main__":
    d = Types.Dict()
    d.EEEE = 3
    print("d=", d)
    print(d.EEEE)
  
###