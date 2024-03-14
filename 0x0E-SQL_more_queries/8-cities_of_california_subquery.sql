-- Write a script that lists all the cities of California 
-- that can be found in the database hbtn_0d_usa
SELECT id, name FROM cities WHERE
WHERE state_id = (
	SELECT id
	FROM state
	state.name= 'California')
ORDER BY id ASC;
