USE dec23;
show tables;

DROP TABLE IF EXISTS actor_movie;
DROP TABLE IF EXISTS Movies;
DROP TABLE IF exists Genre;
DROP TABLE IF EXISTS Actors;

CREATE TABLE IF NOT EXISTS Actors(
a_id int auto_increment primary key,
name varchar(50) unique not null,
age smallint check (age>=0),
worth int check(worth>=0)
);

INSERT INTO Actors(name,age,worth) VALUES
('Chris Evans', 50, 30000000),
('Scarlett Johansson', 29, 31000000),
('Elizabeth Olsen', 29, 32000000);

SELECT * FROM Actors;



CREATE TABLE Genre(
g_id int auto_increment primary key,
name varchar(50) unique not null
);

INSERT INTO Genre(name) VALUES
('Action'),
('Adventure'),
('Thriller'),
('Comedy'),
('Drama');

SELECT * FROM Genre;


CREATE TABLE Movies(
m_id int auto_increment primary key,
title varchar(50) not null,
price float check(price>=0),
return_date int default 0,
genre_id int,
FOREIGN KEY(genre_id) REFERENCES genre(g_id));

INSERT INTO Movies(title,price, return_date,genre_id) VALUES
('The Avengers', 7.5, default, 1),
('Captain America: Civil War', 8, default, 1);



CREATE TABLE actor_movie (
actor_id int,
FOREIGN KEY (actor_id) references actors(a_id),
movie_id int,
FOREIGN KEY (movie_id) references movies(m_id)
);

INSERT INTO actor_movie(actor_id,movie_id) VALUES
(1,1),
(1,2);
SELECT * FROM actor_movie



