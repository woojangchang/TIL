# 장바구니 분석
# association rule
use mydata;

# 1. 가장 많이 판매된 2개 상품 조회
select stockcode, sum(quantity) qty
from dataset3
group by 1;

select *, row_number() over(order by qty desc) rnk
from (
select stockcode, sum(quantity) qty
from dataset3
group by 1) a;

select stockcode
from (
select *, row_number() over(order by qty desc) rnk
from (
select stockcode, sum(quantity) qty
from dataset3
group by 1) a) a
where rnk between 1 and 2;

# 2. 가장 많이 판매된 2개 상품을 모두 구매한 구매자가 구매한 상품
# HAVING 이용
create table bu_list as
select customerid
from dataset3
group by 1
having max(case when stockcode='84077' then 1 else 0 end)=1
and max(case when stockcode = '85123A' then 1 else 0 end) =1;

select distinct stockcode
from dataset3
where customerid in (select customerid from bu_list)
and StockCode not in ('84077', '85123A');