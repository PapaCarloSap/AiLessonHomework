-- Create table users
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	name VARCHAR(255) NOT NULL UNIQUE COMMENT 'login name',
	first_name VARCHAR(100) NOT NULL COMMENT 'First name user',
	last_name VARCHAR(100) NOT NULL COMMENT 'Last name user',
	photo_id INT UNSIGNED COMMENT 'Link on photo',
	created_at DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Registered user';

DROP TABLE IF EXISTS profiles;
CREATE TABLE profiles (
	user_id SERIAL PRIMARY KEY COMMENT 'Link on user in users', 
	gender CHAR(1) NOT NULL COMMENT 'Gender',
	birthday DATE COMMENT 'Birthday of user',
	phone VARCHAR(100) NOT NULL UNIQUE COMMENT 'Phone number',
	email VARCHAR(100) NOT NULL UNIQUE COMMENT 'E-mail',
	addresses_id INT COMMENT 'Link on addresses',
	created_at DATETIME NOT NULL  DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Profile by registered user';

DROP TABLE IF EXISTS addresses;
CREATE TABLE addresses (
	id SERIAL PRIMARY KEY,
	user_id INT UNSIGNED NOT NULL COMMENT 'Link on user owner of housing', 
	address VARCHAR(255) NOT NULL COMMENT 'Address',
	district VARCHAR(130) NOT NULL COMMENT 'District',
	city VARCHAR(130) NOT NULL COMMENT 'City',
	country_id INT UNSIGNED NOT NULL COMMENT 'Link on country',
	postal_code VARCHAR(30) COMMENT 'Postal code (ZIP)',
	type_address ENUM('registration address', 'address for rent'),
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Addresses for registred users or rent out housing';

DROP TABLE IF EXISTS rents;
CREATE TABLE rents (
	id SERIAL PRIMARY KEY,
	description TEXT COMMENT 'House description',
	addresses_id INT UNSIGNED NOT NULL COMMENT 'Link on address',
	price decimal(8, 2) NOT NULL COMMENT 'Price one day/night',
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Addresses for registred users or rent out housing';

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
	id SERIAL PRIMARY KEY,
	customer_user_id INT UNSIGNED NOT NULL COMMENT 'Сustomer housing',
	rent_id INT UNSIGNED NOT NULL COMMENT 'Housing for rent',
	price decimal(8, 2) NOT NULL COMMENT 'Summary price',
	start_date_rent DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Start time rent',
	end_date_rent DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'End time rent',
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'table of transactions for the lease of housing';

DROP TABLE IF EXISTS photos;
CREATE TABLE photos (
	id SERIAL PRIMARY KEY,
	user_id INT UNSIGNED NOT NULL COMMENT 'user', 
	filename VARCHAR(255) NOT NULL COMMENT 'path to file',
	digest varchar(256) NOT NULL comment 'SHA256 дайжест файла',
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Repository of photos';

DROP TABLE IF EXISTS photos_rent;
CREATE TABLE photos_rent (
	photo_id SERIAL PRIMARY KEY COMMENT 'Link on photos',
	rent_id INT UNSIGNED NOT NULL COMMENT 'Link on rent_positions',
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT 'Photos of rent positions ';

DROP TABLE IF EXISTS messages;
CREATE TABLE messages (
	id SERIAL PRIMARY KEY,
	from_user_id INT UNSIGNED NOT NULL COMMENT 'Link on user sender',
	to_user_id INT UNSIGNED NOT NULL COMMENT 'Link on user recipients',
	body TEXT NOT NULL COMMENT 'Text of message',
	is_important BOOLEAN COMMENT 'Mark important',
	is_delivered BOOLEAN COMMENT 'Mark вeliveries',
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Chat';

DROP TABLE IF EXISTS reviews;
CREATE TABLE reviews (
	id SERIAL PRIMARY KEY,
	order_id INT UNSIGNED NOT NULL COMMENT 'Link on order',
	body TEXT NOT NULL COMMENT 'Text of message',
	author ENUM('customer', '', 'seller'),
	created_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'Time create record',
	updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Time update record'
) COMMENT = 'Reviews about orders';

DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  target_id INT UNSIGNED NOT NULL,
  target_type_id INT UNSIGNED NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
 
DROP TABLE IF EXISTS target_types;
CREATE TABLE target_types (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);
 
INSERT INTO target_types (name) VALUES
  ('reviews'),
  ('users'),
  ('rents');