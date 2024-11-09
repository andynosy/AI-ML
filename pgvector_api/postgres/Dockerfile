# Extend from PostgreSQL official image
FROM postgres:15

# Set environment variables for PostgreSQL
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Expose the new port (5433) instead of the default 5432
EXPOSE 5433

# Start PostgreSQL and specify the port
CMD ["postgres", "-p", "5433"]
