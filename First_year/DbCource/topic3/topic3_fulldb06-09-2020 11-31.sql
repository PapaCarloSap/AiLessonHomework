#
# TABLE STRUCTURE FOR: communities
#

DROP TABLE IF EXISTS `communities`;

CREATE TABLE `communities` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор сроки',
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Название группы',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Группы';

INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (1, 'labore', '2015-09-09 03:50:47', '2014-01-20 12:53:31');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (2, 'omnis', '2017-11-29 01:17:32', '2014-09-16 04:25:25');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (3, 'pariatur', '2012-09-05 18:12:32', '2016-11-11 08:09:14');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (4, 'qui', '2012-10-06 15:09:22', '2017-04-14 23:27:07');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (5, 'officia', '2017-12-07 20:02:17', '2015-07-19 23:16:48');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (6, 'corporis', '2013-05-11 21:36:28', '2012-01-15 21:50:20');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (7, 'laborum', '2020-01-25 08:39:41', '2013-03-22 18:37:54');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (8, 'praesentium', '2018-10-10 17:29:54', '2018-03-03 00:36:49');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (9, 'animi', '2019-01-12 02:45:29', '2012-11-07 07:22:36');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (10, 'iste', '2014-11-28 19:52:39', '2018-06-23 15:01:49');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (11, 'quia', '2016-12-26 00:59:08', '2017-09-16 08:02:44');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (12, 'dignissimos', '2017-02-27 10:30:08', '2017-03-23 18:21:29');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (13, 'voluptas', '2019-07-16 03:11:18', '2014-02-23 01:46:07');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (14, 'quos', '2017-09-27 04:24:22', '2011-12-30 05:17:59');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (15, 'sit', '2017-07-23 02:01:20', '2018-10-02 05:04:09');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (16, 'architecto', '2013-09-01 04:27:56', '2013-01-08 17:13:56');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (17, 'neque', '2015-08-26 23:31:07', '2013-07-17 09:39:23');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (18, 'explicabo', '2017-12-10 10:27:16', '2015-09-07 15:09:15');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (19, 'occaecati', '2016-11-24 20:08:58', '2010-12-29 20:40:51');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (20, 'doloremque', '2011-11-08 17:31:33', '2015-03-15 21:10:41');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (21, 'repellat', '2011-08-02 00:27:30', '2015-03-25 20:16:52');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (22, 'rem', '2013-03-02 13:44:49', '2016-01-30 17:46:43');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (23, 'quam', '2012-02-29 09:21:51', '2019-07-24 10:43:57');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (24, 'voluptate', '2020-04-30 09:05:00', '2015-05-22 01:38:50');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (25, 'ipsum', '2011-02-21 10:15:14', '2013-11-19 21:34:44');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (26, 'voluptatem', '2017-04-16 21:27:58', '2018-12-25 20:15:20');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (27, 'maxime', '2018-11-16 13:38:39', '2012-10-11 21:09:34');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (28, 'velit', '2017-08-31 09:33:17', '2020-06-07 01:21:26');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (29, 'minima', '2012-12-29 11:38:44', '2017-11-22 12:04:17');
INSERT INTO `communities` (`id`, `name`, `created_at`, `updated_at`) VALUES (30, 'iusto', '2014-01-13 23:20:02', '2018-05-20 01:42:12');


#
# TABLE STRUCTURE FOR: communities_users
#

DROP TABLE IF EXISTS `communities_users`;

