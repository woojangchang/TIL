use mydata;

# 2010년 대비 2011에 판매 수량이 20% 증가한 상품 찾기

# 1. 2011 상품별 판매 수량
select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2011'
group by 1;

# 2. 2010 상품별 판매 수량
select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2010'
group by 1;

# 둘 결합
select *
from
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2011'
group by 1) a
left join
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2010'
group by 1) b
on a.stockcode = b.stockcode;

# 증가율
select a.stockcode, a.qty, b.qty, a.qty/b.qty-1 qty_increase_rate
from 
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2011'
group by 1) a
left join
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2010'
group by 1) b
on a.stockcode = b.stockcode;

# 증가율 20% 이상인 경우 : subquery로 증가율을 where에 사용
select *
from 
(select a.stockcode, a.qty qty_2011, b.qty qty_2010, a.qty/b.qty-1 qty_increase_rate
from 
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2011'
group by 1) a
left join
(select stockcode, sum(quantity) qty
from dataset3
where substr(invoicedate, 1, 4) = '2010'
group by 1) b
on a.stockcode = b.stockcode) base
where qty_increase_rate >= 1.2;
