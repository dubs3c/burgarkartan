FROM python:3.10-slim-bullseye
ENV PYTHONUNBUFFERED 1

RUN apt update && apt upgrade -y && apt install -y \
  git \
  gcc \
  musl-dev \
  libffi-dev \
  make \
  libxslt-dev \
  dos2unix \
  unzip \
  && useradd -m -s /bin/bash burgarkartan && pip install --upgrade pip

USER burgarkartan
RUN mkdir /home/burgarkartan/project
WORKDIR /home/burgarkartan/project
COPY --chown=burgarkartan . /home/burgarkartan/project/
RUN pip install -r requirements.txt -U --user && echo "export PATH=$(python -c 'import site; print(site.USER_BASE + "/bin")'):$PATH" >> ~/.bashrc