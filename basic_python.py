#######################
# Değişkenler
#######################

# Python da geçici olarak veri saklamak için oluşturduğumuz alanlara değişken denir.
# Akılda tutlamayacak değerleri akılda tutulabilecek isimlerle tanımlamaktır.

"Python" + " Eğitimleri"
"Python" + " Dersleri"

ptn = "Python"
ptn + "Dersleri"
ptn + " Uygulamaları"

uzun_turkce_kelime = "finlandiyalılaştıramadıklarımızcasına"

xx
print(xx)

# Pyhton da değişken tanımlarken uzak durulması gerekenler:

# 1. Türkçe karakter kullanımından kaçınmak.
çember_çapı = 5

# 2. İçerisinde sayı ve harf barındırabilir ancak sayı ile başlayamaz ve boşluk bırakamaz, özel karakter kullanamayız.
number_1 = 10
number_2 = 12
# 1_number = 10

# 3. Sadece harfler, sayılar ve alt tire(_) karakterini içermelidir.
number_1 = 10
# cember capi = 10

# 4. Anahtar kelimeler değişken olarak tanılamanamaz.
import keyword
print(keyword.kwlist)

# and = 4

# 5. Tanımlı fonksiyon, sınıf, metot ve modül isimleri tanımlanmaz.

type(5)
type = 5
type(5)

# 6. Açık, net anlaşılır bir isim kullanılması ve isimlendirme esnasında küçük harfle başlanarak isimlendirilme yapılması önerilir.

# 7. Değişken, Fonksiyon, Parametre isimleri tanımlanırken değişken birden fazla kelime içeriyorsa alt çizgi ile ayrılmalıdır.

def addition (first_number = 10, second_number = 20):
    return first_number + second_number

toplam_deger = addition()

##############################
# Konsol İşlemleri
##############################

# Ekrana Çıktı Yazdırma:
# print()
# Amacımız: Çeşitli yollarla "Analitik Ekip Python Eğitimi" konsola yazdırmak.

# Case 1: Mesajı tek değer içerisinde yazmak.
print("Analitik Ekip Python Eğitimi")

## Case 2: Mesajı birden fazla değer kullanarak tek satırda yazdırmak.
print("Analitik", "Ekip", "Python", "Eğitimi")

# Case 3: Mesajı birden fazla print kullanarak alt alta yazdırmak.
print("Analitik")
print("Ekip")
print("Pyhon")
print("Eğitimi")

# Case 4: Mesajı tek print kullanarak alt alta yazdırmak.
# sep parametresi: bir print içerisinde ayrı ayrı değerlerin arasındaki karakteri belirler.

print("Analitik", "Ekip", "Python", "Eğitimi", sep="\n")

# Case 5: Mesajı birden fazla print kullanarak tek satırda yazdırmak.
# end parametresi: 2 print arasındaki karakteri belirlemeyi sağlar.
print("Analitik", end=" ")
print("Ekip", end=" ")
print("Python", end=" ")
print("Eğitimi")

# Ekrandan Girdi Alma:

tutar = input("Lütfen tutar giriniz:\t")
print(tutar)

type(tutar)

##############################
# Temel Veri Tipleri
##############################

## Veri Tipi Fonksiyonları
# | Fonksiyon İsmi |    Kullanımı    |
# |----------------|-----------------|
# | int()          | Tamsayı         |
# | float()        | Ondalık Sayı    |
# | str()          | Metinsel İfade  |
# | bool()         | Mantıksal İfade |

# Tam Sayı
tam_sayi = 10
type(tam_sayi)

# Ondalıklı Sayı
ondalik_sayi = 10.0
type(ondalik_sayi)

# Metinsel İfade
metinsel_ifade = "Merhaba Python"
type(metinsel_ifade)

# Mantıksal İfade
mantıksal_ifade = True
type(mantıksal_ifade)

##############################
## Tip Dönüşümleri
##############################

# int <-> float
tam_sayi = 10
print(type(tam_sayi))
ondalik_sayi = float(tam_sayi)
print(type(ondalik_sayi))
yeni_tam_sayi = int(ondalik_sayi)
print(type(yeni_tam_sayi))

int(3.55)
round(3.55)

tutar = int(input("Lütfen tutar giriniz:\t"))
type(tutar)

# int <-> str
tam_sayi = 10
print(type(tam_sayi))
metinsel_ifade = str(tam_sayi)
print(type(metinsel_ifade))
yeni_tam_sayi = int(metinsel_ifade)
print(type(yeni_tam_sayi))

