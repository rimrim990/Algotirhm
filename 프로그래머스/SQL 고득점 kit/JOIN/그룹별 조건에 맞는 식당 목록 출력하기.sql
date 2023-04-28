-- 멤버별 리뷰 개수
WITH MR AS (
    SELECT
        member_id,
        COUNT(*) AS 'count'
    FROM rest_review
    GROUP BY member_id)

-- 리뷰 개수가 가장 많은 멤버
SELECT
    member_name,
    review_text,
    DATE_FORMAT(review_date, '%Y-%m-%d') AS 'review_date'
FROM rest_review R
         NATURAL JOIN MR
         NATURAL JOIN member_profile
WHERE MR.count = (SELECT MAX(count) FROM MR)
ORDER BY review_date ASC, review_text ASC;