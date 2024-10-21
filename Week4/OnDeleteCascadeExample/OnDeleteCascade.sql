USE test;
show tables;

DROP TABLE IF EXISTS Movies;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Actors;

DROP TABLE IF EXISTS actor_movie;

CREATE TABLE IF NOT EXISTS Actors(
a_id int auto_increment primary key,
name varchar(50) unique not null,
age smallint check (age>=0),
worth int check(worth>=0)
);

insert into actors(name,age,worth) Values
('Chris Evans',50,30000000),
('Scarlett Johansson', 29, 31000000),
('Elizabeth Olsen', 29,32000000);

SELECT * FROM Actors;

CREATE TABLE Genre (
g_id int auto_increment primary key,
name varchar(50) unique not null);

Insert Into Genre(name) Values
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
FOREIGN KEY(genre_id) REFERENCES genre(g_id) on delete cascade);

INSERT INTO Movies(title,price,return_date,genre_id) Values
('The Avengers',7.5,default,1),
('Captain America: Civil War',8,default,1);

INSERT INTO Movies(title,price,return_date,genre_id) Values
('Hubbies Halloween',7.5,default,4);

-- SELECT * FROM Movies;

CREATE TABLE actor_movie (
actor_id int,
FOREIGN KEY (actor_id) references actors(a_id) on delete cascade,
movie_id int,
FOREIGN KEY (movie_id) references movies(m_id) on delete cascade);

insert into actor_movie(actor_id,movie_id) values
(1,1),
(2,1);
SELECT * FROM actor_movie;

DELETE FROM genre where g_id=1;

SELECT * FROM genre;

SELECT * FROM movies;

