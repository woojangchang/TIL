use mydata;

# 1. 승선 항구별 승객 수
select embarked,
count(passengerid) n_passengers
from dataset4
group by 1
order by 1;

# 2. 승선 항구별, 성별 승객 수
select embarked, sex,
count(passengerid) n_passengers
from dataset4
group by 1, 2 
order by 1, 2;

# 3. 승선 항구별, 성별 승객 비중(%)
select a.embarked,
a.sex,
a.n_passengers,
b.n_passengers n_passengers_tot,
a.n_passengers / b.n_passengers passengers_rat
from (
select embarked, sex,
count(passengerid) n_passengers
from dataset4
group by 1, 2) a
left join (
select embarked,
count(passengerid) n_passengers
from dataset4
group by 1) b
on a.embarked = b.embarked;