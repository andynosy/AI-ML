version: '3.8'

services:
  postgres:
    image: postgres:15
    environment:
      POSTGRES_DB: mydatabase
      POSTGRES_USER: myuser
      POSTGRES_PASSWORD: mypassword
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5433:5433"  # Expose the new internal port on the same port externally
    networks:
      - pg-api-net
    command: ["postgres", "-p", "5433"]  # Tell PostgreSQL to listen on port 5433

volumes:
  pgdata:

networks:
  pg-api-net:
    driver: bridge

