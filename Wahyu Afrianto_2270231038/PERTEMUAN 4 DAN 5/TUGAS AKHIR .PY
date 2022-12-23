total = 0
barang = []
harga = []

while True:

    print("========== FAST AND FORIUS ANTO ===========\n")
    print("========== JLN CAMAN AST ============\n")

    print("""Daftar menu\n
    1. AVANZA \t 55000000
    2. INNOVA  \t 11150000
    3. LANCER \t 20000000
    4. ERTIGA \t 125000000
    5. BMW 13CT \t 30000000
    6. BMW 564VT \t 345000000
    """ )


    Nama = input("Masukkan nama anda :")
    Alamat = input("Masukkan alamat anda :")
    Telepon = input("Masukkan telepon anda :")
    Tanggal = input("Masukkan tanggal pembelian :")
    kode = int(input("pilih menu : "))


    if kode == 1:
        barang.append('AVANZA')
        harga.append('55000000')
        total += 55000000
    elif kode == 2:
        barang.append('INNOVA')
        harga.append('11150000')
        total += 11150000
    elif kode == 3:
        barang.append('LANCER')
        harga.append('20000000')
        total += 20000000
    elif kode == 4:
        barang.append('ERTIGA')
        harga.append('125000000')
        total += 125000000
    elif kode == 5:
        barang.append('BMW 13CT')
        harga.append('30000000')
        total += 30000000
    elif kode == 6:
        barang.append('BMW 564VT')
        harga.append('345000000')
        total += 345000000
    else:
        print('kode tidak valid')

    lanjut = input('lanjut belanja (y/t) : ')
    if lanjut == 't' :
        print("")
        print('Nama :', Nama)
        print('Alamat :', Alamat)
        print('Telepon :', Telepon)
        print('Tanggal :', Tanggal)
        print('Barang yang dibeli : ', barang)
        print('Total yang harus dibayar : ', total, '\n')
        uang = int(input('Masukkan uang pembayaran : '))
        if uang > total:
            print('Kembaliannya : ', uang - total)
        elif uang == total:
            print('Uang pas')
        else:
            print('Uangnya kurang', uang - total)
        break 
    print('Harga barangnya : ', harga)