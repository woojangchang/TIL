use mydata;

# 1. 고객별 첫 구매일
select customerid, min(invoicedate) mndt
from dataset3
group by 1;

# 2. 일자별 첫 구매 고객 수
select mndt, count(distinct customerid) bu
from (
select customerid, min(invoicedate) mndt
from dataset3
group by 1) a
group by mndt;