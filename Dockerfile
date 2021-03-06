FROM python:3.8-alpine

RUN mkdir /app
WORKDIR /app
COPY test_app.py /app/

RUN pip install flask
RUN pip install flask_cors

EXPOSE 5000
CMD ["python", "/app/test_app.py"]
