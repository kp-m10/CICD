FROM ubuntu:latest

RUN apt-get update -y && \
    apt-get install -y python3-pip

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app


RUN pip3 install -r requirements.txt

RUN pip3 install --upgrade pip

RUN pip3 install boto3

RUN pip3 install awscli

WORKDIR /app

COPY . /app

#EXPOSE 5001

ENTRYPOINT [ "python3" , "app.py"]
#CMD [ "app.py" ]
