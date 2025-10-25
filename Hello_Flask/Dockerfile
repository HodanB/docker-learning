# Stage 1 - Build stage
FROM python:3.8-slim AS build
WORKDIR /app

# Install build dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libmariadb-dev \
    pkg-config \
 && rm -rf /var/lib/apt/lists/*  # clean cache

# Copy files
COPY . .

# Install Python dependencies
RUN pip install --no-cache-dir flask mysqlclient

# Stage 2 - Production stage
FROM python:3.8-slim
WORKDIR /app

# Copy built files from stage 1
COPY --from=build /app /app

# Expose port and run the app
EXPOSE 5002

CMD ["python", "app.py"]
