Title:Export results with CSV files with MySQL, Postgres
Date: 2016-09-12
Category: tech
Tags: mysql,postgres
Author: yumebayashi

## Environments
### db
* postgres:9.4.4
* mysql5.6.26

### db-config
* user:hoge
* password:fuga
* host:localhost
* database:mydb



## Postgres
`psql -h localhost -U hoge mydb -c "select id,name from users" -A -F, -t > user.csv`

### option

```
-A, --no-align : unaligned table output mode
-F, --field-separator=STRING : field separator for unaligned output (default: "|")
-t, --tuples-only : print rows only(ignore header)
```

*if you want to skip password request `Password for user hoge:`  
add below file

dir:`$HOME/.pgpass`  
file format:`[host]:[port]:[database]:[user]:[pass]`  
ex) `localhost:5432:mydb:hoge:huga`  
permission:`chmod 600 $HOME/.pgpass`  




## MySQL
`mysql -uhoge -phuga -hlocalhost mydb -e"select id,name from users" | tr '\t' ',' > user.csv`

