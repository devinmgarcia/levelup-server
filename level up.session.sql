SELECT first_name || ' ' || last_name, g.id, e.id, e.date, e.time, game.title FROM levelupapi_event as e
JOIN auth_user
JOIN levelupapi_gamer AS g
JOIN levelupapi_game as game on game.gamer_id = g.id;