FROM python:3.9-slim
COPY app /app
WORKDIR /app
EXPOSE 80
CMD ["python", "main.py"]
