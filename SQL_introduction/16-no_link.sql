-- Lists all records of the table second_table,
-- without rows missing a name value, listed by descending score.
SELECT score, name FROM second_table WHERE name IS NOT NULL ORDER BY score DESC;
