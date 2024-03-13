-- Write a script that creates the MySQL server user user_0d_1
-- creating a user
CREATE USER IF NOT EXISTS 'user_0d_1'
IDENTIFIED BY 'user_0d_1_pwd';
-- GRANTING PREMISSION
GRANT ALL PRIVILEGES
ON *.*
TO 'user_0d_1'@'localhost' WITH GRANT OPTION;