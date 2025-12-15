
FROM alpine:latest

WORKDIR /app

RUN apk add --no-cache python3 py3-pip

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt --break-system-packages

COPY exam.py .

CMD ["python3", "exam.py"]