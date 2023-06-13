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

_w.Signal = _w._i("Signal")
_w.Start = _w._i("Start")
_w.Stop = _w._i("Stop")
_w.Halt = _w._i("Halt")
_w.Resume = _w._i("Resume")
_w.Enable = _w._i("Enable")
_w.Disable = _w._i("Disable")
_w.State = _w._i("State")
_w.Ping = _w._i("Ping")
_w.Pong = _w._i("Pong")
_w.Abort = _w._i("Abort")
_w.Sync = _w._i("Sync")
_w.Reload = _w._i("Reload")

from Node.Service import Service
from Node.Http import Http, Request, Response
from Node.Types import Types
from Node.Io import DEBUG

class Signal(Service):
    
    _SignalTypes = Types.Dict({
    	                        _w.Start:   {},
    	                        _w.Stop:    {},
    	                        _w.Abort:   {},
    	                       })
    
    _PORT = 9050
    
    def Get(self, req):
        raise Http.Error.TargetNotImplemented()
        
    Put = Get
    Post = Get
    Delete = Get
    Head = Get
    
    def _SIGNAL_Get(self, req):    
        DEBUG.SIGNAL.GET(req)
        if req.Pathinfo.notIsEmpty():
            sg=req.Pathinfo.popFirst()
               
        return
        
    def _SIGNAL_Put(self, req): ## receive and push signal
        pp=req.Pathinfo.popFirst()
        if pp is not None:
            pp = self._SignalTypes.Validate(pp)
        return
       
    _SIGNAL_Post = _SIGNAL_Put
    
    pass

SIGNAL = Signal()

def handler(env, begin_response):    
    return SIGNAL.handler(env, begin_response)
    
if __name__ =="__main__":
    from Node.EmulateWsgi import EmulateWsgi 
    
    EmulateWsgi.Start(_w.Signal, handler=handler)
    
    pass

###