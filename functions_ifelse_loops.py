################################################
# METİNSEL İFADELER (STRINGS)
################################################

# Dilimlenebilir
# Değiştirilemez
# İçerisinde karakterler barındırır.
# Bir liste gibi çalışır.

# Metinsel ifadeler tek tırnak, çift tırnak, üç tek tırnak veya üç çift tırnak ile yapılır.
cumle_1 = 'Hayaller, başarının çekirdeğidir.'
cumle_2 = "Hayaller, başarının çekirdeğidir."
cumle_3 = '''Hayaller, başarının çekirdeğidir.'''
cumle_4 = """Hayaller, başarının çekirdeğidir."""

# Case 1: Balıkesir'in höşmerimi meşhurdur.
mesaj_1 = "Balıkesir'in höşmerimi meşhurdur."
mesaj_2 = 'Balıkesir\'in höşmerimi meşhurdur.' # kaçış işareti kullandık
mesaj_3 = """Balıkesir'in höşmerimi meşhurdur."""
mesaj_4 = '''Balıkesir'in höşmerimi meşhurdur.'''

# İki dize birbiri ile toplama (+) operatörü ile birleştirilebilir.
x = "Merhaba"
y = "NTTDATA"
z = x + y
z = x + " " + y

# Python’da karakter dizeleri bir sayı gibi başka bir sayı ile çarpılabilir.
a = "Python "
a * 3

print(*"Python") # Bonus! # karakterleri bir liste gibi tek tek ayırır.

# Metinsel ifadeler üzerinde dilimleme işlemleri:

string_ifade = "Davulun sesi uzaktan hoş gelir"

# Case 1: "Davulun s" yazdır
string_ifade[:9]

# Case 2: "hoş" yazdır
string_ifade[21:24]

# Case 3: "Dvl" yazdır
string_ifade[:5:2]

# Case 5: 'rileg şoh'
string_ifade[::-1][:9]

# Metinsel İfade Metotları
dir(str())

# İşlem Metotları

# upper, lower, capitalize, title

# upper --> Metnin bütün harflerini büyütür.
"Davulun sesi uzaktan hoş gelir".upper()

# lower --> Metnin bütün harflerini küçültür.
"Davulun sesi uzaktan hoş gelir".lower()

# capitalize --> Metnin sadece ilk harfini büyük harf yapar.
"davulun sesi uzaktan hoş gelir".capitalize()

# title --> Metndeki kelimelerin ilk harflerini büyütür.
"Davulun sesi uzaktan hoş gelir".title()

# ljust, center, rjust

# ljust --> Bir metinsel ifadeyi belirtilen karakter ile belirtilen sayı kadar doldurur ve ifadeyi sola yaslar
"- NTTDATA -".ljust(50, "#")
len("- NTTDATA -".ljust(50, "#"))

# center --> Bir metinsel ifadeyi belirtilen karakter ile belirtilen sayı kadar doldurur ve ifadeyi ortalar
"- NTTDATA -".center(50, "#")

# rjust --> Bir metinsel ifadeyi belirtilen karakter ile belirtilen sayı kadar doldurur ve ifadeyi sağa yaslar
"- NTTDATA -".rjust(50, "#")

# strip, lstrip, rstrip

# lstrip --> Bir metinsel ifadenin solundaki fazla karakterlerin silmesini sağlar.
"- NTTDATA -".rjust(50, "#").lstrip("#")

# strip --> Bir metinsel ifadenin solundaki ve sağındaki fazla karakterlerin silmesini sağlar.
"- NTTDATA -".center(50, "#").strip("#")

# rstrip --> Bir metinsel ifadenin sağındaki fazla karakterlerin silmesini sağlar.
"- NTTDATA -".ljust(50, "#").rstrip("#")

# split, rsplit

# split - Bir metinsel ifadeyi belirtilen karakterden bölerek liste formatına dönüştürür.
"Davulun sesi uzaktan hoş gelir".split()
"Davulun sesi uzaktan hoş gelir".split(" ",2) # ilk 2 elemanı bölüp diğer elemanları tek eleman olarak getirdi.

