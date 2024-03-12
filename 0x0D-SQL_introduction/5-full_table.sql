-- Write a script that prints the full description of the table first_table from the database hbtn_0c_0 in your MySQL server.
-- uses the database
SELECT TABLE_NAME, CREATE TABLE
-- the second part of the command
FROM information_schema.tables
-- where part
WHERE table_schema = 'hbtn_0c_0' AND table_name = 'first_table';
