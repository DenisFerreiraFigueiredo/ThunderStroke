#
#
# Clockwork Node

import sys
import os
import syslog

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

_w.Clockwork = _w._i("Clockwork")
_w.CLOCKWORK = _w._i("CLOCKWORK")

_w.Minute = _w._i("Minute")
_w.Minutes = _w._i("Minutes")
_w.Second = _w._i("Second")
_w.Seconds = _w._i("Seconds")
_w.Hour = _w._i("Hour")
_w.Hours = _w._i("Hours")
_w.Day = _w._i("Day")
_w.Days = _w._i("Days")
_w.Month = _w._i("Month")
_w.Months = _w._i("Months")
_w.Year = _w._i("Year")
_w.Years = _w._i("Years")
_w.Week = _w._i("Week")
_w.Weeks = _w._i("Weeks")
_w.Begin = _w._i("Begin")
_w.Half = _w._i("Half")
_w.End = _w._i("End")
_w.Every = _w._i("Every")
_w.Expire = _w._i("Expire")
_w.Expires = _w._i("Expires")
_w.At = _w._i("At")
_w.Active = _w._i("Active")
_w.Job = _w._i("Job")
_w.Jobset = _w._i("Jobset")

from Node.File import Input
from Node.Http import Request, Response
from Node import Node
from Node.Document import Document
from Node.Http import Http
from Node.Io import DEBUG, ERROR

from NodeNosql.Mongodb import Mongodb

from Node.Html import Html

from Node.FlatModel import FlatModel

import threading
import time 
from datetime import datetime, timedelta

def TimeNext(day=None, hour=None, minute=None, second=None):
    tt = datetime.now()
    tm=tt.timestamp()
    #tt = time.mktime(tt)
    if second is not None:
        s= ((int(tt.second / second)+1)*int(second))-tt.second
        dt = timedelta(seconds=s)   
        tt = tt + dt
    if minute is not None:
        m= ((int(tt.minute / minute)+1)*int(minute))-tt.minute
        dt = timedelta(minutes=m)   
        tt = tt + dt
    if hour is not None:
        m= ((int(tt.hour / hour)+1)*int(hour))-tt.hour
        dt = timedelta(hourss=m)   
        tt = tt + dt
     
    #print("tt=", tt)
    next = tt.timestamp()
    #print("-->", next, tm, next-tm)
    return next-tm


class CronJob():
    
    def __init__(self):
        self._Account=None
        self._Id = None # uuid
        self._Name = None
        self._Active= None
        self._Jobset = None
        self._Description = None
        self._Target={
        	            _w.Url: None,
        	            _w.Service: None,
        	            _w.Call: None
        	            }
        self._Schedule={
        	                _w.Start: None,
        	                _w.Stop:  None,
        	                _w.Expires: None,
        	                _w.Next: None
        	                }
        self._TimeZone=None
        self._Retry=None
        
        return
    
    
    
    pass

