Title: Copy S3 to Redshift
Date: 2017-06-07
Category: tech
Tags: s3,redshift
Author: yumebayashi

copy table_name from 's3://bucket/path/' CREDENTIALS 
'aws_access_key_id=[access_key];aws_secret_access_key=[secret_key]' 
delimiter '\t' gzip maxerror 100;

When importing csv data from s3 to redshift,
We can use `delimiter ','` or `CSV` option.
There two options are different.
If we use "CSV" option, we can import such as this file 

```
123,aaa,bbb,"223,54234",111
345,aaa,bbb,777,666
```

If we use `delimiter ',' escape` option, we can import such as this file 

```
1,aaa
2,bbb\,bbb
3,ccc
4,ddd
```
