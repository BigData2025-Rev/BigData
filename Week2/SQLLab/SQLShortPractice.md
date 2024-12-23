# Assignments
## DDL

Pick a topic of interest and create a table with the following:
1. A primary key SERIAL column.
2. A unique column.
3. A TIMESTAMP column.
4. An Integer or Numeric column with a CHECK constraint.

Then, create a related table with a foreign key relationship.

## DML
Work with a partner to insert data into your tables, taking information from them and inserting data.

Update and delete several rows based on a second classmates information.

## DQL

### Basic Problems
Practice SELECTing by using WHERE with:
  * A primary key column.
  * A varchar column.
  * An AND and OR clause.
  * An IN clause with a SET.
  * A BETWEEN clause with numbers.
  * A BETWEEN clause with timestamps.
  * LIKE clause with % and _.

### Subqueries
  * Write a query which selects friends of a user by using an inline view subquery.
  * Write a query which selects posts by a user with a given name using an inline view subquery.
  * Write a query which finds the user with the most posts and the number of posts with a subquery.
  
### Joins
  * Write a query which joins the users and friends table to find mutual friends between two given users. Note: The two users should not be in the result set.
  
## PLpg/SQL
### Triggers
  * Add a column to the friends table that represents when the two users became friends. Write a trigger which will automatically assign the timestamp upon users becoming friends.

### Functions
  * Write a function which accepts a user id and a string and creates a new post for the user with the provided user ID with the string as content, returning the inserted ID.
  * Write a function which accepts two IDs and create a friend relation between them.