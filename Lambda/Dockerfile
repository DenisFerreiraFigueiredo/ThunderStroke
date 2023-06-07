#
# Lambda - Proxy
#

ARG ROLE="Lambda"

FROM node

RUN apk --no-cache add npm

RUN apk add unit-ruby \
#            unit-tools \
            unit-php82 

RUN npm install -g --unsafe-perm unit-http


USER thunder

VOLUME ["/WORK/${ROLE}"]

WORKDIR /TStroke/${ROLE}

COPY * .

#ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
#CMD ["Start"]

###