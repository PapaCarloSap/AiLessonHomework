DESC addresses;
ALTER TABLE addresses
	DROP FOREIGN KEY addresses_country_id_fk;
ALTER TABLE addresses
	ADD CONSTRAINT addresses_country_id_fk
		FOREIGN KEY (country_id) REFERENCES countries(id);
			
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
			
DESC orders;
ALTER TABLE orders
	DROP FOREIGN KEY orders_customer_user_id_fk,
	DROP FOREIGN KEY orders_rent_id_fk;
ALTER TABLE orders
	ADD CONSTRAINT orders_customer_user_id_fk
		FOREIGN KEY (customer_user_id) REFERENCES users(id)
			ON DELETE RESTRICT,
	ADD CONSTRAINT orders_rent_id_fk
		FOREIGN KEY (rent_id) REFERENCES rents(id)
			ON DELETE RESTRICT;
		
DESC photos_rent;
ALTER TABLE photos_rent
	DROP FOREIGN KEY photos_rent_photo_id_fk,
	DROP FOREIGN KEY photos_rent_rent_id_fk;
ALTER TABLE photos_rent
	ADD CONSTRAINT photos_rent_photo_id_fk
		FOREIGN KEY (photo_id) REFERENCES photos(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT photos_rent_rent_id_fk
		FOREIGN KEY (rent_id) REFERENCES rents(id)
			ON DELETE CASCADE;

DESC profiles;
ALTER TABLE profiles
	DROP FOREIGN KEY profiles_user_id_fk,
	DROP FOREIGN KEY profiles_addresses_id_fk;
ALTER TABLE profiles
	ADD CONSTRAINT profiles_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT profiles_addresses_id_fk
		FOREIGN KEY (addresses_id) REFERENCES addresses(id)
			ON DELETE SET NULL;

DESC rents;
ALTER TABLE rents
	DROP FOREIGN KEY rents_user_id_fk,
	DROP FOREIGN KEY rents_addresses_id_fk;
ALTER TABLE rents
	ADD CONSTRAINT rents_user_id_fk
		FOREIGN KEY (user_id) REFERENCES users(id)
			ON DELETE CASCADE,
	ADD CONSTRAINT rents_addresses_id_fk
		FOREIGN KEY (addresses_id) REFERENCES addresses(id)
			ON DELETE RESTRICT;
		
DESC reviews;
ALTER TABLE reviews
	DROP FOREIGN KEY reviews_order_id_fk;
ALTER TABLE reviews
	ADD CONSTRAINT reviews_order_id_fk
		FOREIGN KEY (order_id) REFERENCES orders(id)
			ON DELETE CASCADE;
		
DESC users;
ALTER TABLE users
	DROP FOREIGN KEY users_photo_id_fk;
ALTER TABLE users
	ADD CONSTRAINT users_photo_id_fk
		FOREIGN KEY (photo_id) REFERENCES photos(id)
			ON DELETE SET NULL;

		
-- Индексирование по цене
CREATE INDEX rents_price ON rents(price);
-- Индексирование по имени страны 
CREATE INDEX countries_name ON countries(name);

