use mydata;

# year-1이 원래의 year와 같은 값이 있으면 2년 연속 구매했다고 볼 수 있음
select a.country, substr(a.invoicedate, 1, 4) YY,
count(distinct b.customerid) / count(distinct a.customerid) retention_rate
from 
(select distinct country, invoicedate, customerid
from dataset3) a
left join
(select distinct country, invoicedate, customerid
from dataset3) b
on substr(a.invoicedate, 1, 4) = substr(b.invoicedate, 1, 4) -1
and a.country = b.country
and a.CustomerID = b.CustomerID
group by 1, 2
order by 1, 2;