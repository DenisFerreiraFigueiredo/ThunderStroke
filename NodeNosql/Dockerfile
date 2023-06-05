#
#
#

ARG ROLE="NodeMongodb"

FROM node

RUN echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/main' >> /etc/apk/repositories && \
    echo 'http://dl-cdn.alpinelinux.org/alpine/v3.6/community' >> /etc/apk/repositories && \
    apk update && \
    apk upgrade && \
    apk add mongodb && \
    apk add mongodb-tools

#RUN apk add py3-pip
RUN pip install pymongo
#RUN apk del py3-pip

USER thunder

WORKDIR /WORK/MONGODB

###
