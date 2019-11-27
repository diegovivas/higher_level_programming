-- more SQL proyects
-- because SQL is the bet
-- the best best
SELECT tv_genres.name AS name FROM tv_genres LEFT JOIN tv_show_genres ON tv_show_genres.genre_id = tv_genres.id LEFT JOIN tv_shows ON tv_show_genres.show_id = tv_shows.id WHERE title = 'Dexter' ORDER BY name;
