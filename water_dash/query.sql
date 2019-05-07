SELECT
    trend.topic,
    DATE(MAX(trend.timestamp)) AS last_trended,
    DATE(MIN(trend.timestamp)) AS first_trended,
    COUNT(DISTINCT(DATE(trend.timestamp))) AS days_mentioned,
    MAX(trend.volume) AS highest_volume
FROM trend
INNER JOIN place ON trend.place_id = place.id
WHERE place.name = 'Cape Town'
 AND
    (
       (
               trend.topic LIKE '%water%'
           AND trend.topic NOT LIKE '%watermelon%'
       )
       OR trend.topic LIKE '%drought%'
       OR (
               trend.topic LIKE '%dam%'
           AND trend.topic NOT LIKE '%van damme%'
           AND trend.topic NOT LIKE '%damian%'
           AND trend.topic NOT LIKE '%dame%'
           AND trend.topic NOT LIKE '%damn%'
           AND trend.topic NOT LIKE '%madam%'
           AND trend.topic NOT LIKE '%damanifesto%'
           AND trend.topic NOT LIKE '%notre%dam%'
          )
       OR trend.topic LIKE '%level%'
       OR trend.topic LIKE '%shortage%'
       OR trend.topic LIKE '%flush%'
       OR trend.topic LIKE '%drink%'
       OR trend.topic LIKE '%waste%'
       OR trend.topic LIKE '%save%'
       OR trend.topic LIKE '%crisis%'
       OR trend.topic LIKE '%disaster%'
       OR trend.topic LIKE '%day%zero%'
    )
GROUP BY trend.topic
ORDER BY last_trended DESC
