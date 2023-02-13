# Use an official Python runtime as a parent image
FROM continuumio/miniconda3

RUN apt-get --allow-releaseinfo-change update
RUN apt-get install -y build-essential 

RUN conda install -y -c conda-forge python-igraph
RUN conda install -y -c conda-forge igraph
RUN conda install -y -c conda-forge louvain
RUN conda install -y -c conda-forge leidenalg

RUN /opt/conda/bin/pip install hidef==1.1.3


RUN mkdir /tmp/cdhidefhcx
COPY ./ /tmp/cdhidefhcx/
RUN pip install /tmp/cdhidefhcx

RUN rm -rf /tmp/cdhidefhcx

ENTRYPOINT ["/opt/conda/bin/cdhidefhcxcmd.py"]

CMD ["--help"]
