# Baner
import pyfiglet

ascii_banner = pyfiglet.figlet_format("Umurfi")
print(ascii_banner)
# masukan nama
a = input("[+] Masukan Nama Anda: ")
# Masukan tahun kelahiran
b = int(input("[+] Masukan Tanggal Lahir Anda: "))
c = input("[+] Masukan Bulan Lahir Anda: ")
d = int(input("[+] Masukan Tahun Lahir Anda: "))
# Tahun sekrang
e = 2022
# Hasil
print("[>>] Hai",a,"Kamu Lahir Pada Tanggal",b,c,d)
print("[>>] Umur Kamu Sekarang Adalah",e - d,"Tahun.")
print("\n")
