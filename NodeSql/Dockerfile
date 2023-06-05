#
#
#

ARG ROLE="NodeSql"

FROM node

RUN apk add mariadb && \
    apk add mariadb-client

USER thunder

WORKDIR /WORK/MARIADB

WORKDIR /TStroke/${ROLE}

COPY * .



###
