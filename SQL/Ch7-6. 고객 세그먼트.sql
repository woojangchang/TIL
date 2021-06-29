use mydata;

# 1. RFM

# a. FRM
# Recency : 제일 최근에 구입한 시기가 언제인가?
# Frequency : 어느 정도로 자주 구입했나?
# Monetary : 구입한 총 금액은 얼마인가?

select customerid,
max(invoicedate) mxdt
from dataset3
group by 1;

# recency
select customerid, datediff('2011-12-02', mxdt) recency
from (
select customerid,
max(invoicedate) mxdt
from dataset3
group by 1) a;

# frequency, monetary
select customerid, count(distinct invoiceno) frequency,
sum(quantity*unitprice) monetary
from dataset3
group by 1;

# RFM
select customerid, datediff('2011-12-02', mxdt) recency,
frequency, monetary
from (
select customerid, max(invoicedate) mxdt,
count(distinct invoiceno) frequency,
sum(quantity*unitprice) monetary
from dataset3
group by 1) a;

# 이후에 python에서 K Means Algorithm을 이용해 그룹핑

# 2. 재구매 Segment
# 동일한 상품을 2개 연도 연속 구매
select customerid, stockcode, count(distinct substr(invoicedate, 1, 4)) unique_yy
from dataset3
group by 1, 2;

select customerid, max(unique_yy) mx_unique_yy
from (
select customerid, stockcode, count(distinct substr(invoicedate, 1, 4)) unique_yy
from dataset3
group by 1, 2) a
group by 1;

select customerid,
case when mx_unique_yy >= 2 then 1 else 0 end repurchase_segment
from (
select customerid, max(unique_yy) mx_unique_yy
from (
select customerid, stockcode, count(distinct substr(invoicedate, 1, 4)) unique_yy
from dataset3
group by 1, 2) a
group by 1) a
group by 1;