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
import time
import http.client
import urllib
import requests
import time
import traceback

from Node import Words as _w

from Node.Io import DEBUG
from Node.Mime import Mime
from Node.Types import Types
from Node.Html import Html
from Node.Data import Data
 
_w.Forbidden = _w._i("Forbidden")
_w.Localhost = _w._i("Localhost")
_w.Http = _w._i("Http")
_w.Https = _w._i("Https")
_w.Image = _w._i("Image")
_w.Images = _w._i("Images")


_w.Get = _w._i("Get")
_w.Put = _w._i("Put")
_w.Post = _w._i("Post")
_w.Head = _w._i("Head")
_w.Delete = _w._i("Delete")
_w.Connect = _w._i("Connect")
_w.Trace= _w._i("Trace")
_w.Patch = _w._i("Patch")
_w.Options = _w._i("Options")
_w.Info = _w._i("Info")
_w.Lock = _w._i("Lock")
_w.Unlock = _w._i("Unlock")
_w.Bind = _w._i("Bind")
_w.Unbind = _w._i("Unbind")
_w.Rebind = _w._i("Rebind")
_w.Copy = _w._i("Copy")
_w.Move = _w._i("Move")
_w.Acl = _w._i("Acl")
_w.Checkin = _w._i("Chechin")
_w.Checkout = _w._i("Checkout")
_w.Uncheckout = _w._i("Uncheckout")
_w.Label = _w._i("Label")
_w.Report = _w._i("Report")
_w.Merge = _w._i("Merge")
_w.Search = _w._i("Search")
_w.Link = _w._i("Link")
_w.Unlink = _w._i("Unlink")
_w.Update = _w._i("Update")
_w.Propfind = _w._i("Propfind")
_w.Bpropfind = _w._i("Propfind")
_w.Proppatch = _w._i("Bproppatch")
_w.Pri = _w._i("Pri")
_w.Mkactivity = _w._i("Mkactivity")
_w.Mkcol = _w._i("Mkcol")
_w.Baseline_Control = _w._i("Baseline-Control")
_w.Mkcalendar = _w._i("mkcalendar")
_w.Mkworkspace = _w._i("Mkworkspace")
_w.Mkredirectref = _w._i("Mkredirectref")
_w.Orderpatch = _w._i("Orderpatch")
_w.Version_Control = _w._i("Version-Control")
_w.Updateredirectref = _w._i("updateredirectref")
_w.Purge = _w._i("Purge")
_w.View = _w._i("View")
_w.Notify = _w._i("Notify")
_w.Poll = _w._i("Poll")
_w.Subscribe = _w._i("Subscribe")
_w.Unsubscribe = _w._i("Unsubscribe")
_w.Bcopy = _w._i("Bcopy")
_w.Bdelete = _w._i("Bdelete")
_w.Bmove = _w._i("Bmove")
_w.Bpropfind = _w._i("Bpropfind")
_w.Bproppatch = _w._i("Bproppatch")

_w.Accept = _w._i("Accept")

class Method():

    Get     = _w.Get
    Put     = _w.Put
    Post    = _w.Post
    Head    = _w.Head
    Info    = _w.Info
    Patch   = _w.Patch
    Connect = _w.Connect
    Bind    = _w.Bind
     
    @classmethod 
    def Validate(cls, m, dflt=None):
         m=m.capitalize()
         fn=getattr(cls, m, None)
         if isinstance(fn, str):
             return fn
         return dflt


    pass

#StatusCodes = Types.Dict().loadFromYaml("/Data/Http/StatusCodes", pwd=__file__)


class _Error(Exception):
    
    def __init__(self, code, msg=None, **opts):
        self._Code=code
        self._Message=msg
        self._Explain = None
        self._Options = opts
        return
        
    @property 
    def Code(self):
        return self._Code
        
    @property 
    def Message(self):
        return self._Message
        
    def __call__(self, *m, **opts):
        r = copy.copy(self)
        r._Options.update(opts)
        r._Explain = m
        return r
    
    pass
    
