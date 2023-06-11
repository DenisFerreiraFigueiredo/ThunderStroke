#
#
# Runner Node (Step Functions)

import sys
import os
import syslog

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

_w.RUNNER= _w._i("RUNNER")
_w.Runner = _w._i("Runner")
_w.Low = _w._i("Low")
_w.Statemachine = _w._i("Statemachine")
_w.State = _w._i("State")

from Node.File import Input
from Node.Http import Request, Response
from Node.Docker import Docker
from Node import Node
from Node import Words as _w
from Node.Document import Document

from NodeNosql.Mongodb import Mongodb

import threading

class RunnerServer(threading.Thread):
    
     
    
    def __init__(self, name, priority=_w.Low):
        super().__init__(name=_w.RUNNER)
        self._Name=name
        
            
        self._Priority=priority
        self._Done=False 
        
        if Runner._Mongodb.socketFilePath.is_file():
            pass
        
        self._Client = RunnerServer._Mongodb.Client("mongodb://localhost:27017/")
        
        self._Db = self._Client[_w.Runner]
        self._cJobs=self._Db[_w.Job][self._Name][self._Priority]
        
        self._cJobsets=self._Db[_w.Jobsets][self._Name][self._Priority]
        
        self._cLogs=self._Db[_w.Logs][self._Name][self._Priority]
        
        self._run() 
        return
        
    def doJob(self, jb):
        if isinstance(jb, str):
            pass
        elif isinstance(jb, bool):
            return job
        elif isinstance(jb, dict):
           self.doJob(jb.JOB) 
           self.doTask(jb.TASK)
        elif isinstance(jb, (list, tuple)):
            for e in jb:
                self.doJob(jb)
        return False
    
    def doTask(self, tsk):
        if isinstance(tsk, str):
            pass
        elif isinstance(tsk, bool):
            return tsk
        elif isinstance(tsk, dict):
            self.doTask(tsk.TASK)
            self.doStep(tsk.STEP)
        elif isinstance(tsk, (list, tuple)):
            for e in tsk:
                self.doTask(e)
        return False
        
    def doStep(self, stp):
        if isinstance(stp, str):
            pass
        elif isinstance(stp, bool):
            return stp
        elif isinstance(stp, dict):
            pass
        elif isinstance(stp, (list, tuple)):
            for e in stp:
                self.doStep(e)
        
        return False
        
    def doCommand(self, cmd):
        return False
   
   def _run(self):
       
       while not self._Stop:
           pass
           
       return
    
    def stop(self):
        self._Stop=True
        return
    
    
    
    pass
    
    
class StatemachineServer(threading.Thread):
    
    def __init__(self, name, priority=_w.Low):
        super().__init__(name=_w.RUNNER)
        self._Name=name
        
            
        self._Priority=priority
        self._Done=False 
        
        if Runner._Mongodb.socketFilePath.is_file():
            pass
        
        self._Client = Runner._Mongodb.Client("mongodb://localhost:27017/")
        
        self._Db = self._Client[_w.Statemachine]
        self._cMachines=self._Db[_w.Machine][self._Name][self._Priority]
        self._cStates=self._Db[_w.States][self._Name][self._Priority]
        
        self._cMachinesets=self._Db[_w.Machinesets][self._Name][self._Priority]
        
        self._cLogs=self._Db[_w.Logs][self._Name][self._Priority]
        
        self._run() 
        return
        
        
    def validState(self, st):
        if isinstance(st, str):
        elif isinstance(st, bool):
            pass        
        return False
        
    def validMachineset(self, ms):
        
        return True
        
    def doProcess(self, _id, acct, stt, proc):
        
        return False
        
    def doMachine(self, _id, entry):
        if isinstance(entry, str):
            pass
        elif isinstance(entry, bool):
            return entry
        if isinstance(entry, dict):
             acct=entry.ACCOUNT
             if self.validState(entry.STATE): ## Current state
                 if self.valid.Machineset(entry.MACHINESET):
                     self.doProcess(_id, entry.ACCOUNT, entry.STATE, entry.PROCESS)
             
        elif isinstance(entry, (list, tuple)):
            for e in entry:
                self.doMachine(_id=_id, e)       
        
        return False
        
        
    def _run(self):
       
       while not self._Stop:
           ss = self._cStatemachine.FindWhere({ _w.Active : True })
           if ss is not None:
               for sm in ss:
                   seld.doMachine(sm.Id, sm)
           
            time.slep(0.0005)
                     
       return
    
    def stop(self):
        self._Stop=True
        return
    
    
    pass

class Runner(Node):
   
    _Mongodb = Mongodb(_w.Runner)
   
   
    @classmethod 
    def Info(cls, *args):
        r= { _w.RUNNER: { _w.Version:  (1, 0, 0)}}
        return r
    
    @classmethod 
    def Start(cls, *args):
        return
    
 
        
    @classmethod
    def config(cls, *args):
        cfg = uWsgi(_Domain)
        cfg.begin()
        cfg()
        cfg(_http, ":9000")
        cfg(_module, _Domain)
        cfg(_threads, 2)  
        cfg(_route, "^/iam/",      "redirect:http://localhost:9050/")
        cfg(_route, "^/lambda/",   "redirect:http://localhost:9100/")
        cfg(_route, "^/simpledb/", "redirect:http://localhost:9100/")
            
        
        cfg.end()        
        return self
        
    @classmethod 
    def prepare(cls, *args):
        System.makedir("/opt/Zimbra")
        System.makedir("/WORK")
        return self
    
    @staticmethod 
    def start():
        return
        
    @staticmethod 
    def stop():
        return
    
    @staticmethod 
    def submit():
        System.exec("docker", "run", "--name", "ping-service-container", "-p", "5000:5000", "ping-service")
        return
  
    def prepare(self, *args):
        
        
        
        return self
    	
    _Client = None
    _Db = None
    
    _clAccounts = None
        	
     
    @classmethod 
    def Client(cls):
        if cls._Client is None:
            cls._Client = Mongodb.Client("mongodb://localhost:27017/")
        
        return cls._Client
        
    @classmethod 
    def Db(cls):
        if cls._Db is None:
            cls._Db = cls.Client()[_w.Domain]
        return cls._Db
   	
    _Regions = None
    _Services = None
    
    
   	
    @classmethod 
    def Services(cls):
        if cls._Services is None:
            cls._clServices = Domain.Db()[_w.Services]
            cls._Services = Input.YAML(_w.Services, pwd=__file__).read()
            cls._clServices.loadFrom(_w.Services, cls._Services, True)
                                
        return cls._Services
   
    @classmethod 
    def Regions(cls):
        if cls._Regions is None:
            cls._clSRegions = Domain.Db()[_w.Regions]                    
            cls._Regions = Input.YAML(_w.Regions, pwd=__file__).read()
            cls._clRegions.loadFrom(_w.Regions, cls._Regions, True)
            
        return cls._Regions
            
    @classmethod 
    def Buildup(cls):
        serv=cls.Services()
        
        #do=Docker()
        #gw=do.host(_w.Gateway, "Gateway")
        
        return
    
    
    pass
    
    
def handler(env, begin_response):
    return Domain.handler(env, begin_resoonse)
    
    
if __name__=="__main__":

    
    pass

    