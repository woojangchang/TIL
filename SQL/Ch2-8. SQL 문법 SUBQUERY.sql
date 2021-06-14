# () subquery

select ORDERNUMBER
FROM classicmodels.ORDERS
WHERE CUSTOMERNUMBER IN (SELECT CUSTOMERNUMBER FROM classicmodels.customers WHERE CITY='NYC');

# () 안이 하나의 테이블로 사용되며 이름이 A
select customernumber
from (select customernumber from classicmodels.customers where city='NYC') A ; 

# select customernumber from classicmodels.customers where city='NYC';

select ORDERNUMBER
FROM classicmodels.ORDERS
WHERE CUSTOMERNUMBER IN (SELECT CUSTOMERNUMBER FROM classicmodels.customers WHERE country='USA');