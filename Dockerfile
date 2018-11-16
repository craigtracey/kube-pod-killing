FROM python:2-alpine

RUN apk add --no-cache tini
COPY killer.py /tmp
COPY paricide.py /tmp
ENTRYPOINT ["/sbin/tini", "--", "/sbin/tini", "-s", "--"]
