nama = 'Purwadhika Startup & Coding School'

# jumlah huruf c ?
cari = 'c'
x = nama.upper().replace(cari.upper(), '')
jmlCari = len(nama) - len(x)
print(f'Jumlah huruf \'{cari}\' ada = {jmlCari}')

# jumlah kata 'school'?
cari = 'school'
x = nama.upper().replace(cari.upper(), '')
jmlCari = int((len(nama) - len(x)) / len(cari))
print(f'Jumlah kata \'{cari}\' ada = {jmlCari}')
