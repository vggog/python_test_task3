FROM python:3.10
EXPOSE 8000
WORKDIR /code

RUN apt-get update

COPY requirements.txt /code
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /code

CMD ["python3", "manage.py", "migrate"]
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
