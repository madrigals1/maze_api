FROM python:3.8.6-slim-buster

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache pipenv && \
    pipenv install --system --deploy --clear

EXPOSE 5000

CMD ["python", "manage.py", "run", "-h", "0.0.0.0"]
