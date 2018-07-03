/*
Indexes are used to retrieve data from a database in a very fast manner.
They are not seen by users but speed up searches & queries.
*/

/*
Create an index
*/
CREATE INDEX index_name
ON table_name (column1, column2, ...);

/*
Create a unique index
*/
CREATE UNIQUE INDEX index_name 
ON table_name (column1, column2, ...);

/*
Dropping an index
*/
DROP INDEX table_name.index_name;