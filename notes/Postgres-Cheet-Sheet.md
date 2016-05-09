```
CREATE TABLE tmp_test (
   name character varying(255),
   value1 numeric(8,5),
   value2 numeric(8,5),
   created_at timestamp
)
```

### bulk insert & create table

```
INSERT INTO tmp_test (name,value1,value2,created_at) VALUES
('a',11.111, 111.11, getdate()),
('b',22.222, 222.22, getdate() + interval '1 day'),
('c',33.333, 333.33, getdate() + interval '1 day 12 hour'),
('d',44.444, 444.44, getdate() - interval '1 year');

```
you can omit `(name,value1,value2,created_at)`
if the number of column you insert and the table has are same and know the order of the columns in the table.

```
SELECT * FROM tmp_test ORDER BY name;
 name |  value1  |  value2   |     created_at
------+----------+-----------+---------------------
 a    | 11.11100 | 111.11000 | 2016-04-09 01:41:46
 b    | 22.22200 | 222.22000 | 2016-04-10 01:41:46
 c    | 33.33300 | 333.33000 | 2016-04-10 13:41:46
 d    | 44.44400 | 444.44000 | 2015-04-09 01:41:46
```
---
```
INSERT INTO tmp_test2 (name) SELECT name FROM tmp_test
```

```
SELECT * FROM tmp_test2;
 name | value1 | value2 | created_at
------+--------+--------+------------
 a    |        |        |
 b    |        |        |
 c    |        |        |
 d    |        |        |
```
---
```
CREATE TABLE tmp_test3 AS SELECT name,value1 FROM tmp_test;
```

```
SELECT * FROM tmp_test3 ORDER BY name;
 name |  value1
------+----------
 a    | 11.11100
 b    | 22.22200
 c    | 33.33300
 d    | 44.44400
```
### window function

* make initial data set
```
INSERT INTO tmp_test (name,value1,value2,created_at) VALUES
('a',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('a',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('a',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('a',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('b',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('b',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('b',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('b',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('c',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('c',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('c',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('c',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('d',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('d',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('d',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000)),
('d',random() * 100, random() * 1000, getdate() - (interval '1 second') * floor(random() * 10000));
```

```
SELECT * FROM tmp_test ORDER BY name,created_at;
 name |  value1  |  value2   |     created_at
------+----------+-----------+---------------------
 a    |  2.79153 | 283.88840 | 2016-05-09 02:48:03
 a    | 97.73130 | 690.71222 | 2016-05-09 04:04:00
 a    | 55.56720 | 648.48164 | 2016-05-09 04:07:29
 a    | 65.30828 |  82.12131 | 2016-05-09 04:54:15
 b    | 91.00008 | 520.90237 | 2016-05-09 03:00:32
 b    | 52.57934 | 994.37051 | 2016-05-09 04:10:30
 b    | 94.97609 | 991.10283 | 2016-05-09 04:23:42
 b    | 80.45081 | 281.75994 | 2016-05-09 04:40:12
 c    | 76.16128 | 781.77351 | 2016-05-09 02:59:04
 c    | 27.75059 | 738.44508 | 2016-05-09 03:57:41
 c    | 35.67327 | 322.03239 | 2016-05-09 04:08:57
 c    | 94.81574 | 294.11711 | 2016-05-09 04:56:16
 d    | 79.91998 | 862.42894 | 2016-05-09 03:20:00
 d    | 60.94562 | 388.22237 | 2016-05-09 03:20:56
 d    | 67.12917 | 952.42817 | 2016-05-09 04:46:49
 d    | 24.18907 | 299.34541 | 2016-05-09 05:00:30
```
* add flag by the difference between value1 and value2

```
SELECT *,
       (CASE
            WHEN diff > 500 THEN 1
            WHEN diff > 300 THEN 2
            WHEN diff > 100 THEN 3
            ELSE 0
        END) AS type
FROM
  (SELECT *, abs(value1 - value2) AS diff
   FROM tmp_test
   ORDER BY name,created_at)
```

