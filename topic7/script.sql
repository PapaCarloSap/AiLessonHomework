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