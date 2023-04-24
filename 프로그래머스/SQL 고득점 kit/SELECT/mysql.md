# MySQL 문법 정리

## 날짜

### DATE_FORMAT
- `Date` 타입의 값을 포맷팅하여 출력
```sql
SELECT DATE_FORMAT(registered_date, '%Y-%m-d') FROM patient;
```

### YEAR, MONTH, DAY, HOUR, MINUTE, SECOND
- `Date` 타입에서 특정 날짜 값만 추출

## NULL

### IFNULL
- 값이 `null` 일 경우 대체 값 출력
```sql
SELCT IFNULL(age, 'NONE') FROM patient;
```

## 문자열

### LIKE
- 문자열 검색
```sql
name LIKE '강%'
```

## 집계

### ROUND
- 반올림
```sql
ROUND(2034.18, 1) -- 2034.2
```

## LIMIT
- 상위 n 개의 레코드 출력

### TRUNCATE
- 버림
```sql
TRUNCATE(2024.18, 1) -- 2024.1
```

## 그룹핑
### GROUP BY
- 그룹핑 조건이 일치한 대상을 하나의 그룹으로 묶기
```sql
GROUP BY name, user_id
```

### HAVING
- GROUP BY 에 필터링 조간 추가
```sql
GROUP BY name, user_id
WHERE count(*) > 2
```