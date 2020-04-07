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
ORDER BY
    place_name,
    trend_topic
;