# rsplit - Bir metinsel ifadeyi belirtilen karakterden sağdan bölerek liste formatına dönüştürür.
"Davulun sesi uzaktan hoş gelir".rsplit()
"Davulun sesi uzaktan hoş gelir".rsplit(" ", 2)

# join --> iterable(liste tuple, set gibi) nesneyi metinsel ifadeye çevirmeyi sağlar.
"_".join(['Davulun','sesi','uzaktan','hoş','gelir'])
" ".join([1, 2, 3]) # str veri tipi için kullanılır

# replace, maketrans, translate

# Case 1: bavul kelimesini davul kelimesine dönüştür.
"bavul".replace("b", "d")

# Case 2: tavan kelimesini tabak kelimesine dönüştür.
"tavan".replace("v", "b").replace("n", "k")

"tavan".translate(str.maketrans("vn", "bk"))

#############
# Sorgu Metotları
#############

# startswith, endswith
# startswith --> Bir metinsel ifadenin belirtilen ifade ile başlayıp başlamadığını sorgular.
"www.mercedes-benz.com.tr".startswith("www")

# endswith --> Bir metinsel ifadenin belirtilen ifade ile bitip bitmediğini sorgular.
"www.mercedes-benz.com.tr".endswith("tr")

# count --> String’de bulunan herhangi bir değerin, kaç adet bulunduğunu gösterir.
ornek = "Davulun sesi uzaktan hoş gelir"
ornek.count("u")

# islower, isupper, istitle
"DaVULUN SeSi UzAKTAn HoŞ gELiR".islower()
"DAVULuN SESi UZaKTAN HOŞ GELiR".isupper()
"Davulun Sesi Uzaktan Hoş Gelir".istitle()

# isnumeric, isalpha, isalnum

"12345".isnumeric()   # sayısal olup olmadığını sorar.
"12345A".isnumeric()

"MBO".isalpha()  # karakterlerden oluşup oluşmadığını sorar.
"1MBO".isalpha()

"D12345".isalnum()  # alpha numeric karakterlerden oluşup oluşmadığını sorar.

# isidentifier, isprintable, isspace
"Variable Name".isidentifier()  # bir metinsel ifadenin değişken adı olup olmuyacağını söyler.
"Variable_Name".isidentifier()

"Merhaba NTTDATA".isprintable()   # yazdırılabilir durumda mı
"Merhaba\tNTTDATA".isprintable()   # kaçış karakteri varsa False yapar.

" ".isspace()  # sadece boşluklardan oluşuyorsa True
"dfghjkl".isspace()  # Boşluk harici False

# f-Strings, format()
Santigrat = -273.15
sicaklik = "Ulaşılabilecek en düşük sıcaklık: " + Santigrat + "derecedir."
sicaklik = "Ulaşılabilecek en düşük sıcaklık: " + str(Santigrat) + " derecedir."

# f-Strings
sicaklik = f"Ulaşılabilecek en düşük sıcaklık: {Santigrat} derecedir."
sicaklik = f"Ulaşılabilecek en düşük sıcaklık: {Santigrat:.0f} derecedir."

# .format()
"Ulaşılabilecek en düşük sıcaklık: {} derecedir.".format(Santigrat)
print("Ulaşılabilecek en düşük sıcaklık: {} derecedir.".format(Santigrat))

################################################
# DÖNGÜLER
################################################
# Python'da döngüler (loop)bir kod dizisinin tekrar tekrar çalışmasını sağlayan yapılardır.
# 2 farklı döngü çeşidi bulunmaktadır. Bunlar “while” ve “for” döngüleridir.

teammates = ["rabia", "ozlem", "hasan", "anil", "hatice"]

teammates[0]
teammates[1]
teammates[2]

type(teammates[0])

teammates[0].capitalize()
teammates[1].capitalize()
teammates[2].capitalize()

for mate in teammates:
    print(mate)

for mate in teammates:
    print(mate.capitalize())

for mate in teammates:
    print(mate.capitalize() + " :")

for mate in teammates:
    print(f"Eski İsim: {mate}, Yeni İsim: {mate.capitalize()}")

