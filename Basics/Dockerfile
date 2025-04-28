# Stage 1: Build stage
FROM python:3.9-slim as builder

WORKDIR /app
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip install --no-cache-dir -r requirements.txt

# Stage 2: Runtime stage
FROM python:3.9-alpine

WORKDIR /app
COPY --from=builder /opt/venv /opt/venv
COPY app.py .

# Use the virtual environment from builder
ENV PATH="/opt/venv/bin:$PATH"
ENV FLASK_APP=app.py

EXPOSE 8080
CMD ["python", "app.py"]