/*
A stored procedure is a SQL statement that is saved to be used persistently.
So, instead of rewriting the same SQL statement numerous times, we can save it
as a stored procedure and call it to execute. This saves time and effort.
We can also pass parameters to a stored procedure.
*/

/*
Creating a stored procedure
*/
CREATE PROCEDURE procedure_name
AS 
SELECT * FROM table_name
GO;

/*
Executing a stored procedure
*/
EXEC procedure_name;

/*
Stored procedure with one parameters
*/
CREATE PROCEDURE procedure_name @parameter nvarchar(size_of_parameter)
AS
SELECT * FROM table_name WHERE column = @parameter
GO;

/*
Stored procedure with multiple parameters
*/
CREATE PROCEDURE procedure_name @parameter1 nvarchar(size_of_parameter), @parameter2 nvarchar(size_of_parameter)
AS
SELECT * FROM table_name WHERE column1 = @parameter1 AND column2 = @parameter2
GO;

/*
Executing a stored procedure with multiple parameters
*/
EXEC procedure_name parameter1 = "parameter_value1", parameter2 = "parameter_value2"