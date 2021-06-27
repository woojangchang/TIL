use instacart;

# 1. 10분위 분석
select *,
row_number() over(order by f desc) rnk
from
(select user_id,
count(distinct order_id) f 
from orders
group by 1) a;

select count(distinct user_id)
from
(select user_id,
count(distinct order_id) f 
from orders
group by 1) a;

select *,
case when rnk <= 316 then 'Q1'
when rnk <= 632 then 'Q2'
when rnk <= 948 then 'Q3'
when rnk <= 1264 then 'Q4'
when rnk <= 1580 then 'Q5'
when rnk <= 1895 then 'Q6'
when rnk <= 2211 then 'Q7'
when rnk <= 2527 then 'Q8'
when rnk <= 2843 then 'Q9'
when rnk <= 3159 then 'Q10' end quantile
from
(select *,
row_number() over(order by f desc) rnk
from
(select user_id,
count(distinct order_id) f 
from orders
group by 1) a) a;

create temporary table user_quantile as
select *,
case when rnk <= 316 then 'Q1'
when rnk <= 632 then 'Q2'
when rnk <= 948 then 'Q3'
when rnk <= 1264 then 'Q4'
when rnk <= 1580 then 'Q5'
when rnk <= 1895 then 'Q6'
when rnk <= 2211 then 'Q7'
when rnk <= 2527 then 'Q8'
when rnk <= 2843 then 'Q9'
when rnk <= 3159 then 'Q10' end quantile
from
(select *,
row_number() over(order by f desc) rnk
from
(select user_id,
count(distinct order_id) f 
from orders
group by 1) a) a;

select quantile, sum(f) f
from user_quantile
group by 1;

select sum(f) from user_quantile;

select quantile, sum(f)/3220 f
from user_quantile
group by 1;