FROM python:3.12

ARG democelery

WORKDIR $ARG

COPY . $WORKDIR

RUN pip install -r requirements.txt