###################
# Karar Yapıları ya da Koşul Durumları (if, elif, else)
###################
# Program içerisinde akışın yönünü değiştirmek için kullanılan yapılardır.

number = -10
if number > 0:
    print("Positive")
elif number < 0 :
    print("Negatif")
else:
    print ("Zero")

###################
# For Döngüsü
###################
# Sayılabilir nesne üzerinde tekrarlı işlemlerin yapılmasını sağlayan döngü yapısıdır.

# Case 1: 1-100 değeleri arasındaki 5'in katlarını ekrana yazdırmak.
for number in range(1, 101):
    if number % 5 == 0:
        print(number)

# Case 2: Liste içerisinde çift sayıları liste içerisinden çıkarıp yazdırmak
numbers = [1, 3, 6, 7, 9, 12, 19, 20, 23, 25]
for number in numbers:
    if number % 2 !=0:
        print(number)

# Case 3: Liste içerisinde çift sayıları liste içerisinden çıkarmak.
numbers = [1, 3, 6, 7, 9, 12, 19, 20, 23, 25]
for number in numbers:
    if number % 2 ==0:
        numbers.remove(number)
print(numbers)

###################
# While Döngüsü
###################
# Şarta bağlı olarak tekrarlı işlemlerin yapılmasını sağlayan döngü yapısıdır.

# Case: Bir sayacımız olsun 1-100 arası sayılardan 7'ye tam bölünenleri yazdırma.
sayac = 1
while sayac < 101:
    if sayac % 7 == 0:
        print(sayac)
    sayac += 1

###################
# Fibonacci Sayı Dizisi nedir?
# Fibonacci Dizisi, onun sayının kendisinden bir önceki sayı ile toplanması ile elde edilen sayılar serisidir.
# Fibonacci dizisi herhangi bir rakam ile başlayabilir.
# Örneğin → 0-1-1-2-3-5-8-13- bir Fibonacci Dizisidir ancak Fibonacci Dizisi, 4-4-8-12-20-32-52-84 olarak da devam edebilir.
###################

# Case: 0 ile 1000 arasındaki Fibonacci sayılarını bulan ve diziye atan program yazdırma
dizi = []

sayi_1 = 0
sayi_2 = 1

while sayi_2<1000:
    sayi_3 = sayi_1 + sayi_2
    sayi_1 = sayi_2
    sayi_2 = sayi_3

    dizi.append(sayi_2)
print(dizi)

#######################
# Enumerate: Otomatik Counter/Indexer ile for loop
#######################

# Case: Listedeki kişilerin index numaralarına göre iki gruba bölmek.
# Beklenen çıktı:
# 0 rabia
# 1 ozlem

teammates = ["rabia", "ozlem", "hasan", "anil", "omer", "hatice"]

for mate in teammates:
    print(mate)

for index, mate in enumerate(teammates):
    print(index, mate.capitalize())

xx = list(enumerate(teammates))
index, value = xx[1]

A = []  # 2'ye tam bölünen listesi
B = []  # 2'ye tam bölünmeyen listesi

for index, mate in enumerate(teammates):
    if index % 2 == 0:
        A.append(mate)
    else:
        B.append(mate)

A
B

################################################
# Break & Continue
################################################
# Döngü akışlarını değiştirmek için break ve continue ifadelerini kullanır.

#################
# continue: bir koşul yakalandığında iterasyondaki nesne atlanır.
#################

# Case 1:  1-50 değerleri arasındaki 5'e veya 6'ya tam bölünen sayılardan 15, 24, 30 hariç bölünebilen sayıları ekrana yazdırmak.

for number in range(1,51):
    if (number %5 == 0) or (number %6 == 0):
        if number in [15,24,30]:
            continue
        print(number)

# Case 2: Girilen 5 sayıdan 40'tan büyük olanları yazdırmak.
for i in range(1,6):
    a = input("enter your number: ")
    if a.isnumeric():
        a = int(a)
        if a > 40:
            print(a)
        else:
            continue
    else:
        print("pls enter your number")

# Case 3: Kiraların ortalamasından yüksek olan kiraları yazdırmak.
rents = [300, 500, 800, 1200, 1400, 1500, 2000]

