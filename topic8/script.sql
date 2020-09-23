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
