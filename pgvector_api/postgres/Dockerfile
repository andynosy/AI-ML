# Extend from PostgreSQL official image
FROM postgres:15

# Install pgvector extension
RUN apt-get update && apt-get install -y postgresql-contrib \
    && apt-get install -y postgresql-server-dev-all \
    && apt-get install -y gcc \
    && apt-get install -y make \
    && apt-get install -y git \
    && git clone --depth 1 https://github.com/pgvector/pgvector /pgvector \
    && cd /pgvector && make && make install

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

EXPOSE 5432
