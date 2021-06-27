use instacart;

# 1. 전체 주문 건수
select count(distinct order_id) f
from orders;

# 2. 구매자 수
select count(distinct user_id) bu
from orders;

# 3. 상품별 주문 건수
select *
from order_products__prior a
left join products b
on a.product_id = b.product_id;

# 4. 장바구니에 가장 먼저 넣는 상품 10개
select product_id,
case when add_to_cart_order = 1 then 1 else 0 end f_1st
from order_products__prior;

select product_id,
sum(case when add_to_cart_order = 1 then 1 else 0 end) f_1st
from order_products__prior
group by 1;

select *,
row_number() over(order by f_1st desc) rnk
from (
select product_id,
sum(case when add_to_cart_order = 1 then 1 else 0 end) f_1st
from order_products__prior
group by 1) a;

select *
from (
select *,
row_number() over(order by f_1st desc) rnk
from (
select product_id,
sum(case when add_to_cart_order = 1 then 1 else 0 end) f_1st
from order_products__prior
group by 1) a) a
where rnk <= 10;

select product_id,
sum(case when add_to_cart_order = 1 then 1 else 0 end) f_1st
from order_products__prior
group by 1
order by 2 desc limit 10;

# 5. 시간별 주문 건수
select order_hour_of_day,
count(distinct order_id) f
from orders
group by 1
order by 1;

# 6. 첫 구매 후 다음 구매까지 걸린 평균 일수
select avg(days_since_prior_order) avg_recency
from orders
where order_number = 2;

# 7. 주문 건당 평균 구매 상품 수(UPT, Unit Per Transaction)
select count(product_id) / count(distinct order_id) UPT
from order_products__prior;

# 8. 인당 주문 건수
select count(distinct order_id) / count(distinct user_id) avg_f
from orders;

# 9. 재구매율이 높은 상품 10개
# 상품별 재구매율 계산
select product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior
group by 1;

# 재구매율로 랭크 열 생성
select *,
row_number() over(order by ret_ratio desc) rnk
from (
select product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior
group by 1) a;

# TOP 10
select *
from (
select *,
row_number() over(order by ret_ratio desc) rnk
from (
select product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior
group by 1) a) base
where rnk <= 10;

# 10. department별 재구매율 높은 상품 10개
select *
from (
select *,
row_number() over(order by ret_ratio desc) rnk
from (
select c.department,
product_id,
sum(case when reordered = 1 then 1 else 0 end) / count(*) ret_ratio
from order_products__prior a
left join products b
on a.product_id = b.product_id
left join departments c
on b.department_id = c.departmnet_id
group by 1, 2) a) a
where rnk <= 10;