```
 name |  value1  |  value2   |     created_at      |   diff    | type
------+----------+-----------+---------------------+-----------+------
 a    |  2.79153 | 283.88840 | 2016-05-09 02:48:03 | 281.09687 |    3
 a    | 97.73130 | 690.71222 | 2016-05-09 04:04:00 | 592.98092 |    1
 a    | 55.56720 | 648.48164 | 2016-05-09 04:07:29 | 592.91444 |    1
 a    | 65.30828 |  82.12131 | 2016-05-09 04:54:15 |  16.81303 |    0
 b    | 91.00008 | 520.90237 | 2016-05-09 03:00:32 | 429.90229 |    2
 b    | 52.57934 | 994.37051 | 2016-05-09 04:10:30 | 941.79117 |    1
 b    | 94.97609 | 991.10283 | 2016-05-09 04:23:42 | 896.12674 |    1
 b    | 80.45081 | 281.75994 | 2016-05-09 04:40:12 | 201.30913 |    3
 c    | 76.16128 | 781.77351 | 2016-05-09 02:59:04 | 705.61223 |    1
 c    | 27.75059 | 738.44508 | 2016-05-09 03:57:41 | 710.69449 |    1
 c    | 35.67327 | 322.03239 | 2016-05-09 04:08:57 | 286.35912 |    3
 c    | 94.81574 | 294.11711 | 2016-05-09 04:56:16 | 199.30137 |    3
 d    | 79.91998 | 862.42894 | 2016-05-09 03:20:00 | 782.50896 |    1
 d    | 60.94562 | 388.22237 | 2016-05-09 03:20:56 | 327.27675 |    2
 d    | 67.12917 | 952.42817 | 2016-05-09 04:46:49 | 885.29900 |    1
 d    | 24.18907 | 299.34541 | 2016-05-09 05:00:30 | 275.15634 |    3
```

* add sequential row number order by created_at for each name
```
SELECT * , row_number() over(PARTITION BY name ORDER BY created_at asc) FROM tmp_test ORDER BY name, created_at ASC;
 name |  value1  |  value2   |     created_at      | row_number
------+----------+-----------+---------------------+------------
 a    |  2.79153 | 283.88840 | 2016-05-09 02:48:03 |          1
 a    | 97.73130 | 690.71222 | 2016-05-09 04:04:00 |          2
 a    | 55.56720 | 648.48164 | 2016-05-09 04:07:29 |          3
 a    | 65.30828 |  82.12131 | 2016-05-09 04:54:15 |          4
 b    | 91.00008 | 520.90237 | 2016-05-09 03:00:32 |          1
 b    | 52.57934 | 994.37051 | 2016-05-09 04:10:30 |          2
 b    | 94.97609 | 991.10283 | 2016-05-09 04:23:42 |          3
 b    | 80.45081 | 281.75994 | 2016-05-09 04:40:12 |          4
 c    | 76.16128 | 781.77351 | 2016-05-09 02:59:04 |          1
 c    | 27.75059 | 738.44508 | 2016-05-09 03:57:41 |          2
 c    | 35.67327 | 322.03239 | 2016-05-09 04:08:57 |          3
 c    | 94.81574 | 294.11711 | 2016-05-09 04:56:16 |          4
 d    | 79.91998 | 862.42894 | 2016-05-09 03:20:00 |          1
 d    | 60.94562 | 388.22237 | 2016-05-09 03:20:56 |          2
 d    | 67.12917 | 952.42817 | 2016-05-09 04:46:49 |          3
 d    | 24.18907 | 299.34541 | 2016-05-09 05:00:30 |          4
```
* get values from a previous row in the table. To return a value from the next row, using the LEAD function. below two queries return the same result.(order in over function is inversed)
```
 SELECT * , LAG(created_at, 1) OVER(PARTITION BY name ORDER BY created_at DESC) FROM tmp_test;

 SELECT * , LEAD(created_at, 1) OVER(PARTITION BY name ORDER BY created_at ASC) FROM tmp_test;
```

