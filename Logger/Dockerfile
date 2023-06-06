#
#
#
ARG ROLE ="Logger"

FROM node

RUN apk add syslog-ng && \
    apk add syslog-ng-redis && \
    apk add syslog-ng-python && \
    apk add syslog-ng-ampq && \
    apk add syslog-ng-http && \
    apk add syslog-ng-json && \
    apk add syslog-ng-python && \
    apk add syslog-ng-xml && \
    apk add syslog-ng-sql && \
    apk add syslog-ng-http && \
    apk add syslog-ng-stomp && \
    apk add syslog-ng-tags-parser && \
    apk add syslog-ng-map-value-pairs && \
    apk add syslog-ng-scl && \
    apk add syslog-ng-add-contextual-data && \
    apk add syslog-ng-redis
   

USER thunder

WORKDIR /TStroke/${ROLE}

COPY * .

ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
CMD ["Start"]

###