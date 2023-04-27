-- 코드를 입력하세요
SELECT
    YEAR(sales_date) as YEAR,
    MONTH(sales_date) as MONTH,
    gender,
    COUNT(DISTINCT U.user_id) USERS
FROM user_info as U
    INNER JOIN online_sale as O
ON U.user_id = O.user_id
WHERE gender IS NOT NULL
GROUP BY
    YEAR(sales_date),
    MONTH(sales_date),
    gender
ORDER BY
    YEAR(sales_date) ASC,
    MONTH(sales_date) ASC,
    gender ASC;