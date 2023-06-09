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

import binascii
import zlib
import base64
import uuid

from Node.Io import DEBUG

class Uuid():
       
    @staticmethod 
    def new(name=None):
        
        if name == None:
            r=uuid.uuid1()
        elif type(name) == bool:
             r=uuid.uuid4()
        elif type(name) in (str, bytes):
            r = uuid.uuid3(uuid.NAMESPACE_DNS, str(name))
        else:
            r=uuid.uuid2()
        
        return r
    
    
    @staticmethod 
    def _crc(s):
        h = zlib.crc32(s, 0)
        h = h.to_bytes(4, "big")
        h = base64.urlsafe_b64encode(h)
        while h.endswith(b'='):
            h=h[0:-1]
        r=s+b"."+h
        return r
    
    @staticmethod 
    def SID(u0, crc=False, prefix=None, location=None):
        if prefix is None:
            b=b''
        else:
            b=((prefix[0:3].upper()+"___")[0:3]).encode("utf-8")
            #DEBUF.PREFIX(prefix, b)
        if location is not None:
            b+=((location[0:10].upper()+"___________")[0:10]).encode("utf-8")
            #DEBUG._("location",b)
        
        b=u0.bytes+b
        r = base64.urlsafe_b64encode(b)
        while r.endswith(b'='):
            r=r[0:-1]
            
        if crc:
            r= Uuid._crc(r)
            
        return r
        
    @staticmethod 
    def GID(u0, u1=None, u2=None, crc=False, prefix=None, location=None):
        
        r=Uuid.SID(u0, prefix=prefix, location=location)
        if u1 is not None:
            r+= b':'+Uuid.SID(u1)
            if u2 is not None:
                r+= b':'+Uuid.SID(u2)
        if crc:
            r= Uuid._crc(r)
        return r
    
    pass


if __name__ == "__main__":
    x=Uuid.new()
    print(x)
    x1=Uuid.new(True)
    print(x1)
    x2=Uuid.new(b"Zimbra")
    print(x2)
    
    print(Uuid.SID(x, crc=True))
    print(Uuid.GID(x, x1, crc=True))
    
    s=Uuid.GID(x,x1,x2, crc=False)
    print(s, len(s))
    s=Uuid.GID(x,x1,x2, crc=True)
    print(s, len(s))

    pp=Uuid.SID(x, prefix="Cqc", crc=True)
    print(pp, len(pp))
    pp=Uuid.SID(x, prefix="Cqc")
    print(pp, len(pp))
    pp=Uuid.SID(x, prefix="Cqc", location="0123456789")
    print(pp, len(pp))
    pp=Uuid.SID(x, crc=True, prefix="Cqc", location="0123456789")
    print(pp, len(pp))

###