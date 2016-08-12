Title:Install Mecab
Date: 2016-08-12
Category: tech
Tags:mecab
Author: yumebayashi


### Download

Download mecab core and dictionary.  
[http://taku910.github.io/mecab/#download](http://taku910.github.io/mecab/#download)

files are on google drive, if you want to use cli, need to add option like this.

```
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7cENtOXlicTFaRUE' -O mecab-0.996.tar.gz
wget 'https://drive.google.com/uc?export=download&id=0B4y35FiV1wh7MWVlSDBCSXZMTXM' -O mecab-ipadic-2.7.0-20070801.tar.gz 
```

### Install Mecab core

```
tar zxfv mecab-0.996.tar.gz
cd mecab-0.996
./configure 
make
sudo make install
```

### Install Dictionary

default char set is `EUC-JP`
In this case, set char set `UTF8`
```
tar zxfv mecab-ipadic-2.7.0-20070801.tar.gz
cd mecab-ipadic-2.7.0-20070801
./configure --enable-utf8-only --with-charset=utf8
make
sudo make install
```

```
$ echo '今日はとても熱い' | mecab
今日	名詞,副詞可能,*,*,*,*,今日,キョウ,キョー
は	助詞,係助詞,*,*,*,*,は,ハ,ワ
とても	副詞,助詞類接続,*,*,*,*,とても,トテモ,トテモ
熱い	形容詞,自立,*,*,形容詞・アウオ段,基本形,熱い,アツイ,アツイ
EOS
```