# int <-> bool
tam_sayi = 0 # False
print(type(tam_sayi))
mantiksal_ifade = bool(tam_sayi)
print(type(mantiksal_ifade))
print(mantiksal_ifade)
yeni_tam_sayi = int(mantiksal_ifade)
print(type(yeni_tam_sayi))

bool(0)
bool(1)


# float <-> str
ondalik_sayi = 3.14
print(type(ondalik_sayi))
metinsel_ifade = str(ondalik_sayi)
print(type(metinsel_ifade))
yeni_ondalik_sayi = float(metinsel_ifade)
print(type(yeni_ondalik_sayi))

# bool <-> str
mantiksal_ifade = False
print(type(mantiksal_ifade))
metinsel_ifade = str(mantiksal_ifade)
print(type(metinsel_ifade))
yeni_mantiksal_ifade = bool(metinsel_ifade)
print(type(yeni_mantiksal_ifade))

##############################
# Operatörler
##############################

## Aritmetik Operatörler:
# Aritmetik işlemleri yapmamızı sağlayan operatörlerdir.

# | Operatör |     Anlamı     |
# |----------|----------------|
# | +        | Toplama        |
# | -        | Çıkarma        |
# | *        | Çarpma         |
# | /        | Bölme          |
# | //       | Tam Sayı Bölme |
# | **       | Üs Alma        |
# | %        | Mod            |

## Atama Opeatörleri
# Yapılan işlem sonuçlarını değişkene atamamızı sağlayan operatörlerdir.

# | Operatör |       Anlamı        |
# |----------|---------------------|
# | +=       | Topla ve ata        |
# | -=       | Çıkar ve ata        |
# | *=       | Çarp ve ata         |
# | /=       | Böl ve ata          |
# | //=      | Tam Sayı Böl ve ata |
# | **=      | Üs Al ve ata        |
# | %=       | Mod al ve ata       |


number = 10
number = number + 5
number +=5

## Karşılaştırma Operatörleri
# Değişken değerleri arasında mantıksal biçimde karşılaştırma yapabildiğimiz operatörlerdir.

# | Operatör |           Anlamı           |
# |----------|----------------------------|
# | <        | Küçüktür                   |
# | >        | Büyüktür                   |
# | <=       | Küçüktür ve eşittir        |
# | >=       | Büyüktür ve eşittir        |
# | ==       | Eşit eşittir               |
# | !=       | Eşit değildir              |
# | in       | İçinde                     |

## Mantıksal Operatörler
# Birden fazla karşılaştırma işlemlerini çeşitli mantıksal yapılara göre birleştirmeyi sağlayan operatörlerdir.

# | Operatör | Anlamı |
# |----------|--------|
# | and (&)  | Ve     | # her iki mantıksal sonuç True ise True
# | or (|)   | Veya   | # her iki mantıksal sonuç False ise False
# | not (~)  | Değil  | # True ise False, False ise True

4 > 6 or 3 != 9
4 > 6 and 3 != 9

##############################
# Temel Veri Yapıları
##############################
# Veri yapıları, verileri hafızada bir arada tutabildiğimiz yapılardır.

# Listeler -> List
# Demetler -> Tuple
# Sözlükler -> Dictionary
# Kümeler -> Set

#############
# Listeler:
#############
# Birbirlerinden Farklı
# Sıralı
# Güncellenebilir

# Yöntem 1 - El ile girme
my_list = [1, 2, 3, 4]
my_list

# Yöntem 2 - List fonksiyonu ile sonradan ekleme
my_list = list()

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list

# Yöntem 3 - Köşeli parantez ile sonradan ekleme

my_list = []
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list

# Yöntem 4 - range fonksiyonu kullanılarak list fonksiyonu ile dönüştürme
my_list = list(range(1, 5))
my_list

# start= 10, stop=100, step=8
my_list = list(range(10,100,8))

# Slicing
# Case 1: İlk Eleman
my_list[0]

# Case 2: Son Eleman
my_list[-1]
my_list[len(my_list)-1]

# Case 3: İlk 4 eleman
my_list[:4]

# Case 4: Son 6 eleman
my_list[-6:]

# Case 5: Üçüncü indeksten Sekizinci indekse kadar değerler
my_list[3:8]

# Case 6: En baştan yedinci indeks de dahil değerleri getir
my_list[:8]

# Case 7: Dördüncü indeksten son elemana kadar değerler
my_list[4:]

# Case 8: İlk elemandan son elemana kadar 3'er atla
my_list[::3]

# Case 9: Üçüncü indeksten Onuncu indekse kadar 2'şer atla
my_list[3:10:2]

# Case 10: Elemanları tersten yazdır.
my_list.reverse()
my_list
my_list.sort(reverse=True)
my_list

my_list = my_list[::-1]

