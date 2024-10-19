import os
import random
import string 
data = dict()

while True:
    os.system("cls") 
    print(f" {'\t-DATA PASIEN-\t':※^45}")
    keyFinal = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    nama = input("Nama\t\t:")
    umur = input("Umur\t\t:")
    kelamin = input("Kelamin\t\t:")
    penyakit = input("Jenis Penyakit\t:")
    data[keyFinal] = { 'namakey': nama, 'umurkey': umur, 'kelaminkey': kelamin, 'penyakitkey': penyakit }

    opsi = input("Ingin Input Data Lagi ? (y/t) :").lower()
    if opsi == 't':
        break

print("-" * 55)
print(f"Key\t Nama\t Umur\t Kelamin\t Penyakit")
print("-" * 55)
for key, value in data.items():
    print(f"{key}.\t {value['namakey']}\t {value['umurkey']}\t {value['kelaminkey']}\t {value['penyakitkey']}")

print(" "*55)
print("※"*55)
