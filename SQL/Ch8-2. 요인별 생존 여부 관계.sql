use mydata;

# 1. 성별
select *
from dataset4 limit 10;

# survived 1 : 생존, 0 : 사망

select sex, count(passengerid) n_passengers,
sum(survived) n_survived
from dataset4
group by 1;

# 비중
select sex, count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_ratio
from dataset4
group by 1;

# 2. 연령, 성별
select floor(age/10)*10 ageband,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1
order by 1;

select floor(age/10)*10 ageband,
sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
order by 2, 1;

# 남성, 여성 따로 테이블 생성 후 나이대별 생존률 비교
select floor(age/10)*10 ageband,
sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
having sex = 'male';

select floor(age/10)*10 ageband,
sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
having sex = 'female';

# 두 테이블 조인
select a.ageband,
a.survived_rate male_survived_rate,
b.survived_rate female_survived_rate,
b.survived_rate - a.survived_rate survived_rate_diff
from (
select floor(age/10)*10 ageband,
sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
having sex = 'male') a
left join (
select floor(age/10)*10 ageband,
sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
having sex = 'female') b
on a.ageband = b.ageband
order by 1;

# 3. Pclass (객실 등급)
select pclass,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1
order by 1;

select pclass, sex,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2
order by 2, 1;

select pclass, sex, floor(age/10)*10 ageband,
count(passengerid) n_passengers,
sum(survived) n_survived,
sum(survived) / count(passengerid) survived_rate
from dataset4
group by 1, 2, 3
order by 2, 1;