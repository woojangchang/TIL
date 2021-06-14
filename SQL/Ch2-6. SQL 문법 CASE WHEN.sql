# CASE WHEN 또한 칼럼으로 가져온다.
select COUNTRY,
CASE WHEN COUNTRY IN ('USA', 'CANADA') THEN 'NORTH ARMERICA' ELSE 'OTHERS' END AS REGION
FROM classicmodels.customers;

SELECT CASE WHEN COUNTRY IN ('USA', 'CANADA') THEN 'NORTH AMERICA' ELSE 'OHTERS' END AS REGION,
COUNT(CUSTOMERNUMBER) AS N_CUSTOMERS
FROM classicmodels.CUSTOMERS
GROUP BY
CASE WHEN COUNTRY IN ('USA', 'CANADA') THEN 'NORTH AMERICA' ELSE 'OTHERS' END;

SELECT CASE WHEN COUNTRY IN ('USA', 'CANADA') THEN 'NORTH AMERICA' ELSE 'OHTERS' END AS REGION,
COUNT(CUSTOMERNUMBER) AS N_CUSTOMERS
FROM classicmodels.CUSTOMERS
GROUP BY 1; # SELECT한 첫번째 칼럼이 1, 두번째가 2
