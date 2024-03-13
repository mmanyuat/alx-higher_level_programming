-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2
-- create databse
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost'
IDENTIFIED AS 'user_0d_2_pwd';
-- GRANITING PERMISSION
GRANT SELECT
ON hbtn_0d_2.*
TO 'user_0d_2'@'localhost' WITH GRATN OPTION;
