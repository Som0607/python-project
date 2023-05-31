FROM ubuntu:latest
RUN apt update && apt upgrade -y
RUN apt-get -y install python3.6
#RUN python3 --version'
ADD main.py .

CMD ["python3", "./main.py"]