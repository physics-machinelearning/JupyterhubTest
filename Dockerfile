FROM jupyter/scipy-notebook

RUN pip install jupyterhub-nativeauthenticator

USER root

RUN mkdir config bootstrap

COPY config ./config

COPY bootstrap ./bootstrap

RUN adduser testuser01
RUN mkdir -p -m 777 /home/testuser01/notebook
RUN chown testuser01: /home/testuser01/notebook

RUN adduser testadmin
RUN mkdir -p -m 777 /home/testadmin/notebook
RUN chown testadmin: /home/testadmin/notebook