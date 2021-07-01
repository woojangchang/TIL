use mydata;

select weekofyear(invoicedate) wk,
sum(quantity*unitprice) sales
from dataset3
group by 1
order by 1;