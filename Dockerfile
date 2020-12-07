FROM python:3.8.5

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY organizzare-back /app
WORKDIR /app

CMD [ "python", "run.py" , "runserver"] 