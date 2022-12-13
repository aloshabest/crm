FROM python:3.9
RUN mkdir /code
COPY requirements.txt /code
RUN pip install -r /code/requirements.txt
COPY . /code
CMD python /code/manage.py runserver 0:8000