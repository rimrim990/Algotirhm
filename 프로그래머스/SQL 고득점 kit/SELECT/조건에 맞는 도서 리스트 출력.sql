-- 코드를 입력하세요
SELECT book_id, DATE_FORMAT(published_date, '%Y-%m-%d') as publshed_date
FROM book
WHERE year(published_date) = '2021'
AND category = '인문'
ORDER BY published_date ASC;