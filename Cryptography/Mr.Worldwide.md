# Mr World Wide Pico 2019
```
A musician left us a message. What's it mean?
```
```
picoCTF{(35.028309, 135.753082)(46.469391, 30.740883)(39.758949, -84.191605)(41.015137, 28.979530)(24.466667, 54.366669)(3.140853, 101.693207)_(9.005401, 38.763611)(-3.989038, -79.203560)(52.377956, 4.897070)(41.085651, -73.858467)(57.790001, -152.407227)(31.205753, 29.924526)}
```

## Open Soruce Data

Data looks like Lat Long data punch into google maps and get.  (Use the first letter of each city name)

```
 1  k - Nakanocho, Kamigyo Ward, (K)yoto, Japan
 2  o - (O)desa, Odessa Oblast, Ukraine, 65000
 3  d - (D)ayton, OH 45402, United States
 4  i - (İ)stanbul, Hoca Paşa, 34110 Fatih/İstanbul, Turkey
 5  a - Hazza Bin Zayed the First St - (A)bu Dhabi - United Arab Emirates
 6  k - Unnamed Road, 50480 (K)uala Lumpur, Federal Territory of Kuala Lumpur, Malaysia _ after this one
 7  a - Unnamed Road, (A)ddis Ababa, Ethiopia
 8  l - Av Nueva Loja, (L)oja, Ecuador
 9  a - Martelaarsgracht 5, 1012 TN (A)msterdam, Netherlands
10  s - (S)leepy Hollow, NY 10591, United States
11  k - (K)odiak, AK 99615, United States
12  a - Faculty Of Engineering, Al Azaritah WA Ash Shatebi, Qism Bab Sharqi, (A)lexandria Governorate, Egypt
```

## Solve

Flag is first letter of all the city names:

picoCTF{kodiak_alaska}