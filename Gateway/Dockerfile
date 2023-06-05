#
#
#
ARG ROLE="Gateway"

FROM node

RUN apk add nginx && \
    apk add nginx-mod-http-headers-more && \
    apk add nginx-mod-http-geoip && \
    apk add nginx-mod-http-vod && \
    apk add nginx-mod-http-cookie-flag && \
    apk add nginx-mod-http-echo && \
    apk add nginx-mod-http-upload && \
    apk add nginx-mod-http-array-var && \
    apk add nginx-mod-rtmp && \
    apk add nginx-mod-http-log-zmq && \
    apk add nginx-mod-http-fancyindex && \
    apk add nginx-mod-http-encrypted-session && \
    apk add nginx-mod-http-xslt-filter && \
    apk add nginx-mod-http-accounting && \
    apk add nginx-mod-stream-js && \
    apk add nginx-mod-http-image-filter && \
    apk add nginx-mod-http-upstream-fair && \
    apk add nginx-mod-http-zip && \
    apk add nginx-mod-http-untar && \
    apk add nginx-mod-http-dav-ext && \
    apk add nginx-mod-stream && \
    apk add nginx-mod-http-vts && \
    apk add nginx-mod-http-set-misc && \
    apk add nginx-mod-http-cache-purge && \
    apk add nginx-mod-http-redis2 && \
    apk add nginx-mod-http-js 
  
USER thunder

WORKDIR /TStroke/${ROLE}

#COPY * .

ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
CMD ["Start"]

###