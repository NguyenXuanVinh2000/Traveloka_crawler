CREATE DATABASE IF NOT EXISTS HOTEL;
USE HOTEL;
CREATE TABLE IF NOT EXISTS hotel (hotel_name   longtext CHARSET utf8, hotel_rating varchar(3), hotel_address  longtext CHARSET utf8, hotel_point_review varchar(3), hotel_sum_review int, hotel_url longtext CHARSET utf8);
CREATE USER 'scraper'@'%' IDENTIFIED BY 'pass';
GRANT ALL PRIVILEGES ON *.* TO 'scraper'@'%';
FLUSH PRIVILEGES;
