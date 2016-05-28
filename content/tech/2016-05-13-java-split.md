Title: Splitting words into letters in Java
Date: 2016-05-13
Tags: java

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
