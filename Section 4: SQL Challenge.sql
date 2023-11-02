-- 4.1
CREATE TABLE movie_info (
    Movie_ID INT PRIMARY KEY,
    Movie_Name VARCHAR(255),
    Movie_Length TIME,
    Age_Rating VARCHAR(10)
);


CREATE TABLE screens (
    Screen_ID INT PRIMARY KEY,
    Four_K BOOLEAN
);


CREATE TABLE showings (
    Showing_ID INT PRIMARY KEY,
    Movie_ID INT,
    Screen_ID INT,
    Start_Time TIME,
    Available_Seats INT,
    FOREIGN KEY (Movie_ID) REFERENCES movie_info(Movie_ID),
    FOREIGN KEY (Screen_ID) REFERENCES screens(Screen_ID)
);

-- 4.2
SELECT name, time
FROM movies
WHERE time > '12:00' AND available_seats > 0
ORDER BY time ASC;

-- 4.3
SELECT movie_name 
FROM showings 
GROUP BY movie_name 
ORDER BY COUNT(showing_id) DESC LIMIT 1;
