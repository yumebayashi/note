Title:RedShift Query Tips
Date: 2016-05-09
Category: tech
Tags: redshift
Slug: 2016-05-09-redshift-query-tips
Author: yumebayashi




* Confirm table definition

```
select * from pg_table_def where tablename = 'target_table';
```

* Check running query and its pid
    * terminate query -> `cancel {pid}`

```
select pid,starttime, left(query,50) from stv_recents where status='Running';
```

* Check whether the table needs to be vacuumed or not

```
/** 0.not vacuumed table */
select
  '0_not_sorted' as status,
  sum_result.tablename,
  sum_result.sorted_rows,
  sum_result.rows,
  cast(0 as decimal(5,3)) as sort_percentage
from
(select
  trim(name) as tablename,
  sum(sorted_rows) as sorted_rows,
  sum(rows) as rows
from
  stv_tbl_perm
group by name
order by name) sum_result
where
  sorted_rows = 0
UNION ALL
/** 1.vacuumed table */
select
  '1_sorted' as status,
  sum_result.tablename,
  sum_result.sorted_rows,
  sum_result.rows,
  cast(
    cast(sum_result.sorted_rows as double precision) / cast(sum_result.rows as double precision)
    as decimal(5,3)
  ) as sort_percentage
from
(select
  trim(name) as tablename,
  sum(sorted_rows) as sorted_rows,
  sum(rows) as rows
from
  stv_tbl_perm
group by name
order by name) sum_result
where
  sorted_rows != 0
order by
  status asc,
  sort_percentage asc,
  rows desc;
```

returns like below

```
    status    |             tablename              | sorted_rows |    rows     | sort_percentage
--------------+------------------------------------+-------------+-------------+-----------------
 0_not_sorted | hogehoge_table_0                   |           0 |    40980633 |           0.000
 0_not_sorted | hogehoge_table_1                   |           0 |      108008 |           0.000
 0_not_sorted | hogehoge_table_2                   |           0 |        5002 |           0.000
 0_not_sorted | hogehoge_table_3                   |           0 |        4000 |           0.000
 0_not_sorted | hogehoge_table_4                   |           0 |        1480 |           0.000
 1_sorted     | hogehoge_table_5                   |        1586 |       17003 |           0.093
 1_sorted     | hogehoge_table_6                   |    21258371 |   170611094 |           0.125
 1_sorted     | hogehoge_table_7                   |           1 |           2 |           0.500
 1_sorted     | hogehoge_table_8                   |     2037917 |     3253190 |           0.626

```
