-- 코드를 입력하세요
SELECT
    category,
    price AS 'max_price',
        product_name
FROM food_product
WHERE (category, price) IN
      (SELECT category, MAX(price)
       FROM food_product
       GROUP BY category)
  AND category IN ('과자', '국', '김치', '식용유')
ORDER BY price DESC;