```
 name |  value1  |  value2   |     created_at      |         lag
------+----------+-----------+---------------------+---------------------
 a    |  2.79153 | 283.88840 | 2016-05-09 02:48:03 | 2016-05-09 04:04:00
 a    | 97.73130 | 690.71222 | 2016-05-09 04:04:00 | 2016-05-09 04:07:29
 a    | 55.56720 | 648.48164 | 2016-05-09 04:07:29 | 2016-05-09 04:54:15
 a    | 65.30828 |  82.12131 | 2016-05-09 04:54:15 |
 b    | 91.00008 | 520.90237 | 2016-05-09 03:00:32 | 2016-05-09 04:10:30
 b    | 52.57934 | 994.37051 | 2016-05-09 04:10:30 | 2016-05-09 04:23:42
 b    | 94.97609 | 991.10283 | 2016-05-09 04:23:42 | 2016-05-09 04:40:12
 b    | 80.45081 | 281.75994 | 2016-05-09 04:40:12 |
 c    | 76.16128 | 781.77351 | 2016-05-09 02:59:04 | 2016-05-09 03:57:41
 c    | 27.75059 | 738.44508 | 2016-05-09 03:57:41 | 2016-05-09 04:08:57
 c    | 35.67327 | 322.03239 | 2016-05-09 04:08:57 | 2016-05-09 04:56:16
 c    | 94.81574 | 294.11711 | 2016-05-09 04:56:16 |
 d    | 79.91998 | 862.42894 | 2016-05-09 03:20:00 | 2016-05-09 03:20:56
 d    | 60.94562 | 388.22237 | 2016-05-09 03:20:56 | 2016-05-09 04:46:49
 d    | 67.12917 | 952.42817 | 2016-05-09 04:46:49 | 2016-05-09 05:00:30
 d    | 24.18907 | 299.34541 | 2016-05-09 05:00:30 |
```
* get the time difference(min) between current and previous row
```
SELECT *, EXTRACT(EPOCH FROM next - created_at) / 60  AS stay_min FROM (
SELECT * , LAG(created_at, 1) OVER(PARTITION BY name ORDER BY created_at DESC) AS next FROM tmp_test
)

WITH t AS (
SELECT * , LAG(created_at, 1) OVER(PARTITION BY name ORDER BY created_at DESC) AS next FROM tmp_test
) 
SELECT extract(epoch FROM next - created_at) / 60  AS stay_min FROM t;
```

```
 name |  value1  |  value2   |     created_at      |        next         |     stay_min
------+----------+-----------+---------------------+---------------------+-------------------
 a    |  2.79153 | 283.88840 | 2016-05-09 02:48:03 | 2016-05-09 04:04:00 |             75.95
 a    | 97.73130 | 690.71222 | 2016-05-09 04:04:00 | 2016-05-09 04:07:29 |  3.48333333333333
 a    | 55.56720 | 648.48164 | 2016-05-09 04:07:29 | 2016-05-09 04:54:15 |  46.7666666666667
 a    | 65.30828 |  82.12131 | 2016-05-09 04:54:15 |                     |
 b    | 91.00008 | 520.90237 | 2016-05-09 03:00:32 | 2016-05-09 04:10:30 |  69.9666666666667
 b    | 52.57934 | 994.37051 | 2016-05-09 04:10:30 | 2016-05-09 04:23:42 |              13.2
 b    | 94.97609 | 991.10283 | 2016-05-09 04:23:42 | 2016-05-09 04:40:12 |              16.5
 b    | 80.45081 | 281.75994 | 2016-05-09 04:40:12 |                     |
 c    | 76.16128 | 781.77351 | 2016-05-09 02:59:04 | 2016-05-09 03:57:41 |  58.6166666666667
 c    | 27.75059 | 738.44508 | 2016-05-09 03:57:41 | 2016-05-09 04:08:57 |  11.2666666666667
 c    | 35.67327 | 322.03239 | 2016-05-09 04:08:57 | 2016-05-09 04:56:16 |  47.3166666666667
 c    | 94.81574 | 294.11711 | 2016-05-09 04:56:16 |                     |
 d    | 79.91998 | 862.42894 | 2016-05-09 03:20:00 | 2016-05-09 03:20:56 | 0.933333333333333
 d    | 60.94562 | 388.22237 | 2016-05-09 03:20:56 | 2016-05-09 04:46:49 |  85.8833333333333
 d    | 67.12917 | 952.42817 | 2016-05-09 04:46:49 | 2016-05-09 05:00:30 |  13.6833333333333
 d    | 24.18907 | 299.34541 | 2016-05-09 05:00:30 |                     |
```

