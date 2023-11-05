print("==================")
print("program penghitung luas bangun datar")
print('''
Pilih salah satu bangun datar:
1 = luas persegi
2 = luas lingkaran
3 = luas segitiga
''')

Pilihan = int(input("masukkan pilihan: "))
match pilihan: 
    case 1:
      Sisi = int(input("masukkan sisi: "))
      Luas = sisi*sisi
      print("luas persegi dengan sisi",sisi,"adalah:",luas)
    case 2:
      Jari = int(input("masukkan jari-jari: "))
      Luas = 3.14*jari**2
      print("luas lingkaran dengan jari-jari", jari, "adalah:",luas)
    case 3:
      Alas = int(input ("masukkan alas: "))
      Tinggi = int(input ("masukkan tinggi: "))
      Luas = 1/2*alas*tinggi
      print("luas segitiga dengan alas", alas, "dan tinggi", tinggi,"adalah:",luas)
    case _:
     print("pilihan salah")