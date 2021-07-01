use mydata;

select customerid, count(distinct invoicedate) f_date
from dataset3
group by 1;

select sum(case when f_date = 1 then 1 else 0 end) / sum(1) bounc_rate
from (
select customerid, count(distinct invoicedate) f_date
from dataset3
group by 1) a;

# 국가별
select country, sum(case when f_date = 1 then 1 else 0 end) / sum(1) bounc_rate
from (
select customerid, country, count(distinct invoicedate) f_date
from dataset3
group by 1) a
group by 1
order by 1;