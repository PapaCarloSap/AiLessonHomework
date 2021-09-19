SELECT DISTINCT
	-- имя группы
	communities.name AS group_name
	-- , communities_users.user_id 
	-- среднее количество пользователей в группах*
	, COUNT(communities_users.user_id) OVER() / (SELECT COUNT(*) FROM communities) AS average_number_users_by_groups
	-- , COUNT(communities_users.user_id) OVER() AS "Общее количество людей в группах"
	-- , (SELECT COUNT(*) FROM communities) AS "Количество групп"
	-- самый молодой пользователь в группе
	, FIRST_VALUE(profiles.user_id) OVER(PARTITION BY communities.id ORDER BY profiles.birthday) AS min_age_user_id
	-- , profiles.birthday as "День рожления"
	-- самый старший пользователь в группе
	, FIRST_VALUE(profiles.user_id) OVER(PARTITION BY communities.id ORDER BY profiles.birthday DESC) AS max_age_user_id
	-- общее количество пользователей в группе 
	, COUNT(communities_users.user_id) OVER(PARTITION BY communities.id) AS total_users_by_groups			
	-- всего пользователей в системе		
	, (SELECT count(profiles.user_id) FROM profiles) AS total_users
	-- отношение в процентах (общее количество пользователей в группе / всего пользователей в системе) * 100
	, ((COUNT(communities_users.user_id) OVER(PARTITION BY communities.id)/(SELECT count(profiles.user_id) FROM profiles))*100) AS procent
	
FROM 
	communities_users
	JOIN communities ON communities_users.community_id = communities.id
	JOIN profiles ON communities_users.user_id = profiles.user_id 
; 
	