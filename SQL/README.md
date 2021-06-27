도서 : SQL로 맛보는 데이터 전처리 분석

- MySQL은 기본적으로 대문자, 소문자 구분을 하지 않는다.
- 종료할 때 [File] - [Close Connection Tab] (`Ctrl`+`Shift`+`F4`)로 반드시 Disconnect 하여야 데이터베이스가 손상되지 않는다.



# 파이썬 연동

- `pip install PyMySQL==1.0.0`



## MySQL 연결

```python 
import pymysql.cursors

# localhost or 127.0.0.0
connection = pymysql.connect(host='localhost',
        user='root',
        password='password',
        db='dbname',
        charset='utf8',
        cursorclass=pymysql.cursors.DictCursor)
try:
    with connection.cursor() as cursor:
        # Read a single record
        #sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
        sql = "sql code;"
        cursor.execute(sql)
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()
```



## 데이터를 pandas로 읽기

```python
import pandas as pd

conn = pymysql.connect(host='localhost', user='root', 
                       password='password', db='dbname', charset='utf8',
                       autocommit=True, cursorclass=pymysql.cursors.DictCursor)
try:
   with conn.cursor() as curs:
      sql = "sql code;"
      curs.execute(sql)
      rs = curs.fetchall()

      # DB에서 받아온 값을 DataFrame에 넣음
      df = pd.DataFrame(rs)
      print(df)
finally:
   conn.close()
```

- `curs.fetchone()` : 커서가 있는 위치의 값만을 반환
- `curs.fetchall()` : 커서의 위치와 관계없이 모든 값을 반환
- `conn.close()` : 연결을 끊음



### 파이썬 pandas와 비교

https://pandas.pydata.org/pandas-docs/stable/getting_started/comparison/comparison_with_sql.html#compare-with-sql



# Chapter 2. SQL 문법

- `SELECT`, `DISTINCT`
- `USE`, `FROM`
- `WHERE`, `BETWEEN`, `IN`, `IS NULL`
- `GROUP BY`, `SUM`, `AVG`, `COUNT`, `CASE WHEN ... END`
- `LEFT JOIN`, `ON`, `INNER JOIN`, `FULL JOIN`
- `RANK`, `DENSE_RANK`, `ROW_NUMBER` + `OVER`
  - `PARTITION BY`
- `SUBQUERY`



# Chapter 3. 데이터 추가, 삭제, 갱신, 데이터 정합성

- `INSERT`, `DELETE`, `UPDATE`, `PROCEDURE`, `VIEW`
- 데이터 정합성 : 데이터들의 값이 일치함
  - 예) 전체 매출 = 각 연도별 매출의 합
- MECE (Mutually Exclusive Collectively Exhaustive) : 각 항목들이 상호 배타적이면서 모으면 완전하게 합쳐지는 것
- 항상 정합성을 확인하는 습관을 들여야한다.



# Chapter 4. 자동차 매출 데이터를 이용한 리포트 작성

- `left join ~ on`을 연습하기 좋은 예제
- `SUBSTR(칼럼, 위치, 길이)` : 문자열에서 원하는 부분만 가져오기
  - `select substr('abcde', 2, 3)` : bcd 출력
- `DISTINCT` : 중복값을 제외
  - `COUNT(DISTINCT column_name)` : 중복값을 제외한 개수 세기
- `CREATE TABLE DATA.NAME AS ` : `DATA`에 `NAME`이라는 명을 가진 표 생성 (이후에 `SELECT`문을 사용하여 테이블 생성)
- `SELECT`로 생성한 필드는 조건절 `WHERE`에서 사용할 수 없기 때문에 `SUBQUERY`를 이용한다.

```mysql
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
```

- subquery `from ()` 이후 필드 명을 지정해줘야 한다. (위처럼 a)
- `DATEDIFF( date1, date2 )` : date1 - date2를 반환



# Chapter 5. 상품 리뷰 데이터를 이용한 리포트 작성

- `FLOOR` : 소수점 첫째자리에서 내림
- `LIMIT 10` : 출력 결과를 10줄만 보여주기

```mysql
use mydata;

select `review text`,
case when `review text` like '%size%' then 1 else 0 end size_yn
from dataset2;
```

- `review text` column의 각 value에 `size`라는 단어가 포함되는지 확인
  - `%size%` : size라는 단어의 앞뒤로 글자가 있어도 추출

```mysql
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
```

- `sum(1)`과 `count(*)`은 같은 결과를 출력한다.
  - `sum(1)`은 row마다 1이라는 수를 생성하고 이를 모두 합한 결과를 의미

# Chapter 6. 식품 배송 데이터 분석

- `HAVING` : 조건절
  - `WHERE` : `FROM`에 위치한 테이블에만 조건을 걸 수 있음
  - `HAVING` : 그룹핑한 데이터에 조건을 생성
- `VARIANCE` : 분산 계산