class Error(_Error):
    
    def __init__(self):
        super().__init__(0)
        return
        
    MovedPermanently = _Error(301, "Moved Permanently")    
    
    PermanentRedirect = _Error(308, "Permanent Redirect")
    
    BadRequest = _Error(400, ("Bad ","Request"))
    Unauthorized = _Error(401, "Unauthorized")
    Forbidden = _Error(403, _w.Forbidden)
    PaymentRequired = _Error(402, ("Payment","Required"))
    NotFound = _Error(404, ("Not","Found"))
    MethodNotAllowed = _Error(405, ("Method", "Not","Allowed"))
    NotAcceptable = _Error(406, ("Not","Acceptable"))
    ProxyAuthenticationRequired = _Error(407, ("Proxy", "Authentication", "Required"))
    RequestTimeout = _Error(408, ("Request","Timeout"))
    Conflict =  _Error(409, "Conflict")
    Gone = _Error(401, "Gone")
    LengthRequired = _Error(411, ("Length","Required"))
    PreconditionFailed = _Error(412, ("Precondition","Failed"))
    PayloadTooLarge = _Error(413, ("Payload","Too","Large"))
    RequestUriTooLong = _Error(414, ("Request","URI", "Too","Long"))
    UnsupportedMediaType = _Error(415, ("Unsuported","Media","Type"))
    RequestedRangeNotSatisfiable = _Error(416, ("Requested","Range","Not","Satisfiable"))
    ExpectationFailed = _Error(417, ("Expectation","Failed"))
    ImATeapot = _Error(418, "I'm a teapot" )
    MisdirectedRequest = _Error(421, ("Misdirected","Request"))
    UnprocessableEntity = _Error(422, ("Unprocessable","Entity"))   
    Locked = _Error(423, "Locked")
    FailedDependency = _Error(424, ("Failed","Dependency"))
    UpgradeRequired = _Error(426, ("Upgrade","Required"))
    PreconditionRequired = _Error(428, ("Precondition","Required"))
    TooManyRequests = _Error(429, ("Too", "Many","Requests"))
    RequestHeaderFieldsTooLarge = _Error(431, "Request Header Too Large")
    ConnectionClosedWithoutResponse = _Error(444, "Connection Close without Response")
    UnavailableForLegalReasons = _Error(451, "Unavailable For Legal Reasons")
    ClientClosedRequest = _Error(499, "Client Closed Request")

    InternalServerError = _Error(500, "Internal Server Error")
    TargetNotImplemented = _Error(501, "Not Implemented") 
    BadGateway = _Error(502, "Bad Gateway")
    ServiceUnavailable = _Error(503, "Service Unavailable")
    GatewayTimeout = _Error(504, "Gateway Timeout")
    HttpVersionNotSupported = _Error(505, "HTTP Version Not Supported")
    VariantAlsoNegotiates = _Error(506, "Variant Also Negotiates")
    InsufficientStorage = _Error(507, "Insufficient Storage")
    LoopDetected = _Error(508, "loop Detected")
    NotExtended = _Error(510, "Not Extended")
    NetworkAuthenticationRequired = _Error(511, "Network Authentication Required" )
    NetworkConnectTimeoutError = _Error(599, "Network Connect Timeout Error")

    
    pass
    


class Pathinfo(Types.List):
    
    def __init__(self, s=None):
        super().__init__()
        if s is not None:
            if isinstance(s, str):
                DEBUG.PATHINFO.S(s)
                s=s.lstrip()               
                s=os.path.normpath(s)
                s=s.replace("\\", "/")   
                if s[0]=="/":
                    s=s[1:]      
                DEBUG.PATHINFO.S(s)           
                s=s.split("/")
                while len(s)>0 and s[0]=="":
                    s=s.pop(0)
                DEBUG.PATHINFO.S(s)
            self.extend(s)
        return
        
    def popFirst(self):
        if len(self)>0:
            return self.pop(0)
        return None
        
    def First(self):
        if len(self)==0:
           return None
        return self[0]
        
    def popLast(self):
        if len(self)>0:
            return self.pop(-1)
        return None
    
    pass
    

class Headers(dict):
    
    _ContentType     = "Content-Type"
    _ContentEncoding = "Content-Encoding"
    _ContentLocation = "Content-Location"
    _ContentLength   = "Content-Length"
    _Accept          = _w.Accept
    _AcceptLanguage  = "Accept-Language"
    _AcceptEncoding  = "Accept-Encoding"
    _CacheControl    = "Cache-Control" 
    
    _XSendFile      = "X-SendFile"
    
    def ContentType(self, c=None, dflt=None):
        if c is not None:
            self[self._ContentType]= c
        return self.get(self._ContentType, dflt)
    
    @classmethod 
    def From(cls, h):       
        r=None
        if isinstance(h, (list, tuple)):
            r = Headers()
            for e in h:
                n, v= e
                r[n]=v
        elif isinstance(h, dict):
            r=Headers()
            r.update(h)            
        else:
            r=Headers()
            
        return r
        
    def asList(self):        
        r=self.items()
        return r
        
    pass

