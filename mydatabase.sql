CREATE DATABASE mydatabase;

USE mydatabase;

CREATE TABLE usuarios (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);

INSERT INTO usuarios (username, password) VALUES ('nombredeusuario', 'contraseñasegura');
