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
  procps \
  && groupadd -r -g 997 burgarkartan \
  && useradd -m -s /usr/sbin/nologin -u 998 -g burgarkartan burgarkartan \
  && pip install --upgrade pip

USER burgarkartan
RUN mkdir -p /home/burgarkartan/project
WORKDIR /home/burgarkartan/project
COPY --chown=burgarkartan . /home/burgarkartan/project/
RUN pip install -r requirements.txt -U --user && echo "export PATH=$(python -c 'import site; print(site.USER_BASE + "/bin")'):$PATH" >> ~/.bashrc