CREATE TABLE `communities_users` (
  `community_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на группу',
  `user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на пользователя',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  PRIMARY KEY (`community_id`,`user_id`) COMMENT 'Составной первичный ключ'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Участники групп, связь между пользователями и группами';

INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 1, '2012-12-15 20:04:41');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 3, '2012-07-30 22:41:00');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 53, '2017-03-30 18:49:25');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 74, '2015-05-08 17:33:00');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 76, '2011-04-15 11:28:26');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (1, 96, '2015-11-23 02:09:28');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (2, 83, '2017-01-28 14:19:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (2, 87, '2013-04-11 00:19:04');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (3, 29, '2017-07-28 21:21:07');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (3, 85, '2019-03-29 18:33:24');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (3, 95, '2019-04-14 07:55:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (3, 99, '2015-10-26 22:43:50');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (4, 10, '2013-11-24 07:13:55');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (4, 91, '2014-11-15 06:03:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (5, 30, '2014-08-26 11:25:44');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (5, 49, '2015-07-30 20:36:14');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (6, 50, '2012-05-07 12:13:51');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (6, 84, '2019-04-01 07:30:10');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (6, 87, '2020-05-17 07:14:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (7, 73, '2012-08-26 07:40:42');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (7, 75, '2017-09-02 16:28:58');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (7, 76, '2015-07-08 03:27:59');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (8, 1, '2010-11-12 02:36:31');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (8, 14, '2017-07-09 23:34:52');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (8, 71, '2010-09-30 05:26:32');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (8, 74, '2017-12-05 11:59:49');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (8, 84, '2014-02-18 00:08:14');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (9, 16, '2017-09-25 10:25:21');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (9, 61, '2012-12-27 17:55:31');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (10, 23, '2012-07-26 20:34:28');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (10, 54, '2014-06-13 01:56:04');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (10, 55, '2012-12-31 06:21:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (10, 95, '2017-07-06 05:29:20');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (11, 27, '2014-10-01 00:27:14');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (11, 36, '2018-01-28 16:36:45');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (11, 58, '2013-06-04 02:39:55');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (11, 61, '2011-12-16 16:43:27');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (11, 90, '2018-12-16 13:19:34');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (12, 10, '2017-08-15 21:16:29');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (13, 12, '2015-01-14 05:41:52');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (13, 82, '2014-01-03 14:00:51');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (14, 22, '2017-07-22 00:57:18');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (14, 24, '2014-03-24 18:33:38');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (14, 78, '2018-07-01 14:23:19');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (15, 8, '2011-01-09 09:21:14');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (15, 41, '2011-07-21 08:41:38');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (15, 94, '2019-10-19 22:26:13');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (16, 86, '2018-06-15 03:03:38');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (17, 95, '2017-07-25 18:20:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (18, 22, '2011-08-02 12:09:29');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (18, 25, '2017-10-06 11:50:01');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (18, 45, '2018-04-02 00:05:52');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (18, 47, '2018-03-25 20:29:50');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (18, 73, '2011-10-14 14:05:18');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 23, '2018-10-14 22:13:30');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 36, '2012-05-05 12:33:44');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 47, '2015-01-12 11:52:10');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 65, '2015-01-20 06:31:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 93, '2011-03-06 00:41:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (19, 96, '2012-12-01 09:53:03');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (20, 17, '2016-04-26 03:56:49');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (20, 25, '2011-08-07 03:58:03');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (20, 53, '2014-09-16 16:48:05');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (21, 36, '2018-11-30 19:29:28');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (21, 49, '2011-02-07 04:57:56');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (21, 73, '2012-06-05 00:17:43');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (22, 13, '2013-03-19 09:45:40');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (22, 37, '2013-04-07 00:37:42');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (22, 66, '2015-08-27 16:34:24');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (22, 80, '2017-12-31 10:40:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (22, 91, '2018-07-21 11:49:07');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (23, 8, '2017-10-25 00:32:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (23, 50, '2017-10-01 07:19:33');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (24, 12, '2011-06-26 08:50:55');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (24, 66, '2017-12-05 22:25:59');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (24, 67, '2011-03-26 14:43:19');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (25, 68, '2013-03-26 13:14:31');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (26, 16, '2020-05-11 11:27:52');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (26, 60, '2018-02-13 02:59:06');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (26, 86, '2014-05-02 12:20:09');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (27, 3, '2017-11-06 03:06:37');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (27, 4, '2010-10-11 18:55:28');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (27, 32, '2011-01-21 15:40:23');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (27, 55, '2015-12-17 23:08:58');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (27, 82, '2016-05-09 03:20:55');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (28, 24, '2019-03-08 01:26:52');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (28, 34, '2011-12-13 22:09:44');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (28, 67, '2017-03-01 01:42:13');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (28, 87, '2014-10-05 07:34:38');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (29, 1, '2019-01-29 04:38:13');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (29, 8, '2016-02-09 06:10:17');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (29, 21, '2010-12-22 10:27:57');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (29, 100, '2015-06-26 12:07:24');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (30, 11, '2012-09-07 03:28:30');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (30, 25, '2013-05-26 10:03:45');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (30, 34, '2014-02-05 04:17:55');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (30, 76, '2015-02-14 08:52:58');
INSERT INTO `communities_users` (`community_id`, `user_id`, `created_at`) VALUES (30, 87, '2018-09-10 16:59:09');


#
# TABLE STRUCTURE FOR: friendship
#

DROP TABLE IF EXISTS `friendship`;

CREATE TABLE `friendship` (
  `user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на инициатора дружеских отношений',
  `friend_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на получателя приглашения дружить',
  `status_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на статус (текущее состояние) отношений',
  `requested_at` datetime DEFAULT current_timestamp() COMMENT 'Время отправления приглашения дружить',
  `confirmed_at` datetime DEFAULT NULL COMMENT 'Время подтверждения приглашения',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`user_id`,`friend_id`) COMMENT 'Составной первичный ключ'
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Таблица дружбы';

INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (1, 83, 8, '2014-01-09 05:51:42', '2014-08-08 08:27:50', '2017-08-30 06:35:27', '2013-04-08 20:44:54');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (2, 65, 6, '2017-09-06 00:23:48', '2011-09-19 01:45:34', '2019-06-10 05:33:16', '2016-12-14 18:39:38');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (3, 22, 9, '2018-07-19 04:04:11', '2011-06-09 15:06:51', '2014-06-11 20:32:29', '2014-01-06 10:16:46');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (4, 41, 2, '2013-03-10 02:30:42', '2018-08-01 10:38:45', '2018-02-17 12:36:18', '2017-10-31 04:02:24');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (5, 78, 10, '2017-03-22 02:09:32', '2013-12-08 20:18:17', '2011-11-10 11:27:44', '2014-07-03 10:01:09');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (6, 45, 5, '2011-06-23 09:27:42', '2016-11-01 19:41:09', '2015-06-19 22:41:06', '2014-03-14 09:28:46');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (7, 59, 8, '2016-12-07 08:44:15', '2018-02-06 09:09:00', '2018-06-18 20:25:48', '2017-04-29 22:10:27');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (8, 12, 5, '2019-01-23 23:13:45', '2015-02-09 06:27:05', '2019-06-30 04:17:33', '2013-06-29 08:35:48');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (9, 7, 5, '2011-03-08 15:50:22', '2016-10-03 16:37:58', '2018-11-25 19:53:37', '2011-08-15 16:27:46');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (10, 35, 3, '2012-08-30 16:49:19', '2013-06-09 18:18:14', '2013-04-12 09:14:56', '2014-02-06 22:00:16');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (11, 59, 8, '2016-09-01 15:27:50', '2019-01-13 07:57:49', '2016-10-17 02:09:40', '2013-12-24 10:03:57');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (12, 10, 8, '2012-09-09 15:50:09', '2014-07-13 13:52:52', '2019-07-18 03:55:46', '2018-04-04 05:06:27');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (13, 23, 3, '2016-06-06 09:48:47', '2012-06-16 05:08:54', '2014-07-22 01:37:35', '2017-09-04 10:18:41');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (14, 64, 3, '2018-11-19 11:49:57', '2012-03-09 06:43:12', '2016-06-01 08:59:22', '2019-11-24 20:00:49');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (15, 22, 2, '2011-02-03 16:32:03', '2012-08-22 10:09:17', '2020-01-10 14:57:09', '2013-08-03 18:34:01');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (16, 27, 1, '2020-06-02 10:50:39', '2014-01-08 04:05:08', '2011-09-11 04:16:04', '2020-05-16 11:16:40');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (17, 99, 10, '2012-05-29 10:49:09', '2014-10-04 16:29:19', '2019-10-05 08:34:10', '2017-06-03 10:21:02');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (18, 58, 3, '2017-09-08 12:32:08', '2018-05-26 09:38:31', '2010-11-08 16:54:38', '2012-06-25 01:27:22');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (19, 79, 10, '2020-04-18 03:56:59', '2012-10-01 16:25:43', '2014-08-03 12:37:34', '2019-01-05 10:49:55');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (20, 40, 6, '2014-11-24 20:55:51', '2020-01-28 03:45:56', '2020-04-13 04:22:20', '2016-05-05 13:40:54');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (21, 89, 9, '2019-08-25 14:55:06', '2019-02-04 11:50:20', '2010-12-29 11:16:54', '2016-05-03 04:58:28');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (22, 2, 5, '2014-08-06 15:36:03', '2011-04-24 18:28:56', '2017-03-16 07:27:26', '2011-06-21 08:42:32');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (23, 60, 2, '2019-02-03 16:17:08', '2013-12-18 04:12:16', '2014-05-25 18:38:27', '2018-12-25 23:00:25');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (24, 89, 7, '2018-12-08 10:57:59', '2015-11-02 07:57:06', '2018-10-10 00:02:34', '2014-06-25 20:22:50');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (25, 57, 3, '2011-05-27 04:23:27', '2013-03-10 02:03:39', '2019-08-26 06:50:00', '2015-04-03 00:18:47');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (26, 93, 2, '2012-05-04 05:46:33', '2015-04-17 17:59:59', '2011-12-14 03:44:40', '2016-04-18 15:32:52');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (27, 100, 1, '2018-11-12 07:29:42', '2015-12-23 06:06:47', '2015-10-09 16:14:19', '2015-06-17 12:55:15');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (28, 94, 3, '2014-12-19 23:28:32', '2018-10-29 09:22:48', '2012-05-02 00:26:01', '2017-11-02 00:12:24');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (29, 23, 6, '2018-06-29 11:58:18', '2012-01-03 11:12:32', '2011-12-09 07:58:12', '2020-03-21 12:47:23');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (30, 42, 5, '2017-04-03 18:32:51', '2017-03-04 09:56:58', '2017-10-18 21:41:18', '2019-01-12 17:39:23');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (31, 77, 7, '2017-10-19 06:59:28', '2014-11-07 18:39:48', '2010-12-29 05:15:45', '2016-11-17 06:17:30');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (32, 47, 8, '2017-09-28 15:48:17', '2015-09-05 22:48:06', '2011-05-23 12:58:59', '2015-09-27 11:28:48');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (33, 59, 1, '2012-11-20 10:06:53', '2016-10-15 08:41:12', '2019-10-01 08:17:44', '2014-12-10 22:09:32');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (34, 97, 4, '2015-12-23 23:04:31', '2016-01-14 10:05:57', '2015-03-17 23:40:03', '2016-05-26 13:05:24');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (35, 3, 4, '2017-05-19 22:23:34', '2015-02-04 11:46:18', '2012-03-20 10:44:07', '2012-01-01 09:53:18');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (36, 93, 10, '2015-09-08 09:45:27', '2013-11-17 23:56:52', '2013-09-08 17:23:40', '2012-05-27 06:20:13');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (37, 21, 10, '2019-01-07 18:48:50', '2014-04-02 12:29:22', '2018-02-26 03:16:04', '2014-10-19 07:42:22');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (38, 40, 8, '2016-12-30 02:49:53', '2019-01-18 01:23:10', '2020-02-09 19:17:36', '2010-12-11 18:17:20');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (39, 8, 3, '2015-01-12 08:40:20', '2019-03-25 08:17:16', '2016-11-02 11:04:35', '2018-08-09 22:39:23');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (40, 47, 7, '2014-04-07 18:32:09', '2018-04-26 08:09:30', '2017-07-29 23:12:04', '2013-09-10 13:09:27');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (41, 51, 4, '2019-06-09 22:29:54', '2018-01-29 21:51:06', '2016-04-27 02:38:11', '2015-08-23 09:52:08');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (42, 80, 5, '2019-08-05 13:52:35', '2012-12-05 23:24:41', '2017-10-10 22:33:45', '2019-02-27 01:04:21');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (43, 41, 8, '2019-11-16 18:29:27', '2010-09-13 10:11:24', '2015-01-06 00:34:57', '2012-11-26 08:06:54');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (44, 71, 7, '2015-09-03 02:17:51', '2013-06-16 07:41:22', '2019-09-27 02:36:06', '2012-08-05 12:10:29');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (45, 31, 2, '2013-09-27 05:43:30', '2018-03-19 06:00:31', '2012-01-13 00:52:08', '2012-04-05 07:47:09');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (46, 7, 1, '2016-04-17 12:38:54', '2012-10-16 05:13:21', '2017-02-21 19:14:46', '2011-12-28 18:39:36');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (47, 81, 6, '2013-07-24 19:27:18', '2014-03-20 04:37:03', '2014-01-26 11:06:19', '2019-08-24 02:00:49');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (48, 84, 4, '2010-10-14 01:34:15', '2018-02-13 07:44:29', '2010-10-13 19:33:16', '2012-04-07 00:56:34');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (49, 59, 8, '2017-10-26 07:33:57', '2010-10-24 21:45:31', '2010-12-29 21:42:10', '2018-11-14 07:17:36');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (50, 77, 7, '2016-09-17 08:20:41', '2014-01-25 20:18:41', '2011-03-16 08:12:29', '2019-08-18 22:11:11');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (51, 15, 7, '2010-11-21 14:28:15', '2019-08-10 13:02:25', '2019-01-20 00:28:38', '2020-01-03 04:23:47');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (52, 53, 4, '2012-03-01 19:31:51', '2012-06-05 15:37:00', '2019-11-29 05:07:29', '2020-08-18 09:53:49');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (53, 64, 10, '2018-09-29 03:48:28', '2015-01-12 22:49:39', '2012-07-05 22:13:41', '2014-09-16 11:33:41');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (54, 15, 8, '2018-03-12 06:25:56', '2016-10-04 20:40:24', '2016-06-22 03:54:22', '2017-10-20 12:11:49');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (55, 20, 7, '2015-07-20 11:19:48', '2015-04-21 04:23:48', '2020-04-26 21:51:32', '2020-08-30 05:59:19');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (56, 36, 7, '2010-12-15 12:02:23', '2015-07-13 22:12:26', '2014-11-13 02:52:20', '2020-07-08 17:56:07');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (57, 100, 2, '2013-07-25 03:53:48', '2012-06-08 14:03:04', '2018-09-21 23:01:21', '2014-03-09 15:02:09');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (58, 19, 5, '2019-03-18 22:58:04', '2014-02-26 20:30:46', '2011-11-03 12:46:11', '2017-03-20 11:36:06');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (59, 89, 9, '2017-12-27 00:25:56', '2012-12-13 03:33:20', '2012-09-02 17:08:20', '2015-12-02 09:29:08');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (60, 3, 2, '2015-10-21 04:54:51', '2012-06-14 03:17:07', '2020-07-16 15:57:27', '2013-12-13 01:42:41');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (61, 2, 1, '2019-10-19 20:37:24', '2014-05-01 19:32:59', '2012-11-15 23:50:30', '2011-02-12 22:44:47');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (62, 27, 9, '2012-04-04 21:29:18', '2016-09-30 21:41:38', '2015-06-14 08:45:32', '2019-06-08 15:48:47');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (63, 63, 1, '2014-09-11 02:02:10', '2015-03-18 15:42:07', '2014-12-31 01:19:13', '2011-02-11 10:27:14');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (64, 22, 3, '2019-05-11 19:26:56', '2017-11-09 23:02:52', '2018-10-07 10:49:43', '2013-01-05 18:23:50');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (65, 89, 10, '2016-02-09 02:44:36', '2016-04-25 20:27:35', '2016-10-31 23:51:41', '2015-02-03 16:34:01');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (66, 82, 1, '2011-12-02 20:01:13', '2020-06-25 15:19:55', '2010-11-16 01:41:59', '2010-10-23 06:18:55');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (67, 68, 4, '2014-07-31 04:34:16', '2016-10-29 01:31:59', '2013-02-06 06:19:02', '2020-08-11 20:44:22');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (68, 39, 4, '2015-09-23 15:08:48', '2012-06-24 23:14:05', '2015-04-07 05:50:38', '2015-12-22 07:59:00');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (69, 26, 6, '2010-11-01 17:08:42', '2017-01-09 04:22:12', '2012-02-14 11:57:37', '2019-04-07 05:57:13');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (70, 2, 5, '2012-10-11 15:48:13', '2012-03-10 20:00:10', '2014-11-08 17:54:40', '2014-08-26 18:10:05');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (71, 15, 4, '2016-12-07 00:23:33', '2013-03-10 12:59:43', '2018-06-14 00:26:07', '2016-06-20 15:18:38');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (72, 15, 2, '2017-08-05 01:00:42', '2018-11-03 21:13:17', '2014-08-28 01:50:45', '2017-06-19 12:38:28');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (73, 53, 4, '2013-02-07 05:48:38', '2013-01-30 14:39:56', '2018-05-27 02:34:10', '2014-06-12 00:42:27');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (74, 55, 5, '2014-12-05 16:00:38', '2012-01-10 00:26:39', '2017-08-19 21:06:17', '2013-05-11 15:05:35');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (75, 23, 6, '2013-09-17 07:07:04', '2016-10-10 23:50:18', '2013-08-15 05:08:33', '2011-05-08 00:29:31');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (76, 60, 3, '2015-05-25 15:17:57', '2011-08-27 08:42:16', '2017-03-15 01:20:24', '2014-10-03 22:38:31');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (77, 67, 9, '2016-01-19 08:13:48', '2019-06-03 20:38:11', '2013-02-25 13:58:09', '2018-02-18 06:44:11');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (78, 7, 3, '2016-03-11 04:36:09', '2017-09-15 05:55:01', '2012-10-26 01:44:46', '2013-04-17 14:53:43');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (79, 96, 3, '2014-05-16 03:24:06', '2015-11-14 05:21:25', '2017-02-16 11:39:03', '2016-10-22 21:22:51');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (80, 51, 9, '2015-09-12 03:02:46', '2011-12-01 01:42:01', '2014-02-01 21:32:32', '2014-02-08 19:18:14');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (81, 27, 4, '2014-09-20 00:42:48', '2011-08-01 09:42:38', '2015-02-21 12:41:16', '2017-02-02 17:50:04');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (82, 88, 10, '2015-12-27 06:47:23', '2019-02-18 11:37:06', '2011-02-12 19:52:20', '2014-02-14 15:49:02');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (83, 67, 3, '2015-07-27 04:31:38', '2011-11-24 18:36:56', '2014-10-10 20:09:11', '2016-04-04 01:27:46');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (84, 26, 10, '2012-07-25 08:31:49', '2011-05-25 21:00:32', '2016-03-09 20:34:44', '2019-12-08 03:41:09');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (85, 80, 3, '2011-08-19 06:47:09', '2016-01-20 00:10:58', '2010-12-27 06:02:58', '2016-08-15 06:23:36');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (86, 37, 10, '2012-01-29 07:32:34', '2014-08-25 00:08:39', '2012-02-24 07:05:48', '2015-01-02 23:32:01');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (87, 65, 6, '2019-12-15 10:51:04', '2019-08-21 23:26:26', '2016-04-18 10:21:00', '2014-01-29 19:47:30');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (88, 10, 2, '2018-08-09 13:36:41', '2018-08-03 09:12:41', '2017-10-03 23:21:33', '2020-04-17 00:06:52');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (89, 84, 7, '2019-08-11 14:19:42', '2014-10-28 15:54:50', '2018-10-31 05:27:28', '2013-03-17 17:05:34');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (90, 58, 1, '2011-04-27 21:48:59', '2014-05-21 11:40:43', '2018-11-17 05:45:17', '2014-04-20 19:39:17');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (91, 22, 2, '2015-08-11 18:58:42', '2020-01-21 00:29:17', '2019-02-21 20:29:51', '2011-06-23 04:54:23');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (92, 30, 9, '2019-10-21 06:08:50', '2017-09-02 15:59:24', '2015-08-12 23:50:01', '2019-08-05 05:23:39');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (93, 3, 4, '2015-07-28 09:16:12', '2019-12-10 22:34:44', '2015-07-21 19:02:20', '2018-11-01 03:04:36');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (94, 19, 10, '2011-07-22 12:38:10', '2020-06-01 12:09:05', '2014-09-13 06:22:05', '2013-06-28 12:05:06');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (95, 65, 7, '2016-09-30 06:51:20', '2020-09-05 14:23:10', '2016-08-25 12:23:31', '2017-02-21 03:31:05');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (96, 82, 10, '2015-01-27 01:09:25', '2017-10-07 07:56:14', '2017-09-16 19:36:20', '2016-06-25 21:10:56');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (97, 2, 7, '2011-01-19 14:49:26', '2019-12-07 01:36:36', '2013-09-08 01:52:53', '2012-12-31 04:57:21');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (98, 87, 7, '2017-12-11 05:17:51', '2016-03-31 21:57:13', '2016-05-20 13:26:25', '2015-05-21 23:38:22');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (99, 96, 2, '2018-12-14 08:29:36', '2019-06-13 05:38:37', '2013-05-27 22:50:25', '2016-04-22 16:07:17');
INSERT INTO `friendship` (`user_id`, `friend_id`, `status_id`, `requested_at`, `confirmed_at`, `created_at`, `updated_at`) VALUES (100, 59, 8, '2015-05-23 19:31:07', '2016-11-17 13:40:23', '2017-04-01 09:56:16', '2019-12-04 08:07:33');


#
# TABLE STRUCTURE FOR: friendship_statuses
#

DROP TABLE IF EXISTS `friendship_statuses`;

CREATE TABLE `friendship_statuses` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `name` varchar(150) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Название статуса',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Статусы дружбы';

INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (1, 'ea', '2016-02-17 23:56:49', '2018-11-05 13:45:44');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (2, 'temporibus', '2019-09-05 05:41:47', '2019-02-06 07:34:26');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (3, 'et', '2020-01-26 04:33:38', '2018-08-16 04:35:19');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (4, 'delectus', '2020-01-24 23:13:07', '2014-06-26 21:49:36');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (5, 'minus', '2010-11-20 10:20:13', '2019-09-27 16:07:44');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (6, 'facere', '2018-03-22 05:24:02', '2015-05-16 03:04:15');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (7, 'sunt', '2017-08-08 22:21:40', '2014-03-18 05:36:13');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (8, 'velit', '2018-09-20 22:22:38', '2020-08-17 02:25:49');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (9, 'modi', '2011-05-24 08:12:22', '2012-11-02 15:44:44');
INSERT INTO `friendship_statuses` (`id`, `name`, `created_at`, `updated_at`) VALUES (10, 'eaque', '2018-10-19 04:05:07', '2018-11-21 09:02:24');


#
# TABLE STRUCTURE FOR: media
#

DROP TABLE IF EXISTS `media`;

CREATE TABLE `media` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на пользователя, который загрузил файл',
  `filename` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Путь к файлу',
  `size` int(11) NOT NULL COMMENT 'Размер файла',
  `metadata` longtext CHARACTER SET utf8mb4 COLLATE utf8mb4_bin DEFAULT NULL COMMENT 'Метаданные файла' CHECK (json_valid(`metadata`)),
  `media_type_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на тип контента',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Медиафайлы';

INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (1, 1, 'application/vnd.ms-word.template.macroenabled.12', 1, NULL, 1, '2019-08-17 07:01:03', '2015-07-06 06:24:53');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (2, 2, 'model/vnd.dwf', 8, NULL, 2, '2012-01-24 05:08:48', '2016-10-26 18:37:45');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (3, 3, 'application/pdf', 5, NULL, 3, '2011-12-16 17:18:08', '2020-08-17 18:00:50');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (4, 4, 'application/vnd.kde.kspread', 3, NULL, 4, '2010-11-08 00:41:06', '2011-05-16 21:21:58');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (5, 5, 'application/vnd.dpgraph', 7, NULL, 5, '2012-12-22 12:01:24', '2011-07-26 21:32:14');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (6, 6, 'application/pgp-encrypted', 2, NULL, 6, '2014-02-23 10:06:49', '2012-08-09 19:21:21');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (7, 7, 'video/vnd.dece.video', 4, NULL, 7, '2012-06-15 14:07:56', '2020-06-19 15:48:01');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (8, 8, 'application/vnd.ms-powerpoint.slide.macroenabled.12', 7, NULL, 8, '2012-10-21 10:07:16', '2015-11-14 14:32:37');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (9, 9, 'application/vnd.oasis.opendocument.image', 7, NULL, 9, '2015-05-05 06:22:42', '2018-08-29 11:04:25');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (10, 10, 'application/vnd.wordperfect', 0, NULL, 10, '2014-08-18 03:58:29', '2019-01-05 08:42:43');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (11, 11, 'application/vnd.epson.quickanime', 9, NULL, 11, '2018-06-22 19:39:46', '2013-11-07 20:00:44');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (12, 12, 'video/vnd.mpegurl', 4, NULL, 12, '2010-12-15 01:14:54', '2016-08-18 04:11:19');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (13, 13, 'application/x-sv4crc', 8, NULL, 13, '2019-08-01 12:59:47', '2015-03-01 22:33:15');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (14, 14, 'text/x-fortran', 6, NULL, 14, '2019-05-24 09:25:21', '2017-01-04 12:03:28');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (15, 15, 'application/vnd.seemail', 9, NULL, 15, '2014-04-14 00:03:12', '2011-03-01 23:46:11');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (16, 16, 'text/vnd.dvb.subtitle', 1, NULL, 16, '2015-10-12 00:40:45', '2017-09-13 05:41:10');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (17, 17, 'model/x3d+xml', 5, NULL, 17, '2017-12-20 09:43:47', '2012-08-23 11:09:02');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (18, 18, 'video/vnd.dvb.file', 9, NULL, 18, '2015-05-30 23:08:21', '2016-10-28 17:05:42');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (19, 19, 'application/vnd.ms-lrm', 5, NULL, 19, '2012-01-30 13:01:24', '2010-10-13 22:27:41');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (20, 20, 'text/prs.lines.tag', 7, NULL, 20, '2013-02-22 12:35:43', '2020-06-14 10:15:19');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (21, 21, 'application/vnd.kenameaapp', 8, NULL, 1, '2015-11-29 00:47:08', '2014-02-15 11:56:44');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (22, 22, 'application/vnd.trueapp', 9, NULL, 2, '2020-08-07 09:13:36', '2011-07-14 15:15:08');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (23, 23, 'application/vnd.ms-artgalry', 6, NULL, 3, '2020-01-31 02:03:18', '2019-12-21 02:37:57');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (24, 24, 'application/vnd.lotus-1-2-3', 2, NULL, 4, '2011-12-15 00:46:10', '2020-02-24 07:50:04');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (25, 25, 'image/x-xpixmap', 6, NULL, 5, '2017-02-22 01:15:48', '2010-10-17 14:32:14');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (26, 26, 'video/vnd.dece.pd', 0, NULL, 6, '2014-01-28 16:55:46', '2019-11-26 12:30:16');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (27, 27, 'text/vnd.sun.j2me.app-descriptor', 7, NULL, 7, '2014-12-17 15:42:13', '2013-01-20 06:14:24');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (28, 28, 'image/bmp', 7, NULL, 8, '2017-09-13 01:27:27', '2014-12-20 05:54:34');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (29, 29, 'application/x-debian-package', 5, NULL, 9, '2016-07-02 16:23:56', '2014-07-15 20:24:36');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (30, 30, 'application/vnd.dna', 6, NULL, 10, '2020-05-31 03:16:29', '2017-10-10 06:43:46');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (31, 31, 'application/vnd.oasis.opendocument.presentation-template', 9, NULL, 11, '2020-04-27 00:32:50', '2018-08-29 21:50:39');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (32, 32, 'application/vnd.wap.wmlc', 6, NULL, 12, '2012-09-08 07:32:07', '2014-10-23 05:01:48');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (33, 33, 'image/bmp', 6, NULL, 13, '2012-08-29 05:27:55', '2012-10-02 16:51:39');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (34, 34, 'application/vnd.lotus-approach', 1, NULL, 14, '2014-02-21 18:06:56', '2013-09-21 18:10:16');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (35, 35, 'application/vnd.kde.kformula', 9, NULL, 15, '2014-09-25 19:48:33', '2015-11-10 19:14:19');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (36, 36, 'application/x-texinfo', 3, NULL, 16, '2020-07-19 17:22:48', '2012-11-10 09:24:06');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (37, 37, 'application/vnd.adobe.air-application-installer-package+zip', 7, NULL, 17, '2012-09-24 17:56:56', '2015-03-24 00:22:41');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (38, 38, 'audio/x-caf', 0, NULL, 18, '2014-03-09 05:02:44', '2010-11-19 07:38:45');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (39, 39, 'application/vnd.visionary', 2, NULL, 19, '2020-08-06 15:16:09', '2018-12-03 17:58:08');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (40, 40, 'application/vnd.xara', 6, NULL, 20, '2020-06-26 00:03:19', '2017-12-20 06:11:46');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (41, 41, 'application/vnd.oasis.opendocument.text', 2, NULL, 1, '2018-12-14 00:17:27', '2012-03-20 06:29:39');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (42, 42, 'application/x-silverlight-app', 9, NULL, 2, '2016-11-26 17:32:52', '2012-12-04 07:06:27');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (43, 43, 'audio/ogg', 1, NULL, 3, '2014-04-23 07:20:27', '2020-06-25 23:02:51');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (44, 44, 'image/jpeg', 8, NULL, 4, '2016-12-08 01:46:55', '2016-04-12 04:41:43');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (45, 45, 'application/vnd.tao.intent-module-archive', 5, NULL, 5, '2011-10-25 20:04:10', '2013-07-14 00:28:25');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (46, 46, 'application/vnd.sun.xml.writer.global', 0, NULL, 6, '2015-02-14 15:03:50', '2017-08-09 03:29:52');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (47, 47, 'application/x-cfs-compressed', 1, NULL, 7, '2011-12-04 03:05:30', '2017-07-09 18:07:15');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (48, 48, 'application/x-cfs-compressed', 4, NULL, 8, '2018-03-09 00:37:15', '2019-08-10 02:34:38');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (49, 49, 'image/x-cmx', 3, NULL, 9, '2013-05-26 05:51:32', '2016-03-30 02:25:38');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (50, 50, 'application/vnd.sun.xml.writer', 2, NULL, 10, '2013-07-25 14:40:03', '2016-05-17 20:01:04');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (51, 51, 'application/vnd.smaf', 5, NULL, 11, '2012-10-14 07:15:04', '2010-11-14 09:38:34');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (52, 52, 'application/vnd.ms-artgalry', 8, NULL, 12, '2014-05-16 23:22:45', '2016-07-11 04:23:44');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (53, 53, 'application/x-bittorrent', 8, NULL, 13, '2017-06-30 07:27:06', '2017-02-09 08:12:23');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (54, 54, 'model/mesh', 4, NULL, 14, '2019-07-26 05:36:26', '2016-11-19 22:22:08');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (55, 55, 'application/vnd.oasis.opendocument.formula-template', 9, NULL, 15, '2012-10-31 20:55:41', '2011-06-29 15:06:45');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (56, 56, 'application/vnd.ms-project', 7, NULL, 16, '2012-12-22 05:43:08', '2017-11-04 19:54:52');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (57, 57, 'image/prs.btif', 0, NULL, 17, '2015-04-07 13:53:01', '2015-08-11 07:34:26');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (58, 58, 'application/mathml+xml', 5, NULL, 18, '2011-01-03 08:35:13', '2018-10-17 01:57:35');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (59, 59, 'model/x3d+binary', 0, NULL, 19, '2011-03-09 15:00:48', '2013-05-08 12:25:28');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (60, 60, 'application/vnd.quark.quarkxpress', 9, NULL, 20, '2014-02-17 17:33:17', '2010-12-02 20:34:21');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (61, 61, 'audio/x-ms-wax', 0, NULL, 1, '2018-10-21 10:43:32', '2019-01-29 13:26:08');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (62, 62, 'application/vnd.wordperfect', 8, NULL, 2, '2016-03-09 23:54:55', '2013-06-08 23:27:20');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (63, 63, 'application/vnd.ezpix-package', 4, NULL, 3, '2012-02-25 11:48:40', '2016-09-17 13:26:14');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (64, 64, 'application/vnd.ezpix-album', 5, NULL, 4, '2012-09-26 14:03:48', '2013-07-29 02:23:18');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (65, 65, 'application/vnd.kinar', 3, NULL, 5, '2019-05-15 03:23:12', '2016-03-20 04:32:21');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (66, 66, 'application/vnd.lotus-1-2-3', 5, NULL, 6, '2017-05-14 07:27:26', '2012-07-15 12:04:16');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (67, 67, 'application/yang', 4, NULL, 7, '2017-09-23 11:21:12', '2019-12-28 18:53:05');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (68, 68, 'audio/x-pn-realaudio-plugin', 4, NULL, 8, '2018-09-17 16:25:49', '2012-01-02 21:50:10');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (69, 69, 'application/vnd.dna', 4, NULL, 9, '2020-09-04 14:50:08', '2013-10-21 10:09:17');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (70, 70, 'image/webp', 1, NULL, 10, '2020-03-24 01:37:07', '2018-06-15 16:45:22');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (71, 71, 'application/vnd.dpgraph', 9, NULL, 11, '2016-12-25 19:54:13', '2012-03-22 13:37:24');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (72, 72, 'application/x-subrip', 1, NULL, 12, '2019-05-07 11:55:32', '2013-04-17 13:04:00');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (73, 73, 'text/x-pascal', 3, NULL, 13, '2013-05-02 03:18:29', '2014-10-08 22:02:49');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (74, 74, 'application/vnd.wolfram.player', 2, NULL, 14, '2010-11-27 05:07:47', '2016-11-18 06:31:38');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (75, 75, 'application/vnd.ds-keypoint', 8, NULL, 15, '2019-12-06 22:03:26', '2014-05-24 07:20:52');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (76, 76, 'text/vcard', 5, NULL, 16, '2020-06-07 20:19:38', '2016-01-20 12:19:05');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (77, 77, 'application/x-ms-shortcut', 7, NULL, 17, '2012-08-20 11:52:49', '2015-03-12 19:17:22');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (78, 78, 'application/x-cfs-compressed', 3, NULL, 18, '2017-06-01 01:39:02', '2017-04-09 01:59:08');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (79, 79, 'text/calendar', 7, NULL, 19, '2017-06-28 00:46:35', '2019-07-12 05:44:37');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (80, 80, 'application/x-tcl', 2, NULL, 20, '2012-08-27 23:38:18', '2011-07-08 12:48:50');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (81, 81, 'image/vnd.net-fpx', 1, NULL, 1, '2014-09-17 20:47:22', '2011-07-24 02:50:53');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (82, 82, 'image/vnd.dxf', 4, NULL, 2, '2014-03-06 08:32:22', '2011-09-02 02:52:20');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (83, 83, 'application/vnd.ms-powerpoint.slide.macroenabled.12', 7, NULL, 3, '2012-02-09 23:45:10', '2018-07-09 19:09:54');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (84, 84, 'application/vnd.mozilla.xul+xml', 1, NULL, 4, '2011-08-08 06:48:10', '2014-05-14 20:23:31');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (85, 85, 'application/vnd.ms-htmlhelp', 0, NULL, 5, '2012-07-29 11:40:33', '2012-06-29 19:35:47');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (86, 86, 'application/omdoc+xml', 9, NULL, 6, '2020-08-15 02:03:36', '2019-11-15 23:21:56');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (87, 87, 'application/emma+xml', 8, NULL, 7, '2018-10-21 07:28:15', '2014-04-24 12:27:20');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (88, 88, 'image/x-cmu-raster', 9, NULL, 8, '2017-03-20 07:19:22', '2013-03-08 09:01:15');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (89, 89, 'text/vnd.sun.j2me.app-descriptor', 5, NULL, 9, '2018-06-08 22:50:52', '2019-08-24 12:53:55');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (90, 90, 'audio/adpcm', 7, NULL, 10, '2011-10-14 16:58:56', '2015-12-16 12:52:54');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (91, 91, 'application/x-rar-compressed', 1, NULL, 11, '2018-09-21 09:54:31', '2012-10-06 07:25:30');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (92, 92, 'model/vnd.gtw', 1, NULL, 12, '2019-06-03 06:52:27', '2010-10-24 13:30:29');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (93, 93, 'application/x-research-info-systems', 5, NULL, 13, '2014-07-17 04:23:18', '2011-09-18 12:18:26');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (94, 94, 'application/vnd.openxmlformats-officedocument.wordprocessingml.template', 6, NULL, 14, '2018-04-10 07:15:55', '2019-12-28 03:17:41');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (95, 95, 'application/emma+xml', 3, NULL, 15, '2015-02-01 00:20:17', '2013-01-14 14:20:25');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (96, 96, 'application/vnd.epson.ssf', 6, NULL, 16, '2015-03-17 15:48:07', '2020-01-11 18:03:30');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (97, 97, 'application/vnd.oasis.opendocument.presentation-template', 5, NULL, 17, '2014-07-26 19:53:39', '2019-06-28 15:33:36');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (98, 98, 'application/vnd.syncml.dm+xml', 0, NULL, 18, '2013-11-07 11:37:16', '2015-11-18 01:21:24');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (99, 99, 'application/vnd.sus-calendar', 5, NULL, 19, '2015-08-06 20:49:36', '2018-03-03 04:38:55');
INSERT INTO `media` (`id`, `user_id`, `filename`, `size`, `metadata`, `media_type_id`, `created_at`, `updated_at`) VALUES (100, 100, 'application/vnd.syncml.dm+xml', 5, NULL, 20, '2012-12-07 04:44:56', '2018-03-30 01:44:53');


#
# TABLE STRUCTURE FOR: media_types
#

DROP TABLE IF EXISTS `media_types`;

CREATE TABLE `media_types` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `name` varchar(255) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Название типа',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Типы медиафайлов';

INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (1, 'dicta', '2017-01-19 03:38:35', '2019-07-13 17:39:00');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (2, 'alias', '2011-04-20 01:20:51', '2020-07-17 15:56:36');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (3, 'aut', '2012-05-22 07:35:46', '2017-02-02 12:34:35');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (4, 'ut', '2018-11-05 14:39:35', '2012-11-07 04:10:45');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (5, 'voluptas', '2012-12-27 20:33:11', '2020-01-08 07:02:13');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (6, 'in', '2014-11-17 03:46:28', '2018-10-09 13:42:26');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (7, 'rerum', '2013-11-10 08:49:11', '2014-02-02 11:39:37');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (8, 'quaerat', '2018-11-14 10:40:10', '2017-07-18 13:03:06');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (9, 'quibusdam', '2013-10-24 22:08:10', '2015-08-15 05:40:39');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (10, 'ea', '2017-07-14 11:41:43', '2011-09-22 23:36:19');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (11, 'neque', '2017-07-31 09:57:14', '2015-05-09 14:35:25');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (12, 'recusandae', '2019-01-19 20:49:23', '2018-10-22 07:46:53');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (13, 'eligendi', '2011-10-26 20:46:23', '2016-12-23 08:28:57');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (14, 'optio', '2011-03-27 18:04:23', '2011-10-18 16:37:04');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (15, 'repellendus', '2016-01-27 21:02:47', '2013-06-04 06:07:21');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (16, 'et', '2013-12-01 08:30:41', '2017-10-27 11:41:15');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (17, 'molestiae', '2014-03-14 15:50:00', '2011-10-18 12:14:28');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (18, 'minus', '2016-11-03 04:33:58', '2017-09-13 16:30:24');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (19, 'quos', '2017-05-01 07:41:11', '2017-03-15 14:29:53');
INSERT INTO `media_types` (`id`, `name`, `created_at`, `updated_at`) VALUES (20, 'tenetur', '2013-12-09 11:08:57', '2015-01-06 22:54:32');


#
# TABLE STRUCTURE FOR: messages
#

DROP TABLE IF EXISTS `messages`;

CREATE TABLE `messages` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `from_user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на отправителя сообщения',
  `to_user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на получателя сообщения',
  `body` text COLLATE utf8_unicode_ci NOT NULL COMMENT 'Текст сообщения',
  `is_important` tinyint(1) DEFAULT NULL COMMENT 'Признак важности',
  `is_delivered` tinyint(1) DEFAULT NULL COMMENT 'Признак доставки',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Сообщения';

INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (1, 18, 78, 'Aut eum cupiditate voluptatem ipsa sed odio accusantium. Eveniet incidunt officia suscipit. Libero consequatur et minus sint. Voluptate et molestiae vero fuga excepturi quia excepturi nobis.', 0, 0, '2020-03-22 21:18:40', '2013-02-17 15:37:06');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (2, 89, 69, 'Repudiandae blanditiis harum et repellendus dolorum nam qui. Non ducimus fugiat voluptatem voluptas.', 0, 0, '2020-04-28 04:26:16', '2019-08-08 07:21:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (3, 1, 46, 'Dolor quasi dolores placeat hic. Rem odio explicabo enim ut quia et quo. Rerum qui recusandae nihil quas eveniet est. Voluptatem et inventore dolorem facilis.', 1, 1, '2015-03-12 06:01:41', '2013-11-23 00:06:36');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (4, 59, 76, 'Sunt est esse non. Esse dolores ut adipisci. Non et non corporis voluptas.', 0, 1, '2011-04-21 01:39:00', '2010-12-10 02:36:47');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (5, 85, 27, 'Nihil illum alias sit est quia eveniet. Dicta optio quod nam praesentium. Quibusdam excepturi et ullam molestiae atque ullam.', 0, 1, '2019-06-20 06:12:28', '2016-02-20 14:50:43');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (6, 16, 64, 'Distinctio et quibusdam dolores libero nobis. Recusandae hic perferendis ut laudantium aliquid fugit. Provident et excepturi odit deleniti. Laboriosam explicabo eum similique voluptate non minima dolores ea.', 1, 0, '2019-09-11 20:15:18', '2014-02-16 06:27:06');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (7, 78, 38, 'Ea laudantium temporibus repellat tempora et. Necessitatibus tempora sunt voluptate perspiciatis voluptate. Consequatur voluptas optio ut nesciunt occaecati asperiores. Porro distinctio et fugit non error.', 1, 0, '2019-04-12 01:33:36', '2015-11-27 05:38:40');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (8, 89, 67, 'Aspernatur soluta itaque illo blanditiis expedita molestiae sint. Aut occaecati repellat cum et ratione soluta odio quis. Nemo quo accusamus aut reprehenderit voluptate. Iste dolor necessitatibus dignissimos suscipit.', 0, 1, '2011-04-23 15:28:15', '2019-07-14 04:54:40');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (9, 5, 86, 'Dignissimos voluptatem ea blanditiis est. Nostrum similique accusantium eligendi mollitia et tempora. Corporis consequuntur iusto et quia vel doloremque eos. Eaque consequatur sequi enim eaque. Accusantium est placeat corrupti tempora quos autem ullam.', 1, 1, '2019-09-08 04:42:03', '2015-04-10 23:52:42');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (10, 60, 93, 'Commodi blanditiis deleniti consequatur est et. Dicta expedita quia alias necessitatibus odit. Et aspernatur accusantium ut eligendi similique excepturi nisi.', 1, 1, '2017-02-14 22:24:58', '2014-12-18 20:54:18');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (11, 63, 16, 'Doloribus ullam illum neque eos sint. Odio quod sint quos. Error autem occaecati ea consequatur dolores.', 1, 1, '2015-02-14 04:07:41', '2020-07-01 09:04:03');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (12, 67, 28, 'Maiores id repudiandae eum similique esse aliquid totam. Quasi eum minima non similique aut dolores est. Deserunt vel accusamus omnis. Cumque quasi eos tempora et.', 1, 1, '2012-07-29 04:52:59', '2012-06-02 08:35:09');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (13, 1, 88, 'Placeat omnis ut voluptatem quos. Itaque nesciunt incidunt iure voluptas harum. Ipsam minus quae beatae dicta aliquam aspernatur provident et. Aliquid non non aut molestiae.', 0, 0, '2013-04-20 23:45:00', '2018-01-16 20:32:19');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (14, 65, 43, 'Repellendus et et molestiae amet quod ipsum. Rerum ut voluptas enim ipsum corrupti facilis quo. Est et eum autem.', 1, 1, '2015-08-25 14:15:55', '2012-07-31 08:10:53');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (15, 28, 15, 'Consectetur sed est aut eveniet. Omnis ut aut sit sit vero. Qui consequatur nobis sit consequuntur rerum consequuntur perferendis. In possimus fugiat et vero delectus officia.', 0, 1, '2016-11-21 17:37:18', '2020-08-11 20:27:02');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (16, 26, 45, 'Facilis aut hic omnis est dolores. Ea voluptatibus illo autem sapiente reprehenderit exercitationem ratione aut. Dicta suscipit quo earum non nisi omnis veritatis ipsum. Animi neque illum amet incidunt.', 1, 0, '2016-06-12 14:39:18', '2020-01-04 23:14:38');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (17, 93, 14, 'Consequatur neque et debitis sit. Voluptatem omnis iste asperiores reprehenderit et maxime. Et aut maiores ut quis qui.', 0, 0, '2011-11-12 10:41:16', '2017-07-02 08:12:49');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (18, 14, 93, 'Dolor voluptate ad praesentium necessitatibus. Molestiae animi labore adipisci adipisci explicabo repellat. Voluptatem porro rerum voluptas. Mollitia aspernatur vitae ut repellendus aut.', 0, 0, '2018-02-11 17:36:43', '2016-10-18 14:44:51');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (19, 60, 73, 'Eum aut molestiae iste quae dolores. Ut eum laboriosam qui asperiores doloremque. Architecto quia esse animi culpa.', 1, 0, '2013-01-09 08:51:04', '2018-01-31 14:16:04');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (20, 69, 44, 'Dolorem eos quis tempore impedit consequatur nesciunt dolores. A eaque est vitae iure architecto consequatur voluptates. Iure quasi non doloremque.', 1, 0, '2014-07-23 17:23:59', '2015-01-16 13:54:51');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (21, 100, 84, 'Omnis voluptatem dicta perspiciatis aut autem. Dolores iste fugit non commodi. Qui dolores sint iure natus omnis odit est. Voluptas dolorem officiis velit veritatis.', 0, 0, '2019-07-03 18:50:06', '2017-07-17 06:10:12');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (22, 8, 77, 'Voluptatibus illo sit ut cum commodi quia. Aut quo sapiente sit facere. Possimus illo iusto aut repellendus voluptas. Accusantium incidunt odio dicta dolore veniam distinctio quia.', 1, 1, '2013-01-14 02:03:02', '2011-12-31 19:00:17');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (23, 22, 96, 'Eum nihil laudantium voluptas et. Id minus animi aut non pariatur velit. Modi nostrum impedit possimus qui. Quisquam a modi est ratione est.', 1, 0, '2017-12-31 06:58:42', '2017-12-23 05:54:25');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (24, 43, 26, 'Vel natus provident velit et. Dolorum minima optio nam. Voluptatum ea unde quis qui omnis vero dolorum vel. Quo magni ipsum hic illum dolorem voluptatum eveniet.', 1, 0, '2012-12-29 20:34:19', '2015-07-16 08:36:20');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (25, 81, 2, 'Vel et nemo in. Earum quia odit quo sit. Consectetur dolorem vitae porro voluptas deleniti et.', 0, 1, '2012-10-09 11:41:47', '2015-03-22 15:53:07');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (26, 19, 44, 'Magni saepe doloremque id. Esse quam in perferendis consectetur voluptas. Necessitatibus atque provident mollitia modi voluptatem pariatur debitis aut.', 0, 0, '2013-06-27 14:53:41', '2016-02-14 19:17:38');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (27, 17, 86, 'Vitae veritatis cupiditate sunt repudiandae qui. Deserunt ut perspiciatis ex molestias quasi nam aut.', 0, 1, '2016-09-12 20:07:45', '2013-01-28 08:16:41');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (28, 72, 18, 'Ea nisi dolores voluptatem eius. Repellat consequuntur tenetur fuga. Porro itaque qui id enim similique maxime voluptas. Soluta non autem modi nostrum tempora.', 0, 0, '2012-08-05 23:32:18', '2014-05-04 22:16:56');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (29, 73, 36, 'Ut nihil laudantium itaque distinctio ratione maxime libero. Porro laboriosam consequatur aperiam velit non sed.', 0, 1, '2019-09-08 22:41:09', '2014-07-10 03:43:31');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (30, 60, 100, 'Minima aspernatur aspernatur aperiam numquam sed enim. Et culpa est harum optio. Aut fugit nisi in velit non vel.', 0, 0, '2013-12-10 05:17:59', '2015-05-14 09:11:59');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (31, 51, 86, 'A est cumque omnis iure placeat. Ut cumque ut in aut.', 0, 0, '2017-02-28 02:15:31', '2012-04-07 17:56:48');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (32, 45, 43, 'Et illo sit repudiandae nihil. Officia eius in tenetur ut. Ea rerum neque iste dolorem libero.', 0, 0, '2020-01-09 11:36:23', '2020-07-18 08:39:59');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (33, 100, 59, 'Non vero libero molestiae et excepturi. Totam maiores sit tempore ab suscipit. Id repellat atque reprehenderit et veritatis cumque. Dolorum fugit aliquam in molestiae.', 1, 1, '2014-04-04 15:43:50', '2014-07-22 06:37:53');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (34, 35, 59, 'Est dignissimos occaecati possimus qui. Dicta non debitis consequuntur et earum laudantium. Amet voluptatem fuga facilis aut provident aliquid.', 1, 1, '2011-02-27 17:47:00', '2018-02-20 10:02:05');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (35, 31, 4, 'Molestiae nam voluptatum inventore. Rerum quisquam aspernatur dolores magnam.', 1, 0, '2013-11-10 05:54:51', '2019-01-22 16:42:51');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (36, 2, 30, 'Error distinctio quos illum excepturi at eius sequi libero. Itaque quia quam distinctio rerum consequatur. Aspernatur qui maiores incidunt voluptatem est. Eos exercitationem aut aut magnam nihil.', 1, 1, '2018-09-25 10:37:06', '2014-02-26 06:55:44');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (37, 88, 10, 'Repellat consequatur quis voluptatibus consequatur eius nihil. Aut ipsum et tempora adipisci similique nisi eius. Reiciendis aut earum perferendis illo temporibus molestias. Quo ipsa est voluptatum.', 0, 0, '2019-08-24 21:33:27', '2018-05-22 00:58:16');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (38, 6, 9, 'Id voluptatem similique dolorem necessitatibus qui quam reiciendis cumque. Eum omnis soluta amet id rerum voluptatem. Quo voluptatem id minus eius.', 0, 0, '2012-01-28 20:19:09', '2014-07-21 15:45:13');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (39, 5, 49, 'Numquam sit itaque et. Commodi alias sit officiis aliquid non eum est dicta. Perspiciatis nesciunt id aut saepe. Neque aut quam porro.', 1, 0, '2015-09-19 11:12:30', '2011-06-04 19:56:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (40, 35, 86, 'Eligendi commodi facere ducimus cum dolorum nobis. Doloremque voluptas nemo sit minima qui est aperiam. Velit nemo iste quaerat voluptas ipsum vero nesciunt. Ipsum non aliquid amet officia voluptates.', 0, 0, '2020-02-20 05:21:08', '2019-10-21 11:19:00');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (41, 50, 53, 'Ad voluptates voluptas dolorum sunt. Rem similique ut et quia vel. Sunt et voluptas voluptate consequatur aliquam deleniti architecto.', 0, 1, '2019-11-18 16:12:23', '2019-02-01 05:23:52');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (42, 29, 67, 'Reiciendis rem hic aut repellat qui quis. Autem laborum minima enim ea. Hic sunt harum officiis dolor. Doloremque nihil delectus quidem qui tempore soluta excepturi.', 1, 0, '2011-11-10 12:23:14', '2013-11-21 16:34:02');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (43, 38, 1, 'Enim sit architecto rerum fuga minima. Deserunt eum laboriosam reprehenderit quia. Atque velit saepe non ut.', 0, 1, '2019-04-22 02:33:45', '2016-11-26 23:49:42');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (44, 84, 11, 'Nobis expedita nesciunt praesentium aut incidunt officia. Est excepturi id in molestiae quam. Recusandae soluta ut maiores excepturi architecto.', 1, 1, '2017-01-31 12:00:47', '2014-07-03 01:21:52');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (45, 37, 44, 'Ipsum deserunt corporis nulla facere alias. Repudiandae nam labore ab mollitia doloremque veritatis. Unde aut id cum sunt commodi quod repellendus velit. Ut sed magni aut voluptatum possimus.', 0, 0, '2013-01-29 14:26:48', '2016-08-04 12:57:29');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (46, 10, 87, 'In molestiae enim provident molestiae. Qui consequuntur voluptatem et non facilis voluptas quibusdam. Deleniti ut doloremque eius necessitatibus.', 0, 0, '2013-09-05 16:52:42', '2015-03-20 15:35:20');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (47, 29, 54, 'Eum voluptates dolores ipsam exercitationem. Aut officia ratione sit molestias quisquam qui nobis. Pariatur cupiditate natus eum ipsum. Odit voluptatum sit ut numquam. Officia et dolor debitis aspernatur facere.', 0, 0, '2020-05-17 02:08:01', '2017-02-01 00:29:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (48, 29, 28, 'Deleniti velit assumenda debitis asperiores odit voluptatum dolores ut. Eum ea sed possimus voluptatem porro nihil a. Laboriosam deleniti ex voluptate aliquid. Aliquam recusandae magnam tempore asperiores reprehenderit.', 1, 0, '2018-11-20 03:32:43', '2015-01-20 06:38:41');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (49, 12, 64, 'Minus at ut temporibus iusto. Autem eveniet eum esse ullam nulla. Assumenda harum odit doloribus doloribus occaecati. Minus iste cupiditate aut enim assumenda qui.', 1, 0, '2013-07-12 12:35:36', '2013-09-03 15:29:02');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (50, 86, 43, 'Quo laudantium et quis magnam asperiores tempore. Voluptas aspernatur cupiditate autem culpa. Impedit itaque nihil natus enim est. Quisquam voluptatem dolorem vero asperiores quae.', 0, 1, '2018-05-19 06:34:05', '2017-08-10 21:03:28');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (51, 67, 88, 'Facere nostrum voluptatem et voluptates modi facere. Repudiandae reprehenderit quaerat iusto reprehenderit voluptatem eligendi eum. Adipisci quos ex alias distinctio.', 1, 1, '2019-11-11 03:09:52', '2019-04-30 06:39:00');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (52, 72, 54, 'Et qui temporibus recusandae eaque dolorem voluptatem et. Nam qui in nobis rerum consequuntur. Veniam illo doloremque nobis ad dolor omnis. Temporibus facilis et in.', 0, 1, '2015-11-28 21:36:09', '2011-07-04 22:55:31');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (53, 97, 78, 'Beatae beatae totam autem. Perspiciatis sed quas aliquid excepturi sunt. Occaecati rerum laudantium tenetur. Suscipit voluptas non voluptatum sit qui repellendus veritatis. Unde quibusdam ipsa id explicabo laudantium.', 0, 0, '2015-10-18 16:20:46', '2015-10-10 03:54:44');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (54, 63, 2, 'Corporis sit optio aspernatur suscipit deleniti. Earum tenetur quibusdam aperiam ad id. Quaerat qui quasi quae ratione laborum fuga.', 0, 0, '2010-11-06 11:55:17', '2018-11-08 21:55:05');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (55, 26, 97, 'Est ratione facere molestias ullam deserunt impedit et. Et dolore aut ab accusamus ut deleniti. Cumque dolorum neque sit neque.', 0, 1, '2018-10-28 17:10:02', '2017-06-17 18:01:08');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (56, 87, 76, 'Hic eum facere nobis numquam. Cupiditate a voluptas quis rerum dolor hic itaque. Temporibus alias et non velit. Exercitationem commodi rem quae modi natus ut.', 0, 0, '2010-12-21 07:15:43', '2011-12-10 03:24:40');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (57, 50, 16, 'Vitae velit quasi nobis ut nemo. Et eaque voluptatibus modi incidunt est totam. Dolor mollitia nam modi asperiores.', 1, 1, '2015-12-04 00:05:54', '2011-04-23 20:22:00');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (58, 43, 88, 'Ratione minima ut architecto a adipisci a. Quia aut sed corporis et quam. Atque veritatis officia nihil esse ullam asperiores sunt. Excepturi sunt perspiciatis corrupti id temporibus voluptatem similique.', 0, 0, '2020-03-30 10:38:06', '2017-12-31 19:07:25');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (59, 16, 26, 'Et error id velit sunt quas fugiat est voluptas. Maiores et voluptate dolor in nobis. Est facere facilis sint aut.', 0, 0, '2019-02-02 09:00:59', '2014-11-07 10:18:01');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (60, 98, 52, 'Eaque fuga consequuntur ex id. Autem suscipit labore veniam enim optio sit. Non qui blanditiis non nam eum.', 1, 1, '2019-09-19 23:59:51', '2011-06-19 13:31:31');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (61, 69, 8, 'At est accusantium aut excepturi magni. Sint ipsum dolorum aut ut aut enim. Et animi voluptatem aspernatur ducimus sit.', 0, 0, '2012-10-26 05:26:47', '2018-03-26 05:38:31');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (62, 38, 97, 'Vero aut corrupti dolorem voluptates. Omnis illo vero et eos commodi. Dolor ea fugit rerum est voluptatibus aspernatur.', 0, 0, '2018-02-25 12:29:32', '2013-07-23 18:37:18');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (63, 61, 66, 'Quos ut perferendis quos officiis. Unde optio velit totam mollitia et qui. Est inventore soluta itaque quod inventore. Fuga illum dolores accusamus laboriosam ab fuga. Natus reprehenderit voluptas odio.', 0, 1, '2018-01-14 22:59:33', '2019-10-26 11:40:01');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (64, 25, 73, 'Est error sed perferendis vel totam voluptatem enim placeat. Aliquam ad enim quia fuga voluptatem fugit dignissimos. Et in maxime tempore at ut. Amet rerum adipisci accusamus dolores quo. Incidunt atque aliquam est vero.', 0, 0, '2011-05-31 11:00:22', '2016-10-23 21:46:51');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (65, 29, 10, 'Inventore aliquam commodi voluptas iste rerum. Nulla minus unde voluptatem. Voluptate saepe aut eius molestiae. Sed dolores rerum architecto molestiae fugiat aut.', 1, 0, '2012-03-18 07:04:43', '2018-09-28 23:51:26');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (66, 15, 96, 'Aperiam illum nulla laboriosam illo et voluptatem. Veniam nisi praesentium eum aut voluptatem minima nisi quis. Molestiae commodi alias fugit laudantium ratione.', 1, 0, '2014-11-23 12:40:21', '2011-05-05 16:31:07');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (67, 98, 87, 'Ipsam libero dolor eligendi aut. Sed natus cumque dolorem quis et autem. Eos omnis hic ullam error. Ducimus quod autem et sed.', 0, 1, '2018-08-19 13:05:26', '2012-11-22 01:41:20');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (68, 50, 95, 'Et tenetur minus commodi et. Expedita saepe quibusdam placeat pariatur similique. Voluptatem sapiente quae rerum laboriosam consequatur reprehenderit beatae optio.', 0, 0, '2015-06-16 08:27:34', '2020-01-02 03:21:13');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (69, 65, 12, 'Itaque vitae quo officia eligendi minima tenetur. Error nostrum et sed tempora sed. Sunt sit facere quae qui.', 1, 1, '2014-11-18 22:40:37', '2012-12-06 08:13:37');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (70, 96, 90, 'Et odit omnis facere incidunt accusantium. A tempore eos repellat sequi quis reiciendis similique. Ut possimus et ea nihil distinctio dolor dolorem. Maiores quidem dolores nulla et est.', 0, 1, '2016-04-30 10:02:04', '2020-09-02 19:50:19');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (71, 9, 83, 'Dolorem beatae dolor tenetur aut tenetur. Est qui voluptatem voluptatem dicta id. Possimus aspernatur placeat ut dolorem sint.', 1, 0, '2014-12-05 08:05:27', '2018-09-22 14:21:57');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (72, 66, 58, 'Ullam quis pariatur vero perferendis. Numquam dicta et voluptatem qui provident quia cupiditate. Perferendis sint consequatur repellendus asperiores. Itaque sint perferendis nobis quia sed.', 1, 0, '2016-02-27 07:41:24', '2011-11-28 07:32:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (73, 99, 8, 'Explicabo saepe sequi voluptates quam consectetur alias. Non quibusdam ex necessitatibus et. Qui est repudiandae qui ut illum.', 0, 1, '2018-04-27 16:05:00', '2014-04-18 04:22:22');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (74, 46, 14, 'Optio at provident dignissimos non harum quos. Ullam maxime tenetur sequi optio distinctio. Labore eos quia sed at.', 0, 1, '2015-11-28 03:38:24', '2018-05-07 19:15:48');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (75, 34, 43, 'Et voluptas et numquam perferendis est aut. Aperiam et quia magnam dolorum et. Aut quis hic ratione quod. Voluptatem a veniam excepturi voluptatem laborum quia fuga qui. Aut ipsam fuga voluptatem vel.', 0, 1, '2011-07-27 02:55:16', '2011-04-22 04:59:28');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (76, 66, 3, 'Consequatur quod sunt nemo dolorem modi. Sequi ipsa incidunt consequatur ad explicabo sapiente. Magni sed necessitatibus aut porro beatae. Facere laudantium velit molestiae ipsa asperiores et.', 1, 1, '2011-08-25 17:45:11', '2019-05-09 11:44:12');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (77, 50, 4, 'Hic quae molestiae deleniti sint ut enim. Voluptatem magnam ut nulla repellat et. Saepe consequatur nihil natus asperiores est. Esse voluptatum quo numquam dolor illum soluta illum animi.', 0, 0, '2020-02-20 16:10:06', '2013-04-08 03:18:23');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (78, 100, 11, 'Et quam voluptatem quisquam commodi tempore quibusdam. Possimus commodi adipisci est laborum suscipit qui et rerum. Minima ea aliquam qui corporis asperiores quo eaque. Temporibus eius accusamus dolor debitis expedita consequatur.', 0, 1, '2012-02-29 02:14:43', '2016-12-03 15:11:32');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (79, 70, 24, 'Qui cupiditate aperiam quo suscipit quae in. Totam nisi iusto odio autem et. Maiores illo velit iusto voluptate.', 0, 1, '2014-05-05 11:58:37', '2017-10-03 21:42:22');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (80, 84, 99, 'Suscipit et omnis ut quidem dolor. Sequi enim dolor in ea quo repellat perspiciatis. Beatae adipisci voluptatum voluptas iure. Sit inventore delectus et ducimus voluptatem.', 0, 1, '2019-04-01 23:50:57', '2018-04-15 05:28:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (81, 34, 99, 'Corporis ut mollitia nesciunt et. Asperiores minus distinctio numquam pariatur nemo nobis voluptas. Similique quos ipsam est et molestiae. Inventore placeat expedita fuga laudantium dolor.', 1, 0, '2016-05-12 13:55:05', '2011-05-24 20:11:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (82, 94, 31, 'Aut amet rerum eos sit deleniti cum totam. Dolorem sit et ipsa iure. Exercitationem voluptatem doloremque ad enim ut cupiditate ipsa. Aut reiciendis ad perspiciatis totam omnis eius.', 0, 0, '2020-02-11 23:42:43', '2016-09-28 16:29:45');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (83, 86, 43, 'Natus eos minima praesentium autem. Minus omnis placeat ratione. Deserunt esse nemo dolores voluptatem corrupti. Ea exercitationem voluptatem vero similique nesciunt dolorum.', 0, 0, '2018-02-06 14:10:18', '2017-10-13 00:38:21');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (84, 25, 50, 'Sint unde soluta vel cumque eos et. Autem iusto cumque veniam placeat esse. Voluptatem corporis tenetur quod et.', 0, 1, '2016-03-14 12:14:34', '2013-04-01 19:19:47');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (85, 55, 21, 'Consequatur expedita laudantium eos maiores. Cumque exercitationem tempore nesciunt accusantium. Ut minus incidunt atque consequuntur autem sed. Quos recusandae corrupti et voluptatibus.', 1, 0, '2019-07-27 02:25:42', '2016-03-11 18:54:48');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (86, 40, 63, 'Eaque ratione ut enim quis ab nesciunt et. Vitae quae sunt sit dolore. Aut beatae nesciunt enim.', 0, 1, '2013-02-08 15:46:10', '2019-04-20 08:39:43');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (87, 4, 5, 'Quis alias dolor id quia officiis. Doloribus repellendus veritatis iusto qui eos. Voluptatem laboriosam optio sed sed.', 0, 1, '2017-01-08 10:49:08', '2020-05-22 06:10:09');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (88, 21, 2, 'Sed accusamus harum quia sed earum quos. Est sequi voluptatem et velit. Nam quam perferendis pariatur ut cumque odio voluptates. Eum qui hic et laudantium.', 0, 1, '2016-10-08 05:02:29', '2012-10-22 06:10:25');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (89, 13, 66, 'Doloremque adipisci aut necessitatibus. Placeat consequatur corporis temporibus officiis similique.', 0, 1, '2019-06-17 10:27:53', '2013-02-27 08:46:15');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (90, 16, 46, 'Itaque provident pariatur consequatur suscipit deserunt consequatur eum mollitia. Molestias corporis dolores saepe quam ullam. Eius quia qui quidem. Ipsa quod reiciendis cum laborum illum occaecati similique. Ut officiis voluptas dolorem incidunt eligendi eos.', 1, 1, '2012-06-16 18:31:55', '2014-02-01 04:03:52');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (91, 9, 81, 'Totam ipsam nisi et dolores rerum dignissimos. Deleniti voluptatem ab deserunt quia. Commodi blanditiis voluptatem sit dolores. Ut voluptatem ullam blanditiis fuga rerum incidunt omnis ut.', 0, 1, '2010-09-15 00:12:25', '2013-12-20 08:52:44');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (92, 48, 58, 'Eius omnis enim perferendis ut aut. Culpa in dicta nihil. Sed dicta officiis et eos. Voluptatem consequatur voluptatem harum ut.', 0, 1, '2020-02-07 05:44:23', '2014-08-22 00:18:31');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (93, 84, 47, 'Corporis rerum praesentium sint id nesciunt inventore. Omnis in delectus autem quidem. Necessitatibus necessitatibus quibusdam asperiores.', 0, 0, '2015-05-23 13:53:08', '2017-02-18 21:04:26');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (94, 69, 53, 'Voluptatem et laborum voluptatibus aut asperiores sit ut. Recusandae dolore voluptate molestiae modi explicabo qui. Aut est ratione quod quia nemo consequuntur. Dolor ex voluptatem occaecati neque reiciendis non placeat.', 0, 1, '2013-08-23 12:51:35', '2019-10-03 04:32:49');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (95, 70, 52, 'Fuga voluptatem dolorem est non sed molestias. Dolor vero qui voluptas consectetur asperiores rerum. Est asperiores totam asperiores officiis consequatur veniam tenetur. Ut sint ab aut officia ut quia. Sit sint ea similique vel illo.', 1, 0, '2015-01-20 05:19:22', '2017-09-15 02:31:56');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (96, 51, 4, 'Ipsam at ad debitis sit incidunt. Recusandae incidunt autem quas sed aspernatur voluptatum voluptas. Odit nisi corporis ut voluptatum consequatur asperiores fugit. Quia necessitatibus qui enim dignissimos qui facere unde.', 1, 0, '2017-01-14 07:21:44', '2019-10-16 21:16:02');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (97, 51, 45, 'Autem dolorum aut ullam quas accusantium sint quod. Nostrum quis dolor deleniti illo. Doloribus est est voluptatem vel et. Harum quo vel quis iusto qui.', 1, 0, '2017-01-30 06:28:31', '2018-04-09 00:53:38');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (98, 34, 36, 'Ipsam sed suscipit fugit enim hic error quidem. Atque ad facilis quia distinctio minus. Harum enim omnis dolor cupiditate qui.', 0, 0, '2010-10-19 20:12:35', '2016-08-22 06:27:07');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (99, 87, 59, 'Sunt ut architecto unde quos sunt. Aut unde voluptatem debitis quam ut minus. Aut fugiat provident qui quia eos similique rem culpa.', 1, 0, '2016-04-12 13:29:54', '2013-08-25 00:04:44');
INSERT INTO `messages` (`id`, `from_user_id`, `to_user_id`, `body`, `is_important`, `is_delivered`, `created_at`, `updated_at`) VALUES (100, 85, 41, 'Nobis consectetur architecto similique placeat laborum officia consequuntur dolor. Est saepe voluptatibus in blanditiis qui autem voluptatum nisi. Ut error temporibus illo adipisci sint. Amet et libero optio illo a rem aperiam vitae. Soluta consectetur ducimus repellat.', 1, 1, '2016-11-21 21:36:03', '2015-06-27 06:31:00');


#
# TABLE STRUCTURE FOR: profiles
#

DROP TABLE IF EXISTS `profiles`;

CREATE TABLE `profiles` (
  `user_id` int(10) unsigned NOT NULL COMMENT 'Ссылка на пользователя',
  `gender` char(1) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Пол',
  `birthday` date DEFAULT NULL COMMENT 'Дата рождения',
  `photo_id` int(10) unsigned DEFAULT NULL COMMENT 'Ссылка на основную фотографию пользователя',
  `status` varchar(30) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'Текущий статус',
  `city` varchar(130) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'Город проживания',
  `country` varchar(130) COLLATE utf8_unicode_ci DEFAULT NULL COMMENT 'Страна проживания',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Профили';

INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (1, 'm', '1996-12-04', 0, 'Velit nihil quam cum tempore u', 'New Rosalinda', 'Norfolk Island', '2019-01-19 15:00:25', '2014-03-11 13:25:01');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (2, 'm', '2011-12-29', 686, 'Asperiores iure ex ut voluptat', 'Alexville', 'Qatar', '2020-02-08 12:45:09', '2018-11-26 07:40:09');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (3, 'm', '1999-08-29', 6212, 'Aperiam ut autem delectus nequ', 'East Vivienne', 'Holy See (Vatican City State)', '2017-10-07 05:00:57', '2019-05-29 15:18:14');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (4, 'f', '1973-12-21', 1450, 'Illum cumque maxime ratione ea', 'South Theodoraport', 'Liechtenstein', '2013-03-07 10:58:28', '2011-08-09 00:45:21');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (5, 'f', '2016-06-30', 888, 'Animi sunt et dicta deleniti c', 'East Maymie', 'Sierra Leone', '2016-06-06 04:51:56', '2013-09-03 15:47:01');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (6, 'm', '2019-01-04', 705203, 'Et eius quo non voluptatem vol', 'Ortizport', 'Montserrat', '2013-07-13 13:02:06', '2018-05-15 01:55:45');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (7, 'f', '2010-05-14', 3, 'Libero nesciunt ipsum sint vol', 'Lake Jovanberg', 'Trinidad and Tobago', '2011-01-25 08:46:51', '2013-03-30 20:25:44');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (8, 'm', '1979-12-20', 56, 'Et repudiandae quasi consectet', 'Haileystad', 'Papua New Guinea', '2015-05-31 08:53:03', '2017-05-28 15:13:21');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (9, 'm', '2013-10-05', 6782000, 'Omnis facere animi officiis ra', 'Judahmouth', 'Colombia', '2017-12-03 06:02:45', '2017-11-25 16:41:35');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (10, 'm', '2010-01-24', 12, 'Inventore corporis harum vero ', 'West Mireille', 'Suriname', '2013-01-08 04:43:08', '2017-09-23 04:14:58');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (11, 'm', '1980-12-02', 81171, 'Et excepturi quia rerum harum.', 'Roryborough', 'Trinidad and Tobago', '2019-05-07 14:18:07', '2019-10-12 16:21:10');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (12, 'f', '1996-03-27', 959, 'Est maiores neque vero non in ', 'Larsontown', 'Montserrat', '2015-11-10 02:14:53', '2017-05-04 03:08:54');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (13, 'f', '1994-09-01', 9, 'Commodi maiores ut tenetur qui', 'East Anastasiabury', 'Singapore', '2013-12-29 17:25:53', '2011-11-12 03:49:05');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (14, 'm', '2017-12-23', 536473, 'Rerum odio excepturi laboriosa', 'South Marcellus', 'Sweden', '2016-03-11 06:45:48', '2017-08-28 12:10:22');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (15, 'm', '1981-09-22', 748589148, 'Tempora esse sint qui laudanti', 'South Zackary', 'Montserrat', '2018-10-10 09:28:41', '2014-05-04 08:22:47');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (16, 'm', '1993-03-31', 861, 'Sint quas quia quo esse invent', 'Lake Eastertown', 'Netherlands', '2020-06-13 00:47:46', '2011-02-18 08:50:21');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (17, 'm', '2013-01-11', 11628452, 'Dolorum occaecati incidunt fac', 'Xzavierland', 'Nicaragua', '2017-07-03 17:30:15', '2013-05-08 04:26:15');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (18, 'f', '2018-09-22', 8582, 'Consequuntur laudantium est ve', 'Lake Elenora', 'Tokelau', '2015-11-22 17:09:54', '2016-06-03 14:39:18');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (19, 'm', '1974-05-04', 599, 'Accusamus quam adipisci sit qu', 'Lake Velvachester', 'Argentina', '2013-09-18 11:43:40', '2011-03-21 18:27:36');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (20, 'm', '1997-07-20', 1, 'Rerum necessitatibus quia non ', 'Seanshire', 'Ukraine', '2018-11-03 03:45:55', '2018-06-21 15:24:51');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (21, 'f', '1971-01-24', 60315072, 'Molestias qui architecto offic', 'West Jillian', 'Indonesia', '2015-03-02 03:37:10', '2018-01-11 21:37:57');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (22, 'm', '2001-10-24', 1106494, 'Enim omnis id id eos commodi. ', 'Lake Maia', 'Poland', '2019-05-19 23:43:12', '2018-08-30 23:24:03');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (23, 'f', '2002-06-28', 861153868, 'In magnam voluptatem quia repe', 'West Ryleighton', 'Tajikistan', '2017-01-27 15:15:39', '2013-09-07 23:35:18');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (24, 'f', '1976-08-16', 97590628, 'Aliquam labore similique quia ', 'Kochchester', 'Uruguay', '2013-06-16 11:33:52', '2016-08-26 15:33:55');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (25, 'm', '1976-09-28', 81903898, 'Iusto voluptatem dolorem ipsum', 'New Cristian', 'Montserrat', '2016-10-12 22:19:36', '2011-01-17 12:57:33');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (26, 'f', '2002-11-08', 751388, 'Magni fuga consequuntur quia d', 'South Elroymouth', 'Slovakia (Slovak Republic)', '2016-03-15 13:53:38', '2017-12-13 02:03:22');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (27, 'f', '2013-11-12', 6945599, 'Repellat iusto et velit volupt', 'Blockhaven', 'Macedonia', '2013-11-12 04:24:48', '2012-07-28 17:47:02');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (28, 'm', '2006-10-02', 53168126, 'Quasi velit modi voluptate ape', 'Port Claudeberg', 'Norfolk Island', '2017-09-14 07:51:19', '2014-11-01 23:47:45');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (29, 'f', '1972-10-13', 976, 'Dolorum similique veritatis ma', 'Port Alekside', 'Equatorial Guinea', '2011-12-22 20:17:28', '2013-05-09 12:11:09');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (30, 'f', '1991-09-12', 692650, 'Molestiae repellendus dolorum ', 'Vonport', 'Bosnia and Herzegovina', '2017-10-03 04:54:24', '2013-12-13 07:17:19');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (31, 'm', '2011-09-08', 804487, 'Earum distinctio voluptatibus ', 'Alanshire', 'Somalia', '2012-07-31 06:09:02', '2013-05-18 00:13:47');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (32, 'f', '2019-07-06', 855, 'Illum in iste aut iure aut qua', 'North Tyrique', 'Afghanistan', '2019-06-04 03:20:22', '2019-04-13 03:26:32');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (33, 'm', '1993-12-22', 55, 'Nobis beatae ut ullam et. Culp', 'East Serenity', 'Togo', '2015-08-10 08:08:04', '2012-11-27 02:54:31');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (34, 'f', '1979-01-01', 67, 'Nobis quia quis vel temporibus', 'Francomouth', 'Guinea-Bissau', '2011-09-05 04:57:09', '2015-11-26 04:10:25');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (35, 'm', '2012-01-11', 4781, 'Quia repellat illum ipsum erro', 'North Earnestine', 'Sierra Leone', '2015-05-31 17:37:38', '2011-01-25 10:47:42');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (36, 'm', '1981-03-06', 82316476, 'Autem odit dignissimos tenetur', 'Ginoville', 'Thailand', '2010-10-22 02:40:55', '2013-08-26 14:13:16');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (37, 'm', '1980-03-14', 3540, 'Dolore temporibus ea aut liber', 'Gerlachfurt', 'Rwanda', '2012-11-28 12:59:56', '2014-02-09 22:30:20');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (38, 'f', '2003-05-31', 9228901, 'Beatae et fugit ipsum. Ut ut s', 'Streichville', 'Guadeloupe', '2014-04-26 05:11:02', '2011-07-08 22:55:04');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (39, 'f', '2012-11-09', 6, 'Sunt iure pariatur deleniti mi', 'Balistreritown', 'Bosnia and Herzegovina', '2019-08-29 05:54:58', '2017-10-21 23:48:07');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (40, 'm', '1975-03-08', 75, 'Cupiditate sint est ut dolor v', 'Jastfort', 'India', '2016-10-27 01:33:22', '2015-04-02 13:56:50');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (41, 'f', '2006-03-08', 7451095, 'Mollitia modi sit temporibus a', 'Brionnachester', 'Angola', '2019-10-05 12:09:56', '2015-12-25 01:11:15');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (42, 'f', '2018-04-09', 804876287, 'Autem debitis velit fugit assu', 'North Yadirachester', 'Chile', '2017-10-08 04:42:11', '2018-03-28 16:56:07');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (43, 'm', '2006-09-23', 8, 'Dolor quis vero voluptate. Sit', 'Lake Isabell', 'Antigua and Barbuda', '2011-02-21 21:28:00', '2019-02-10 13:02:13');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (44, 'f', '1997-10-10', 34, 'Excepturi illo voluptatem odit', 'Ashleyview', 'Costa Rica', '2014-12-23 05:36:27', '2015-07-17 18:05:24');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (45, 'm', '1986-01-09', 8095482, 'Unde omnis rerum a repellat. D', 'New Tonystad', 'Italy', '2019-05-30 14:31:51', '2019-08-25 14:07:08');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (46, 'f', '2012-04-14', 8525229, 'Ut placeat consectetur nisi su', 'West Johathanville', 'Saint Lucia', '2012-06-02 07:53:29', '2013-01-04 01:53:19');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (47, 'm', '2003-06-06', 669, 'Quod et voluptate quasi in vel', 'Morarshire', 'Spain', '2017-02-24 18:23:10', '2018-12-19 10:20:13');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (48, 'f', '1972-04-29', 71959, 'Qui et repudiandae fuga. Vero ', 'Fritschview', 'Indonesia', '2020-06-11 01:43:12', '2012-04-10 00:29:01');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (49, 'f', '2008-08-09', 159, 'Voluptas consequatur neque qui', 'North Otiliamouth', 'Afghanistan', '2015-08-10 01:07:18', '2015-05-29 10:35:46');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (50, 'f', '2009-11-20', 957, 'Ratione sapiente quibusdam quo', 'East Karley', 'Djibouti', '2018-11-14 18:29:19', '2011-04-30 16:49:27');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (51, 'm', '2008-04-04', 505870, 'Itaque sunt exercitationem eiu', 'Port Marietta', 'Solomon Islands', '2019-04-14 21:40:07', '2016-12-01 17:55:14');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (52, 'f', '2019-01-12', 45, 'Dolores voluptate odio velit q', 'Schillerchester', 'Antigua and Barbuda', '2012-08-07 01:43:04', '2016-06-13 07:01:59');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (53, 'm', '2000-02-19', 311, 'Cum et ut nemo quos. Suscipit ', 'Jazlynborough', 'Saudi Arabia', '2017-03-07 02:46:50', '2011-04-07 09:58:50');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (54, 'm', '1975-02-13', 76, 'Libero aliquam atque voluptas ', 'Lennaview', 'Finland', '2012-03-14 15:26:00', '2018-03-07 00:06:59');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (55, 'm', '1988-09-14', 2488, 'Impedit tempora debitis in sed', 'Thompsonmouth', 'Bosnia and Herzegovina', '2011-03-17 05:41:52', '2020-05-02 11:16:12');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (56, 'f', '1977-06-24', 90287, 'Ut dignissimos quisquam quia p', 'Port Levi', 'India', '2016-02-24 15:09:02', '2012-08-20 21:26:13');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (57, 'm', '1987-03-20', 82719, 'Ipsum id quis perspiciatis sit', 'East Torey', 'United States Minor Outlying Islands', '2020-01-06 05:08:02', '2019-05-27 16:20:54');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (58, 'm', '1983-07-20', 180, 'Dolorum voluptates et cumque a', 'Port Juana', 'Korea', '2019-09-30 01:37:33', '2015-11-07 21:36:11');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (59, 'f', '1992-08-09', 393, 'Ab impedit molestiae at tempor', 'Liamland', 'Ethiopia', '2018-05-03 20:22:36', '2015-08-31 09:26:12');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (60, 'm', '1991-01-13', 2, 'Placeat asperiores sit beatae ', 'South Elijahland', 'Egypt', '2014-05-27 20:51:48', '2011-05-27 23:17:44');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (61, 'm', '1984-08-26', 5, 'Facere sunt et adipisci conseq', 'Clementinebury', 'Burundi', '2018-09-07 21:29:26', '2017-10-07 13:04:19');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (62, 'm', '1999-07-30', 89031087, 'Perspiciatis blanditiis quia p', 'Alview', 'Djibouti', '2011-03-23 21:07:45', '2012-10-23 02:51:33');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (63, 'm', '1970-03-13', 929622, 'Qui et quia odio nemo incidunt', 'New Harrisonfort', 'Mexico', '2014-12-17 16:31:47', '2015-11-19 12:57:07');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (64, 'm', '2002-05-03', 52310055, 'Sed iusto sit reiciendis quam ', 'North Amanda', 'Greenland', '2020-08-18 17:22:07', '2020-07-31 22:01:37');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (65, 'f', '1999-01-16', 5802462, 'Est et reiciendis corporis. Vo', 'Fredaton', 'El Salvador', '2020-05-26 12:30:20', '2010-11-29 22:04:58');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (66, 'f', '2002-09-20', 485332958, 'Corporis qui sint aut et dicta', 'Grahamfurt', 'Israel', '2017-10-15 14:15:36', '2015-01-24 06:56:11');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (67, 'm', '1982-08-31', 932789, 'Iusto illo ad cumque amet tota', 'New Evelynview', 'Czech Republic', '2017-06-24 11:51:09', '2015-09-12 21:00:26');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (68, 'm', '1996-10-13', 717015570, 'In itaque ut voluptatum rerum ', 'East Davonte', 'Pakistan', '2010-12-03 13:37:42', '2015-08-07 07:46:17');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (69, 'm', '2018-12-20', 331, 'Accusantium quo explicabo dolo', 'Lake Simone', 'Cayman Islands', '2011-10-14 08:03:45', '2015-10-27 22:20:04');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (70, 'm', '2008-09-29', 52215299, 'Nobis repellendus minima recus', 'West Tylerfort', 'Puerto Rico', '2015-08-10 00:20:02', '2016-04-08 19:50:51');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (71, 'm', '2006-09-26', 8985, 'Officia est corporis rem dolor', 'East Agustin', 'Kazakhstan', '2017-12-28 05:22:31', '2018-04-30 07:19:13');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (72, 'm', '2002-01-19', 356917, 'Repellat voluptas ut ipsa et q', 'Tremainefort', 'Cocos (Keeling) Islands', '2011-11-06 06:31:06', '2020-05-22 01:29:31');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (73, 'f', '2006-01-17', 9716136, 'Eos ipsa culpa tempore animi v', 'South Christaview', 'Botswana', '2011-12-29 07:30:28', '2013-01-20 15:43:58');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (74, 'f', '2008-07-30', 2683485, 'Quam consequatur omnis archite', 'New Tessie', 'Iraq', '2012-07-31 12:27:22', '2010-11-17 09:17:36');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (75, 'm', '2007-04-28', 6518860, 'Quas in est eos aliquam corrup', 'Douglasport', 'Isle of Man', '2015-10-30 19:38:33', '2017-05-29 15:02:09');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (76, 'm', '2017-06-27', 24, 'Sunt accusantium quae providen', 'Lake Rodrigo', 'Tokelau', '2013-01-07 08:31:46', '2012-09-26 12:05:19');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (77, 'm', '1998-09-23', 577991, 'Sit non ullam quaerat consequa', 'Sinceretown', 'Pakistan', '2019-12-11 19:30:17', '2015-10-25 03:23:32');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (78, 'm', '2001-08-26', 9527942, 'Dolor magni cupiditate et amet', 'East Ocie', 'Isle of Man', '2019-08-09 04:59:46', '2016-10-22 13:35:07');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (79, 'f', '1988-02-03', 278, 'Possimus dolores magnam molest', 'Thompsonfort', 'Bosnia and Herzegovina', '2016-03-19 22:07:02', '2016-02-04 10:53:33');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (80, 'f', '1996-11-21', 82064, 'Et consequatur non ea pariatur', 'New Kevon', 'New Zealand', '2018-11-13 05:20:26', '2018-11-11 08:16:03');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (81, 'm', '1991-07-29', 44, 'Aut ut officiis ex quisquam. S', 'North Brendon', 'Bangladesh', '2018-11-27 03:20:17', '2017-06-30 06:06:33');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (82, 'f', '1972-05-23', 582642, 'Ea repellat amet quia tempora ', 'Granvillemouth', 'Taiwan', '2016-09-01 19:29:44', '2017-07-03 10:41:59');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (83, 'f', '1971-12-13', 43, 'Dolore culpa ut qui omnis labo', 'South Alethachester', 'Poland', '2014-06-07 17:26:26', '2020-02-05 04:31:45');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (84, 'f', '2018-12-07', 604, 'Minima qui deleniti repellat u', 'East Simonestad', 'Barbados', '2017-03-31 13:34:57', '2017-07-04 02:06:11');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (85, 'f', '2019-02-23', 91, 'Est quia ipsa dignissimos ea. ', 'North Frederiqueside', 'Austria', '2020-02-16 02:03:24', '2017-01-23 14:20:53');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (86, 'm', '2015-03-05', 78, 'Nihil deleniti aut expedita qu', 'Ziemeland', 'Kiribati', '2019-12-15 11:06:46', '2015-10-13 07:10:29');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (87, 'm', '2016-06-05', 35756, 'Est corporis quia quisquam iur', 'West Asa', 'Belgium', '2016-09-09 14:06:06', '2011-12-19 10:03:39');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (88, 'm', '2004-02-27', 850826470, 'Qui hic est quaerat cumque nih', 'Lillaton', 'Tunisia', '2016-05-22 09:11:31', '2013-07-08 01:27:46');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (89, 'f', '2009-05-25', 85372871, 'Non distinctio consequuntur au', 'Berniefort', 'Bulgaria', '2018-06-24 04:58:19', '2015-08-13 07:07:51');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (90, 'f', '2017-09-10', 623394, 'Dolore qui suscipit voluptatib', 'Dietrichstad', 'Lebanon', '2016-07-17 14:10:55', '2012-01-17 12:07:10');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (91, 'm', '2000-04-13', 2153084, 'Quis quidem error explicabo do', 'Port Pattie', 'China', '2019-04-27 07:59:52', '2016-03-21 07:01:01');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (92, 'f', '2015-12-19', 11, 'Non quos id facere in. Minima ', 'Port Marcia', 'Saint Kitts and Nevis', '2012-03-30 10:41:52', '2019-02-12 20:04:38');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (93, 'f', '2005-06-02', 142, 'Ab provident vel accusantium r', 'Hellerfurt', 'Azerbaijan', '2017-06-04 02:00:57', '2020-03-23 06:01:36');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (94, 'f', '2001-03-27', 645, 'Quia et provident hic animi eu', 'Luettgenberg', 'Malaysia', '2014-05-21 09:19:02', '2014-02-15 15:02:51');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (95, 'm', '1984-06-09', 5500675, 'Voluptatem qui reiciendis qui ', 'Eldoramouth', 'British Indian Ocean Territory (Chagos Archipelago)', '2020-03-22 03:42:51', '2013-12-19 22:08:50');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (96, 'm', '1979-07-15', 28181469, 'Neque quis quia rem voluptas s', 'West Ariane', 'Svalbard & Jan Mayen Islands', '2015-06-21 15:56:16', '2011-09-23 01:06:07');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (97, 'm', '2010-06-22', 4341, 'Facere minima fugit impedit at', 'Lake Winfield', 'Holy See (Vatican City State)', '2020-03-13 16:35:58', '2013-07-03 09:42:39');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (98, 'm', '1978-09-17', 703244, 'Illo quasi omnis id iusto ipsu', 'New Mohammad', 'Chad', '2013-02-15 16:58:12', '2020-03-28 12:13:08');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (99, 'm', '1994-11-08', 51, 'Tenetur est earum corporis con', 'Antoniomouth', 'Belarus', '2017-03-01 23:52:52', '2016-06-24 17:28:21');
INSERT INTO `profiles` (`user_id`, `gender`, `birthday`, `photo_id`, `status`, `city`, `country`, `created_at`, `updated_at`) VALUES (100, 'm', '1971-06-21', 7560600, 'Enim consequatur quos modi aut', 'Kristyton', 'Faroe Islands', '2016-07-02 17:45:35', '2016-05-03 19:11:52');


#
# TABLE STRUCTURE FOR: users
#

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT COMMENT 'Идентификатор строки',
  `first_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Имя пользователя',
  `last_name` varchar(100) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Фамилия пользователя',
  `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Почта',
  `phone` varchar(100) COLLATE utf8_unicode_ci NOT NULL COMMENT 'Телефон',
  `created_at` datetime DEFAULT current_timestamp() COMMENT 'Время создания строки',
  `updated_at` datetime DEFAULT current_timestamp() ON UPDATE current_timestamp() COMMENT 'Время обновления строки',
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `phone` (`phone`)
) ENGINE=InnoDB AUTO_INCREMENT=101 DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Пользователи';

INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (1, 'Clementine', 'Medhurst', 'jones.cristian@example.com', '606-638-7032x980', '2013-08-31 10:57:30', '2013-05-05 10:05:40');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (2, 'Guadalupe', 'Kub', 'ccummerata@example.net', '518.855.8478', '2011-09-18 18:03:09', '2020-02-25 05:38:42');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (3, 'Jerrold', 'Mosciski', 'amanda04@example.net', '520.415.4029', '2010-10-28 20:40:52', '2020-08-17 12:41:53');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (4, 'Berniece', 'Cole', 'glover.gunnar@example.com', '(635)180-0759x1490', '2017-04-12 08:44:37', '2017-10-24 23:28:35');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (5, 'Johnny', 'Dibbert', 'wsenger@example.net', '00652194832', '2017-10-25 10:01:01', '2016-11-07 12:07:43');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (6, 'Amalia', 'Rogahn', 'nat94@example.net', '1-729-262-3834', '2012-01-09 11:34:31', '2019-01-15 23:20:45');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (7, 'Hudson', 'Legros', 'farrell.tillman@example.org', '420.954.8103x00997', '2018-06-26 00:05:50', '2011-01-02 09:16:47');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (8, 'Juliet', 'Thompson', 'addison.howe@example.net', '(023)983-8458x475', '2015-08-19 04:53:26', '2014-07-21 13:25:15');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (9, 'Harrison', 'Davis', 'meda27@example.org', '1-742-421-4176x3355', '2013-03-02 17:11:54', '2011-06-02 22:55:34');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (10, 'Jules', 'Haley', 'uhaley@example.net', '1-511-144-3694', '2018-04-16 18:07:34', '2014-08-23 12:07:07');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (11, 'Cristina', 'Torp', 'ngutkowski@example.com', '+66(0)9024294659', '2012-11-22 18:46:45', '2015-10-01 12:33:14');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (12, 'Bryon', 'Gerhold', 'harvey.sylvester@example.com', '1-025-888-8519x7441', '2017-06-07 13:39:17', '2016-09-05 18:07:30');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (13, 'Quincy', 'Terry', 'raynor.arnulfo@example.org', '+53(2)3146542622', '2013-04-16 18:59:40', '2019-12-08 22:15:32');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (14, 'Thelma', 'Beahan', 'wyman.marguerite@example.org', '(615)138-6894x29125', '2011-08-17 04:18:51', '2016-06-29 03:58:57');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (15, 'Jacynthe', 'Schowalter', 'elvie.friesen@example.net', '249.574.6071x68028', '2019-09-28 09:45:41', '2015-02-09 11:05:35');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (16, 'Karson', 'Bashirian', 'volkman.natalie@example.org', '013.931.0971x9341', '2019-10-09 06:36:47', '2014-12-09 02:10:38');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (17, 'Carolina', 'Hauck', 'hpagac@example.com', '08085761551', '2019-08-26 11:40:30', '2013-09-08 09:23:55');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (18, 'Taurean', 'Dach', 'graham.shad@example.net', '756-020-1699', '2018-10-05 03:07:57', '2018-12-17 06:36:25');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (19, 'Marlen', 'Hickle', 'blanda.keyshawn@example.net', '(977)434-7082', '2015-02-22 22:53:01', '2011-10-23 19:15:46');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (20, 'Lulu', 'Hilll', 'swillms@example.net', '468.443.1690', '2014-06-16 02:34:12', '2010-11-14 13:00:30');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (21, 'Luigi', 'Bartoletti', 'sammie.bernier@example.org', '+79(9)7248476861', '2012-04-22 14:57:53', '2020-05-09 22:32:38');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (22, 'Dagmar', 'Haley', 'wmueller@example.org', '1-564-015-6179x022', '2014-07-20 08:49:23', '2020-05-16 07:21:09');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (23, 'Gladyce', 'Lakin', 'bogan.agnes@example.org', '228-159-4680x814', '2019-09-07 05:19:15', '2011-10-20 02:00:29');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (24, 'Luz', 'Morar', 'buckridge.trent@example.com', '506-778-5259x58763', '2014-11-01 01:39:30', '2018-12-16 19:06:34');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (25, 'Edwin', 'Reilly', 'zconn@example.org', '829-657-6804', '2018-02-16 04:39:00', '2010-10-06 20:58:10');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (26, 'Broderick', 'Cormier', 'nakia.jenkins@example.net', '335-462-0196x850', '2014-10-31 07:16:05', '2015-12-04 05:40:10');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (27, 'Arnold', 'Hoppe', 'hagenes.lina@example.net', '1-243-638-2583', '2011-11-06 17:40:21', '2011-05-18 22:23:09');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (28, 'Nikolas', 'Kulas', 'jace.casper@example.org', '263.828.3714x94026', '2016-02-08 19:24:42', '2019-06-19 16:29:07');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (29, 'Bartholome', 'Reichel', 'bessie.hudson@example.org', '(900)045-2826', '2017-09-10 19:43:53', '2018-08-11 22:14:32');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (30, 'Carroll', 'Oberbrunner', 'nadia.homenick@example.net', '965-486-5889x90451', '2020-03-07 01:54:36', '2017-12-19 07:46:29');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (31, 'Wilton', 'Douglas', 'roderick06@example.org', '281-512-6691x7401', '2015-08-17 21:51:06', '2015-02-02 06:27:42');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (32, 'Tabitha', 'Nitzsche', 'bgibson@example.org', '(727)491-3009x1162', '2016-04-27 16:44:39', '2018-09-07 21:35:47');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (33, 'Lisette', 'Ernser', 'gfeeney@example.net', '450.032.7516x3860', '2014-05-09 20:55:34', '2013-03-28 06:49:31');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (34, 'Reyna', 'Mayer', 'hansen.dakota@example.com', '043.135.5169', '2011-12-07 00:11:54', '2016-02-04 12:44:35');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (35, 'Meghan', 'Hirthe', 'lemke.braeden@example.net', '942.219.1791x47835', '2018-06-01 05:56:05', '2018-07-04 03:05:13');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (36, 'Kylee', 'Sanford', 'ho\'connell@example.com', '693.114.3106x02370', '2014-08-27 15:21:56', '2019-08-15 03:41:01');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (37, 'Estelle', 'Nolan', 'iarmstrong@example.org', '06793581454', '2016-02-20 00:46:39', '2011-05-11 08:11:43');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (38, 'Lolita', 'Prohaska', 'danial.hessel@example.net', '+58(6)4796623421', '2011-10-04 09:36:19', '2018-03-23 01:51:53');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (39, 'Josiane', 'Heller', 'mathew.doyle@example.com', '07031599948', '2016-08-16 13:32:09', '2013-01-06 12:22:50');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (40, 'Gordon', 'Stamm', 'qrosenbaum@example.org', '095.801.3586', '2010-09-21 06:52:53', '2014-10-28 04:56:46');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (41, 'Annie', 'Wiza', 'ricardo86@example.com', '(719)630-0812x77338', '2020-02-23 11:36:25', '2010-10-30 12:41:22');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (42, 'Maximillia', 'Osinski', 'toy.abby@example.org', '1-959-708-7919', '2013-07-31 02:04:37', '2016-07-06 05:09:14');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (43, 'Hulda', 'Heller', 'bergstrom.giovanni@example.org', '588.358.0982x60928', '2020-08-09 07:20:48', '2015-09-18 16:42:33');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (44, 'Cullen', 'Heaney', 'katelin.hudson@example.com', '703-031-1135', '2017-01-15 14:26:18', '2012-07-06 10:01:51');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (45, 'Mathilde', 'McCullough', 'edward02@example.com', '960-463-5263', '2018-10-29 07:22:05', '2016-08-08 21:01:40');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (46, 'Roxane', 'Kuhn', 'shania00@example.com', '054-214-1577x937', '2017-08-02 20:58:35', '2016-01-04 16:22:56');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (47, 'Dock', 'O\'Hara', 'dean.gleason@example.net', '00479031909', '2016-04-22 07:18:20', '2019-06-08 23:53:13');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (48, 'Noelia', 'Stark', 'huels.daniella@example.net', '(977)680-2284x294', '2011-12-24 13:33:28', '2016-03-02 04:48:48');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (49, 'Neil', 'Cassin', 'virginia33@example.net', '(342)039-9697x644', '2016-06-06 17:57:20', '2015-01-04 14:06:58');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (50, 'Soledad', 'Wisozk', 'jaunita.wuckert@example.com', '513-493-2509x315', '2011-01-09 06:57:27', '2018-10-04 02:32:48');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (51, 'Pansy', 'Wilderman', 'fisher.kaci@example.net', '1-328-614-7474', '2017-04-29 12:27:40', '2014-12-24 22:28:24');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (52, 'Dee', 'Hegmann', 'rupert.o\'keefe@example.org', '810-293-6166', '2011-09-12 05:23:33', '2020-07-21 20:27:41');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (53, 'Susan', 'Blick', 'anne64@example.com', '1-752-762-6265', '2012-12-18 03:03:04', '2018-01-08 17:06:29');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (54, 'Cory', 'Raynor', 'vjakubowski@example.org', '(382)218-1254x677', '2019-10-24 03:58:57', '2018-10-23 15:51:54');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (55, 'Mia', 'Robel', 'maud.zboncak@example.net', '+09(8)4395423847', '2013-02-26 21:43:37', '2016-04-27 10:20:47');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (56, 'Flossie', 'Kohler', 'eebert@example.com', '760-156-4107x376', '2011-01-21 07:45:39', '2017-09-22 07:17:23');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (57, 'Marisol', 'Ferry', 'pmohr@example.net', '633.943.7442x95791', '2015-06-18 11:49:47', '2014-01-14 09:52:06');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (58, 'Rudy', 'McLaughlin', 'anastasia.langworth@example.com', '564-376-2653x6473', '2011-03-12 10:06:30', '2019-01-23 23:58:12');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (59, 'Santino', 'Will', 'rozella24@example.com', '00102232523', '2020-05-15 09:52:38', '2013-05-04 20:03:07');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (60, 'Raymond', 'Schroeder', 'kirstin.morar@example.org', '952-269-8054', '2016-10-03 11:06:53', '2018-09-21 19:16:33');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (61, 'Marcos', 'D\'Amore', 'cordie92@example.org', '753-543-9384', '2012-01-04 15:37:55', '2018-07-20 03:06:47');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (62, 'Earnest', 'Schoen', 'aaron.fay@example.com', '(393)568-2521', '2019-09-24 13:19:38', '2017-09-02 23:48:35');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (63, 'Orlando', 'Parisian', 'dblick@example.net', '1-129-730-0123x58391', '2015-12-16 12:59:13', '2014-06-03 03:53:05');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (64, 'Nedra', 'Wiegand', 'columbus.thompson@example.org', '107-399-1124x122', '2018-12-28 16:47:09', '2019-06-16 09:21:08');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (65, 'Lorine', 'Bruen', 'prosenbaum@example.com', '788-904-4760x7324', '2019-06-22 09:57:49', '2016-03-19 05:39:19');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (66, 'Isidro', 'Hegmann', 'shields.percival@example.org', '942.935.1937', '2020-06-22 16:07:33', '2012-11-22 18:26:34');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (67, 'Sheila', 'Schuster', 'candelario03@example.com', '002-368-6213', '2016-10-04 12:05:35', '2016-03-16 01:28:02');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (68, 'Shawna', 'Kovacek', 'zwitting@example.net', '780.971.8757x29562', '2015-06-21 06:45:15', '2018-04-28 04:12:32');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (69, 'Destany', 'Jacobson', 'deangelo.hackett@example.com', '803-180-7717', '2010-10-09 07:46:56', '2018-05-11 09:02:48');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (70, 'Kellen', 'Johnson', 'hvon@example.org', '(732)848-2254x929', '2017-07-18 01:34:38', '2015-08-21 06:26:08');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (71, 'Ressie', 'Boehm', 'weston.harvey@example.com', '633-877-8614x4737', '2014-03-23 22:57:11', '2012-03-08 08:37:18');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (72, 'Winston', 'Bruen', 'tjenkins@example.net', '1-605-007-2185x512', '2013-06-05 06:56:57', '2018-07-13 11:07:59');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (73, 'Karlee', 'Oberbrunner', 'ipadberg@example.org', '315-039-7955', '2011-05-02 03:38:08', '2012-11-18 04:29:03');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (74, 'Payton', 'Jakubowski', 'donnell74@example.org', '904.909.8648x8988', '2010-09-29 15:43:40', '2015-09-16 07:26:46');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (75, 'Noemy', 'Price', 'harvey.dagmar@example.com', '(713)280-9661x15443', '2018-05-29 21:49:51', '2016-12-17 07:11:45');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (76, 'Reese', 'Wintheiser', 'joy40@example.net', '978-951-3774x992', '2015-07-08 16:24:21', '2015-07-30 01:50:22');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (77, 'Loren', 'Bahringer', 'pwisozk@example.com', '1-752-367-2920x135', '2014-05-25 08:41:41', '2013-12-28 09:53:40');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (78, 'Alayna', 'Weimann', 'lsteuber@example.org', '632.294.4627', '2013-02-12 22:28:05', '2015-02-10 20:25:24');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (79, 'Mervin', 'Boehm', 'larson.jeffrey@example.org', '(784)564-0937x824', '2016-02-19 22:05:22', '2019-01-11 14:22:09');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (80, 'Reid', 'Walter', 'monte.miller@example.org', '+30(8)1496448450', '2018-02-13 09:11:07', '2018-03-07 05:29:40');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (81, 'Joesph', 'Braun', 'waters.nicholas@example.org', '(980)272-5361', '2019-04-18 05:33:28', '2012-08-19 21:12:36');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (82, 'Lorenzo', 'Medhurst', 'hillary46@example.net', '1-025-495-0794x7110', '2016-02-06 08:09:39', '2019-03-23 10:13:10');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (83, 'Ahmad', 'Hudson', 'morton98@example.com', '(660)201-6442', '2013-09-04 13:42:12', '2013-03-14 22:49:06');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (84, 'Adeline', 'Keeling', 'kimberly20@example.org', '(560)895-4628x9468', '2014-11-06 09:08:24', '2013-10-09 06:34:21');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (85, 'Luther', 'Hoppe', 'creola.turcotte@example.com', '497-522-2323x596', '2013-07-08 18:36:32', '2019-07-05 10:36:19');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (86, 'Dolly', 'Crona', 'eliza.turner@example.net', '200.134.1760x965', '2014-08-23 00:25:03', '2011-06-24 00:10:36');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (87, 'Juliet', 'Morar', 'jast.jalon@example.com', '06572847640', '2018-05-22 23:22:03', '2011-08-03 06:18:27');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (88, 'Eliseo', 'Jacobi', 'rosalinda81@example.com', '316-650-9983x9463', '2011-05-13 05:44:19', '2014-12-16 08:52:59');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (89, 'Coy', 'Fadel', 'jdoyle@example.net', '648-171-9701', '2014-05-22 03:51:26', '2010-10-21 00:29:49');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (90, 'Gaetano', 'Mayert', 'percy41@example.org', '(698)623-1577', '2019-05-14 23:27:31', '2014-05-27 22:00:00');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (91, 'Curtis', 'Block', 'jacobs.damian@example.net', '070-108-2457x18654', '2011-04-22 04:20:13', '2017-10-09 20:19:50');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (92, 'Zane', 'Schiller', 'cortney58@example.com', '1-610-484-9481x06489', '2017-04-14 00:50:34', '2014-06-06 06:32:12');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (93, 'Sasha', 'Smith', 'xlang@example.com', '088.168.9639', '2018-01-25 09:07:36', '2010-10-09 09:03:06');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (94, 'Maymie', 'Schneider', 'bergnaum.kaylah@example.net', '426.945.9974x33264', '2020-02-13 21:56:59', '2020-09-05 14:49:43');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (95, 'Annabell', 'King', 'alexane.feeney@example.net', '(753)606-6532', '2016-04-11 06:08:09', '2010-10-16 01:56:44');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (96, 'Janie', 'Steuber', 'haylee32@example.org', '105-284-0904x048', '2017-03-29 14:50:27', '2019-12-24 20:22:11');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (97, 'Arnold', 'Cronin', 'davion05@example.org', '(426)516-0645x644', '2013-10-19 17:40:43', '2017-11-21 09:51:57');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (98, 'Desmond', 'Gorczany', 'alexis07@example.org', '+75(0)8948762520', '2014-09-07 05:05:43', '2011-11-02 13:59:58');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (99, 'Roy', 'Lowe', 'jaylan19@example.com', '+36(5)1170191032', '2014-03-02 13:26:26', '2019-07-27 12:49:36');
INSERT INTO `users` (`id`, `first_name`, `last_name`, `email`, `phone`, `created_at`, `updated_at`) VALUES (100, 'Robyn', 'McCullough', 'alene.schroeder@example.com', '154-455-2201x6857', '2017-06-06 17:12:15', '2019-07-19 06:47:06');


