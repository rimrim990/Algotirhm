-- 코드를 입력하세요
SELECT
    DISTINCT CAR_ID,
             IF (CAR_ID IN
                 (SELECT CAR_ID
                  FROM car_rental_company_rental_history
                  WHERE '2022-10-16' BETWEEN start_date AND end_date), '대여중', '대여 가능')
    AS 'availability'
FROM car_rental_company_rental_history
ORDER BY car_id DESC;