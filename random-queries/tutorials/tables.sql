/*
Creating a table
*/
CREATE TABLE table_name (
    column1 datatype NOT NULL PRIMARY KEY,
    column2 datatype NOT NULL,
    column3 datatype FOREIGN KEY REFERENCES reference_table(reference_column),
    ...
    
);

/*
Creating a table using another table
*/
CREATE TABLE new_table_name AS
    SELECT column1, column2, ...
    FROM existing_table_name
    WHERE ...;


/*
Dropping a table
*/
DROP TABLE table_name;

/*
Dropping a table inside a table, but not the table itself
*/
TRUNCATE TABLE table_name;