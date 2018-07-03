/*
Creating a view
*/
CREATE VIEW view_name AS
SELECT column_1, column_2, ...
FROM table_name
WHERE condition;


/* 
Updating a view
*/
CREATE OR REPLACE VIEW view_name AS
SELECT column_1, column_2, ...
FROM table_name
WHERE condition;

/*
Dropping a view
*/
DROP VIEW view_name;