-- lists all cities contained in the database
SELECT `cities.id`, `cities.name`, `states.name` FROM `cities` AS c
INNER JOIN `states` AS s ON c.state_id=s.id
ORDER BY c.id;
