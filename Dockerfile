FROM python:3.8

WORKDIR /usr/src/flask-lesson

COPY . ./
RUN pip3 install -r requirements.txt
RUN echo http://localhost:5000/

EXPOSE 5000

ENTRYPOINT gunicorn --bind 0.0.0.0:5000 app:app