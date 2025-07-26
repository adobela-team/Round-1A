FROM --platform=linux/amd64 python:3.9-slim

WORKDIR /app

# Install libGL for PyMuPDF rendering support
RUN apt-get update && \
    apt-get install -y --no-install-recommends libgl1 && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt . 
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Ensure input/output folders exist to prevent mount errors
RUN mkdir -p /app/input /app/output

CMD ["python", "main.py"]
