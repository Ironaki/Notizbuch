FROM python:3.7

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

ENV FLASK_APP app.py
ENV FLASK_ENV development
ENV FLASK_DEBUG 1


CMD ["flask", "run", "--host=0.0.0.0"]
