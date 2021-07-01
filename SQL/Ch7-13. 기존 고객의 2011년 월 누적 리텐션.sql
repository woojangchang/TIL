use mydata;

# 기존 고객
select customerid
from dataset3
group by 1
having min(substr(invoicedate, 1, 4))='2010';

# 기존 고객의 2011년 구매 내역
select *
from dataset3
where customerid in
(select customerid
from dataset3
group by 1
having min(substr(invoicedate,1,4))='2010')
and substr(invoicedate,1,4)='2011';

# 고객별 2011년 첫 구매 월
select customerid, substr(invoicedate,1,7) mm
from (
select *
from dataset3
where customerid in
(select customerid
from dataset3
group by 1
having min(substr(invoicedate,1,4))='2010')
and substr(invoicedate,1,4)='2011') a
group by 1;

select mm, count(customerid) n_customers
from (
select customerid, substr(invoicedate,1,7) mm
from (
select *
from dataset3
where customerid in
(select customerid
from dataset3
group by 1
having min(substr(invoicedate,1,4))='2010')
and substr(invoicedate,1,4)='2011') a
group by 1, 2) a
group by 1
order by 1;