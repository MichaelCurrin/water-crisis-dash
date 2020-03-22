-- Corona virus trends
SELECT
    place.name AS place_name,
    DATE(trend.timestamp) AS date,
    trend.topic AS trend_topic,
    trend.volume AS global_24_hr_volume
FROM trend
INNER JOIN place ON trend.place_id = place.id
                AND place.child_name != 'Town'
WHERE
          trend.topic LIKE '%corona%'
       OR trend.topic LIKE '%covid%'
       OR trend.topic LIKE '%symptom%'
       OR trend.topic LIKE '%confirmed%case%'
       OR trend.topic LIKE '%virus%'
       OR trend.topic LIKE '%social%distanc%'
       OR trend.topic LIKE '%panic%buy%'
       OR trend.topic LIKE '%stay%home%'
       OR trend.topic LIKE '%quarantine%'
       OR trend.topic LIKE '%outbreak%'
       OR trend.topic LIKE '%lockdown%'
       OR trend.topic LIKE '%epidemic%'
       OR trend.topic LIKE '%pandemic%'
       OR trend.topic LIKE '%disease%'
ORDER BY
    place_name,
    trend_topic
;
