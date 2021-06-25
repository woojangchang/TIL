use classicmodels;

# 1. 국가별, 도시별 매출액
# customers의 country, city 열 사용
select country, city, priceeach*quantityordered
from orders a
left join orderdetails b
on a.ordernumber = b.ordernumber
left join customers c
on a.customernumber = c.customernumber;

select country, city, sum(priceeach*quantityordered) SALES
from orders a
left join orderdetails b
on a.ordernumber = b.ordernumber
left join customers c
on a.customernumber = c.customernumber
group by 1, 2
order by 1, 2;

# 2. 북미 vs 비북미 비교
# CASE WHEN 사용
select case when country in ('usa', 'canada') then 'North America'
else 'Others' end country_grp
from customers;

select case when country in ('usa', 'canada') then 'North America'
else 'Others' end country_grp, sum(priceeach*quantityordered) SALES
from orders a
left join orderdetails b
on a.ordernumber = b.ordernumber
left join customers c
on a.customernumber = c.customernumber
group by 1
order by 2 desc;

# 3. 매출 top 5 국가 및 매출
# STAT이라는 테이블 생성
create table classicmodels.STAT as
select c.country, sum(priceeach*quantityordered) as SALES
from orders a
left join orderdetails b
on a.ordernumber = b.ordernumber
left join customers c
on a.customernumber = c.customernumber
group by 1
order by 2 desc;

select *
from stat;

select country, sales, dense_rank() over(order by sales desc) RNK
from stat;

create table stat_rnk as
select country, sales, dense_rank() over(order by sales desc) RNK
from stat;

select *
from stat_rnk;

select *
from stat_rnk
where rnk between 1 and 5;

# SUBQUERY를 이용하여 TABLE을 생성하지 않고 원하는 데이터 불러오기
select *
from
(select country, sales, dense_rank() over(order by sales desc) RNK
from
(select c.country, sum(priceeach*quantityordered) as sales
from orders a
left join orderdetails b
on a.ordernumber = b.ordernumber
left join customers c
on a.customernumber = c.customernumber
group by 1) a) a
where rnk <= 5;