nested_list = [[1, 2], [3, 4, ["Python", 0]], "Mercedes", [5, [6, 7], 8]]

# "Python" değerine ulaşma
nested_list[1][2][0]

# 8 değerine ulaşma
nested_list[3][2]

# "Mercedes" değerine ulaşma
nested_list[2]

# Liste Metotları
dir(list())

var_list = [1, 3.14, "Python", True, [3,4,5]]

# append -> sona eleman ekler
var_list.append("Daimler")

# pop -> eleman çıkarır (index bazlı)
var_list.pop()
var_list.pop(2)

# remove -> eleman çıkarır (eleman bazlı)
var_list.remove(3.14)

# insert -> eleman ekler (index bazlı)
var_list.insert(0,"DAIMLER")
var_list.insert(len(var_list), "DAIMLER")
var_list.insert(-1, "AKBANK")

# copy
num_list = [1, 2, 3, 4]
num_list2 = num_list.copy()

num_list2.append(5)
num_list2.append(6)

#############
# Demetler-Tuple
#############
# Birbirlerinden farklı
# Sıralı
# Güncellenemez, Değiştirilemez.

# Yöntem 1 - El ile oluşturma
demet = (1,2,3,4)

# Yöntem 2 - Range Fonksiyonu ile Oluşturma
demet = tuple(range(1,5))

# Yöntem 3 - Liste üzerinden oluşturma
liste = [1,2,3,4]
demet = tuple(liste)

# Demet Eleman İşlemleri:

demet_2 = tuple(range(10,100,5))

# Case 1: İlk Eleman
demet_2[0]

# Case 2: Son Eleman
demet_2[-1]

# Case 3: İlk 4 eleman
demet_2[:4]

# Case 4: Son 6 eleman
demet_2[-6:]

# Case 5: Üçüncü indeksten Sekizinci indekse kadar değerler
demet_2[3:8]

# Case 6: En baştan yedinci indeks de dahil değerleri getir
demet_2[:8]

# Case 7: Dördüncü indeksten son elemana kadar değerler
demet_2[4:]

# Case 8: İlk elemandan son elemana kadar 3'er atla
demet_2[::3]

# Case 9: Üçüncü indeksten Onuncu indekse kadar 2'şer atla
demet_2[3:10:2]

# Case 10: Elemanları tersten yazdır.
demet_2[::-1]

# İç İçe Demet
nested_tupple = ((1, 2), (3, 4, ("Python", 0)), "Daimler", (5, (6, 7), 8))

# "Python" değerine ulaşma
nested_tupple[1][2][0]

# 8 değerine ulaşma
nested_tupple[3][2]

dir(tuple())

num_tuple = (1, 2, 3, 3, 4, 4, 5, 5, 5, 6, 7, 8, 8, 9)

num_tuple.count(5) # bu elemanın kaç defa olduğunu söyler
num_tuple.index(3) # bu elamanın kacıncı indexde olduğunu söyler

#############
# Sözlükler
#############
# Anahtar - değer (key, value)
# birden fazla
# !sayılamaz!
# Güncellenebilir

# sozluk = {anahtar: deger}

# Sözlük Oluşturma:
# Yöntem 1 - El ile oluşturma
sozluk = {"Data Science": "Veri Bilimi",
          "Deep Learning": "Derin Öğrenme"}

# Yöntem 2 - Liste ve Tuple Çifti ile oluşturma
sozluk_liste = [("Data Science", "Veri Bilimi"), ("Deep Learning", "Derin Öğrenme")]
sozluk = dict(sozluk_liste)

sozluk = {1: "Ad",
          2: "Soyad",
          [1, 2, 3]: "Liste"} # sözlük değiştirilemez yapıya sahip olmasından dolayı liste değiştirilebilir olduğu için hata alıyor.

sozluk = {1: "Ad",
          2: "Soyad",
          (1, 2, 3): "Demet"} # sadece tuplelar da hata almıyor yapısı gereği

sozluk = {1: "Ad",
          2: "Soyad",
          {1, 2, 3}: "Küme"}

sozluk = {1: "Ad",
          2: "Soyad",
          {1: 1, 2: 2, 3: 3}: "Sözlük"}

# sözlük eleman işlemleri:

