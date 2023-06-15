#
#
#

import sys
import os
import subprocess
import ntplib 
from time import ctime 

from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

from Node import Words as _w

class System():
    
    _isDevelop = None
    @classmethod 
    def isDevelop(cls):
        if cls._isDevelop is None:
            if System.isDocker():
                cls._isDevelop = False
            elif os.env.get("ANDROID_DATA", None) is None:
                cls._isDevelop=False
            else:
                cls._isDevelop =True
        return cls._isDevelop 

    _isDocker=None        
    @classmethod 
    def isDocker(cks):
        if cls._isDocker is None:
            if os.path.is_file("./dockerenv"):
               cls._isDocker=True
            elif os.path.is_pipe("var/run/docker.sock"):
               cls._isDocker=True
            else:
                cls._isDocker=False
            
        return cls._isDocker 
   
    @staticmethod
    def exec(cmd, *args):
        
        r = subprocess.run([cmd, *args], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        r.stdout = r.stdout.split(b"\n")
        return r
    
    @staticmethod 
    def makedir(s):
        os.makedirs(s, exist_ok=True)
        return
    
    
    @staticmethod 
    def getNetwork():
        r=System.exec("ip", "address")
        net= {}
        for e in r.stdout:
            print(e)
            if len(e)==0:
                pass
            else:
                print(e[0])
                if e[0]!=32:
                    ifc={}
                    n=e.split(b": ",3)
                    ni=n[1]
                    flg=n[2]
                    flg = flg.split(b" ")
                    ifc["flags"]=flg[0]
                    net[ni]=ifc
                    print(n)
                else:
                    e=e.strip()
                    if e.startswith(b"inet "):
                        s = e.split(b" ")
                        ifc["ip4"]=s[1]
                        pass
                    pass
        print(net)
        return
    
    
    @classmethod 
    def SyncTime(cls):
        c=ntplib.NTPClient()
        if c is not None:
            response = c.request('pool.ntp.org') 
            ct=ctime(response.tx_time)
            
            print(ct, type(ct))
        
        
        return
    
    pass
    
    
if __name__ =="__main__":
    System.SyncTime()
    sys.exit(0)
    System.getNetwork()


###