rents.sum() # listelerde sum veya mean gibi aggretion fonk. tanımlı değil
rents.mean()

rents_sum = 0
for rent in rents:
    rents_sum += rent

rents_sum # toplam kira

rents_mean = rents_sum / len(rents) # Kiraların ortalaması

# Kiraların ortalamasından yüksek olan kiralar için:

for rent in rents :
    if rent >= rents_mean:
        print(rent)
    else:
        continue

#################
# Break: Bir koşul sağlandığında durmak için kullanılır.
#################

# Case: Elimizde 1500 lira kira bütçemiz var. Bütçemizi aşan kiralara geldiğinde yazdırmayı durdurmak.
rents = [300, 500, 800, 1200, 1400, 1500, 2000]

for rent in rents:
    if rent == 1500:
        print("max kira bütçesi")
        break
    print(rent)

#####################
# While Else Döngüsü
#####################

# Case 1: 0 değeri girilene kadar girilen bir sayının negatif mi yoksa pozitif mi olduğunu ekrana yazdırmak.

## sayı kontrol if-else i nasıl yazılır???
while True:
    number = input("Bir sayı giriniz (Çıkış yapmak için 0'a basın): ")
    if number.isnumeric():
        number = int(number)
        if number == 0:
            print("Program sonlandırılmıştır.")
            break
        elif number < 0:
            print("Girilen sayı negatiftir.")
        else:
            print("Girilen sayı pozitiftir.")
    else:
        print("Sayı Gir!")

# Case 2: Sayı tahmini yapmayı yazdırmak.
import random
sayi = random.randint(1, 100) # rastgele sayı tanımlanıyor.
# randint: Min ve max aralığında integer olan bir sayı döner. Max dahildir. min <= n <= max

hak = 5 # hak sayısı belirleniyor.
print("""Sayı Tahmin Oyununa Hoşgeldiniz.....
1-100 arasında Bir sayı tahmin ediniz....
5 Hakkınız Var....
""")
while (0 < hak):
    tahmin = int(input("Bir Sayı Giriniz.....")) # kullanıcıdan sayı isteniyor.

    if (tahmin == sayi):
        print("Tebrikler Sayıyı Doğru Tahmin ettiniz..") # tahmin sayıya eşit ise yazılacak mesaj.
        break # döngü kırılıyor.
    elif (tahmin < sayi):
        print("Tahmininiz Tutulan sayıdan Küçüktür arttırın :)")
        hak = hak - 1 # kullanıcı sayıyı tahmin edemediğinde hak değeri 1 azalıyor.
        print("Kalan Hakkınız {}".format(hak)) # hak değeri 0 olana kadar hak sayısı yazdırılıyor.
    elif (tahmin > sayi):
        print("Tahmininiz Tutulan sayıdan Büyüktür azaltın :)")
        hak = hak - 1 # kullanıcı sayıyı tahmin edemediğinde hak değeri 1 azalıyor.
        print("Kalan Hakkınız {}".format(hak)) # hak değeri 0 olana kadar hak sayısı yazdırılıyor.

if (hak == 0):
    print("Maalesef 5 hakkınızda da Tahmin edilen sayıyı bulamadınız Bir daha deneyin :)")
    print("Tahmin edilmesi gereken sayı: {}".format(sayi))

################################################
# Comprehensions: tek satırda veri yapısı oluşturmak
################################################

# List Comp
# Set Comp
# Dict Comp
# Tuple Comp YOK!

####################
# List Comprehensions
####################

# Case 1 [expression iteration]
# Case: rents listesindeki kiraların 2 katını bir listede toplamak.

rents = [300, 500, 800, 1200, 1400, 1500, 2000]

new_rents = []

for rent in rents:
    new_rents.append(int(rent*2))

[int(rent*2) for rent in rents]

# Case 2 [expression iteration condition]
# Case: rents listesindeki kiraların ortalamasından yüksek olanları bir listede toplamak.

new_rents = []
rents_sum = 0
for rent in rents:
    rents_sum += rent

rents_mean = rents_sum / len(rents)

