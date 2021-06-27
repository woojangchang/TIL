use mydata;

select `clothing id`,
sum(case when `review text` like '%size%' then 1 else 0 end) n_size
from dataset2
group by 1;

select `clothing id`,
sum(case when `review text` like '%size%' then 1 else 0 end) n_size_t,
sum(case when `review text` like '%size%' then 1 else 0 end) / sum(1) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) / sum(1) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) / sum(1) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) / sum(1) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) / sum(1) n_tight
from dataset2
group by 1;

create table size_stat as
select `clothing id`,
sum(case when `review text` like '%size%' then 1 else 0 end) n_size_t,
sum(case when `review text` like '%size%' then 1 else 0 end) / sum(1) n_size,
sum(case when `review text` like '%large%' then 1 else 0 end) / sum(1) n_large,
sum(case when `review text` like '%loose%' then 1 else 0 end) / sum(1) n_loose,
sum(case when `review text` like '%small%' then 1 else 0 end) / sum(1) n_small,
sum(case when `review text` like '%tight%' then 1 else 0 end) / sum(1) n_tight
from dataset2
group by 1;