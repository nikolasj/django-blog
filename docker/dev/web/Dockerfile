FROM python:3.8.2-alpine
MAINTAINER bandirom@localhost

ENV HOME /usr/src/web
# set work directory
WORKDIR $HOME

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV TZ Europe/Kyiv
ENV LANG C.UTF-8

# install general dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev libffi-dev

# install Ipython dependencies
RUN apk add build-base libzmq zeromq-dev

# install Pillow dependencies
RUN apk add jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev harfbuzz-dev fribidi-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./docker/dev/web/requirements.txt  ./requirements.txt
RUN pip install -r requirements.txt

# copy project
COPY ./web /usr/src/web/

# copy entrypoint.sh
COPY ./docker/dev/web/entrypoint.sh /entrypoint.sh


# run entrypoint.sh
#ENTRYPOINT ["sh", "/entrypoint.sh"]

