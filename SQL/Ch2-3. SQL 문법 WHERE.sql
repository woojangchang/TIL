# WHERE : 조건절

# WHERE 칼럼명 BETWEEN 값1 AND 값2
# 특정 칼럼의 값이 값1과 값2 사이인 모든 행 가져오기
SELECT *
FROM classicmodels.orderdetails
WHERE priceEach BETWEEN 30 AND 50;

# 대소 관계 (같지 않다 : <>)
SELECT *
FROM classicmodels.orderdetails
WHERE priceEach >= 30;

# 여러 값 찾기
SELECT CUSTOMERNUMBER
FROM classicmodels.CUSTOMERS
WHERE COUNTRY IN ('USA', 'Canada'); # NOT IN : 특정값 제외

# IS NULL
SELECT EMPLOYEENUMBER
FROM classicmodels.employees
WHERE reportsTo IS NULL; # IS NOT NULL : NULL 제외

# 특정 문자열이 들어간 칼럼 찾기
SELECT ADDRESSLINE1
FROM classicmodels.customers
WHERE addressLine1 LIKE '%ST%'; # %는 문자를 의미

# 여러 조건을 줄 때 AND 사용
SELECT EMPLOYEENUMBER
FROM classicmodels.employees
WHERE reportsTo IS NOT NULL AND EMPLOYEENUMBER > 1400; # IS NOT NULL : NULL 제외