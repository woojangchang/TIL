use mydata;

# 1. Department Nmae, Clothing Nmae별 평균 평점 계산
select `department name`, `clothing id`, avg(rating) avg_rate
from dataset2
group by 1, 2;

# 2. Department별 순위 생성
select *, row_number() over(partition by `department name`
order by avg_rate) rnk
from (
select `department name`, `clothing id`, avg(rating) avg_rate
from dataset2
group by 1, 2) a;

# 3. 1~10위 데이터 조회
select *
from (
select *, row_number() over(partition by `department name`
order by avg_rate) rnk
from (
select `department name`, `clothing id`, avg(rating) avg_rate
from dataset2
group by 1, 2) a) a
where rnk <= 10;

# a. Department별 평균 평점이 낮은 10개 상품
create temporary table stat as
select *
from (
select *, row_number() over(partition by `department name`
order by avg_rate) rnk
from (
select `department name`, `clothing id`, avg(rating) avg_rate
from dataset2
group by 1, 2) a) a
where rnk <= 10;

select `clothing id`
from stat
where `department name` = 'bottoms';

# 위의 clothing id에 해당하는 리뷰 내용 보기
select *
from dataset2
where `clothing id` in
(select `clothing id`
from stat
where `department name` = 'bottoms');