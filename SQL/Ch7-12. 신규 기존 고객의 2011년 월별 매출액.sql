use mydata;

# 기존 고객 : 2010년에 구매한 고객
# 신규 고객 : 2011년에 구매한 고객

select case when substr(mndt, 1, 4) = '2011' then 'new' else 'exi' end new_exi,
customerid
from (
select customerid, min(invoicedate) mndt
from dataset3
group by 1) a;

select a.customerid, b.new_exi, a.invoicedate, a.unitprice, a.quantity
from dataset3 a
left join (
select case when substr(mndt, 1, 4) = '2011' then 'new' else 'exi' end new_exi,
customerid
from (
select customerid, min(invoicedate) mndt
from dataset3
group by 1) a) b
on a.customerid = b.customerid
where substr(a.invoicedate, 1, 4) = '2011';


select b.new_exi, substr(a.invoicedate, 1, 7) mm,
sum(a.unitprice*a.quantity) sales
from dataset3 a
left join (
select case when substr(mndt, 1, 4) = '2011' then 'new' else 'exi' end new_exi,
customerid
from (
select customerid, min(invoicedate) mndt
from dataset3
group by 1) a) b
on a.customerid = b.customerid
where substr(a.invoicedate, 1, 4) = '2011'
group by 1, 2;