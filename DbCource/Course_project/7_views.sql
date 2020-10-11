-- Вывести логин арендодателя страну город и цену сдаваемого жилья 
DROP VIEW IF EXISTS user_rent_price_view;
CREATE VIEW user_rent_price_view AS 
	SELECT 
		users.name AS login,
		countries.name AS countries,
		addresses.city AS city,
		rents.price AS price 
	FROM 
		users
		RIGHT JOIN rents ON rents.user_id = users.id
		LEFT JOIN addresses ON rents.addresses_id = addresses.id
		LEFT JOIN countries ON addresses.country_id = countries.id
	ORDER BY countries;

-- Вывести пользователя и его отценки при путешествии по странам 
DROP VIEW IF EXISTS user_country_estimate;
CREATE VIEW user_country_estimate AS 
	SELECT 
		users.name AS login,
		countries.name AS countries,
		reviews.estimate AS estimate 
	FROM 
		users
		RIGHT JOIN orders ON orders.customer_user_id = users.id
		JOIN rents ON orders.rent_id = rents.id
		LEFT JOIN addresses ON rents.addresses_id = addresses.id
		LEFT JOIN countries ON addresses.country_id = countries.id
		JOIN reviews ON reviews.order_id = orders.id
	ORDER BY login,estimate; 

