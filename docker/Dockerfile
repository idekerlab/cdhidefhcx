# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN mkdir /tmp/cdhidefhcx
COPY ./ /tmp/cdhidefhcx/
RUN pip install /tmp/cdhidefhcx

RUN rm -rf /tmp/cdhidefhcx

ENTRYPOINT ["/opt/conda/bin/cdhidefhcxcmd.py"]

CMD ["--help"]
