-- 1 Составьте список пользователей users, которые осуществили хотя бы один заказ orders в интернет магазине.
INSERT INTO  orders 
	(user_id)
VALUES 
    (4), (2);

SELECT 
	users.name, 
	orders.id AS order_id
FROM 
	users
JOIN
	orders
ON
	users.id=orders.user_id ;

-- 2 Выведите список товаров products и разделов catalogs, который соответствует товару.
SELECT 
	products.name AS product_name,
	catalogs.name AS catalog_name
FROM
	products
JOIN 
	catalogs
ON
	products.catalog_id = catalogs.id;