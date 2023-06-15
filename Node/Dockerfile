#
# Node base image
#

FROM alpine

RUN addgroup -S stroke && \
    adduser -S thunder -G stroke
    
    
RUN apk update && \
    apk upgrade && \
    apk add curl

RUN apk add python3 && \
#    apk add python3-dev && \
#RUN apk add py3-dython
    apk add py3-tzlocal && \
#    apk add py3-tornado && \ 
#    apk add py3-btrfs-progs && \
#RUN apk add py3-python-jwt
#RUN apk add py3-python-stdnum
#RUN apk add py3-python-multipart
#RUN apk add py3-python-archive
     apk add py3-python-socks && \
     apk add py3-pyzmq

#    apk add py3-http-ece && \

RUN apk add py3-redis && \
    apk add py3-httpx && \
    apk add py3-httpbin && \
    apk add py3-httplib2 && \
    apk add py3-paho-mqtt && \
    apk add py3-pyzmq && \
#    apk add py3-partd && \
    apk add py3-zipp && \
    apk add py3-zipstream && \
#    apk add py3-html5lib && \
#    apk add py3-mongodb && \
    apk add py3-simplejson && \
    apk add py3-ijson

#RUN apk aďd py3-jsonpickle

RUN apk add py3-json-database && \
    apk add py3-ujson && \
    apk add py3-xmltodict && \
    apk add py3-dicttoxml && \
    apk add py3-ruamel.yaml && \
    apk add py3-rapidyaml && \
    apk add py3-pip && \
    apk add py3-snmp && \
    apk add py3-img2pdf && \
#    apk add py3-pypdf && \
    apk add py3-pdfrw && \
#    apk add py3-docker-py && \
#    apk add py3-pypng && \
    apk add archivemount && \
#    apk add cython && \
    apk add py3-html5lib
#RUN apk add py3-dsnpython

RUN pip install pyyaml pymongo requests wsgiserver celery ntplib

RUN pip install requests-unixsocket

RUN apk add libzmq zeromq

#RUN apk del py3-pip

RUN apk add unit \
#            unit-tools \
            unit-python3 unit-openrc
    
RUN apk add memcached && \
    apk add redis hiredis

#USER thunder

ENV THUNDERSTROKE_ROLE=${ROLE}

VOLUME ["/WORK"]

WORKDIR /TStroke/${ROLE}

COPY * .

WORKDIR /TStroke

EXPOSE 80 443

#ENTRYPOINT ["/usr/bin/python3", "-m", "Node"]
#CMD ["Start"]



###