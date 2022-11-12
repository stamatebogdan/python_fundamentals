import gzip

continut_fisier = b"Continut fisier arhiva"

with gzip.open('arhiva.gz','wb') as f:
    f.write(continut_fisier)

with open("arhiva.gz",'r') as f:
    print(f.read())

with gzip.open("arhiva.gz", "rb") as f:
    print(f.read())