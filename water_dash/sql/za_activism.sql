-- South Africa activitsm
/**
 *  Trend data filtered to South African (country and town level).
 */

WITH selected_countries AS (
    SELECT
        Place.child_name AS type,
        Place.name,
        Country.id
    FROM Place
    INNER JOIN Country ON Place.id = Country.id
    WHERE Place.name IN ('South Africa')
),

selected_towns AS (
    SELECT
        Place.child_name AS type,
        Place.name,
        Town.id
    FROM Place
    INNER JOIN Town ON Place.id = Town.id
    INNER JOIN selected_countries ON Town.country_id = selected_countries.id
),

filtered_places AS (
    SELECT *
    FROM selected_countries
    UNION
    SELECT *
    FROM selected_towns
)


SELECT
    trend.topic AS topic,
    filtered_places.type AS place_type,
    filtered_places.name AS place_name,
    -- Value is after midnight so volume is actually the total for the whole of previous day.
    DATE(trend.timestamp, '-1 day') AS trend_date,
    trend.volume
FROM trend
INNER JOIN filtered_places ON trend.place_id = filtered_places.id
WHERE (
    trend.topic LIKE '%sandton%'
   OR trend.topic LIKE '%enough%'
   OR trend.topic LIKE '%next%'
   OR trend.topic LIKE '%patriarchy%'
   OR trend.topic LIKE '%usual%'
   )
  AND trend_date >=  DATE('now', 'start of month')
ORDER BY
    trend_date,
    LOWER(trend.topic),
    place_type,
    place_name
