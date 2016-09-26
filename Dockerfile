FROM python:3.5

ENV PYTHONBUFFERED 1

#Add DefectDojo
ADD . /django.nV

WORKDIR "/django.nV"

RUN pip install -r requirements.txt

RUN ./reset_db.sh