Musteri_Bilgileri = {
    "112233": {
        "Adı": "Mehmet",
        "Soyadı": "Bey",
        "Lokasyon": "Turkiye",
        "mail": "Mehmet.Bey@anonim.com",
        "Sektör": "E-Commerce",
        "telefon": 123456,
        "Danısman_Bilgileri": {
            "Adı": "Rabia",
            "Soyadı": "Koç",
            "Alanı": ["Python", "SAP"],
            "Unvanı": ["Data Scientist", "Junior BI Consultant"]
        }
    },
    "445566": {
        "Adı": "Ayşe",
        "Soyadı": "Hanım",
        "Lokasyon": "İstanbul",
        "mail": "Ayse.Hanım@anonim.com",
        "Sektör": "Bankacılık",
        "telefon": 654321,
        "Danısman_Bilgileri": {
            "Adı": "Özlem",
            "Soyadı": "Yaren",
            "Alanı": ["SAP", "SQL"],
            "Unvanı": ["SAP Consultant", "Senior BI Consultant"]
        }
    }
}

# Case 1 - Mehmet Bey'e ait bütün bilgileri getir.
Musteri_Bilgileri["112233"]

# Case 2 - Ayşe Hanım'ın mail adresine ulaş.
Musteri_Bilgileri["445566"]["mail"]

# Case 3 - Mehmet Bey'in danışmanının alanını getir.
Musteri_Bilgileri["112233"]["Danısman_Bilgileri"]["Alanı"]

# Case 4 - Ayşe Hanımın Danışman_Bilgileri kısmındaki "Ünvanı"ı güncelle.
# ["SAP Consultant", "Head of BI Consultant", "AMS Director"]
Musteri_Bilgileri["445566"]["Danısman_Bilgileri"]["Unvanı"] = ["SAP Consultant", "Head of BI Consultant", "AMS Director"]

# Case 5 - Mehmet Bey'in telefon numarasını güncelle.

Musteri_Bilgileri["112233"]["telefon"] = 9876542

# Sözlüklerde Toplulaştırma İşlemleri:

import pandas as pd
pd.set_option('display.max_columns', None)

df = pd.read_csv ("https://raw.githubusercontent.com/rabia-koc/Mercedes-Car-Model-Analysis/main/Exploratory%20Data%20Analysis/merc.csv")

df.head()
df.to_csv("Mercedes.csv")
df = pd.read_csv("Mercedes.csv", index_col=0)
df.head()

# Araç modellerine göre price, transmission, mileage toplulaştırılması:

agg_dict = {"price": "mean",
            "transmission":"unique",
            "mileage": "mean"}

# price: fiyat
# transmission: vites türü
# mileage: km

df.groupby("model").agg(agg_dict).head(10)

# model ve yıl bazında ortalama fiyat gösterimi(sözlükte tek key-value çiftini alabiliyoruz)
df.groupby(["model","year"]).agg({"price":"mean"}).head(50)

# modellerin ortalama fiyatları yılların sıralanmış şekilde
df.groupby(["model","year"]).agg({"price":"mean"}).sort_values(by="year", ascending=False).head(50)

# modellerin ortalama fiyatları fiyatlar sıralanmış şekilde
df.groupby(["model","year"]).agg({"price":"mean"}).sort_values(by="price", ascending=False).head(50)

# Sık Kullanılan Sözlük Metotları
dir(dict())

# Sık kullanılan sözlük metotları üzerinden işlemler:
game = {
    "id": 1,
    "name": "Legend Of Zelda",
    "type": ["Warrior", "Sword"],
    "base": {
        "Vitality": 100,
        "Attack": 10,
        "Defense": 8,
        "First Attack": 12,
        "Full Defense": 14,
        "Speed": 20
    }
}

# items
game.items() # tuple çiftlerini getirir.

# values
game.values() # sadece değerleri bir liste olarak getirir.

# keys
game.keys()  # sadece anahtarları getirir.

# get & setdefault
game.get("id")
game.get("types") # eğer sözlük içinde yoksa none döndürür.

game.setdefault("id", 0)
game.setdefault("types", "Shield")   # sözlük içinde yoksa en son satıra eklenir ve hata vermez!!

#############
# Kümeler
#############
# Sayılamayan
# Matematikteki kümelere benzeyen
# Birbirlerinden farklı
# Eşsiz değerleri tutan veri yapılarıdır

# Küme Oluşturma:
# Yöntem 1 - El ile oluşturma
kume = {1, 1, 2, 3, 4, 5, 5, 6, 7, 8}

# Yöntem 2 - Başka veri yapısından oluşturma
uzun_turkce_kelime = "finlandiyalılaştıramadıklarımızcasına"
kume_2 = set(uzun_turkce_kelime)

# Yöntem 3 - range() Fonksiyonu ile oluşturma
kume_3 = set(range(1,10,2))

# Eleman İşlemleri
# kume[0] # Error!
set(list(kume)[2:5]) # küme de slicing işlemi yapamadığımız için listeye dönüştürmek gerekiyor

dir(set())











