use classicmodels;

create table PRODUCT_SALES as
select d.productname,
sum(quantityordered*priceeach) SALES
from orders a
left join customers b
on a.customernumber = b.customernumber
left join orderdetails c
on a.ordernumber = c.ordernumber
left join products d
on c.productcode = d.productcode
where b.country = 'USA'
group by 1;

select *
from
(select *,
row_number() over(order by sales desc) RNK
from product_sales) a
where rnk <=5
order by rnk;