SELECT customer.first_name, customer.last_name, customer.email, address.address
FROM address
JOIN customer ON address.address_id = customer.address_id
WHERE address.city_id = 312;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE category.name = 'Comedy';

SELECT actor.actor_id, actor.first_name, actor.last_name, film.title, film.description, film.release_year
FROM actor
JOIN film_actor ON film_actor.actor_id = actor.actor_id
JOIN film ON film_actor.film_id = film.film_id
WHERE actor.actor_id = 5;

SELECT customer.first_name, customer.last_name, customer.email, address.address 
FROM customer
JOIN store ON store.store_id = customer.store_id
JOIN address ON customer.address_id = address.address_id
JOIN city ON address.city_id = city.city_id
WHERE customer.store_id = 1 AND city.city_id IN (1, 42, 312, 459);

SELECT title, description, release_year, rating, special_features
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
WHERE film.rating = 'G' AND film_actor.actor_id = 15 AND film.special_features LIKE '%behind the scenes%';

SELECT film.film_id, film.title, actor.actor_id, actor.first_name, actor.last_name
FROM film
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE film.film_id = 369;

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON film_category.category_id = category.category_id
WHERE film.rental_rate = 2.99 AND category.name = 'Drama';

SELECT film.title, film.description, film.release_year, film.rating, film.special_features, category.name, actor.first_name, actor.last_name
FROM film
JOIN film_category ON film_category.film_id = film.film_id
JOIN category ON category.category_id = film_category.category_id
JOIN film_actor ON film_actor.film_id = film.film_id
JOIN actor ON actor.actor_id = film_actor.actor_id
WHERE category.name = 'Action' AND actor.first_name = 'Sandra' AND actor.last_name = 'Kilmer';
