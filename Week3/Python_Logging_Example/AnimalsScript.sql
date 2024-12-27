-- remember pip install mysql-connector-python in python 
CREATE Database animals;
USE animals;
DROP TABLE IF EXISTS animals;
CREATE TABLE animals(animalid int AUTO_INCREMENT Primary Key ,name varchar(255), age int, color varchar(255), type varchar(255));