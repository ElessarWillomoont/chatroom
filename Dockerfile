FROM ubuntu 
WORKDIR /project

ADD requirements.txt .
RUN pip3 install -r requirements.txt