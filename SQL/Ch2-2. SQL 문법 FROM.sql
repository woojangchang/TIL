/*
SELECT 계산식 또는 칼럼명
FROM DB명.TABLE명
*/

# 하나의 DB만 사용하며, 매번 DB를 입력하는 것이 번거로울 때
USE classicmodels;

SELECT SUM(AMOUNT)
FROM PAYMENTS;