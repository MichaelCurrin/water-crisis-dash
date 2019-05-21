/**
 *  Trend data filtered to South African (country and town level).
 *  Each topic appears once against a place, with stats for that topic in
 *  that place. Topics are sorted case insensitively. Hashtags will appear
 *  first and then the phrases will follow.
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


/**
 * Column ordering and order clause make it easy to see the same topic
 * across places. The topic type and place type are used for easy reading.
 * The max volume can be null if all the values to group are null, but the
 * date and count columns will always set.
 */
SELECT
    CASE WHEN trend.hashtag THEN 'hashtag' ELSE 'phrase' END AS topic_type,
    trend.topic,
    filtered_places.type AS place_type,
    filtered_places.name AS place_name,
    DATE(MAX(trend.timestamp)) AS last_trended_at_place,
    DATE(MIN(trend.timestamp)) AS first_trended_at_place,
    COUNT(DISTINCT(DATE(trend.timestamp))) AS days_mentioned_at_place,
    MAX(trend.volume) AS highest_global_volume
FROM trend
INNER JOIN filtered_places ON trend.place_id = filtered_places.id
GROUP BY
    topic_type,
    trend.topic,
    place_type,
    place_name
ORDER BY
    LOWER(trend.topic),
    place_type,
    place_name
