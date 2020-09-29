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

