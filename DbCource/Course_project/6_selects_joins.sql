USE rental_housing;

-- Определить самое дешевое сдаваемое жилье в Беларусии
SELECT 
	rents.id,
	rents.price AS price,
	countries.name AS country, 
	addresses.city AS city,
	addresses.address AS address
FROM 
	rents
	LEFT JOIN addresses ON rents.addresses_id = addresses.id
	LEFT JOIN countries ON addresses.country_id = countries.id
WHERE 
	countries.name = 'Belarus';
ORDER BY 
	price, city DESC LIMIT 1;

-- Определить 10 пользователей которые наиболешее количество раз сдавали жилье в аренду
-- и какая у них средняя отценка по отзывам
-- Замечание: т.к. сгенеренные данные получились такими что за выполненный заказ отзывов было больше чем по одному(), то для такой ситуации сделал зарпрос №2  

-- Запрос 1. Если бы пользователи могли оставлять только по одному  отзыву за заказ
SELECT 
	CONCAT( users.first_name, ' ', users.last_name) AS user_name,
	COUNT(orders.id) AS count_orders,
	AVG(reviews.estimate) AS average_estimate	
FROM 
	users
	RIGHT JOIN rents ON rents.user_id = users.id 
	JOIN orders ON orders.rent_id = rents.id
	LEFT JOIN reviews ON reviews.order_id = orders.id AND reviews.author != 'seller'
GROUP BY
	user_name
ORDER BY count_orders DESC LIMIT 10
;

-- Запрос 2. Пользователи оставляют несколько запросов за заказ
SELECT 
	CONCAT( users.first_name, ' ', users.last_name) AS user_name,
	COUNT(rent_select.count_orders_id) AS count_orders
	,AVG(rent_select.avg_reviews_estimate) AS average_estimate
FROM 
	users
	RIGHT JOIN (SELECT 
		rents.user_id AS rents_user_id, 
		COUNT(orders.id) AS count_orders_id, 
		AVG(reviews.estimate) AS avg_reviews_estimate
	FROM
		rents  
		JOIN orders ON orders.rent_id = rents.id
		LEFT JOIN reviews ON reviews.order_id = orders.id AND reviews.author != 'seller'
	GROUP BY
		orders.id
		) AS rent_select ON rents_user_id = users.id
GROUP BY
	user_name
ORDER BY count_orders DESC LIMIT 10
;
-- вспомогательный запрос
SELECT 
	CONCAT( users.first_name, ' ', users.last_name) AS user_name,
	COUNT(orders.id) AS count_orders
	,AVG(reviews.estimate) AS average_estimate
FROM 
	users
	RIGHT JOIN rents ON rents.user_id = users.id 
	JOIN orders ON orders.rent_id = rents.id
	LEFT JOIN reviews ON reviews.order_id = orders.id AND reviews.author != 'seller'
GROUP BY
	orders.id
ORDER BY user_name -- DESC LIMIT 20
;

SELECT 
	CONCAT( users.first_name, ' ', users.last_name) AS user_name,
	COUNT(rent_select.count_orders_id) AS count_orders,
	AVG(rent_select.avg_reviews_estimate) AS average_estimate
FROM 
	users
	RIGHT JOIN (SELECT 
		rents.user_id AS rents_user_id, 
		COUNT(orders.id) AS count_orders_id, 
		AVG(reviews.estimate) AS avg_reviews_estimate
	FROM
		rents  
		JOIN orders ON orders.rent_id = rents.id
		LEFT JOIN reviews ON reviews.order_id = orders.id AND reviews.author != 'seller'
	GROUP BY
		orders.id
		) AS rent_select ON rents_user_id = users.id
GROUP BY
	user_name
ORDER BY count_orders DESC LIMIT 10
;
	
