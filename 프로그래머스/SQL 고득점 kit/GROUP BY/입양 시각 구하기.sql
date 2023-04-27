-- 코드를 입력하세요
WITH RECURSIVE time AS (
    SELECT 0 AS num
    UNION ALL
    SELECT num+1 FROM time
    WHERE num < 23
)
SELECT
    num,
    IFNULL(animal.count, 0) AS 'count'
FROM time
         LEFT JOIN (
    SELECT
        HOUR(datetime) AS 'hour',
        COUNT(*) AS 'count'
    FROM animal_outs
    GROUP BY HOUR(datetime)) AS animal
                   ON animal.hour = time.num
ORDER BY time.num;