SELECT leader_id, leaders.first_name, leaders.last_name, follower_id, followees.first_name, followees.last_name 
FROM friends
JOIN users AS leaders ON leader_id = leaders.id
JOIN users AS followees ON follower_id = followees.id
ORDER BY leaders.last_name;