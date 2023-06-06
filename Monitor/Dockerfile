#
#
#

ARG ROLE="Monitor"

FROM node


USER thunder

WORKDIR /TStroke/${ROLE}

COPY * .

ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
CMD ["Start"]


###