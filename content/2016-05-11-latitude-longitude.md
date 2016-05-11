Title:Calculate approximate distance between two latitude/longitude points by simple query
Date: 2016-05-11
Category: tech
Tags: sql
Slug: 2016-05-11-latitude-longitude
Author: yumebayashi



* make initial data set
```
CREATE TABLE tmp_test (
   name character varying(255),
   lat1 numeric(8,5),
   lng1 numeric(8,5),
   lat2 numeric(8,5),
   lng2 numeric(8,5)
)
```

```
INSERT INTO tmp_test VALUES
('tokyo-shinjuku',35.680605, 139.767351,35.689862,139.700253);
```

```
select * from tmp_test ;
      name      |   lat1   |   lng1    |   lat2   |   lng2
----------------+----------+-----------+----------+-----------
 tokyo-shinjuku | 35.68061 | 139.76735 | 35.68986 | 139.70025
```


### plan
* consider the Earth as sphere
* calculate m/degree for each lat/lng
* calculate the distance of each directions
* calculate the distance by Pythagorean theorem
  
* [Earth radius](https://en.wikipedia.org/wiki/Earth_radius)  
R : 6,371km = 6371000m  

Calculating the distance of latitude direction is simple.
$$ \frac{2\pi R}{360} abs(lat1 - lat2)  $$

Calculating the distance of longitude direction is a bit complicated.  
Radius varies by its latitude.  
<img src="/note/images/explain.png" width="300px">  
I fix the radius by the middle point of two latitudes.

$$ \frac{2\pi}{360} Rcos(\frac{\frac{(lat1 + lat2)}{2}\pi}{180}) abs(lng1 -lng2) $$

then apply Pythagorean theorem
$$  \sqrt{(\frac{2\pi R}{360} (lat1 - lat2))^2 + (\frac{2\pi}{360} Rcos(\frac{\frac{(lat1 + lat2)}{2}\pi}{180}) (lng1 -lng2))^2} $$
↓
$$ \frac{2\pi R}{360} \sqrt{(lat1 - lat2)^2 +  (cos(\frac{\frac{(lat1 + lat2)}{2}\pi}{180}) (lng1 -lng2))^2} $$

```
select *, 2 * pi() * 6371000 / 360 * sqrt(power((lat1-lat2),2) + power(cos((lat1 + lat2) / 2 * pi() /180) * (lng1-lng2),2)) as distance from tmp_test;

```
```
      name      |   lat1   |   lng1    |   lat2   |   lng2    |     distance
----------------+----------+-----------+----------+-----------+------------------
 tokyo-shinjuku | 35.68061 | 139.76735 | 35.68986 | 139.70025 | 6146.88718108597
```

