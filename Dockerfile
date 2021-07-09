FROM python:latest
COPY requirements.txt /code/
RUN pip install -r code/requirements.txt
COPY . /code/
EXPOSE 8000
CMD ["python", "code/manage.py", "runserver", "0.0.0.0:8000"]
