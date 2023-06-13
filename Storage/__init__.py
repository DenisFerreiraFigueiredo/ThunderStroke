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

_w.Storage = _w._i("Storage")

from NodeNosql import NodeNosql

import gridfs

from Storage.Bucker import Bucker
from Storage.Blob import Blob
from Storage.FtpServer import FtpServer

class Grinder(NodeNosql):
    
    _PORT = 11000
    _VERSION = (1, 1, 0) 
    
    
    pass




###