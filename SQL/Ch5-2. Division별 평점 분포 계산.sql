use mydata;

# 1. DIVISION별 평균 평점 계산
# a. DIVISION NAME별 평균 평점
select `division name`, avg(rating) avg_rate
from dataset2
group by 1
order by 2 desc;

# b. DEPARTMENT별 평균 평점
select `department name`, avg(rating) avg_rate
from dataset2
group by 1
order by 2 desc;

# c. Trend의 평점 3점 이하 리뷰
select *
from dataset2
where `department name`	= 'trend'
and rating <= 3;

# 2. case when
select case when age between 0 and 9 then '0009'
when age between 10 and 19 then '1019'
when age between 20 and 29 then '2029'
when age between 30 and 39 then '3039'
when age between 40 and 49 then '4049'
when age between 50 and 59 then '5059'
when age between 60 and 69 then '6069'
when age between 70 and 99 then '70+' end ageband,
age
from dataset2
where `department name`	= 'trend'
and rating <= 3;

# 3. FLOOR
select floor(age/10)*10 ageband, age
from dataset2
where `department name`	= 'trend'
and rating <= 3;

# a. Trend 평점 3점 이하 리뷰의 연령 분포
select floor(age/10)*10 ageband, count(*) cnt
from dataset2
where `department name`	= 'trend'
and rating <= 3
group by 1
order by 2 desc;

# b. Department별 연령별 리뷰 수
select floor(age/10)*10 ageband, count(*) cnt
from dataset2
where `department name`	= 'trend'
group by 1
order by 2 desc;

# c. 50대 3점 이하 Trend 리뷰
select *
from dataset2
where `department name`	= 'trend'
and rating <= 3
and age between 50 and 59 limit 10;