-- Aggregated State of the Nation Address (SONA) data.
SELECT
    trend.topic,
    DATE(MAX(trend.timestamp)) AS last_trended,
    DATE(MIN(trend.timestamp)) AS first_trended,
    COUNT(DISTINCT(DATE(trend.timestamp))) AS days_mentioned,
    MAX(trend.volume) AS highest_volume
FROM trend
INNER JOIN place ON trend.place_id = place.id
WHERE place.name = 'South Africa'
    AND (
       trend.topic LIKE 'SONA%'
    OR trend.topic LIKE '%Eksom%'
    OR trend.topic LIKE '%nation%'
    OR trend.topic LIKE '%president%'
    OR trend.topic LIKE '%Ramaphosa%'
)
GROUP BY trend.topic
ORDER BY last_trended DESC
;
