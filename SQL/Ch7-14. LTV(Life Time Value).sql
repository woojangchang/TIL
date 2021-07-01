use mydata;

# AMV(Average Member Value) : 인당 평균 지불 금액
# Retention Rate : 다음 Time Interval에 몇 %의 고객이 구매하는지
select count(b.customerid)/count(a.customerid) retention_rate
from (
select distinct customerid
from dataset3
where substr(invoicedate,1,4)='2010') a
left join (
select distinct customerid
from dataset3
where substr(invoicedate,1,4)='2011') b
on a.customerid = b.customerid;

# AMV
select sum(unitprice*quantity) / count(distinct customerid) amv
from dataset3
where substr(invoicedate,1,4)='2011';

# 예상 구매자 수
select count(distinct customerid) n_bu
from dataset3
where substr(invoicedate,1,4)='2011';

/*
2011년 총 구매자 수=765이므로 2012년 예상 구매자 수는 765*0.3509=268.43
2012년 예상 매출 = 268.43 * AMV = 185463
2011년 매출액+2011년 구매자의 2012년 예상 매출액 = 2011년 구매자의 LTV
*/

# 2011년 매출액
select sum(unitprice*quantity) sales_2011
from dataset3
where substr(invoicedate,1,4)='2011';

/*
2012년 예상 매출 = 528535 + 185463 = 713998
2011 구매자의 가치 LTV = 713998 / 765 = 933
*/