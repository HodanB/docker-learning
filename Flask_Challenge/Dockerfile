FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir flask redis
EXPOSE 5000
CMD ["python", "app.py"]


