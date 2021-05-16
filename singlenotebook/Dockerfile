FROM jupyter/scipy-notebook
USER root
RUN pip install notebook
CMD ["jupyterhub-singleuser", "--allow-root"]