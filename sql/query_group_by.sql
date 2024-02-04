-- Group records by a specific key

SELECT School, AVG(G), COUNT(MinPlayed)
FROM players
GROUP BY School;