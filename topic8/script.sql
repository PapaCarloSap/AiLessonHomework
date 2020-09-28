-- 3 Определить кто больше поставил лайков (всего) - мужчины или женщины?
SELECT
   profiles.gender,
   COUNT(likes.id) count_like 
FROM
   likes 
   JOIN
      profiles USING(user_id) 
GROUP BY
   profiles.gender 
ORDER BY
   count_like DESC LIMIT 1;


-- 4 Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).
SELECT
   TIMESTAMPDIFF(YEAR, birthday, NOW()) as age,
   COUNT(likes.id) AS count_like 
FROM
   profiles 
   LEFT JOIN
      likes 
      ON likes.target_id = profiles.user_id 
      AND likes.target_type_id = 2 
GROUP BY
   profiles.user_id 
ORDER BY
   profiles.birthday DESC LIMIT 10;

-- 5 Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети(критерии активности необходимо определить самостоятельно).
-- Активность считал по сумме постов, лайков, сообщений и загруженных медиафайлов каждым пользователем
SELECT 
	CONCAT( first_name, ' ', last_name) AS user,
	COUNT(media.id) + COUNT(posts.id) + COUNT(likes.id) + COUNT(messages.id) AS overall_activity
FROM 
	users 
	LEFT JOIN media ON media.user_id = users.id
	LEFT JOIN posts ON posts.user_id = users.id
	LEFT JOIN likes ON likes.user_id = users.id
	LEFT JOIN messages ON messages.from_user_id = users.id
GROUP BY 
	user
ORDER BY 
	overall_activity LIMIT 10;