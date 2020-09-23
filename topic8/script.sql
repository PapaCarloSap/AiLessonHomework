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