use mydata;

# review text에 size라는 단어가 있는지 확인
select `review text`,
case when `review text` like '%size%' then 1 else 0 end size_yn
from dataset2;

select sum(case when `review text` like '%size%' then 1 else 0 end) n_size,
count(*) n_total
from dataset2;

select sum(case when `review text` like '%size%' then 1 else 0 end) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) n_tight,
count(*) n_total
from dataset2;

select `department name`,
sum(case when `review text` like '%size%' then 1 else 0 end) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) n_tight,
sum(1) n_total
from dataset2
group by 1;

select floor(age/10)*10 ageband,
`department name`,
sum(case when `review text` like '%size%' then 1 else 0 end) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) n_tight,
sum(1) n_total
from dataset2
group by 1, 2
order by 1, 2;

select floor(age/10)*10 ageband,
`department name`,
sum(case when `review text` like '%size%' then 1 else 0 end) / sum(1) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) / sum(1) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) / sum(1) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) / sum(1) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) / sum(1) n_tight
from dataset2
group by 1, 2
order by 1, 2;