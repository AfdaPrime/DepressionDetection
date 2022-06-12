-- Create table for the database
-- CREATE TABLE IF NOT EXISTS diary (id INTEGER PRIMARY KEY,content TEXT NOT NULL,time TEXT not NULL,depression_level FLOAT NOT NULL);
-- CREATE TABLE IF NOT EXISTS user (id INTEGER PRIMARY KEY,name TEXT NOT NULL,username TEXT NOT NULL,password TEXT not NULL);

-- querying data fram table(see data from data base)
-- SELECT * FROM user;
SELECT * FROM user WHERE username = 'afda';
-- .tables

-- insert data
-- INSERT INTO user (name,username,password) VALUES ('fzsf','afda','afda');

-- delete table
-- DROP TABLE user;

-- SELECT password FROM user 