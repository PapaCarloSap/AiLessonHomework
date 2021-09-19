SELECT * FROM users LIMIT 10;
SELECT * FROM profiles LIMIT 10;
SELECT * FROM messages LIMIT 10;
SELECT * FROM media_types LIMIT 10;
SELECT * FROM media LIMIT 10;
SELECT * FROM friendship_statuses LIMIT 10;
SELECT * FROM friendship LIMIT 10;
SELECT * FROM communities_users LIMIT 10;
SELECT * FROM communities LIMIT 10;
SELECT * FROM user_statuses LIMIT 10;

-- Таблица статусов
DESC profiles;
SELECT * FROM profiles LIMIT 10;
UPDATE profiles SET status = NULL;

CREATE TABLE user_statuses (
	id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY COMMENT "Идентификатор строки", 
	name VARCHAR(100) NOT NULL COMMENT "Название статуса (уникально)", 
	create_at DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT "Время создания строки",
	update_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT "Время обновления" 
) COMMENT "Справочник статусов";
DESC user_statuses;
INSERT INTO user_statuses (name) VALUES
	('single'),
	('married');
SELECT * FROM user_statuses;
ALTER TABLE profiles RENAME COLUMN status TO user_status_id;
ALTER TABLE profiles MODIFY COLUMN user_status_id INT UNSIGNED;

-- Обновление created_at и updated_at 
UPDATE users SET updated_at = NOW() WHERE updated_at < created_at;
UPDATE profiles SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE messages SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE media_types SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE media SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE friendship_statuses SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE friendship SET updated_at = NOW() WHERE updated_at < created_at;  
UPDATE communities SET updated_at = NOW() WHERE updated_at < created_at; 

-- profiles
UPDATE profiles SET photo_id = FLOOR(1 + RAND() * 100);
UPDATE profiles SET user_status_id = FLOOR(1 + RAND() * 2);

-- media_types
TRUNCATE media_types;
INSERT INTO media_types (name) VALUES
  ('photo'),
  ('video'),
  ('audio')
;

-- media 
UPDATE media SET media_type_id = FLOOR(1 + RAND() * 3);
UPDATE media SET user_id = FLOOR(1 + RAND() * 100);

CREATE TEMPORARY TABLE extensions (name VARCHAR(10));
INSERT INTO extensions VALUES ('jpeg'), ('avi'), ('mpeg'), ('png');
select * from extensions;
CREATE TEMPORARY TABLE filepaths (`path` VARCHAR(255));
INSERT INTO filepaths (`path`) SELECT filename FROM media ORDER BY id;
select * from filepaths;
DESC media;
UPDATE media SET filename = CONCAT(
  'http://dropbox.net/vk/',
  filename,
  (SELECT filename FROM filepaths LIMIT 1),
  '.',
  (SELECT name FROM extensions ORDER BY RAND() LIMIT 1)
);
SELECT * FROM media LIMIT 10;

UPDATE media SET size = FLOOR(10000 + (RAND() * 1000000)) WHERE size < 1000;

UPDATE media SET metadata = CONCAT('{"owner":"', 
  (SELECT CONCAT(first_name, ' ', last_name) FROM users WHERE id = user_id),
  '"}'); 
  ALTER TABLE media MODIFY COLUMN metadata JSON;
  
 -- friendships
 RENAME TABLE friendship TO friendships;
 SELECT * FROM friendships LIMIT 100;
 UPDATE friendships SET friend_id = friend_id + 1 WHERE user_id = friend_id;
 
-- friendship_statuses
SELECT * FROM friendship_statuses;
TRUNCATE friendship_statuses;
INSERT INTO friendship_statuses (name) VALUES
  ('Requested'),
  ('Confirmed'),
  ('Rejected');
 UPDATE friendships SET status_id = FLOOR(1 + RAND() * 3); 

-- communities
SELECT * FROM communities;
DELETE FROM communities WHERE id > 20;

-- communities_users
SELECT * FROM communities_users;
UPDATE communities_users SET community_id = FLOOR(1 + RAND() * 20);