use mydata;

select `department name`, 
floor(age/10)*10 ageband, 
avg(rating) avg_rate
from dataset2
group by 1, 2;

select *,
row_number() over(partition by ageband order by avg_rate) rnk
from (
select `department name`, 
floor(age/10)*10 ageband, 
avg(rating) avg_rate
from dataset2
group by 1, 2) a;

select *
from (
select *,
row_number() over(partition by ageband order by avg_rate) rnk
from (
select `department name`, 
floor(age/10)*10 ageband, 
avg(rating) avg_rate
from dataset2
group by 1, 2) a) a
where rnk = 1;