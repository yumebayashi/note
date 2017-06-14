Title: Replace tab with comma using sed on MacOS 
Date: 2017-06-14
Category: tech
Tags: linux
Author: yumebayashi


mac os doesn't recognize `\t` as tab charactor. 
```
sed -e 's/[[:cntrl:]]/,/g' text
```