for rent in rents:
    if rent > rents_mean:
        new_rents.append(int(rent))

[rent for rent in rents if rent > rents_mean ]

# Case 3 [expression1 if condition else expression2 iteration]
# Case: rents listesindeki kiraların 1000'den büyük olanlarına %10 zam geri kalanına %20 zam yaparak bir listede toplamak.

new_rents = []
for rent in rents:
    if rent > 1000:
        new_rents.append(int(rent*0.10 + rent))
    else:
        new_rents.append(int(rent * 0.20 + rent))

[int(rent*0.10 + rent) if rent > 1000 else int(rent * 0.20 + rent)  for rent in rents]

# Case 4 [expression1 if condition1 else (expression2 if condition2 else expression3) iteration]
# Case: rents listesindeki kiraların koşullara göre "Cheap", "Expensive", "Medium" listesini oluşturmak.

new_rents = []
for rent in rents:
    if rent < 100:
        new_rents.append("Cheap")
    elif rent >= 1500:
        new_rents.append("Expensive")
    else:
        new_rents.append("Medium")

["Cheap" if rent < 100 else ("Expensive" if rent >= 1500 else "Medium") for rent in rents]

# Case 5 [[expression iteration] iteration]
# Case: [[1, 2, 3], [4, 5, 6], [7, 8, 9]] matrisinin transpozunu almak.

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

for i in range(len(matrix)):
    print(matrix[i])

# Uzun yol:

tr = []

for i in range(len(matrix)):
    print(i)
    new_row = []
    for row in matrix:
        new_row.append(row[i])
    tr.append(new_row)

for i in range(len(tr)):
    print(tr[i])

# Kısa yol
# [[expression iteration] iteration]
[[row[i] for row in matrix] for i in range(len(matrix))]

# Case 6 [expression1 iteration1 iteration2]
# Case: [['40', '20', '10', '30'], ['20', '40', '20', '30', '20'], ['30', '20', '30', '50', '60', '30', '20', '20'], ['80', '80', '80'], ['900', '900', '100', '100']] bütün elemanları int'e çevirerek tek listede toplamak.

nested_list = [['40', '20', '10', '30'], ['20', '40', '20', '30', '20'], ['30', '20', '30', '50', '60', '30', '20', '20'], ['80', '80', '80'], ['900', '900', '100', '100']]

all_list  = []

for sub_list in nested_list:
    for value in sub_list:
        all_list.append(int(value))

# [expression1 iteration1 iteration2]
[int(value) for sub_list in nested_list for value in sub_list]

####################
# Dict Compherensions
####################

# Case 1: ["HTA", "OTM", "PC", "Truck", "Bus", "Smart", "Unimog"] listesine 1'den başlayacak şekilde id değerleri atayarak bir sözlük oluşturmak.
# Beklenen çıktı:
# {1: 'HTA', 2: 'OTM', 3: 'PC', 4: 'Truck', 5: 'Bus', 6: 'Smart', 7: 'Unimog'}

Franchises = ["HTA", "OTM", "PC", "Truck", "Bus", "Smart", "Unimog"]

xx = list(enumerate(Franchises, start=1))
index, value = xx[0]

my_dict = {}
for index in enumerate(Franchises, start=1):
    my_dict[index] = value

{index:value for index, value in enumerate(Franchises, start=1)}

# Case 2: supermarket_sales veri setinin numerik değişkenlerinden aşağıdaki toplulaştırma (agg) sözlüğünü oluşturmak.

# Beklenen Çıktı:
# {'Unit price': ['mean', 'min', 'max', 'var'],
#  'Quantity': ['mean', 'min', 'max', 'var'],
#  'Tax 5%': ['mean', 'min', 'max', 'var'],
#  'Total': ['mean', 'min', 'max', 'var'],
#  'cogs': ['mean', 'min', 'max', 'var'],
#  'gross margin percentage': ['mean', 'min', 'max', 'var'],
#  'gross income': ['mean', 'min', 'max', 'var'],
#  'Rating': ['mean', 'min', 'max', 'var']}

import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv("datasets/supermarket_sales.csv")
df.head()
df.columns
df.dtypes

