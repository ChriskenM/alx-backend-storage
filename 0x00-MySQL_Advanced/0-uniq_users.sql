-- Script to creates table users if it doesn't exist
-- email attribute is unique
CREATE TABLE IF NOT EXISTS holberton.users (
	id INT AUTO_INCREMENT PRIMARY KEY,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
);
