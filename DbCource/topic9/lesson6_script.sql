-- В базе данных shop и sample присутствуют одни и те же таблицы, учебной базы данных. 
-- Переместите запись id = 1 из таблицы shop.users в таблицу sample.users. 
-- Используйте транзакции.
-- Сделал если я правильно понял что применение транзакции необходимо было выполнить именно в этом ключе 
USE shop;
SELECT * FROM users;
SELECT
   @user_name := name, 
   @user_birthday_at:=birthday_at, 
   @user_created_at:=created_at, 
   @user_updated_at:=updated_at   
FROM
   users 
WHERE
   id = 1; 
  
USE sample;
START TRANSACTION;
INSERT INTO
   users (name, birthday_at, created_at, updated_at) 
VALUES
   (
      @user_name, @user_birthday_at, @user_created_at, @user_updated_at
   )
;
COMMIT;
SELECT * FROM users;

-- Создайте представление, которое выводит название name товарной позиции из таблицы products и соответствующее название каталога name из таблицы catalogs.
DROP VIEW IF EXISTS view_product;
CREATE VIEW view_product AS 
	SELECT 
		products.name AS product_name,
		catalogs.name AS catalog_name 
	FROM 
		products
		LEFT JOIN catalogs ON products.catalog_id = catalogs.id; 
SELECT * FROM view_product;