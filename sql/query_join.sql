-- Join tables together based on primary keys

SELECT schools.School, players.PTS
FROM schools
INNER JOIN players ON schools.School = players.School;