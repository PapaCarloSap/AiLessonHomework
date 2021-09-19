-- Добавил тригер но думаю может правильнее было сделать id по трем ключам id, order_id, author
-- тригеры должны бы  решить проблему с которой сталкнулся в запросе 6_selects_join.sql

DELIMITER //
DROP TRIGGER IF EXISTS check_count_reviews_insert//
CREATE TRIGGER check_count_reviews_insert BEFORE INSERT ON reviews
FOR EACH ROW
BEGIN
	IF (SELECT COUNT(reviews.id) FROM reviews WHERE reviews.order_id = NEW.order_id AND reviews.author = NEW.author)>0
	THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Added canceled. Reviews is added early';
	END IF;
END//

DROP TRIGGER IF EXISTS check_count_reviews_update//
CREATE TRIGGER check_count_reviews_update BEFORE UPDATE ON reviews
FOR EACH ROW
BEGIN
	IF (SELECT COUNT(reviews.id) FROM reviews WHERE reviews.order_id = NEW.order_id AND reviews.author = NEW.author)>0
	THEN
		SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Updated canceled';
	END IF;
END//
DELIMITER ;

select * from reviews;
INSERT INTO `reviews` (`order_id`, `body`, `estimate`, `author`, `created_at`, `updated_at`) VALUES (116, 'Dolore quis aperiam repudiandae consequatur id voluptates provident architecto. Quo quibusdam nobis quisquam qui doloribus aut. Rem voluptatum aperiam accusantium optio nam doloribus amet.', 5, 'customer', '2017-01-11 01:10:20', '2020-09-17 01:53:46');

-- показать пользователя поставишего больше всех лайков
DELIMITER //
DROP PROCEDURE show_count_likes//
CREATE PROCEDURE show_count_likes()
BEGIN
	SELECT 
		CONCAT( users.first_name, ' ', users.last_name) AS user_name,
		count(likes.id) AS count_likes
	FROM 
		likes
		JOIN users ON users.id = likes.user_id 
	GROUP BY 
		user_name
	ORDER BY count_likes DESC LIMIT 10
	;
END//
DELIMITER ;

CALL show_count_likes();

-- Немного оконных функций
-- Самое дешевое сдаваемое жилье по стране
-- Самое дорогое сдаваемое жилье по стране
DELIMITER //
DROP PROCEDURE min_max_price_by_countries//
CREATE PROCEDURE min_max_price_by_countries()
BEGIN
	SELECT DISTINCT 
		countries.name, 
		FIRST_VALUE(rents.price) OVER(PARTITION BY addresses.country_id ORDER BY rents.price) AS min_price,
		FIRST_VALUE(rents.price) OVER(PARTITION BY addresses.country_id ORDER BY rents.price DESC) AS max_price,
		COUNT(rents.id) OVER(PARTITION BY addresses.country_id) AS count_rents
	FROM 
		addresses
		RIGHT JOIN rents ON addresses.id = rents.addresses_id
		JOIN countries ON addresses.country_id = countries.id 
	;
END//
DELIMITER ;

CALL min_max_price_by_countries();


