def menuAwal():
    a = int(input("--->>>>SELAMAT DATANG<<<<---\nmau hitung apa?\n\n1. luas segitiga\n2. luas persegi\n3. luas persegi panjang\n4. luas jajar genjang\n5. keluar\nMasukkan Pilihan (1/2/3/4/5) : "))
    if a == 1:
        luasSegitiga()
    elif a == 2:
        luasPersegi()
    elif a == 3:
        luasPersegiPanjang()
    elif a == 4:
        luasJajarGenjang()
    else:
        keluar()

def luasSegitiga():
    alas = float(input("Masukkan Alas : "))
    tinggi = float(input("Masukkan Tinggi : "))
    luas = 1/2 * alas * tinggi
    print(f"Luas Segitiga : {luas}\n")
    menuAwal()
    
def luasPersegi():
    sisi = float(input("Masukkan Sisi : "))
    luas = sisi**2
    print(f"Luas persegi : {luas}\n")
    menuAwal()
        
def luasPersegiPanjang():
    panjang = float(input("Masukkan Panjang : "))
    lebar = float(input("Masukkan Lebar : "))
    luas = panjang * lebar
    print(f"Luas Segitiga : {luas}\n")
    menuAwal()

def luasJajarGenjang():
    alas = float(input("Masukkan Alas : "))
    tinggi = float(input("Masukkan Tinggi : "))
    luas = alas * tinggi
    print(f"Luas Segitiga : {luas}\n")
    menuAwal()

def keluar():
    print("\n---->>>>>TERIMA KASIH<<<<<----")
    print("--------PROGRAM SELESAI-------")
    
menuAwal()
