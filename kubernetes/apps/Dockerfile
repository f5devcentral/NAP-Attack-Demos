FROM python:3.10-slim

WORKDIR /app
COPY authorizer.py .

RUN pip install flask

EXPOSE 9000
CMD ["python", "authorizer.py"]
