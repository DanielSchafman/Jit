FROM python:3.9-slim

RUN apt-get update && \
    apt-get install -y curl && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -L https://github.com/zricethezav/gitleaks/releases/download/v8.18.1/gitleaks_8.18.1_linux_x64.tar.gz | tar xz && \
    mv gitleaks /usr/local/bin/

WORKDIR /code

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x main.py

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

ENTRYPOINT ["python3", "main.py"]
