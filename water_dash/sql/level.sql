-- For both lockdown and water level
-- e.g. '#lockdownlevel' '#level1' 'level 1'

SELECT 
  topic, 
  count(*)
FROM trend
WHERE topic like 'level%'
GROUP BY topic
ORDER BY topic;
