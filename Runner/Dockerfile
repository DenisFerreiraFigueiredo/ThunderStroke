#
# Runner (StepFunction)
#

ARG ROLE="Runner"

FROM nodenosql

USER thunder

WORKDIR /TStroke/${ROKE}

COPY * .

ENTRYPOINT ["/usr/bin/python3", "-m", "${ROLE}"]
CMD ["Start"]

###