FROM python:3.12

ARG WORKDIR=/democelery

WORKDIR $WORKDIR

COPY . .

RUN pip install -r requirements.txt