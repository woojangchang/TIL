# SELECT
# 칼럼 조회
SELECT CUSTOMERNUMBER
FROM CLASSICMODELS.CUSTOMERS;

# 집계 함수
select sum(AMOUNT), # ,로 여러 칼럼 조회
count(CHECKNUMBER)
from classicmodels.payments;

/*
# * 모든 결과 조회
select *
from classicmodels.orders
*/

# 칼럼명 변경 조회 (as는 쓰지 않아도 된다.)
select count(PRODUCTCODE) as N_PRODUCTS
from classicmodels.products;

# 중복 제외 조회
select distinct ORDERNUMBER
from classicmodels.orderdetails;