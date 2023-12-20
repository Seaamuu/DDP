class Animal:
    def __init__(self, name, makanan, hidup, berkembang_biak):
        self.name = name
        self.makanan = makanan
        self.hidup = hidup
        self.berkembang_biak = berkembang_biak

    def cetak(self):
        print("====================================================="
              "\nNama Hewan\t: ", self.name, 
              "\nJenis Makanan\t: ", self.makanan, 
              "\nAsal Habitat\t: ", self.hidup, 
              "\nCara Berkembang biak\t: ", self.berkembang_biak )
        
class Mamalia(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, nama_ilmiah, masa_hidup):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.nama_ilmiah = nama_ilmiah
        self.masa_hidup = masa_hidup

    def cetak(self):
        super().cetak()
        print("\nNama Ilmiah\t:",self.nama_ilmiah,
              "\nMasa Hidup\t:", self.masa_hidup,
              "\n=====================================================\t")
        
class Serangga(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, nama_ilmiah, masa_hidup):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.nama_ilmiah = nama_ilmiah
        self.masa_hidup = masa_hidup

    def cetak(self):
        super().cetak()
        print("\nNama Ilmiah\t:",self.nama_ilmiah,
              "\nMasa Hidup\t:", self.masa_hidup,
              "\n=====================================================\t")

class Reptil(Animal):
    def __init__(self, name, makanan, hidup, berkembang_biak, nama_ilmiah, masa_hidup):
        super().__init__(name, makanan, hidup, berkembang_biak)
        self.nama_ilmiah = nama_ilmiah
        self.masa_hidup = masa_hidup

    def cetak(self):
        super().cetak()
        print("\nNama Ilmiah\t:",self.nama_ilmiah,
              "\nMasa Hidup\t:", self.masa_hidup,
              "\n=====================================================\t")


#objek animal
w = Animal("Badak", "Buah buahan", "Hutan hujan dataran rendah", "melahirkan")
w.cetak()

#objek mamalia
x = Mamalia("Lumba lumba", "Ikan/cumi cumi", "laut", "melahirkan", "dolphin", "55 - 60 tahun")
x.cetak()

#objek serangga
y = Serangga("Kupu Kupu", "Nektar", "Hutan/Taman Bunga", "Bertelur", "Lepidoptera", "15 - 29 hari")
y.cetak()

#objek Reptil
z = Reptil("Buaya", "Daging", "Perairan tawar", "Bertelur", "Crocodylidae", "50 - 70 tahun")
z.cetak()