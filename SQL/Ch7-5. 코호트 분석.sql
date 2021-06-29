use mydata;

# 코호트 분석 : 시간 흐름에 따라 사용자의 리텐션, 구매 패턴, 행동 패턴을 파악하는데 사용되는 분석

# 고객별 첫 구매일
select customerid,
min(invoicedate) mndt
from dataset3
group by 1;

# 각 고객의 주문 일자, 구매액
select customerid, invoicedate, unitprice*quantity sales
from dataset3;

# join
select *
from (
select customerid,
min(invoicedate) mndt
from dataset3
group by 1) a
left join
(select customerid, invoicedate, unitprice*quantity sales
from dataset3) b
on a.customerid = b.customerid;

select substr(mndt, 1, 7) mm,
timestampdiff(month, mndt, invoicedate) datediff,
count(distinct a.customerid) bu,
sum(sales) sales
from
(select customerid, min(invoicedate) mndt
from dataset3
group by 1) a
left join
(select customerid, invoicedate, unitprice*quantity sales
from dataset3) b
on a.customerid = b.customerid
group by 1, 2;