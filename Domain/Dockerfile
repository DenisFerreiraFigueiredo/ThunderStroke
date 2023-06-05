#
#
# Domain Node

ARG ROLE="Domain"

FROM nodenosql

#RUN apk add docker

#RUN apk add py3-pip && \
RUN pip install docker ntpclient

RUN apk add ntpsec unbound
  
#RUN apk del py3-pip
    
#RUN addgroup thunder docker

USER thunder

WORKDIR /TStroke/$ROLE


COPY unbound.conf /etc/unbound/unbound.conf
COPY root.hints /var/unbound/etc/root.hints 
COPY root.key /var/unbound/etc/root

COPY $ROLE/* .

ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
CMD ["Start"]

###