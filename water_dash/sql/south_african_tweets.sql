-- South African tweets in this month or the previous month.
SELECT
    trend.topic,
    DATE(MAX(trend.timestamp)) AS last_trended,
    DATE(MIN(trend.timestamp)) AS first_trended,
    COUNT(DISTINCT(DATE(trend.timestamp))) AS days_mentioned,
    MAX(trend.volume) AS highest_volume
FROM trend
INNER JOIN place ON trend.place_id = place.id
WHERE place.name = 'South Africa'
GROUP BY trend.topic
HAVING last_trended >=  DATE('now','start of month','-1 month')
   AND highest_volume IS NOT NULL
ORDER BY last_trended DESC;