# Numerik değişkenlerin seçimi
num_cols = [col for col in df.columns if df[col].dtype != "O"]

agg_list = ["mean","min","max","var"]

{col:agg_list for col in num_cols}

# Case 3: "supermarket_sales" veri setinden numerik değişkenleri kullanarak aşağıdaki sözlüğü oluşturmak.
# Beklenen çıktı:
# {'Unit price': ['Unit price_mean', 'Unit price_min', 'Unit price_max', 'Unit price_sum'],
#  'Quantity': ['Quantity_mean', 'Quantity_min', 'Quantity_max', 'Quantity_sum'],
#  'Tax 5%': ['Tax 5%_mean', 'Tax 5%_min', 'Tax 5%_max', 'Tax 5%_sum'],
#  'Total': ['Total_mean', 'Total_min', 'Total_max', 'Total_sum'],
#  'cogs': ['cogs_mean', 'cogs_min', 'cogs_max', 'cogs_sum'],
#  'gross margin percentage': ['gross margin percentage_mean', 'gross margin percentage_min', 'gross margin percentage_max', 'gross margin percentage_sum'],
#  'gross income': ['gross income_mean', 'gross income_min', 'gross income_max', 'gross income_sum'],
#  'Rating': ['Rating_mean', 'Rating_min', 'Rating_max', 'Rating_sum']}

import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv("datasets/supermarket_sales.csv")
df.head()
df.columns
df.dtypes

# Numerik değişkenlerin seçimi
num_cols = [col for col in df.select_dtypes(include=["float64", "int64"])]
agg_list = ['mean', 'min', 'max', 'sum']

# Kısa yol
{col: [col + "_" + agg_val for agg_val in agg_list] for col in num_cols}

# Uzun Yol
agg_dict = {}
for col in num_cols:
    concat_list = []
    for agg_val in agg_list:
        concat_list.append(col + "_" + agg_val)
    agg_dict[col] = concat_list
agg_dict

# Case 4: İsminde "GROSS" olan değişkenlerin başına FLAG diğerlerine NO_FLAG eklemek.

# before:
# ['INVOICE ID',
# 'BRANCH',
# 'CITY',
# 'CUSTOMER TYPE',
# 'GENDER',
# 'PRODUCT LINE',
# 'UNIT PRICE',
# 'QUANTITY',
# 'TAX 5%',
# 'TOTAL',
# 'DATE',
# 'TIME',
# 'PAYMENT',
# 'COGS',
# 'GROSS MARGIN PERCENTAGE',
# 'GROSS INCOME',
# 'RATING']

# after:
# ['NO_FLAG_INVOICE ID',
#  'NO_FLAG_BRANCH',
#  'NO_FLAG_CITY',
#  'NO_FLAG_CUSTOMER TYPE',
#  'NO_FLAG_GENDER',
#  'NO_FLAG_PRODUCT LINE',
#  'NO_FLAG_UNIT PRICE',
#  'NO_FLAG_QUANTITY',
#  'NO_FLAG_TAX 5%',
#  'NO_FLAG_TOTAL',
#  'NO_FLAG_DATE',
#  'NO_FLAG_TIME',
#  'NO_FLAG_PAYMENT',
#  'NO_FLAG_COGS',
#  'FLAG_GROSS MARGIN PERCENTAGE',
#  'FLAG_GROSS INCOME',
#  'NO_FLAG_RATING']

import pandas as pd
pd.set_option('display.max_columns', None)
df = pd.read_csv("datasets/supermarket_sales.csv")

df.columns = [col.upper() for col in df.columns]

df.columns

[col for col in df.columns if "GROSS" in col] # içimde GROSS geçenler

["FLAG_" + col for col in df.columns if "GROSS" in col]

["FLAG_" + col if "GROSS" in col else "NO_FLAG_" + col for col in df.columns]

df.columns = ["FLAG_" + col if "GROSS" in col else "NO_FLAG_" + col for col in df.columns]

####################
# Set Comp
####################

liste = [1,3,4,7,10,3,1, 6,4]

[num for num in liste if num % 2 == 0]

{num for num in liste if num % 2 == 0}