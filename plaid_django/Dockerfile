FROM python:3
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install supervisor nginx

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN ln -s /code/nginx.conf /etc/nginx/sites-enabled/
RUN nginx -t
RUN service nginx restart
RUN supervisord -n -c supervisor.conf
