---

# pgvector API

This project provides a Dockerized setup for a PostgreSQL database enhanced with the `pgvector` extension for vector storage and similarity search. It includes a FastAPI application to handle API key generation, vector storage, and similarity search requests via HTTP endpoints.

## Features

- **pgvector Extension**: Enables vector storage and similarity search in PostgreSQL.
- **API Key Management**: Secure access to endpoints using API keys.
- **Endpoints**:
  - Generate new API keys.
  - Insert vectors with metadata.
  - Query similar vectors using Euclidean distance.

## Prerequisites

- **Docker** and **Docker Compose**

## Directory Structure

```
pgvector_api/
├── docker-compose.yml      # Docker Compose configuration
├── postgres/               # PostgreSQL setup
│   ├── Dockerfile          # Dockerfile to install PostgreSQL with pgvector
│   └── init.sql            # Initialization script for creating tables and installing pgvector
└── api/                    # FastAPI setup
    ├── Dockerfile          # Dockerfile for FastAPI
    └── main.py             # FastAPI application code
```

## Getting Started

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/pgvector_api.git
   cd pgvector_api
   ```

2. **Start the Application**:
   Use Docker Compose to start PostgreSQL and FastAPI services.
   ```bash
   docker-compose up -d
   ```

3. **Check Logs**:
   Ensure both containers are running without errors:
   ```bash
   docker-compose logs -f
   ```

## API Endpoints

The following endpoints are available on `http://localhost:8080`.

### 1. Generate API Key

Generate an API key for access control.

**Endpoint**: `POST /generate_api_key`  
**Request Body**:
   ```json
   {
     "description": "Example API Key"
   }
   ```
**Response**:
   ```json
   {
     "api_key": "your_generated_api_key",
     "description": "Example API Key"
   }
   ```

### 2. Insert Vector

Insert a vector along with a description. Requires a 1536-dimensional vector (adjustable in the database setup).

**Endpoint**: `POST /insert_vector`  
**Headers**: `X-API-Key: your_api_key`  
**Request Body**:
   ```json
   {
     "description": "Sample item",
     "embedding": [0.1, 0.2, ...]  // 1536 floats
   }
   ```
**Response**:
   ```json
   {
     "id": 1,
     "description": "Sample item"
   }
   ```

### 3. Query Similar Items

Find the top 5 most similar items to a given query vector.

**Endpoint**: `GET /similar_items`  
**Headers**: `X-API-Key: your_api_key`  
**Request Body**:
   ```json
   {
     "query_vector": [0.1, 0.2, ...]  // 1536 floats
   }
   ```
**Response**:
   ```json
   {
     "similar_items": [
       {"id": 1, "description": "Sample item"},
       ...
     ]
   }
   ```

## Configuration

The PostgreSQL database and FastAPI service are configured in `docker-compose.yml`:

- **Database**: PostgreSQL with `pgvector` extension enabled.
- **FastAPI**: API service for interacting with vectors and managing API keys.

Adjust vector dimensions in `init.sql` as needed for your application.

## Troubleshooting

- **Container Logs**: Check logs for errors.
  ```bash
  docker-compose logs -f
  ```
- **Restarting Services**: If any issues occur, restart the services.
  ```bash
  docker-compose down && docker-compose up -d
  ```

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for more information.

---

This README provides a clear guide to setting up, configuring, and using the Dockerized pgvector database with FastAPI for vector similarity search. Adjust as needed based on specific project requirements or additional details.
