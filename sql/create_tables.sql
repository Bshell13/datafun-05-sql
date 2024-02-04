-- Start by deleting any tables if the exist already
-- We want to be able to re-run this script as needed.
-- DROP tables in reverse order of creation 
-- DROP dependent tables (with foreign keys) first

DROP TABLE IF EXISTS players;
DROP TABLE IF EXISTS schools;

-- Create the schools table 
-- Note that the schools table has no foreign keys, so it is a standalone table

CREATE TABLE schools (
    Rk INTEGER,
    School TEXT PRIMARY KEY,
    ConfW INTEGER,
    ConfL INTEGER,
    ConfWL REAL,
    OverallW INTEGER,
    OverallL INTEGER,
    OverallWL REAL,
    PtsPerGOwn REAL,
    PtsPerGOpp REAL,
    SRS REAL,
    SOS REAL
);

-- Create the players table
-- Note that the players table has a foreign key to the schools table
-- This means that the players table is dependent on the schools table
-- Be sure to create the standalone schools table BEFORE creating the players table.

CREATE TABLE players (
    Rk TEXT INTEGER,
    Player TEXT,
    Class TEXT,
    Pos TEXT,
    School TEXT PRIMARY KEY,
    G INTEGER,
    MinPlayed INTEGER,
    RB INTEGER,
    AST INTEGER,
    STL INTEGER,
    BLK INTEGER,
    TOV INTEGER,
    PF INTEGER,
    PTS INTEGER,
    FGPercent REAL,
    TwoPPercent REAL,
    ThreePPercent REAL,
    FTPercent REAL,
    FOREIGN KEY (School) REFERENCES schools(School)
);