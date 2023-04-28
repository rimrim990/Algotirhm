-- 2021 년에 가입한 회원 id 테이블
WITH U AS (SELECT
               user_id
           FROM user_info U
           WHERE YEAR(joined) = '2021')

-- 2021 년에 가입한 회원들의 구매 내역
SELECT
    YEAR(sales_date) AS 'year',
    MONTH(sales_date) AS 'month',
    COUNT(DISTINCT user_id) AS 'purchased_users',
    ROUND(COUNT(DISTINCT user_id) / (SELECT COUNT(user_id) FROM U), 1) AS 'purchased_ratio'
FROM online_sale
WHERE user_id IN (SELECT user_id FROM U)
GROUP BY YEAR(sales_date), MONTH(sales_date)
ORDER BY YEAR(sales_date) ASC, MONTH(sales_date) ASC;