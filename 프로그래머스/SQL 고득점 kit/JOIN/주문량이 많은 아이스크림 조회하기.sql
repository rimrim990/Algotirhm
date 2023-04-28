-- 7월 출하량
WITH J AS (SELECT
               flavor,
               SUM(total_order) AS 'total'
           FROM july
           GROUP BY flavor)

SELECT
    F.flavor
FROM first_half F
         INNER JOIN J
WHERE F.flavor = J.flavor
GROUP BY F.flavor
ORDER BY SUM(total_order) + total DESC
    LIMIT 3;