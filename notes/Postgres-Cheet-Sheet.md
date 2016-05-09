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
insert into tmp_test (name,value1,value2,created_at) values
('a',11.111, 111.11, getdate()),
('b',22.222, 222.22, getdate() + interval '1 day'),
('c',33.333, 333.33, getdate() + interval '1 day 12 hour'),
('d',44.444, 444.44, getdate() - interval '1 year');

```
you can omit (name,value1,value2,created_at)
if the number of column you insert and the table has are same and know the order of the columns in the table.

```
select * from tmp_test order by name;
 name |  value1  |  value2   |     created_at
------+----------+-----------+---------------------
 a    | 11.11100 | 111.11000 | 2016-04-09 01:41:46
 b    | 22.22200 | 222.22000 | 2016-04-10 01:41:46
 c    | 33.33300 | 333.33000 | 2016-04-10 13:41:46
 d    | 44.44400 | 444.44000 | 2015-04-09 01:41:46
```

```
insert into tmp_test2 (name) select name from tmp_test
```

```
select * from tmp_test2;
 name | value1 | value2 | created_at
------+--------+--------+------------
 a    |        |        |
 b    |        |        |
 c    |        |        |
 d    |        |        |
```

```
create table tmp_test3 as select name,value1 from tmp_test;
```

```
select * from tmp_test3 order by name;
 name |  value1
------+----------
 a    | 11.11100
 b    | 22.22200
 c    | 33.33300
 d    | 44.44400
```
