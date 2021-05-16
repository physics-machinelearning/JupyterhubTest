FROM jupyter/scipy-notebook

RUN pip install jupyterhub-nativeauthenticator

USER root

RUN mkdir config bootstrap

COPY config ./config

COPY share ./share

COPY bootstrap ./bootstrap

RUN adduser testuser01
RUN mkdir -p -m 777 /home/jovyan/share/testuser01
RUN chown testuser01: /home/jovyan/share/testuser01

RUN adduser testadmin
RUN mkdir -p -m 777 /home/jovyan/share/testadmin
RUN chown testadmin: /home/jovyan/share/testadmin