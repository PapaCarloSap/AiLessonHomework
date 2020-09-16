-- 1.1 Пусть в таблице users поля created_at и updated_at оказались незаполненными. Заполните их текущими датой и временем.
DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(15)
); 
INSERT INTO users (name) VALUES ('Иван'), ('Петр'), ('Алексей'), ('Генадий');
ALTER TABLE users 
	ADD (created_at datetime), 
	ADD (updated_at datetime);
UPDATE users 
	SET created_at = CURRENT_TIMESTAMP(),
	updated_at = CURRENT_TIMESTAMP();
SELECT * FROM users; 

-- 1.2 Таблица users была неудачно спроектирована. Записи created_at и updated_at были заданы типом VARCHAR и в них долгое время помещались значения в формате 20.10.2017 8:10. Необходимо преобразовать поля к типу DATETIME, сохранив введённые ранее значения.
DROP TABLE IF EXISTS users;
CREATE TABLE users(
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	created_at VARCHAR(15),
	updated_at VARCHAR(15)
); 
INSERT INTO	users (created_at, updated_at) VALUES ('20.10.2017 8:10', '8.12.2017 22:10'), ('1.1.2020 10:10', '1.1.2020 10:10');
ALTER TABLE users
	ADD (created_ta_new datetime),
	ADD (updated_ta_new datetime);
UPDATE users SET 
	created_ta_new = STR_TO_DATE(created_at,'%d.%m.%Y %H:%i'),
	updated_ta_new = STR_TO_DATE(updated_at,'%d.%m.%Y %H:%i');
ALTER TABLE users
	DROP created_at, 
	DROP updated_at;
ALTER TABLE users 
	RENAME COLUMN created_ta_new TO created_at,
	RENAME COLUMN updated_ta_new TO updated_at;

-- 1.3 В таблице складских запасов storehouses_products в поле value могут встречаться самые разные цифры: 0, если товар закончился и выше нуля, если на складе имеются запасы. Необходимо отсортировать записи таким образом, чтобы они выводились в порядке увеличения значения value. Однако нулевые запасы должны выводиться в конце, после всех записей.
DROP TABLE IF EXISTS storehouses_products;
CREATE TABLE storehouses_products (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	value int UNSIGNED
);
INSERT INTO storehouses_products (value) VALUES (0), (2500), (0), (30), (500), (1);
select * from storehouses_products LIMIT 10;
SELECT value FROM (SELECT value, IF (value>0,1,2) AS my_group FROM storehouses_products	ORDER BY my_group, value) AS order_storehouses_products;

-- 2.1 Подсчитайте средний возраст пользователей в таблице users.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(10),
	age INT UNSIGNED 
);
INSERT INTO users (name, age) VALUES ('Андрей', 10), ('Алексей', 20), ('Иван', 30), ('Евгений', 40);
select * from users LIMIT 10;
SELECT AVG(age) medium_age FROM users;

-- 2.2 Подсчитайте количество дней рождения, которые приходятся на каждый из дней недели. Следует учесть, что необходимы дни недели текущего года, а не года рождения.
DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255) COMMENT 'Имя покупателя',
  birthday_at DATE COMMENT 'Дата рождения',
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
) COMMENT = 'Покупатели';
INSERT INTO users (name, birthday_at) VALUES
    ('Геннадий', '1990-10-05'),
    ('Наталья', '1984-11-12'),
    ('Александр', '1985-05-20'),
    ('Сергей', '1988-02-14'),
    ('Иван', '1998-01-12'),
    ('Мария', '1992-08-29');
INSERT INTO users (name, birthday_at) VALUES
	('Толя', '1990-10-06'),
	('Светлана', '1990-10-04'),
	('Катя', '1985-05-19');

SELECT * FROM users;
SELECT 
	WEEK(birthday_at) AS birthday_week,
	COUNT(*) AS total_birthday_on_week
FROM users 
GROUP BY birthday_week 
ORDER BY birthday_week; 
