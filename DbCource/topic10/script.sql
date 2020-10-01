-- Проанализировать какие запросы могут выполняться наиболее часто в процессе работы приложения и добавить необходимые индексы.
CREATE INDEX profiles_birthday ON profiles(birthday);
SELECT user_id, birthday FROM profiles WHERE LEFT (YEAR(birthday), 3) = 200;
CREATE INDEX posts_user_id_to_community_id ON posts(user_id, community_id);
SELECT * FROM posts WHERE user_id = 31 AND community_id = (SELECT id FROM communities WHERE name = 'architecto');