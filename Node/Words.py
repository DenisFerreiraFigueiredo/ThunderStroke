#
#
#

import sys
from pathlib import Path

ipth = Path(__file__).parent.parent
ipth = str(ipth)

if ipth not in sys.path:
    sys.path.insert(0, ipth)

_i = sys.intern

#class Words():

DOMAIN = _i("DOMAIN")
LAMBDA = _i("LAMBDA")
IAM = _i("IAM")
SDB = _i("SDB")
APIG = _i("APIG")
LOG = _i("LOG")
SMS = _i("SMS")
SQS = _i("SQS")
DDB = _i("DDB")
MDB = _i("MDB")
STG = _i("STG")

BUCKET = _i("BUCKET")
SERVER = _i("SERVER")
    
NODE = _i("NODE")
THUNDERSTTOKE = _i("THUNDERSTROKE")
    
SimpleDb = _i("SimpleDb")

Domain = _i("Domain")
Version = _i("Version")
Docker = _i("Docker")
Default = _i("Default")
Lambda = _i("Lambda")
Services = _i("Services")
Regions = _i("Regions")
Thunderstroke = _i("Thunderstroke")
Gateway = _i("Gateway")
Accounts = _i("Accounts")
Name = _i("Name")
Entity = _i("Entity")
User = _i("User")
Users = _i("Users")
Group = _i("Group")
Groups = _i("Groups")
Organization = _i("Organization")
Organizations = _i("Organizations")
Defaukt = _i("Default")
Error = _i("Error")
_True = _i("True")
_False = _i("False")
Test = _i("Test")
Start = _i("Start")
End = _i("End")
Description = _i("Description")
Javascript = _i("Javascript")
Java = _i("Java")
Python = _i("Python")
Message = _i("Message")

Thunder = _i("Thunder")
Stroke = _i("Stroke")
_thunder = _i("thunder")
_stroke = _i("stroke")

_http = _i("http")
_html = _i("html")
_socket = _i("socket")
_module = _i("module")
_threads = _i("threads")
_master = _i("master")	
_docker = _i("docker")
_create = _i("create")
_network = _i("network")
_connect = _i("connect")
_start = _i("start")
_restart = _i("restart")
_config = _i("config")
_stop = _i("stop")
_status = _i("status")
_prepare = _i("prepare")
_info = _i("info")
_verbosity = _i("verbosity")

_thunderstroke = _i("thunderstroke")

UTF_8 = _i("UTF-8")

    #pass
###