#soal nomor dua
def kelulusan(nilai):
    if nilai >= 0 and nilai <= 60:
        return "Gagal"
    elif nilai <= 70:
        return "Baik"
    elif nilai <= 80:
        return "Sangat baik"
    elif nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid!"
    
print(kelulusan(80))

