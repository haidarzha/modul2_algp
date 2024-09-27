import math

bil1 = int(input("Masukkan bilangan pertama: "))
bil2 = int(input("Masukkan bilangan kedua: "))

#cari hasil jumlah
hasiljumlah = bil1 + bil2
print("Hasil jumlah bil1 dan bil2: {}".format(hasiljumlah))
#cari hasil kurang
hasilkurang = bil1 - bil2
print("Hasil kurang bil1 dan bil2: {}".format(hasilkurang))
#cari hasil kali
hasilkali = bil1 * bil2
print("Hasil kali bil1 dan bil2: {}".format(hasilkali))
#cari hasil sisa bagi
hasilmodulo = bil1 % bil2
print("Sisa pembagian bil1 dengan bil2: {}".format(hasilmodulo))
#cari hasil pembagian float
hasilfloatdev = bil1 / bil2
print("Pembagian bil1 dengan bil2: {}".format(hasilfloatdev))
#cari hasil logaritma menggunakan import math
if bil1 > 0:
    log_bil1 = math.log10(bil1)
    print("Logaritma dari bil1 (log10(bil1)): {}".format(log_bil1))
else:
    print("Logaritma hanya bisa dihitung untuk bilangan positif.")
#cari hasil pangkat
hasilpangkat = bil1 ** bil2
print("Hasil pangkat bil1 dan bil2: {}".format(hasilpangkat))
