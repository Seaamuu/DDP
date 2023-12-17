class Gempa:
    #member1 atribut / properti
    lokasi = ''
    skala = 0

    #member2 konstruktor
    def __init__(self, lokasi, skala):
         self.lokasi = lokasi
         self.skala = skala


    #member3 method
    def dampak(self):
          if self.skala < 2:
             print('Dampak gempa tidak terasa.')
          elif self.skala >= 2 and self.skala <= 4:
               print('Dampak gempa bangunan retak-retak')
          elif self.skala >= 4 and self.skala <= 6:
                print('Dampak gempa bangunan roboh')
          elif self.skala >= 6:
                print('Dampak gempa bangunan roboh dan berpotensi tsunami')
    
