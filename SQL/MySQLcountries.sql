SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.language = 'Slovene'
ORDER BY languages.percentage DESC;

SELECT countries.name, COUNT(*) AS num_of_cities 
FROM countries
JOIN cities ON countries.id = cities.country_id
GROUP BY countries.name
ORDER BY num_of_cities DESC;

SELECT cities.name, cities.population
FROM cities
JOIN countries ON countries.id = cities.country_id
WHERE countries.name = 'Mexico' AND cities.population > 500000
ORDER BY cities.population DESC;

SELECT countries.name, languages.language, languages.percentage
FROM countries
JOIN languages ON countries.id = languages.country_id
WHERE languages.percentage > 89
ORDER BY languages.percentage DESC;

SELECT name
FROM countries
WHERE surface_area < 501 AND population > 100000;

SELECT name, government_form, capital, life_expectancy 
FROM countries
WHERE government_form = 'Constitutional Monarchy' AND capital > 200 AND life_expectancy > 75;

SELECT countries.name, cities.name AS city_name, cities. district, cities.population
FROM countries
JOIN cities ON countries.id = cities.country_id
WHERE countries.name = "Argentina" AND cities.district = "Buenos Aires" AND cities.population > 500000;

SELECT countries.region, COUNT(*) AS num_of_countries 
FROM countries 
GROUP BY countries.region
ORDER BY num_of_countries DESC;
-- 

