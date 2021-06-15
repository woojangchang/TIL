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
- `RANK`, `DENSE_RANK`, `ROW_NUMBER`
- `SUBQUERY`

