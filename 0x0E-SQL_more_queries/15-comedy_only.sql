-- more SQL proyects
-- because SQL is the bet
-- the best best
SELECT title FROM tv_genres LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id LEFT JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id WHERE name = "Comedy" ORDER BY title;
