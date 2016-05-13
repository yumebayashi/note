Title: splitting words into letters in Java
Date: 2016-05-13
Category: tech
Tags: java
Slug: 2015-05-13-java-split
Author: yumebayashi

* -java7

```
"hoge".split("");
// ["", "h", "o", "g", "e"]
"hoge".split("(?<=.)");
// ["h", "o", "g", "e"]
```

* java8-

```
"hoge".split("");
// ["h", "o", "g", "e"]
```
