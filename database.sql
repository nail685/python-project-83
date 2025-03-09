DROP TABLE IF EXISTS urls;
DROP TABLE IF EXISTS data_base;

CREATE TABLE if NOT EXISTS urls (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    name VARCHAR(50) NOT NULL,
    created_at TIMESTAMP NOT NULL,
);

CREATE TABLE if NOT EXISTS data_base (
    id BIGINT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    id_url BIGINT REFERENCES urls(id) NOT NULL
    name VARCHAR(50),
    response_cod int NOT NULL,
    h1 VARCHAR(50),
    title VARCHAR(150),
    description VARCHAR(255),
    created_at TIMESTAMP,
);