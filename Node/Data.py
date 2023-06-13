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


import json
import yaml
import xml

class Data():
    
    @staticmethod 
    def fromJson(dt):
        r=json.loads(dt)
        return r
        
    @staticmethod 
    def toJson(j, encode=None):
        r=json.dumps(j)
        if encode is not None:
            r=r.encode(encode)
        return r
    
    @staticmethod 
    def fromYaml(dt):
        return r
        
    @staticmethod 
    def toYaml(y, encode=None):
        r=yaml.dump(y)
        if encode is not None:
            r=r.encode(encode)
        return r
        
    @staticmethod 
    def fromXml(dt):
        return r
        
    @staticmethod 
    def toXml(x, encode=None):
        r=xml.dump(x)        
        if encode is not None:
            r=r.encode(encode)
        return r
        
    
    pass


###