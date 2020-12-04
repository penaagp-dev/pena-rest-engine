FROM alpine

RUN apk update
RUN apk --no-cache add gcc musl-dev python3 python3-dev
RUN pip3 install --upgrade pip
COPY requirements.txt /
RUN pip3 install -r /requirements.txt
WORKDIR /app
EXPOSE 6969