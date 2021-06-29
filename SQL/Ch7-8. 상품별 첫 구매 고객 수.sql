use mydata;

# 1. 고객별, 상품별 첫 구매 일자
select customerid, stockcode, min(invoicedate) mndt
from dataset3
group by 1, 2;

# 2. 고객별 구매와 기준 순위 생성(랭크)
select *,
row_number() over(partition by customerid order by mndt) rnk
from (
select customerid, stockcode, min(invoicedate) mndt
from dataset3
group by 1, 2) a;

# a. 고객별 첫 구매 내역 조회
select *
from (
select *,
row_number() over(partition by customerid order by mndt) rnk
from (
select customerid, stockcode, min(invoicedate) mndt
from dataset3
group by 1, 2) a) a
where rnk = 1;

# b. 상품별 첫 구매 고객 수 집계
select stockcode, count(distinct customerid) first_bu
from (
select *
from (
select *,
row_number() over(partition by customerid order by mndt) rnk
from (
select customerid, stockcode, min(invoicedate) mndt
from dataset3
group by 1, 2) a) a
where rnk = 1) a
group by 1
order by 2 desc;