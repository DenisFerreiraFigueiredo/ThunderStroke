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
    
import copy
    
from Node import Words as _w

from Node.Html import Html

class Theme():
    
    _StyleSheet = "Styles/Node.css"
    
    pass

class View():
    
    _Theme = {
    	         _w.Default : Theme()
    	        }
        
    _BasePage = dict()
    
    _ErrorPage = None
    
    @classmethod 
    def BasePage(cls, theme=_w.Default):
        bp =cls._BasePage.get(theme, None)
        if bp is None:
            with Html() as pg:
                cls._BasePage[theme]=pg
                with pg.Head() as hd:
                    with hd.Title() as ti:
                        ti("Node")
                    hd.Stylesheet("Styles/Node.css")
                with pg.Body() as bd:
                    pass
                bp = pg 
                
        return bp
    
    @classmethod 
    def ErrorPage(cls):
        if cls._ErrorPage is None:
            ep = copy.deepcopy(cls.BasePage(_w.Defaukt))
            
        
        return
    
    pass
    
    
    
if __name__ =="__main__":
     
     s = View.BasePage()
     
     print(str(s))

####