class Request():
    
    __MaxContentLength = 16*1024*1024 ## 16M
    
    @staticmethod 
    def From(e):
        if isinstance(e, Request):
            return e
        return Request(e)
        
    _DataTypes = {
    	            Mime.TextPlain: lambda x: x,
    	            Mime.ApplicationJson: lambda x: Data.fromJson(x),
    	            Mime.ApplicationYaml: lambda x: Data.fromYaml(x),
    	            Mime.ApplicationXml: lambda x: Data.FromXml(x),
    	            }
    
    def __init__(self, env=None):
        super().__init__()
        if not isinstance(env, dict):
           raise ValueError()
                     
        #DEBUG("env=", env)    
            
        #al = env.get("HTTP_ACCEPT_LANGUAGE", None)
        #ae = env.get("HTTP_ACCEPT_ENCODING", None)
        rf = env.get("HTTP_REFERER", None)
        
        self._Accept = None
        self._AcceptLanguage = None
        self._AcceptEncoding = None
        
        hh={}
        for e, v in env.items():
            DEBUG.ENV("-->", e, "=",v)
            if e.startswith("HTPP_"):
                #v=env.get(e, None)
                e=e[5:].replace("_","-").title()
                e=sys.intern(e)
                hh[e]=v
                #DEBUG.HEADERS(e, v)
                if e==Headers.Accept:
                    if v is not None:
                        if ';' in v:
                            v = v.split(';', 2)
                            acm = v[1]
                            v = v[0]
                        v = Mime.Validate(v, Mime.Any)
                        self._Accept=v
                elif e==Headers.AcceptLanguage:
                    self._AcceptLanguage = v
                elif e==Headers.AcceptEncoding:
                    self._AcceptEncoding = v
         
        self._Method = Method.Validate(env.get("REQUEST_METHOD", Method.Get), Method.Get)                            
        self._Version = env.get("wsgi.version", (1,0))
        self._Path= env.get("PATH_INFO", "")
        self._Pathinfo = Pathinfo(self._Path)
        self._PathArg = dict()
        #self._Accept = ac,", "")
        self._Query = None
        self._ContentType = Mime.Validate(env.get("CONTENT_TYPE", ""), Mime.TextPlain)
        self._ContentLength = int(env.get("CONTENT_LENGTH", "0"))
        self._ServerName = env.get("SERVER_NAME", _w.Localhost)
        self._ServerPort = int(env.get("SERVER_PORF", "80"))
        self._ServerProtocol = env.get("SERVER_PROTOCOL", "Http/1.1")
        self._Scheme = env.get("wsgi.url_scheme", _w.Http)
        self._Headers = hh
        self._RemoteAddress = env.get("REMOTE_ADDR", "")
        self._RequestUri = env.get("REQUEST_URI", "")
        self._Input = env.get("wsgi.input", None)
        self._ErrorOutput = env.get("wsgi.errors", None)
        self._PathParm = list()
        self._ServerSoftware = env.get("SERVER_SOFTWARE", None)
        
        dt= self.Read()
        ct = self._ContentType
        fn = self._DataTypes.get(ct, None)
        if callable(fn):
            dt=fn(dt)
        self._Content=dt
        return
          
    @property 
    def Version(self):
        return self._Version
        
    @property
    def Path(self):
        return self._Path
    
    @property 
    def Pathinfo(self):
        return self._Pathinfo
        
    def PathParm(self):
        return self._PathParm
    
    @property 
    def Method(self):
        return self._Method
    
    @property 
    def ScriptName(self):
        return self._ScriptName
        
    def RemoteAddress(self):
        return self._RemoteAddress
        
    @property 
    def RequestUri(self):
        return self._RequestUri 
        
    @property 
    def PathArg(self):
        return self._PathArg
             
    @property 
    def QueryStrinf(self):
        return self._QueryString
        
    def Query(self, var=None, dft=None):
        if self._Query is None:
            qq=urllib.parse.parse_qs(self._QueryString)
            for e, v in qq.items():
                if len(v)==0:
                    qq[e]=None
                elif len(v)==1:
                    qq[e]=v[0]       
            self._Query = qq
        if var is not None:
            return self._Query.get(var, dflt)        
        return self._Query
        
    def ContentType(self, ct=None):
        if ct is not None:
            return (self._ContentType==ct)
        return self._ContentType
    
    @property 
    def ContentLength(self):
        return self._ContentLength
    
    @property 
    def ServerName(self):
        return self._ServerName
    
    @property 
    def ServerPort(self):
        return self._ServerPort
    
    def Accept(self, at=None):
        if at is not None:
            if self._Accept==at:
                return True
            else:
                return False
        return self._Accept        
        
    def Headers(self):
        return self._Headeds
    
    @property 
    def Input(self):
        return self._Input
        
    def Read(self):
        fd=self.Input
        #print("fd=", fd)
        s=fd.read(Request.__MaxContentLength)    
        #print("s=", s)
        c=fd.read(1)
        #print("c=", c)
        if c!=b"":
            raise Http.Error.PayloadTooLarge()
        return s
        
        
    def ErrorOutput(self):
        return self._ErrorOutput
        
    pass
    
