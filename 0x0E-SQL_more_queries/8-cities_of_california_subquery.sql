-- more SQL proyects
-- because SQL is the bet
-- the best best
SELECT id, name FROM cities WHERE state_id=(SELECT id FROM states WHERE states.name='California');
