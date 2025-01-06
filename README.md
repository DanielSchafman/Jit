Gitleaks Runner Usage Guide:

1. Pull the Docker Image
    Pull the latest Docker image from Docker Hub:

    docker pull danielschafman/gitleaks-runner:latest

2. Run the Container
    Scan Current Directory Without Saving Output to a File:
    docker run --rm -v $(pwd):/scan danielschafman/gitleaks-runner gitleaks detect --source=/scan --no-git

3. Scan Current Directory and Save Output to a File
    docker run --rm -v $(pwd):/scan danielschafman/gitleaks-runner gitleaks detect --source=/scan --no-git --report-path /scan/output.json




