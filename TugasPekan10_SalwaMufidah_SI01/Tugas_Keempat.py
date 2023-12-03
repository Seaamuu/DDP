#soal nomor empat
def filter_konsonan(string, hapus): 
    for char in hapus:
        if char in string:
            string = string.replace(char, '')
    print(string)

filter_konsonan("Nurul Fikri", ["a", "i", "u", "e", "o"])