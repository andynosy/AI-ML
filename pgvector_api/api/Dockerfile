# api/Dockerfile
FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

# Install psycopg2 for PostgreSQL connection
RUN pip install psycopg2-binary

# Copy FastAPI application code
COPY . /app

# Run on port 8080
EXPOSE 8080

