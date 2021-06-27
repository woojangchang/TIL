use instacart;

select product_id,
sum(reordered) / sum(1) reordered_rate,
count(distinct order_id) f
from order_products__prior
group by product_id
order by reordered_rate desc;

select a.product_id,
sum(reordered) / sum(1) reordered_rate,
count(distinct order_id) f
from order_products__prior a
left join products b
on a.product_id = b.product_id
group by product_id
having count(distinct order_id) > 10;

select a.product_id,
b.product_name,
sum(reordered) / sum(1) reordered_rate,
count(distinct order_id) f
from order_products__prior a
left join products b
on a.product_id = b.product_id
group by 1, 2
having count(distinct order_id) > 10;
