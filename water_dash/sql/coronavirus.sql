-- Aggregated Corona virus trends
SELECT
    trend.topic,
    DATE(MAX(trend.timestamp)) AS last_trended,
    DATE(MIN(trend.timestamp)) AS first_trended,
    COUNT(DISTINCT(DATE(trend.timestamp))) AS days_mentioned,
    MAX(trend.volume) AS highest_volume
FROM trend
INNER JOIN place ON trend.place_id = place.id
WHERE place.name = 'Worldwide'
 AND (
       -- See https://en.wikipedia.org/wiki/Severe_acute_respiratory_syndrome_coronavirus_2
       
       -- Take into account misspellings of corona
          trend.topic LIKE '%c_r_n_%' 
       -- Covid-19 and related
       OR trend.topic LIKE '%covid%'
       
       -- 2019-nCoV (from novel coronavirus).
       OR trend.topic LIKE '%nCoV%'
       -- CoV-2
       OR trend.topic LIKE '%CoV%2%'
       OR trend.topic LIKE '%SARS%'
       
       OR trend.topic LIKE '%symptom%'
       OR trend.topic LIKE '%confirmed%case%'
       
       OR trend.topic LIKE '%social%distanc%'
       OR trend.topic LIKE '%panic%buy%'
       
       OR trend.topic LIKE '%stay%home%'
       OR trend.topic LIKE '%quarantine%'
       OR trend.topic LIKE '%lockdown%'
       
       OR trend.topic LIKE '%strain%'
       OR trend.topic LIKE '%virus%'
       OR trend.topic LIKE '%outbreak%'
       OR trend.topic LIKE '%epidemic%'
       OR trend.topic LIKE '%pandemic%'
       OR trend.topic LIKE '%disease%'
       
       -- Origin of the outbreak
       OR trend.topic LIKE '%China%'
       OR trend.topic LIKE '%Wuhan%'
     )
GROUP BY trend.topic
ORDER BY last_trended DESC;
