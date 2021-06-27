use instacart;

# 상품별 재구매율
select *
from (
select *,
row_number() over(order by ret_ratio desc) rnk
from (
select product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior
group by 1) a) a;

create temporary table product_repurchase_quantile as
select a.product_id,
case when rnk <= 929 then 'Q1'
when rnk <= 1858 then 'Q2'
when rnk <= 2786 then 'Q3'
when rnk <= 37158 then 'Q4'
when rnk <= 4644 then 'Q5'
when rnk <= 5573 then 'Q6'
when rnk <= 6502 then 'Q7'
when rnk <= 7430 then 'Q8'
when rnk <= 8359 then 'Q9'
when rnk <= 9288 then 'Q10' end rnk_grp
from
(select *,
row_number() over(order by ret_ratio desc) rnk
from
(select product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior
group by 1) a) a
group by 1, 2;

create temporary table order_products__prior2 as
select product_id,
days_since_prior_order
from order_products__prior a
inner join orders b
on a.order_id = b.order_id;

select a.rnk_grp,
a.product_id,
variance(days_since_prior_order) var_days
from product_repurchase_quantile a
left join order_products__prior2 b
on a.product_id = b.product_id
group by 1, 2
order by 1;

select rnk_grp,
avg(var_days) avg_var_days
from (
select a.rnk_grp,
a.product_id,
variance(days_since_prior_order) var_days
from product_repurchase_quantile a
left join order_products__prior b
on a.product_id = b.product_id
left join orders c
on b.order_id = c.order_id
group by 1, 2) a
group by 1
order by 1;