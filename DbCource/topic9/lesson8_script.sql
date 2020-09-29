-- Создайте хранимую функцию hello(), которая будет возвращать приветствие, в зависимости от текущего времени суток. 
-- С 6:00 до 12:00 функция должна возвращать фразу "Доброе утро", 
-- с 12:00 до 18:00 функция должна возвращать фразу "Добрый день", 
-- с 18:00 до 00:00 — "Добрый вечер", с 00:00 до 6:00 — "Доброй ночи".
DROP FUNCTION IF EXISTS hello;
DELIMITER //
CREATE FUNCTION hello ()
RETURNS VARCHAR(255) DETERMINISTIC
BEGIN
	DECLARE cur_time INT DEFAULT CURRENT_TIME()+0; 
	IF (cur_time >= 60000 AND cur_time < 120000) THEN
		RETURN 'Доброе утро!';
	ELSEIF (cur_time >= 120000 AND cur_time < 180000) THEN
		RETURN 'Добрый день!';
	ELSEIF (cur_time >= 180000) THEN
		RETURN 'Добрый вечер!';
	ELSE
		RETURN 'Доброй ночи!';
	END IF;
END//
DELIMITER ;
SELECT hello();

-- В таблице products есть два текстовых поля: name с названием товара и description с его описанием. 
-- Допустимо присутствие обоих полей или одно из них. Ситуация, когда оба поля принимают неопределенное значение NULL неприемлема. 
-- Используя триггеры, добейтесь того, чтобы одно из этих полей или оба поля были заполнены. При попытке присвоить полям NULL-значение необходимо отменить операцию.
DELIMITER //
DROP TRIGGER IF EXISTS check_product_name_description_insert//
CREATE TRIGGER check_product_name_description_insert BEFORE INSERT ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND NEW.description IS NULL) THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Added canceled';
	END IF;
END//

DROP TRIGGER IF EXISTS check_product_name_description_update//
CREATE TRIGGER check_product_name_description_update BEFORE UPDATE ON products
FOR EACH ROW
BEGIN
	IF (NEW.name IS NULL AND OLD.description IS NULL) 
		OR (OLD.name IS NULL AND NEW.description IS NULL)
	THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Updated canceled';
	END IF;
END//
DELIMITER ;

INSERT INTO products 
	(name, description, price, catalog_id)
VALUES
	-- (NULL, NULL, 15000,1);	
	(NULL, 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 15000,1);
	-- ('Intel Core i9 - 9900K', NULL, 15000,1);
	-- ('Intel Core i9 - 9900K', 'Процессор для настольных персональных компьютеров, основанных на платформе Intel.', 15000,1);
-- UPDATE products SET name = NULL WHERE id = 16;	
UPDATE products SET description = NULL WHERE id = 15;	

select * from products;