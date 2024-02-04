-- Updating the records of the games won and games lost

UPDATE schools
SET ConFW = 6,
ConFWL = (ConFW)/(ConFW + ConFL),
OverallW = 18,
OverallWL = (OverallW)/(OverallW + OverallL)
WHERE school = 'Kansas';

