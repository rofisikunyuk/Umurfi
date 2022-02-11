# Baner
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Umurfi")
print(ascii_banner)
# masukan nama
a = str(input("\033[1;31m[+]\033[1;37m Masukan Nama Anda: "))
# Masukan tahun kelahiran
b = int(input("\033[1;31m[+]\033[1;37m Masukan Tanggal Lahir Anda: "))
c = str(input("\033[1;31m[+]\033[1;37m Masukan Bulan Lahir Anda: "))
d = int(input("\033[1;31m[+]\033[1;37m Masukan Tahun Lahir Anda: "))
# Tahun sekrang
e = 2022
# Hasil
print("\033[1;32m[+]\033[1;37m Hai",a,"Kamu Lahir Pada Tanggal",b,c,d)
print("\033[1;32m[+]\033[1;37m Umur Kamu Sekarang Adalah",e - d,"Tahun.")
print("\n")
