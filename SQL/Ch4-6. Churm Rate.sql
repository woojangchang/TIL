# churn rate = 활동 고객이 비활동 고객으로 전환되었는지 나타내는 지표
# churn = 구매일(접속일) 이후 일정기간 구매, 접속하지 않은 상태

use classicmodels;

# 1. churn rate 구하기
select max(orderdate) mx_order
from orders;

# 각 고객이 가장 최근 구매한 날짜
select customernumber, max(orderdate) mx_order
from orders
group by 1;

# datediff
select customernumber, mx_order, '2005-06-01',
datediff('2005-06-01', mx_order) diff
from
(select customernumber, max(orderdate) mx_order
from orders
group by 1) base;

# diff >= 90 : churm 가정
select *,
case when diff >= 90 then 'CHURN' else 'NON-CHURN' end churn_type
from
(select customernumber, mx_order, '2005-06-01',
datediff('2005-06-01', mx_order) diff
from
(select customernumber, max(orderdate) mx_order
from orders
group by 1) base) base;

select
case when diff >= 90 then 'CHURN' else 'NON-CHURN' end churn_type,
count(distinct customernumber) n_cus
from
(select customernumber, mx_order, '2005-06-01',
datediff('2005-06-01', mx_order) diff
from
(select customernumber, max(orderdate) mx_order
from orders
group by 1) base) base
group by 1;

# 2. churn 고객이 가장 많이 구매한 productline
# 고객별 chrun table 생성
create table churn_list as
select case when diff >= 90 then 'CHURN' else 'NON-CHURN' end churn_type,
customernumber
from
(select customernumber, mx_order, '2005-06-01' END_POINT,
datediff('2005-06-01', mx_order) diff
from
(select customernumber, max(orderdate) mx_order
from orders
group by 1) base) base;

# productline별 구매자 수
select c.productline, count(distinct b.customernumber) BU
from orderdetails a
left join orders b
on a.ordernumber = b.ordernumber
left join products c
on a.productcode = c.productcode
group by 1;

select d.churn_type, c.productline, count(distinct b.customernumber) BU
from orderdetails a
left join orders b
on a.ordernumber = b.ordernumber
left join products c
on a.productcode = c.productcode
left join churn_list d
on b.customernumber = d.customernumber
group by 1, 2
order by 1, 3 desc;