class ClockworkServer(threading.Thread):
    
    _Cycles = {
    	                _w.Second:  lambda x: TimeNext(second=x),
    	                _w.Seconds: lambda x: TimeNext(second=x),
    	                _w.Minute:  lambda x: TimeNext(minute=x),
    	                _w.Minutes: lambda x: TimeNext(minute=x),
    	                _w.Hour:    lambda x: TimeNext(hour=x),
    	                _w.Hours:   lambda x: TimeNext(hour=x),
    	                _w.Day:    None,
    	                _w.Days:    None,
    	                _w.Week:   None,
    	                _w.Weeks:   None,
    	                _w.Month:  None,
    	                _w.Months:  None,
    	                _w.Year:   None,	  
    	                _w.Years:   None             
    	              }
    
    _TimeLapse = {
    	            _w.Begin: None,
    	            _w.End:   None,
    	            _w.Every: None,
    	            _w.At:    None
    	            }
    
    def __init__(self, name, timecycle=_w.Minute, lapse=5):
        super().__init__(name=_w.CLOCKWORK)
        self._Name=name
        self._Timecycle=timecycle ## minutes
        
        if not timecycle in self._Cycles:
            raise ValueError()
            
        self._Lapse=lapse
        self.next_t = time.time() 
        self.i=0 
        self.done=False 
        
        self._Client = Mongodb.Client("mongodb://localhost:27017/")
        self._Db = self._Client[_w.Clockwork]
        self._cJobs=self._Db[_w.Job+"."+self._Name]
        
        self._cJobsets=self._Db[_w.Jobset+"."+self._Name]
        
        self._run() 
        return
        
    def GetJob(self):
        
        return
             
    def _run(self): 
        req=self._cJobs.FindWhere({ _w.Active: True })
        
        for entry in req:
            DEBUD(entry)
            if entry.ACTIVE:
                ff=True
                if entry.JOBSET is not None:
                    js=self._Cjobsets.Find(entry.JOBSET)
                    if js is not None:
                        if not js.ACTIVE:
                            ff=False
                sc=entry.SCHEDULE
                if sc is None:
                    ff=False
                else:
                    pass
                if ff:
                   tg=entry.TARGET
                   if tg is not None:
                       ar=tg.ARGUMENTS
                       
                       url=tg.URL
                       if url is not None:
                           pass
                       ser=tg.SERVICE
                       if ser is not None:
                           pass
                       cl=tg.CALL
                       if cl is not None:
                           pass
                       ik=tb.INVOKE
                       if ik is not None:
                           pass
                       sg=tg.SIGNAL
                       if sg is not None:
                           pass                           
                       
        
        tc=self._Cycles.get(self._Timecycle, None) 
        if callable(tc):
            self.next_t=tc(self._Lapse)
        else:
            self.next_t=5         
        self.i+=1 
        DEBUG(self._Name, self.i, self.next_t)
        if not self.done: 
            threading.Timer(self.next_t, self._run).start() 
             
    def stop(self): 
        self.done=True 

    pass



class Clockwork(Node):
    
    _PORT = 9030
    _VERSION = (1, 2,0)
   
   
    class Interval():
       
        Minute = 60
        Hour = 60*60
        Day = 60*60*24
       	
        pass
    
    @classmethod 
    def Start(cls, *args, **opts):
        cls._ServerMinute=ClockworkServer(name=_w.Minutes, timecycle=_w.Minute, lapse= 1) 
        cls._ServerHour=ClockworkServer(name=_w.Hours, timecycle=_w.Hour, lapse= 1) 
        cls._ServerDay=ClockworkServer(name=_w.Days, timecycle=_w.Day, lapse= 1) 
        cls._ServerWeek=ClockworkServer(name=_w.Weeks, timecycle=_w.Week, lapse= 1) 
        cls._ServerMonth=ClockworkServer(name=_w.Months, timecycle=_w.Month, lapse= 1) 
        cls._ServerYear=ClockworkServer(name=_w.Yesrs, timecycle=_w.Minute, lapse= 1) 
        return
        
    @classmethod
    def config(cls, *args):
        return self
        
    @classmethod 
    def prepare(cls, *args):
        return self
        
    @staticmethod 
    def stop():
        return
     
    	
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
   	
        
  
    
    
    pass
    
    
def handler(env, begin_response):
    return Domain.handler(env, begin_resoonse)
    
    
if __name__=="__main__":
    
    
    
    a=ClockworkServer(name="oper", timecycle=_w.Seconds, lapse=5) 
    b=ClockworkServer(name="work", timecycle=_w.Seconds, lapse=1) 
    for e in range(1,100):
        ERROR(e)
        time.sleep(0.5) 
    a.stop()
    b.stop()
    sys.exit(0)
    #Domain.Buildup()
    EmulateWsgi(_w.Clockwork)

    d = Domain.Db()  
    

    