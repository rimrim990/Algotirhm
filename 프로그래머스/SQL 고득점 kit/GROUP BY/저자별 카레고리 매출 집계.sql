-- 코드를 입력하세요
SELECT
    A.author_id,
    A.author_name,
    B.category,
    SUM(sales * price) AS 'total_sales'
FROM book B
         INNER JOIN author A
                    ON B.author_id = A.author_id
         INNER JOIN book_sales S
                    ON B.book_id = S.book_id
WHERE DATE_FORMAT(sales_date, '%Y-%m') = '2022-01'
GROUP BY A.author_id, category
ORDER BY A.author_id ASC, category DESC;