use mydata;

select country, stockcode, count(distinct customerid) bu,
sum(quantity*unitprice) sales
from dataset3
group by 1, 2
order by 3 desc, 4 desc;