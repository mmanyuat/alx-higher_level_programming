-- Write a script that creates the MySQL server user user_0d_1
-- creating a user
CREATE USER 'user_0d_1'
IDENTIFIED AS 'user_0d_1_pwd';
-- GRANTING PREMISSION
GRANT PRIVILEGES *
ON *.*
TO 'user_0d_1'@'user_0d_1_pwd';
