use classicmodels;

# 2003년 구매한 고객이 2004년에도 구매한 내역
select a.customernumber, a.orderdate, b.customernumber, b.orderdate
from orders a
left join orders b
on a.customernumber = b.customerNumber
and substr(a.orderdate, 1, 4) = substr(b.orderdate, 1, 4)-1;

# 국가별 Retention Rate(%)
select c.country,
substr(a.orderdate, 1, 4) YY,
count(distinct a.customernumber) BU_1,
count(distinct b.customernumber) BU_2,
count(distinct b.customernumber) / count(distinct a.customernumber) RETENTION_RATE
from orders a
left join orders b
on a.customerNumber = b.customernumber
and substr(a.orderdate, 1, 4) = substr(b.orderdate, 1, 4)-1
left join customers c
on a.customernumber = c.customernumber
group by 1, 2;