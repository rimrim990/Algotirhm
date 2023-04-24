-- 코드를 입력하세요
SELECT first_half.flavor
FROM first_half
         LEFT JOIN icecream_info
                   ON first_half.flavor = icecream_info.flavor
WHERE ingredient_type = 'fruit_based'
  AND total_order > 3000
ORDER BY total_order DESC;