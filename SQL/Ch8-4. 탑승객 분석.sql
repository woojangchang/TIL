use mydata;

# 1. 출발지, 도착지별 승객 수
select boarded, destination, count(passengerid) n_passengers
from dataset4
group by 1, 2
order by 3 desc;

# 상위 5개 경로
select *,
row_number() over(order by n_passengers desc) rnk
from (select boarded, destination, count(passengerid) n_passengers
from dataset4
group by 1, 2
order by 3 desc) a;

# 임시 테이블로 저장
create temporary table route as
select boarded, destination
from (
select *,
row_number() over(order by n_passengers desc) rnk
from (select boarded, destination, count(passengerid) n_passengers
from dataset4
group by 1, 2
order by 3 desc) a) base
where rnk between 1 and 5;

# 경로에 해당하는 승객 이름
select name_wiki, a.boarded, a.destination
from dataset4 a
inner join
route b
on a.boarded = b.boarded
and a.destination = b.destination;

# 2. Hometown별 탑승객 수 및 생존율
select hometown,
sum(1) n_passengers,
sum(survived)/sum(1) survived_ratio
from dataset4
group by 1;

# 탑승객 수가 10명 이상이면서 생존률 0.5 이상
select hometown,
sum(1) n_passengers,
sum(survived)/sum(1) survived_ratio
from dataset4
group by 1
having sum(1) >= 10 and survived_ratio >= 0.5;