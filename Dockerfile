FROM ubuntu:latest
LABEL maintener="mateusfrancofs3@gmail.com"
RUN apt-get update -y
RUN apt-get install -y libmysqlclient-dev python-pip python-dev build-essential
RUN mkdir project
WORKDIR /project
COPY . /project
EXPOSE 5000
RUN pip install -r requirements.txt
ENTRYPOINT ["python"] 
CMD ["run.py"]