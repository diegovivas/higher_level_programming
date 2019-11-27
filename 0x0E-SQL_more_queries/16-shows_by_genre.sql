-- more SQL proyects
-- because SQL is the bet
-- the best best
SELECT title, name FROM tv_shows LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id LEFT JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id ORDER BY title, name;
