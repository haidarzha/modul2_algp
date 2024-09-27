import math
#Lintang dan bujur kota Tangerang
LintangTangerang = math.radians(float(input("Lintang Kota Tangerang: ")))
BujurTangerang = math.radians(float(input("Bujur Kota Tangerang: ")))
LintangJakarta = math.radians(float(input("Lintang kota Jakarta: ")))
BujurJakarta = math.radians(float(input("Bujur kota Jakarta: ")))
R = 6371
Lat = LintangJakarta - LintangTangerang
Long = BujurJakarta - BujurTangerang
a = math.sin(Lat/2)**2 + math.cos(LintangTangerang) * math.cos(LintangJakarta) * math.sin(Long/2)**2
C = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
d = R * C
print("Jarak antara dua titik tersebut adalah ", d, " kilometer.")