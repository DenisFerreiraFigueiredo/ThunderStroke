#
# Storage - Proxy / cell
#

ARG ROLE="Storage"

FROM node

RUN apk add libnfs libnfs-tools nfs nfs-tools
RUN apk add samba cfis-utils
RUN pip install pyftpdlib

USER thunder

VOLUME ["/WORK/${ROLE}"]

WORKDIR /TStroke/${ROLE}

COPY * .

#ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
#CMD ["Start"]

###