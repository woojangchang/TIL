# ERD(Entity Relational Diagram)를 그려 구조화 해봐야함
use classicmodels;

# 1. 매출액
# a. 일별 매출액
select a.orderdate, priceeach*quantityordered as SALES
from orders a
left
join orderdetails B
on A.ORDERNUMBER = B.ORDERNUMBER;

select a.orderdate,
sum(priceeach*quantityordered) as sales
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1; # orderdate로 그룹 묶고 orderdate로 오름차순

# b. 월별 매출액 조회
select substr(a.orderdate, 1, 7) MM,
sum(priceeach*quantityordered) as sales
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1;

# c. 연도별 매출액 조회
select substr(a.orderdate, 1, 4) as YY,
sum(priceeach*quantityordered) as SALES
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1;

# 2. 구매자 수, 구매 건수
select orderdate, customernumber, ordernumber
from orders;

select count(ordernumber) N_ORDERS,
count(distinct ordernumber) N_ORDERS_DISTINCT
from orders;

select orderdate, count(distinct customernumber) N_PURCHASER,
count(ordernumber) N_ORDERS
from orders
group by 1
order by 1;

# 3. 인당 매출액
select substr(a.orderdate, 1, 4) YY,
count(distinct a.customernumber) N_PURCHASER,
sum(priceeach*quantityordered) as SALES
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1;

select substr(a.orderdate, 1, 4) YY,
count(distinct a.customernumber) N_PURCHASER,
sum(priceeach*quantityordered) as SALES,
sum(priceeach*quantityordered) / count(distinct a.customernumber) AMV
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1;

# 4. 건당 구매 금액
# ATV(Average Transaction Value)
select substr(a.orderdate, 1, 4) YY,
count(distinct a.customernumber) N_PURCHASER,
sum(priceeach*quantityordered) as SALES,
sum(priceeach*quantityordered) / count(distinct a.ordernumber) ATV
from orders a
left
join orderdetails b
on a.ordernumber = b.ordernumber
group by 1
order by 1;