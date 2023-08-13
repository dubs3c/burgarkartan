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
  && useradd -m -s /bin/bash burgarkartan && pip install --upgrade pip

#USER burgarkartan
RUN mkdir -p /var/www/burgarkartan && chown -R www-data:www-data /var/www/burgarkartan
WORKDIR /var/www/burgarkartan
COPY --chown=www-data . /var/www/burgarkartan/
USER www-data
RUN pip install -r requirements.txt -U --user && echo "export PATH=$(python -c 'import site; print(site.USER_BASE + "/bin")'):$PATH" >> ~/.bashrc