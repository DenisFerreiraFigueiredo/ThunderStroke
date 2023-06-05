#
# Lambda - Proxy
#

ARG ROLE="Lambda"

FROM node

USER thunder

VOLUME ["/WORK/${ROLE}"]

WORKDIR /TStroke/${ROLE}

COPY * .

#ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
#CMD ["Start"]

###