from Gempa import *

lokasi_gempa = "Banten"
skala_gempa = 1.2

gempa = Gempa(lokasi_gempa, skala_gempa)
gempa.dampak()

lokasi_gempa = "Palu"
skala_gempa = 6.1

ggempa = Gempa(lokasi_gempa, skala_gempa)
gempa.dampak()

lokasi_gempa = "Cianjur"
skala_gempa = 5.6

gempa = Gempa(lokasi_gempa, skala_gempa)
gempa.dampak()

lokasi_gempa = "Jayapura"
skala_gempa = 3.3

gempa = Gempa(lokasi_gempa, skala_gempa)
gempa.dampak()


lokasi_gempa = "Garut"
skala_gempa = 4.0

gempa = Gempa(lokasi_gempa, skala_gempa)
gempa.dampak()
