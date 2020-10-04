DROP TABLE IF EXISTS logs;
CREATE TABLE logs(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	created_at DATETIME NOT NULL,
	name_table VARCHAR(30) NOT NULL,
	id_record INT UNSIGNED NOT NULL,
	name_record VARCHAR(255) NOT NULL	
)COMMENT='логи' ENGINE=Archive;

--  users, catalogs и products
-- products
DELIMITER //
DROP TRIGGER IF EXISTS added_log_record_from_products_to_log//
CREATE TRIGGER added_log_record_from_products_to_log AFTER INSERT ON products
FOR EACH ROW
BEGIN
	INSERT INTO logs(created_at, name_table, id_record, name_record) VALUES (NEW.created_at, 'products', NEW.id, NEW.name);
END//
DELIMITER ;

INSERT INTO products
  (name, description, price, catalog_id)
VALUES
  ('TEST NAME PRODUCT', 'TEST DESCRIPTION', 9999.99, 1);
  
select * from logs;
select * from products;

-- users
DELIMITER //
DROP TRIGGER IF EXISTS added_log_record_from_users_to_log//
CREATE TRIGGER added_log_record_from_users_to_log AFTER INSERT ON users
FOR EACH ROW
BEGIN
	INSERT INTO logs(created_at, name_table, id_record, name_record) VALUES (NEW.created_at, 'users', NEW.id, NEW.name);
END//
DELIMITER ;

INSERT INTO users 
	(name, birthday_at) 
VALUES
  	('TEST NAME', '1990-01-01');
select * from logs;
select * from users;

-- catalogs
DELIMITER //
DROP TRIGGER IF EXISTS added_log_record_from_catalogs_to_log//
CREATE TRIGGER added_log_record_from_catalogs_to_log AFTER INSERT ON catalogs
FOR EACH ROW
BEGIN
	INSERT INTO logs(created_at, name_table, id_record, name_record) VALUES (CURRENT_TIMESTAMP, 'catalogs', NEW.id, NEW.name);
END//
DELIMITER ;

DELETE FROM catalogs 
WHERE catalogs.name = 'TEST CATALOG';
INSERT INTO catalogs VALUES
  (NULL, 'TEST CATALOG');
select * from logs;
select * from catalogs;

