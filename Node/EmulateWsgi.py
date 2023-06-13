#
#
# Node base image

import sys
import os
import time

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

import logging
from logging.handlers import SysLogHandler

import wsgiserver    

from Node.Io import DEBUG

def _handler(env, begin_response):   
    h = ( ("content-type", "text/plain"),
    	    ) 
    begin_response("200 Ok", h)
    return [b"test OK"]
    
def _handlerImage(env, begin_response):   
    h = ( ("content-type", "text/plain"),
    	    ) 
    begin_response("200 Ok", h)
    return [b"test image OK"]
    
    
def _handlerStyle(env, begin_response):   
    h = ( ("content-type", "text/plain"),
    	    ) 
    begin_response("200 Ok", h)
    return [b"test style OK"]
    
def _handlerScript(env, begin_response):   
    h = ( ("content-type", "text/plain"),
    	    ) 
    begin_response("200 Ok", h)
    return [b"test script OK"]
    
    
    
    
class Xxx():
    
    def handler(self, env, begin_response):   
        DEBUG("env", env)
        pp=env.get("PATH_INFO", "")
        pp=pp.split("/")
        if pp[0]=="":
            pp.pop(0)
        p0=pp[0].capitalize()
        if p0 in ("Image","Images"):
            return _handlerImage(env, begin_response)
        elif p0 in ("Script", "Scripts"):
            return _handlerScript(env, begin_response)
             
        h = ( ("content-type", "text/plain"),
        	    ) 
        begin_response("200 Ok", h)
        return [b"test OK", b" clas call"]
    
    
    pass

class EmulateWsgi():
    
    @staticmethod 
    def Start(name=None, port=8080, handler=None):
        
 
        print("handle=", handler)
        if callable(handler):
            pass
        elif hasattr(handler, "handler"):
            handler=handler.handler
                                
        server = wsgiserver.WSGIServer(handler, host='0.0.0.0', port=port)
    
        server = wsgiserver.WSGIServer(handler, host='0.0.0.0', port=port)
        print("Wsgi Server", name,"started at port=", port)
        server.start()
    
        return
    
       
    pass


if __name__ == "__main__":
    
    #Node.BuildPages()
    #print(Node.MainPage)
    #)Node.logger().debug('...')
    Zzz = Xxx()
    
    EmulateWsgi.Start("teste", port=8080, handler=Zzz.handler)

###