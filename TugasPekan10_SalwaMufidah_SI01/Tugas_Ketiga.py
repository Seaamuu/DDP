#soal nomor tiga
def duplikasi(fruits):
    result = []
    for fruit in fruits:
        if fruit not in result:
            result.append(fruit)
            result.append(fruit)
    return result

fruits = ['pepaya', 'mangga', 'pisang', 'durian', 'jambu']
print(duplikasi(fruits))