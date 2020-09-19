DROP TABLE IF EXISTS likes;
CREATE TABLE likes (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  target_id INT UNSIGNED NOT NULL,
  target_type_id INT UNSIGNED NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

DROP TABLE IF EXISTS target_types;
CREATE TABLE target_types (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL UNIQUE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO target_types (name) VALUES
  ('messages'),
  ('users'),
  ('media'),
  ('posts');
  
 INSERT INTO likes
  SELECT
    id,
    FLOOR(1 + (RAND() * 100)),
    FLOOR(1 + (RAND() * 100)),
    FLOOR(1 + (RAND() * 4)),
    CURRENT_TIMESTAMP
  FROM messages;
  
 SELECT * FROM likes LIMIT 10;

CREATE TABLE posts (
  id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  user_id INT UNSIGNED NOT NULL,
  community_id INT UNSIGNED,
  head VARCHAR(255),
  body TEXT NOT NULL,
  media_id INT UNSIGNED,
  is_public BOOLEAN DEFAULT TRUE,
  is_archived BOOLEAN DEFAULT FALSE,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (1, 83, 59, 'Quia sit ipsa sed excepturi accusantium dolorem dolores dolore.', 'Nisi ullam vel tempore maxime in quo fugiat aut. Sit consectetur veritatis consequuntur quia cumque quia et ad. Eveniet doloremque fugiat dolores saepe provident. Dolore reprehenderit repellat dignissimos nulla.', 72, 1, 1, '2020-07-26 09:26:02', '2013-05-29 14:02:16');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (2, 20, 81, 'Sed consequuntur quae et porro quia sed magni.', 'Vel voluptas autem tenetur dolorem. Velit rerum libero voluptatibus qui quis ut dolorem. Accusamus rerum a in error facilis. Veniam earum soluta qui quae quis.', 74, 0, 0, '2014-05-04 21:02:05', '2011-05-11 03:28:08');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (3, 39, 92, 'Et molestiae aut alias doloribus.', 'Aut et assumenda velit minima. Eum quos est dicta et eum eos quia ex. Soluta vel tempora et quam. Nostrum quo iure natus est unde.', 3, 1, 0, '2017-05-17 20:47:40', '2016-07-11 20:09:17');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (4, 70, 14, 'Et maxime architecto molestiae velit dolores consequatur.', 'Rem atque itaque quas numquam sint et quia saepe. Voluptatem ipsam non et recusandae et nihil. Fugit itaque sint dignissimos omnis libero.', 44, 0, 1, '2012-05-06 19:45:55', '2015-01-26 22:42:00');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (5, 44, 76, 'Minima blanditiis voluptatem nemo adipisci placeat saepe.', 'At et quae corporis sequi nihil voluptatem voluptatem. Officia nostrum facilis delectus voluptate voluptas ipsum aspernatur. Rem nemo natus rerum illo accusamus quo omnis mollitia. Qui non aut tempora cupiditate.', 95, 0, 1, '2014-12-26 19:24:10', '2015-05-22 13:51:32');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (6, 47, 76, 'Et eveniet labore harum eos voluptas voluptas error.', 'Assumenda possimus id quae at voluptates. Quis laudantium dolores distinctio ipsam quaerat consequuntur. Aut sed vitae omnis id.', 53, 0, 1, '2013-06-18 06:53:13', '2013-10-18 16:34:09');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (7, 90, 64, 'Error alias tenetur qui iusto aut sunt similique.', 'Facere officia at repellendus est adipisci consequuntur eum. Ipsum iusto provident non est dolorem. Voluptatem autem ut ut non iste eum velit repellendus.', 8, 0, 0, '2018-03-04 21:46:56', '2014-10-20 02:27:23');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (8, 85, 38, 'Minus sunt deleniti in quaerat corrupti at et.', 'Quo aut velit consequatur aut id. Et in et tempore aspernatur earum. Autem nihil ea quaerat qui sed cumque quis. Et voluptatum eveniet et dolores quis consequatur.', 24, 1, 0, '2011-09-17 05:26:59', '2018-10-27 02:24:16');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (9, 81, 28, 'Quidem sed eum non enim libero et.', 'Explicabo cumque eum aut nostrum excepturi unde consequatur. Dicta sit fugit nam rerum. Voluptatum consequuntur repellendus ut voluptate recusandae.', 35, 1, 0, '2020-03-10 08:52:20', '2013-03-15 05:53:23');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (10, 63, 98, 'Illo aut suscipit nulla.', 'Dolorum exercitationem illum temporibus nulla excepturi. Quia eum fugit inventore voluptas culpa. Facere dicta occaecati rem iste. Voluptatibus et deserunt non.', 44, 1, 0, '2013-01-31 13:28:39', '2016-06-08 04:20:53');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (11, 60, 51, 'Ex qui odio nam autem.', 'Odit quia sed incidunt. Dolor cum in aliquid nostrum. Et placeat beatae id in vel. Enim quos eius quas dolor nesciunt voluptatem rerum.', 7, 0, 1, '2019-09-20 04:30:46', '2020-03-02 01:34:00');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (12, 78, 56, 'Dolore explicabo aut sunt dolores.', 'Doloribus omnis tempora non labore est dolore id. Molestiae est dolorem nisi ad. Quis aperiam iusto placeat quia eos.', 43, 0, 1, '2019-05-10 10:31:29', '2019-11-30 22:43:01');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (13, 63, 88, 'Saepe enim explicabo eos sapiente nesciunt debitis voluptate.', 'Consectetur animi vel assumenda nam. Sit natus cumque ducimus quis voluptas necessitatibus. Quas commodi pariatur distinctio est in commodi. Aliquid veniam atque doloremque rerum voluptatem et.', 53, 0, 1, '2014-06-02 10:45:14', '2016-07-28 22:49:03');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (14, 1, 54, 'Voluptatem libero et neque aut perspiciatis.', 'Voluptatum aut laudantium consequuntur rem et facere. Ad incidunt doloremque fugiat quas sit expedita earum.', 81, 1, 1, '2017-09-16 04:46:31', '2013-12-16 01:51:50');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (15, 97, 68, 'Pariatur rerum accusantium ipsam optio aut provident.', 'Voluptas sunt veniam rerum molestiae. Eos quia molestiae tempore sed. Maxime illo illum et et dolore. Est non nulla provident.', 58, 1, 1, '2011-02-19 01:56:48', '2018-10-05 18:38:31');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (16, 90, 81, 'Vel recusandae et pariatur eaque.', 'Occaecati saepe earum repellendus accusantium sed consequuntur. Eos dolor consectetur aut dolor sint. Quia eveniet ut maxime officiis quia. Et ut incidunt neque excepturi.', 17, 0, 0, '2014-01-24 01:23:57', '2014-02-24 13:26:48');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (17, 49, 39, 'Et nesciunt error aut vel eos quia aperiam.', 'Debitis voluptas ea doloribus sit omnis. Dolor et doloremque quam aliquam enim ea id. Labore dolorum facilis optio eligendi dolores aut.', 32, 1, 0, '2018-12-12 04:32:04', '2018-04-02 07:08:04');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (18, 61, 60, 'Eos culpa repellendus eaque natus omnis.', 'Consequatur rem ratione et dolores. Quo ea voluptas aliquam aut aliquam. Molestiae hic voluptas id necessitatibus et quod pariatur veritatis.', 14, 1, 0, '2020-04-27 18:39:35', '2017-01-19 09:13:02');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (19, 33, 10, 'Sunt at quaerat ea sit esse veritatis.', 'Vero numquam maxime consequuntur dolor. Aperiam est occaecati sed voluptate non.', 49, 1, 1, '2018-11-12 01:33:16', '2018-06-15 05:27:58');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (20, 10, 35, 'Ea illum corporis consequuntur.', 'Veritatis id quo incidunt est sunt ut. Consequatur laboriosam eum velit rerum voluptate quisquam. Consequuntur voluptatem nisi consequatur. Fugiat dolorum deserunt reprehenderit ut qui maiores.', 36, 0, 1, '2017-11-18 08:30:20', '2011-11-17 11:51:22');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (21, 19, 5, 'Ipsum blanditiis dolorum nisi in ab earum.', 'Eos eum laboriosam ea minima tenetur expedita nulla quia. Non quis esse facere omnis quia. Est voluptate adipisci ab qui quia. Quisquam qui repellat assumenda asperiores ipsum. Facilis aut iusto ut.', 85, 1, 1, '2016-01-26 03:55:01', '2020-05-01 12:46:15');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (22, 90, 80, 'Placeat sed quas quaerat impedit est.', 'Voluptatem perferendis et qui consequatur provident. Quisquam eligendi voluptas voluptas nihil voluptates sint numquam et.', 40, 0, 1, '2015-12-30 13:21:45', '2012-02-22 05:05:25');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (23, 54, 77, 'Quia voluptates cupiditate perferendis aliquam.', 'Quidem quidem quidem optio mollitia voluptatem qui. Molestiae tempore quod similique aut veniam earum corrupti. Quis aut ex ad temporibus non vel facere. Assumenda minus impedit magni voluptate aliquam quidem assumenda.', 83, 0, 0, '2018-01-06 14:31:02', '2012-06-14 01:52:37');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (24, 85, 1, 'Debitis dolorum ut et recusandae sequi.', 'Natus consectetur earum perspiciatis aliquid. Neque enim rerum porro repudiandae. Autem asperiores eius quis ratione ex.', 36, 1, 1, '2017-05-27 02:06:02', '2015-07-17 07:59:14');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (25, 88, 82, 'Nulla fugiat tempora provident quo vero.', 'Dolorem corrupti voluptas dolorem beatae vel ab. Eius et quibusdam modi saepe. Tempore rerum consectetur suscipit eveniet eveniet ut sed.', 90, 0, 0, '2012-07-27 13:06:50', '2013-04-10 18:48:23');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (26, 44, 98, 'A mollitia libero rem quo.', 'Assumenda eum pariatur sequi amet assumenda. Inventore tempora blanditiis tempora esse ratione ab voluptatem ipsa. Et reiciendis placeat nihil magni.', 14, 0, 0, '2017-05-16 02:44:13', '2017-04-04 19:14:38');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (27, 7, 53, 'Quia porro non ex minus reprehenderit fugiat et.', 'Quaerat non optio minima alias a aliquid asperiores deleniti. Libero totam vitae aut at. Sapiente nemo iusto itaque aut qui provident. Sunt quibusdam id in et aut sed. Dolore explicabo magnam nulla alias exercitationem est illum qui.', 92, 1, 0, '2011-08-11 21:50:44', '2017-03-12 17:54:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (28, 81, 77, 'Nam voluptates libero est ipsum adipisci quasi iusto voluptatem.', 'Voluptatibus eos quas eius inventore nobis. Consequuntur sit consequuntur repellendus vel dolores magnam. Eaque voluptatem libero quod rerum facilis expedita maxime.', 49, 1, 0, '2016-02-17 15:47:19', '2016-09-24 00:39:31');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (29, 40, 47, 'Aut ratione omnis rerum quia eligendi.', 'Cum sunt iste dolorem consectetur. Illo neque autem inventore et iure magnam facilis. Dolore voluptas incidunt rerum provident ipsum deserunt eveniet.', 48, 0, 0, '2015-11-17 13:20:04', '2016-07-25 16:53:43');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (30, 2, 74, 'At aut sunt tempore et id fuga quibusdam.', 'Dicta iure corporis praesentium voluptas dolores corrupti eaque. Quidem ullam expedita esse eveniet rerum aperiam asperiores. Est similique officiis consequuntur assumenda et. Expedita repellat omnis ut ab.', 5, 0, 1, '2020-06-14 02:31:59', '2013-07-21 05:19:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (31, 34, 92, 'Cumque fugiat sint facilis nostrum aut accusantium.', 'Et maiores facilis vel est est. Ut odio est omnis. Quis consequuntur ratione animi in nobis. Quis aut qui nemo aut.', 99, 1, 0, '2015-03-22 08:55:55', '2017-10-30 10:02:04');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (32, 75, 7, 'Qui excepturi fugiat perspiciatis vitae.', 'Impedit veritatis voluptatem officia nobis. Ad quam temporibus ad praesentium reiciendis expedita. Molestiae incidunt corporis odit beatae fugit et. Ut quia et culpa voluptate fugiat quos.', 19, 1, 0, '2019-03-24 01:24:24', '2013-10-08 05:45:31');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (33, 29, 66, 'Aliquid est doloribus est est ipsum nobis dolorem.', 'Et aliquam eligendi maiores harum deserunt. Minus aut nihil ipsum natus occaecati ipsam eos. Nesciunt aut perferendis eveniet ab inventore odio vero reprehenderit. Impedit est excepturi corrupti architecto.', 73, 1, 0, '2014-12-26 18:13:27', '2015-07-04 00:59:25');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (34, 27, 30, 'Nisi accusamus vero nobis nemo.', 'Corporis accusantium hic commodi autem. Soluta maiores possimus libero maxime minima. Molestiae deserunt autem cum voluptatem et illum.', 72, 0, 0, '2012-09-26 18:17:07', '2015-06-18 04:32:57');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (35, 31, 36, 'Et incidunt sapiente hic aut adipisci aut.', 'Quo quas qui ut consectetur nihil. Omnis atque veritatis qui error deleniti ducimus. Soluta consectetur nihil quo adipisci aperiam repellat sint. Quos ipsum deleniti est consequuntur hic nemo consequatur.', 84, 1, 1, '2020-05-06 04:39:34', '2017-01-08 01:45:56');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (36, 13, 85, 'Suscipit qui mollitia itaque nihil et.', 'Porro et aut sunt voluptates eaque. Facere pariatur laudantium delectus voluptas. Corporis molestiae pariatur voluptatem sint. Commodi quis sapiente illum error quo est.', 26, 1, 1, '2013-11-07 00:43:40', '2019-07-14 06:15:28');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (37, 31, 28, 'Et sequi fuga est architecto sint tempore quaerat.', 'Laboriosam voluptatem perferendis est quia. Accusamus porro voluptas placeat alias. Saepe modi doloribus reiciendis adipisci quo iure.', 23, 0, 0, '2014-04-03 06:08:29', '2017-03-23 14:55:32');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (38, 54, 99, 'Sapiente maiores molestiae quisquam aliquid eveniet natus enim.', 'Tempore qui consequatur commodi quos quo voluptates eveniet. Quis cumque aliquam aliquid accusantium enim et est perferendis. Minima ducimus et perspiciatis et excepturi. Eius voluptatem vel consequatur quis ipsum quibusdam.', 91, 1, 0, '2019-04-16 10:38:08', '2013-03-03 17:30:43');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (39, 56, 49, 'Facere et molestiae qui sit.', 'Sed mollitia nam est id quidem consectetur harum. Autem quia nobis quas laboriosam iste. Suscipit corrupti maxime sit dicta aut natus. Libero ut et sit.', 24, 0, 1, '2013-11-11 06:34:58', '2017-04-02 03:43:16');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (40, 51, 39, 'Excepturi perferendis et possimus repellat quis mollitia.', 'Dolores amet tempore velit aut sit perspiciatis nam. Quis voluptatem vel dolor dolorem iusto vel soluta. Id ex quod quisquam. Non tempore quia vel et.', 55, 1, 1, '2020-02-29 09:51:09', '2013-05-15 21:56:12');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (41, 35, 38, 'Non qui minima minus maiores molestiae cupiditate.', 'Et dolores qui et deleniti in velit. Autem provident culpa enim et ab a consequatur. Voluptatem ex enim minima commodi et.', 93, 0, 0, '2018-04-17 07:38:53', '2011-05-25 17:29:51');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (42, 88, 38, 'Accusamus amet et rerum quidem aut quo minus.', 'Tenetur molestias et ea id distinctio corrupti consectetur. Et qui vitae numquam enim non quibusdam in. Cum omnis voluptas et id explicabo ipsam.', 26, 1, 1, '2012-10-28 17:00:33', '2012-12-18 10:26:34');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (43, 86, 43, 'Ullam minus quam impedit harum velit quod.', 'Ullam omnis excepturi ullam veritatis quia. Sequi ipsum voluptas quis. Incidunt corrupti dolores voluptatem excepturi nostrum voluptatibus.', 53, 0, 1, '2017-11-11 03:32:06', '2016-07-25 20:13:52');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (44, 96, 72, 'Est consectetur dolor assumenda ducimus voluptatum labore doloremque.', 'Dignissimos optio iusto laudantium soluta. Et aut beatae nesciunt iure qui quasi modi. Facilis harum enim ad est laboriosam quia sapiente. Fuga error praesentium voluptatem ipsa doloremque.', 89, 0, 1, '2016-03-13 06:04:09', '2019-10-25 16:57:28');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (45, 31, 33, 'Sint quis optio assumenda culpa expedita numquam laborum.', 'Tempora explicabo eum ipsum eos aut consequatur atque aut. Velit deleniti fugit aperiam est exercitationem culpa ut delectus. Nulla nesciunt adipisci rem ducimus quibusdam cum molestiae.', 14, 1, 1, '2013-11-08 22:35:43', '2018-08-06 14:43:33');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (46, 68, 30, 'Neque eaque deserunt voluptatem nam explicabo facilis perspiciatis voluptatem.', 'Quas officia sed cumque sunt iste. Cupiditate est natus ut laborum dolores. Amet inventore molestiae iure dignissimos id accusamus.', 55, 0, 0, '2014-01-02 04:03:42', '2010-11-18 12:20:12');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (47, 52, 6, 'Quia quas eum libero vero.', 'Et est iure officia labore. Et voluptas dolores earum commodi. Sunt in quas et quo corporis voluptatem. Incidunt repellendus molestiae minus dolorum non ut.', 78, 0, 0, '2018-11-09 18:28:21', '2012-12-22 15:40:55');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (48, 99, 23, 'Maxime debitis molestiae rerum quia.', 'Quasi dolores dolorem dolores sapiente reiciendis. Nostrum ad fuga et nemo et. Eum magni occaecati sapiente autem. Quaerat et quas veniam quo quidem aut.', 34, 0, 1, '2012-09-28 17:30:50', '2013-02-18 17:29:25');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (49, 98, 82, 'Culpa omnis molestias nostrum et.', 'Nulla autem nihil voluptatem numquam enim ipsum quaerat. Eligendi consequuntur veritatis quo impedit cumque recusandae. Qui veniam enim voluptate est ut. Qui blanditiis et nam.', 92, 1, 1, '2016-02-07 20:49:15', '2020-06-27 18:28:06');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (50, 55, 27, 'Labore pariatur blanditiis nam est distinctio et laboriosam neque.', 'Eligendi repudiandae et inventore vero incidunt placeat. In atque aut eos consequatur non voluptatem et. Eos recusandae minima eum cupiditate et eum dolor aspernatur. Aut alias quia aut voluptatibus.', 57, 1, 1, '2019-12-19 20:50:07', '2016-10-16 10:36:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (51, 47, 50, 'Vel nihil repellat non aliquid quos ut.', 'Laborum qui unde sed inventore. Quibusdam rerum sit quis. Quidem unde quia dolor blanditiis. Sapiente ut unde quae et.', 81, 1, 1, '2017-04-20 07:13:29', '2017-05-27 17:49:14');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (52, 64, 41, 'Tempora repellat omnis et dolor.', 'Praesentium quisquam quos ut cum ipsam molestiae. Doloribus expedita repellat non voluptas quia iusto tenetur.', 85, 1, 1, '2013-12-28 08:43:38', '2014-05-12 22:11:22');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (53, 52, 69, 'Ipsam tempora eos numquam numquam.', 'Aspernatur impedit id cum magni dolores. Qui quidem optio ab ut. Voluptatem aut doloribus eum nihil.', 25, 0, 1, '2020-05-20 15:44:49', '2019-04-27 00:57:26');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (54, 84, 46, 'Et aut cumque ipsam non exercitationem voluptatem.', 'Consequatur cupiditate voluptatem qui saepe ab. Sit et qui a porro nihil aspernatur sunt. Deserunt consequatur id fugiat id sapiente fuga quia aut.', 89, 0, 0, '2017-06-07 13:20:58', '2017-12-10 13:35:37');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (55, 6, 31, 'Incidunt debitis et totam incidunt nam rem.', 'Voluptatum possimus omnis debitis rem eos. Dicta neque possimus ab iste quis minus ratione. Ipsa architecto quas nobis occaecati aut est exercitationem. Minus nulla nulla pariatur et mollitia tenetur iste.', 93, 0, 0, '2017-02-28 03:35:45', '2014-04-18 04:04:30');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (56, 98, 41, 'Necessitatibus dolorem blanditiis error est.', 'Unde ipsa facere ea expedita architecto illum nihil. Corrupti earum recusandae in. Quae aspernatur velit porro repellat.', 45, 0, 1, '2019-09-24 08:59:20', '2014-07-23 11:40:17');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (57, 79, 7, 'Nobis similique nemo reiciendis veniam nisi.', 'Dolorum laboriosam placeat cumque quis et error rem. Excepturi sed voluptates quia temporibus.', 8, 1, 1, '2016-01-04 07:41:46', '2019-10-27 00:27:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (58, 27, 68, 'Eos tempore eaque dolorum exercitationem repellendus aut.', 'Unde voluptatem occaecati eius dolores earum sit qui. Neque ut ut ratione qui mollitia est est. Nostrum molestias dolore porro voluptatem aut recusandae.', 23, 0, 0, '2011-10-30 21:50:50', '2012-09-30 06:22:01');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (59, 8, 73, 'Delectus nostrum in voluptas.', 'Officia incidunt nobis rerum est nisi sint architecto. Error numquam ut laudantium numquam. Sunt aut suscipit ratione ratione. Id non reiciendis perferendis velit temporibus.', 87, 0, 0, '2018-06-18 06:59:58', '2017-11-07 15:57:54');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (60, 27, 92, 'Veritatis suscipit non et dolor facilis libero.', 'Veniam voluptatibus quam nihil ex voluptatum. Pariatur est dicta explicabo asperiores est accusamus. Unde consequatur quibusdam quae sed. Omnis enim porro exercitationem vitae.', 41, 0, 1, '2016-05-04 12:41:41', '2019-10-20 08:56:50');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (61, 67, 42, 'Cumque aut enim sit adipisci et sint.', 'Temporibus in ut ullam at excepturi voluptas aliquam adipisci. Autem pariatur libero amet necessitatibus odit eligendi. Qui officiis velit iusto recusandae iure. Delectus cum vero non nihil ab sapiente.', 66, 0, 0, '2020-07-05 09:39:27', '2017-04-28 10:01:46');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (62, 13, 21, 'Ullam id consequatur voluptas illo accusamus et molestias.', 'Est sunt quos inventore voluptatem aut id modi. Itaque omnis quae quis ipsa ut tempora. Atque numquam quos modi est. Dolores consequuntur similique magnam quis eligendi molestias voluptatem.', 33, 1, 1, '2015-08-26 18:10:08', '2013-12-12 08:19:48');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (63, 52, 55, 'Rerum libero fugiat et et laboriosam harum.', 'Dolorum sit quo molestiae nihil aut. Totam quidem dolor excepturi blanditiis nihil corporis deleniti temporibus. Laborum aspernatur temporibus harum.', 88, 0, 1, '2017-05-31 19:05:00', '2015-07-07 10:14:55');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (64, 1, 25, 'Odio qui minus provident iusto.', 'Nisi dolores maiores rerum nobis qui molestias quod. Doloribus natus quis velit nulla dolor. Optio nulla inventore est ipsam. Laudantium aspernatur dolorum dolorem libero sed qui quam minima.', 82, 1, 0, '2012-02-29 03:06:58', '2016-12-29 07:37:28');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (65, 50, 75, 'Aliquam odio odio enim aut eum eos hic perferendis.', 'Corporis quis nobis officiis. Officiis alias eos provident velit veniam soluta ea. Corrupti quo maiores et quis blanditiis.', 2, 1, 1, '2014-12-28 17:43:41', '2015-01-06 04:59:40');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (66, 7, 73, 'Neque ratione recusandae error qui quis inventore facilis.', 'Enim quia dolorem minima minima. Laboriosam qui ut consequatur quo dicta quis. Id commodi qui quae blanditiis.', 1, 1, 0, '2014-08-01 15:30:14', '2018-02-06 07:27:52');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (67, 99, 7, 'Iusto eos labore rem doloribus voluptatibus qui accusantium.', 'Laudantium corporis deserunt blanditiis numquam hic quo. Tempore qui atque quae nisi nobis rerum quia. Delectus ea et aliquam est. Aut unde itaque est nobis mollitia.', 87, 1, 1, '2020-08-15 04:19:57', '2013-02-02 02:21:24');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (68, 13, 46, 'Aut vitae corporis ipsum dignissimos.', 'Minima dolor amet nulla impedit est. Nihil aut dolores aperiam iusto harum dolor id.', 12, 1, 0, '2015-04-11 17:09:36', '2020-07-08 19:46:02');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (69, 98, 44, 'Suscipit non perspiciatis iusto voluptatibus mollitia qui modi.', 'Quam non odio accusamus deleniti sed libero omnis. Dolores ea inventore rerum veniam non atque. Aliquam totam est accusantium commodi dolorum. Totam recusandae eos quas.', 41, 0, 1, '2016-09-12 06:24:13', '2010-09-19 05:55:25');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (70, 10, 2, 'Incidunt repellendus omnis recusandae sunt ut doloremque.', 'Ducimus exercitationem velit vero facilis voluptatem officiis odio omnis. Illum sunt reiciendis qui omnis a debitis doloribus saepe. Porro numquam cum nulla voluptatum ducimus ratione.', 73, 0, 0, '2010-10-04 23:11:32', '2018-12-05 21:35:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (71, 40, 49, 'Reprehenderit ut voluptatem corrupti quidem dolor voluptas.', 'Architecto repellendus eveniet et sapiente earum aliquid quia rerum. Et unde repudiandae sint.', 50, 1, 0, '2018-01-26 14:34:12', '2011-03-02 14:01:06');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (72, 93, 22, 'Rerum occaecati eligendi accusantium maiores.', 'Ea omnis quo et mollitia esse quas. Dolores sunt dolorem soluta dolorum vel et voluptas. Sint dolores minus adipisci asperiores.', 96, 1, 1, '2019-08-18 21:40:39', '2013-05-07 13:28:14');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (73, 47, 38, 'Aperiam blanditiis et vel nostrum.', 'Quidem quibusdam commodi non ut. Natus omnis et distinctio explicabo aut quaerat voluptas. Natus dolor rem ratione saepe ex commodi.', 67, 1, 0, '2010-10-27 11:13:57', '2019-11-25 14:02:08');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (74, 100, 41, 'In reiciendis vero error quae recusandae.', 'Distinctio pariatur suscipit maxime delectus dicta sit. Aperiam quisquam illo et beatae. Quos et et et ullam ut iusto sint. Qui autem quas et exercitationem voluptatem suscipit.', 33, 0, 0, '2018-05-20 03:30:27', '2011-12-21 10:04:15');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (75, 60, 49, 'Ut rerum aut adipisci omnis sunt.', 'Ea est consequatur id repudiandae culpa beatae. Tenetur at ipsum ullam est et voluptate repudiandae. Rem quidem ea assumenda est.', 50, 1, 1, '2015-07-25 01:41:54', '2018-10-03 17:23:48');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (76, 19, 58, 'Molestias ipsam eos rerum necessitatibus dolores.', 'Cum laborum mollitia ratione ipsum ab omnis quod. Molestias soluta et at et.', 68, 1, 1, '2013-03-23 20:20:07', '2016-02-20 17:35:28');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (77, 30, 91, 'Qui rerum voluptate ut in aut et.', 'Unde consequatur perferendis dolor sed. Modi necessitatibus enim ipsum facere rerum et illo. Quia nisi quae saepe et voluptatem.', 98, 0, 1, '2011-08-24 06:33:12', '2016-03-19 17:28:15');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (78, 90, 43, 'Sunt sint similique qui deserunt vel.', 'Voluptates iure hic quis necessitatibus odit enim. Quia quos quia nam doloremque nostrum. Similique qui incidunt veritatis earum nemo perferendis.', 50, 0, 0, '2011-06-03 18:00:12', '2012-09-10 17:26:44');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (79, 17, 49, 'Voluptatem mollitia et exercitationem tempore reiciendis itaque.', 'Eligendi ullam quis atque id ea rerum sed. Minima vel ut qui. Magni aut nostrum debitis amet qui rerum.', 11, 1, 1, '2017-12-28 10:42:24', '2018-03-05 11:04:14');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (80, 65, 64, 'Corrupti dolor amet aut magnam deserunt deserunt.', 'Qui repudiandae doloribus iure omnis unde cum. Est in ut unde unde. Suscipit et aut quidem occaecati. Ut sequi quas mollitia non.', 89, 0, 1, '2018-10-02 13:53:24', '2012-12-09 14:13:39');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (81, 89, 64, 'Omnis sed et enim fuga.', 'Sit et rerum perferendis enim rerum. Expedita aut in neque nulla at optio rerum. Magnam ullam corrupti repellat sed voluptatem.', 79, 1, 1, '2011-12-15 16:05:48', '2017-04-21 19:36:22');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (82, 29, 98, 'Est accusantium id delectus id repellendus.', 'Voluptatibus qui error quia dolorum enim earum veniam aut. Vel pariatur quibusdam non quos dolores sit. Illo molestias assumenda voluptatem quia. Nesciunt quo est sit eveniet enim.', 82, 1, 0, '2017-10-06 06:25:36', '2014-02-03 02:50:05');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (83, 21, 30, 'Omnis est aut optio vitae cupiditate aliquid.', 'Voluptas magni aut animi ad qui. Sint omnis et voluptatibus magnam eius. Qui ipsa est quia et. Et corporis et et soluta quis.', 68, 0, 0, '2012-03-30 15:43:14', '2013-02-19 07:27:35');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (84, 72, 10, 'Magnam cum deleniti itaque dicta.', 'Est molestias vitae dignissimos eveniet voluptatum et repellat aliquam. Saepe inventore dolores ducimus eos quia incidunt corporis eum. Id commodi et blanditiis.', 79, 0, 1, '2013-06-27 12:16:05', '2014-11-09 07:57:44');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (85, 29, 68, 'Magnam omnis id temporibus quia eum earum eos.', 'Veritatis aspernatur similique amet. Rerum facere at eum debitis maiores. Quis illo dignissimos est sapiente qui reprehenderit nisi neque. Aperiam et et sit voluptas quidem. Fugit voluptatem ut facilis aut id doloribus.', 92, 1, 0, '2018-02-20 20:06:09', '2020-09-05 16:39:56');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (86, 73, 72, 'Non consequuntur accusantium cum magnam ut iure voluptate est.', 'Minus sed beatae aspernatur dolor vel odio. Saepe et voluptatem perferendis nihil dolores dolorem sunt. Eum modi quia doloribus accusantium id dignissimos.', 100, 0, 1, '2013-05-18 19:44:44', '2020-06-17 14:43:30');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (87, 18, 39, 'Autem voluptas sapiente aperiam et.', 'Nulla ipsam laborum qui porro sed eaque consequatur. Voluptatem exercitationem mollitia rerum esse. Alias accusantium nihil ipsam officia corporis est. Officiis reprehenderit saepe repellat sequi. Facilis et est quo necessitatibus possimus velit omnis.', 94, 0, 0, '2014-09-02 07:23:06', '2017-12-16 22:24:30');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (88, 49, 13, 'Alias aperiam itaque molestiae sint.', 'Minima neque quam quis delectus et porro. Vitae quia accusamus aut molestias quo architecto. Odit nesciunt qui dolores eos. Non aspernatur quidem expedita.', 88, 1, 0, '2012-04-01 20:05:36', '2016-03-26 03:15:28');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (89, 40, 57, 'Aliquam ut qui et nisi.', 'Aut laudantium nobis iste impedit dolor consequatur quis omnis. Assumenda corrupti et quibusdam ea. Ut est hic error est quia.', 73, 0, 1, '2014-09-18 01:33:22', '2018-10-18 14:19:25');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (90, 19, 24, 'Rerum quod eos illum sed in assumenda reiciendis.', 'Quas eum aut reiciendis iusto. Expedita nisi dolor recusandae qui tempora quia. Fugit quis doloribus saepe eius. Maiores ratione repellendus excepturi adipisci quia.', 14, 1, 0, '2019-08-19 06:40:58', '2015-05-02 20:44:40');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (91, 78, 44, 'Eligendi incidunt eveniet velit sit.', 'Est nihil quis soluta itaque earum. Reprehenderit dolores unde molestiae modi rerum quia. Ab repellendus qui dolor modi.', 17, 0, 0, '2013-07-28 23:56:33', '2017-09-06 22:24:37');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (92, 32, 23, 'Est itaque magni culpa et.', 'Rerum aut et ut illo alias saepe quam tempore. Ut et molestias quo dolorum. Quia unde ut ipsa odio fugit iusto.', 1, 1, 1, '2015-12-07 08:28:13', '2014-06-09 14:13:54');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (93, 50, 87, 'Qui qui dolores voluptas ipsum.', 'Voluptas autem voluptatem natus tempore occaecati quia maiores vel. Enim sunt et deleniti id sit. Blanditiis sint tenetur ratione exercitationem deleniti. Aut sapiente voluptatibus nulla debitis magni esse deserunt. Est laboriosam repellat rem sit dolor distinctio.', 55, 1, 0, '2011-08-15 01:23:40', '2018-10-20 05:25:03');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (94, 58, 60, 'Esse suscipit libero voluptatum.', 'Quos quibusdam asperiores dolor autem. Doloremque placeat repellendus cum sunt iure. Reiciendis doloribus aut vel itaque minus velit dolore. Amet fugiat ut molestiae ea tempora et.', 92, 0, 0, '2019-05-25 03:53:32', '2018-06-26 11:34:09');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (95, 87, 40, 'Labore sequi in natus eveniet.', 'Officiis aut rerum et omnis unde natus. Nihil eaque blanditiis in dolor labore. Ea non commodi cumque voluptas ea facilis aliquam.', 69, 1, 1, '2015-04-16 09:29:32', '2017-06-13 09:18:38');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (96, 64, 36, 'Tenetur hic debitis rem voluptatum.', 'Modi reiciendis natus sint laudantium nulla. Et fuga molestiae non voluptatem repudiandae. Aspernatur quo quisquam recusandae et maiores dolor excepturi sed. Odit ducimus pariatur similique id.', 80, 1, 0, '2019-08-16 17:55:18', '2014-08-09 03:15:16');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (97, 85, 95, 'Sed molestias architecto odio omnis et.', 'Est omnis aut quidem corporis sit. Voluptas quod esse ipsa at provident labore voluptatem.', 48, 0, 0, '2014-12-13 08:08:31', '2019-05-13 15:35:01');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (98, 41, 26, 'Rerum dolor earum molestiae eaque.', 'Et nostrum aut rem quibusdam animi. Minus porro temporibus tempore deserunt voluptatem occaecati voluptas.', 50, 1, 0, '2020-07-01 07:17:16', '2011-08-21 20:54:40');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (99, 47, 96, 'Rerum et temporibus fuga corporis voluptates porro.', 'Minus praesentium rem mollitia molestiae ullam ipsam non. Sit voluptatem exercitationem voluptatem id. Sunt dolorum qui laudantium molestias in. Officia ut et at omnis in accusantium. Tenetur molestiae repellendus quo et consequuntur necessitatibus est.', 71, 0, 1, '2015-01-30 18:19:03', '2020-03-24 10:34:47');
INSERT INTO `posts` (`id`, `user_id`, `community_id`, `head`, `body`, `media_id`, `is_public`, `is_archived`, `created_at`, `updated_at`) VALUES (100, 88, 37, 'Culpa doloribus sit deserunt sint amet deserunt voluptatem odio.', 'Consequatur adipisci voluptas deleniti iusto voluptatem sit. Soluta error consequuntur debitis quisquam accusamus omnis facilis quas. Consequatur nobis iure deleniti eum. Nisi natus assumenda quisquam quia.', 8, 0, 1, '2016-05-13 20:49:34', '2014-11-20 14:39:03');

UPDATE posts SET updated_at = NOW() WHERE updated_at < created_at;

-- 2 Создать все необходимые внешние ключи и диаграмму отношений.
DESC profiles;
ALTER TABLE profiles 
	DROP FOREIGN KEY profiles_user_id_fk,
	DROP FOREIGN KEY profiles_photo_id_fk,
	DROP FOREIGN KEY profiles_user_status_id_fk;
ALTER TABLE profiles 
	ADD CONSTRAINT profiles_user_id_fk
		FOREIGN KEY (user_id) REFERENCES  users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT profiles_photo_id_fk
		FOREIGN KEY (photo_id) REFERENCES media(id)
			ON DELETE SET NULL,
	ADD CONSTRAINT profiles_user_status_id_fk
		FOREIGN KEY (user_status_id) REFERENCES user_statuses(id)
			ON DELETE SET NULL;

DESC communities_users;
ALTER TABLE communities_users 
	DROP FOREIGN KEY communities_users_community_id_fk,
	DROP FOREIGN KEY communities_users_user_id_fk;
ALTER TABLE communities_users 
	ADD CONSTRAINT communities_users_community_id_fk
		FOREIGN KEY (community_id) REFERENCES communities(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT communities_users_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE;
		
DESC media;
ALTER TABLE media 
	DROP FOREIGN KEY media_user_id_fk,
	DROP FOREIGN KEY media_media_types_id_fk;
ALTER TABLE media 
	ADD CONSTRAINT media_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT media_media_types_id_fk
		FOREIGN KEY (media_type_id) REFERENCES media_types(id);
		
DESC friendships;
ALTER TABLE friendships
	DROP FOREIGN KEY friendships_user_id_fk,
	DROP FOREIGN KEY friendships_friend_id_fk,
	DROP FOREIGN KEY friendships_status_id_fk;
ALTER TABLE friendships 
	ADD CONSTRAINT friendships_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT friendships_friend_id_fk
		FOREIGN KEY (friend_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT friendships_status_id_fk 
		FOREIGN KEY (status_id) REFERENCES friendship_statuses(id);
		
DESC likes;
ALTER TABLE likes 
	DROP FOREIGN KEY likes_user_id_fk,
	DROP FOREIGN KEY likes_target_type_id_fk;
ALTER TABLE likes 
	ADD CONSTRAINT likes_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT likes_target_type_id_fk
		FOREIGN KEY (target_type_id) REFERENCES target_types(id);
		
DESC messages;
ALTER TABLE messages
	DROP FOREIGN KEY messages_from_user_id_fk,
	DROP FOREIGN KEY messages_to_user_id_fk;
ALTER TABLE messages 
	ADD CONSTRAINT messages_from_user_id_fk
		FOREIGN KEY (from_user_id) REFERENCES users(id)
			ON DELETE RESTRICT,
	ADD CONSTRAINT messages_to_user_id_fk
		FOREIGN KEY (to_user_id) REFERENCES users(id)
			ON DELETE RESTRICT;
		
DESC posts;
UPDATE posts SET community_id = FLOOR(Rand()*20+1);
ALTER TABLE posts 
	DROP FOREIGN KEY posts_user_id_fk,
	DROP FOREIGN KEY posts_community_id_fk,
	DROP FOREIGN KEY posts_media_id_fk;
ALTER TABLE posts
	ADD CONSTRAINT posts_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT posts_community_id_fk
		FOREIGN KEY (community_id) REFERENCES communities(id),
	ADD CONSTRAINT posts_media_id_fk
		FOREIGN KEY (media_id) REFERENCES media(id);

-- 3 Определить кто больше поставил лайков (всего) - мужчины или женщины?
SELECT 'Gender:', gender, 'имеет наибольшее количество лайков в размере ', like_count
	FROM (
		SELECT 
			gender, COUNT(user_id) AS like_count
			FROM profiles
			WHERE user_id IN (SELECT user_id FROM likes)
			GROUP BY gender 
	) AS gender_likes
	-- ORDER BY MAX(like_count);
	ORDER BY like_count DESC 
	LIMIT 1;

-- 4 Подсчитать общее количество лайков десяти самым молодым пользователям (сколько лайков получили 10 самых молодых пользователей).