# Stage 1: Get Gitleaks binary
FROM zricethezav/gitleaks:latest As gitleaks

# Stage 2: Python base image
FROM python:3.10-alpine3.16
WORKDIR /code

# Copy files and Gitleaks binary
COPY --from=gitleaks /usr/bin/gitleaks /usr/local/bin/gitleaks
COPY . .

# Install dependencies
RUN pip install -r requirements.txt
RUN chmod +x main.py

# Default entry point
ENTRYPOINT ["python3", "main.py"]