class Response():  ## http.client.HTTPResponse
    
    def __init__(self, request=None, status=200, message=None, headers=None, contenttype=None, payload=None):
        self._Request= request
        self._Status= status
        self._Message=message
        self._Payload=payload
        self._Headers=Headers.From(headers)
        if contenttype is not None:
            self.ContentType(contenttype)
        return
        
    def ContentType(self, c=None):
        return self._Headers.ContentType(c)
        
    def Status(self, status=None, message=None):
        if status is not None:
            self._Status=int(status)
        if message is not None:
            self._Message=message
        return self._Status
        
    def Message(self, m=None):
        if message is not None:
            self._Message=message
        return self._Message
        
    def StatusCode(self):
        return str(self._Status)+" "+(self._Message if self._Message is not None else "")
        
    def Header(self, entry, val=None, dflt=None):
        if val is not None:
            self._Headers[entry]=val
        return self._Headers.get(entry, dflt)
        
    def HeaderList(self):
        r=list()
        for e, v in self._Headers.items():
            r.append((e, v))
        return r
        
    def Payload(self, s=None):
        if s is not None:
            self._Payload=s
        return self._Payload 
        
    pass
    

class WsgiHandler():


    def __init__(self, name):
        self._Name=name
        return
    
    @property 
    def Name(self):
        return self._Name             
    
    def Get(self, req):
        return None
        
    def Put(self, env):
        raise Http.Error.MethodNotAllowed()
    
    def Post(self, env):
        raise Http.Error.MethodNotAllowed()
    
    def Head(self, env):
        return None
        
    def Options(self, env):
        raise Http.Error.MethodNotAllowed()
        
    def Connect(senf, env):
        raise Http.Error.MethodNotAllowed()
       
    def Delete(self, env):
        raise Http.Error.MethodNotAllowed()
        
    def Info(self, env):
        raise Http.Error.MethodNotAllowed()
        
    def Patch(self, env):
        raise Http.Error.MethodNotAllowed()
        
    def Lock(self, env):
        raise Http.Error.MethodNotAllowed()
        
    def Unlock(self, env):
        raise Http.Error.MethodNotAllowed()   
        
    def _router(self, part):
        return None

    def do(self, req):
        DEBUG.DO(self.__class__.__name__, "-->")
        mm = req.Method
        
        ac =req.Accept()           
        DEBUG.ACCEPT(ac)
        
        ct = req.ContentType        
        DEBUG.METHOD(mm, ct)
        
        pp=req.Pathinfo
        if pp.notIsEmpty():
            DEBUG.DO.PATH(pp)
            pp=pp.First().capitalize()
            DEBUG.DO.PATH(pp)             
            DEBUG.DO.PATH.ARG(req.PathArg)
            fi="_"+pp.upper()+"_"
            fn=fi+mm
            fn=getattr(self, fn, None)
            if callable(fn):
               tg=req.Pathinfo.popFirst()
               req.PathParm().append(tg)
               resp=fn(req)
            else:
                fi=getattr(self, fi, None)
                if callable(fi):
                    tg=req.Pathinfo.popFirst()
                    req.PathParm().append(tg)
                    resp=fi(req)
                else:
                    tg=self._router(pp)
                    if tg is not None:
                        DEBUG.TARGET(tg.Name, tg)
                        req.Pathinfo.popFirst()
                        req.PathParm().append(tg)
                        return tg.do(req)
                    else:
                        fn = getattr(self, mm, None)
                        if callable(fn):
                            resp = fn(req)
                        else:
                            raise Http.Error.MethodNotAllowed()
            
        return resp
        
    def _error(self, exc, ct=Mime.ApplicationJson):
        resp={
        	     _w.Error: exc.Code,
        	     _w.Message: exc.Message
        	     }        
        return self.doResponse(resp, ct=ct)      
        
    def doResponse(self, resp, ct):
        DEBUG.RESP(resp)     
        if not isinstance(resp, Response):
            if isinstance(resp, Html):
               resp=bytes(str(resp), _w.UTF_8)
               
            elif isinstance(resp, dict):
                if ct==Mime.ApplicationJson:
                   resp=Data.toJson(resp, encode=_w.UTF_8)
                else:
                   resp=str(resp).encode(_w.UTF_8)
               
            elif isinstance(resp, (list, tuple)):
                 if ct==Mime.ApplicationJson:
                     resp=Data.toJson(resp, encode=_w.UTF_8)
                 else:
                     er=list()
                     for e in rr:
                         if isinstance(e, str):
                             er.append(e.encode(_w.UTF_8))
                         else:
                             er.append(e)
                     resp=er
                    
            elif resp is None:
                 resp=[b""]
                
            elif isinstance(resp, str):
                resp = [resp.encode(_w.UTF_8)]
                
            elif isinstance(resp, bytes):
                resp=[resp]
               
            resp=Response(status=0, payload=resp)
           
            if ct is not None:
                resp.ContentType(ct)
                
        return resp
       
        
    def handler(self, env, begin_response):
        stm= int(time.clock()*1000)
        DEBUG.HANDLER(self.__class__.__name__, "-->")
        
        env=Wsgi.Request.From(env)
       
        DEBUG.PATHINFO(env.Pathinfo)
        
        try:
            ct =env.Accept()
            resp = self.do(env)     
            DEBUG.RESP(resp)     
            resp = self.doResponse(resp, ct)     
            resp.Status(200)                
        except _Error as er:
            resp = self._error(er)
            cd=er.Code
            if cd==0:
                cd=500
            if isinstance(resp, Response):
                resp.Status(cd)
            else:
                resp=Response(status=cd, payload=resp)    
                    
                    
        ste=int(time.clock()*1000)
        
        resp.Header("x-timestamp-duration", str(ste-stm))        
        
        DEBUG.STATUS(resp.StatusCode())
        DEBUG.HEADERS(resp.HeaderList())
        begin_response(resp.StatusCode(), resp.HeaderList())
            
        rr = resp.Payload()
        if rr is None:
            rr=[]
        elif not isinstance(rr, (list, tuple)):
            rr=[rr]
        
        DEBUG.HANDLER.RR(type(rr), rr)
        return rr
        

    pass
    
