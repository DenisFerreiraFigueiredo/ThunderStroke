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

_w.Graphql = _w._i("Graphql")



from Nodes.Types import Types
from Nodes.Tokenizer import Tokenizer


class GraphQl():
    
    _GraphQlWords = (_w.Query,
    	                _w.All,
    	                _w.Redundant,
    	                _w.Find,
    	                _w.Mutation,
    	                _w.Search,
    	                _w,Subscription,
    	                _w.Type,
    	                _w.Limit,
    	                
    	                )
    
    @classmethod 
    def Load(cls):
        return
    
    
    pass
    
    
    
if __name__ =="__main__":
    
    
    
    pass











###