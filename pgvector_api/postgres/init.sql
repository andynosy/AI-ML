-- postgres/init.sql
CREATE EXTENSION IF NOT EXISTS vector;

-- Table for storing vectors
CREATE TABLE items (
    id SERIAL PRIMARY KEY,
    description TEXT,
    embedding VECTOR(1536) -- Adjust dimensionality as needed
);

-- Table for storing API keys
CREATE TABLE api_keys (
    id SERIAL PRIMARY KEY,
    api_key VARCHAR(64) NOT NULL UNIQUE,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    expires_at TIMESTAMP
);

-- Insert a sample API key (for testing)
INSERT INTO api_keys (api_key, description) VALUES ('mysecretapikey', 'Test API Key');