class Wsgi(dict, WsgiHandler):
    
    Request = Request
    Response = Response
    
    def __init__(self, parent, name, route=None):
        super().__init__()
        WsgiHandler.__init__(self, name)
        name= name.replace(" ", '').replace("-", "_")
        name = name.capitalize()
        self._Parent=parent
        #self._Name=name
        if route is None:
            self._Route=name
        else:
            self._Route=route
        if parent is not None:
            if isinstance(parent, Wsgi):
                parent[name]=self
        return
              
    @property 
    def Route(self):
        return self._Route
      
    @property 
    def Parent(self):
        return self._Parent
        
 
            
    def _router(self, part):
        r=None
        part=part.upper()
        for e, v in self.items():
            DEBUG.ROUTER(e, v)
            if isinstance(v._Route, str) and v._Route.upper()==part:
                 return v
            elif isinstance(v._Route, (list, tuple)):
                 for ee in v._Route:
                     if ee.upper()==part:
                         return v
            elif callable(v._Route) and v.Route(part):
                 return v
                      
        return None
        
             
    
        
        
    pass
    
class Http():
   
    Error = Error
    Headers = Headers
    
    pass
    

if __name__ =="__main__":
    from Node.EmulateWsgi import EmulateWsgi 
    
    #raise Http.Error.Forbidden("zzz")

    #q ="a=1&b=2"
    #print("parse --", urllib.parse.parse_qs(q))
    
    class Image(Wsgi):
        pass


    class Xxx(Wsgi):
        pass
        
        
        
    xxx = Xxx(None, "xxx")
    yyy = Image(xxx, "Image")

    EmulateWsgi.Start(name="Http", handler=xxx.handler)


###