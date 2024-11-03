def luas_jajar_genjang(alas, tinggi):
    return alas * tinggi

def keliling_jajar_genjang(alas, sisi_miring):
    return 2 * (alas + sisi_miring)

def luas_trapesium(alas_atas, alas_bawah, tinggi):
    return (alas_atas + alas_bawah) * tinggi / 2

def keliling_trapesium_beraturan(alas_atas, alas_bawah, sisi_miring):
    return alas_atas + alas_bawah + 2 * sisi_miring

def keliling_trapesium_tak_beraturan(alas_atas, alas_bawah, sisi_miring, sisi_tegak):
    return alas_atas + alas_bawah + sisi_miring + sisi_tegak

def luas_persegi_lima(sisi):
    return 5 * sisi * (sisi / (2 * (3**0.5)))

def keliling_persegi_lima(sisi):
    return 5 * sisi

def luas_permukaan_balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

def volume_balok(p, l, t):
    return p * l * t

def luas_permukaan_kerucut(r, s):
    return 3.14 * r * (r + s)

def volume_kerucut(r, t):
    return (1/3) * 3.14 * r**2 * t

def luas_permukaan_prisma(sisi, tinggi, jumlah_sisi):
    return (jumlah_sisi * sisi * tinggi) + (2 * (sisi**2 / (4 * (3**0.5) / 3)))

def volume_prisma(sisi, tinggi, jumlah_sisi):
    return (sisi**2 / (4 * (3**0.5) / 3)) * tinggi

while True:
    print("""
    Pilih Jenis Bangun:
    1. Bangun Datar
    2. Bangun Ruang
    """)
    jenis_bangun = input("Pilih (1/2) atau 'next' untuk keluar: ")
    if jenis_bangun.lower() == 'q':
        print("Program dihentikan.")
        break

    if jenis_bangun == '1':
        print("""
        Pilih Bangun Datar:
        1. Jajar Genjang
        2. Trapesium
           a. Beraturan
           b. Tak Beraturan
        3. Persegi Lima
        """)
        bangun_datar = input("Pilih Bangun Datar (1/2a/2b/3): ")
        
        if bangun_datar == '1':
            alas = float(input("Masukkan alas jajar genjang: "))
            tinggi = float(input("Masukkan tinggi jajar genjang: "))
            sisi_miring = float(input("Masukkan sisi miring jajar genjang: "))
            print("Nama Bangun : Jajar Genjang")
            print("Luas :", luas_jajar_genjang(alas, tinggi))
            print("Keliling :", keliling_jajar_genjang(alas, sisi_miring))
        
        elif bangun_datar == '2a':
            alas_atas = float(input("Masukkan alas atas trapesium: "))
            alas_bawah = float(input("Masukkan alas bawah trapesium: "))
            tinggi = float(input("Masukkan tinggi trapesium: "))
            sisi_miring = float(input("Masukkan sisi miring trapesium: "))
            print("Nama Bangun : Trapesium Beraturan")
            print("Luas :", luas_trapesium(alas_atas, alas_bawah, tinggi))
            print("Keliling :", keliling_trapesium_beraturan(alas_atas, alas_bawah, sisi_miring))
        
        elif bangun_datar == '2b':
            alas_atas = float(input("Masukkan alas atas trapesium: "))
            alas_bawah = float(input("Masukkan alas bawah trapesium: "))
            tinggi = float(input("Masukkan tinggi trapesium: "))
            sisi_miring = float(input("Masukkan sisi miring trapesium: "))
            sisi_tegak = float(input("Masukkan sisi tegak trapesium: "))
            print("Nama Bangun : Trapesium Tak Beraturan")
            print("Luas :", luas_trapesium(alas_atas, alas_bawah, tinggi))
            print("Keliling :", keliling_trapesium_tak_beraturan(alas_atas, alas_bawah, sisi_miring, sisi_tegak))

        elif bangun_datar == '3':
            sisi = float(input("Masukkan panjang sisi persegi lima: "))
            print("Nama Bangun : Persegi Lima")
            print("Luas :", luas_persegi_lima(sisi))
            print("Keliling :", keliling_persegi_lima(sisi))

        else:
            print("Pilihan tidak valid.")

    elif jenis_bangun == '2':
        print("""
        Pilih Bangun Ruang:
        1. Balok
        2. Kerucut
        3. Prisma
        """)
        bangun_ruang = input("Pilih Bangun Ruang (1/2/3): ")

        if bangun_ruang == '1':
            p = float(input("Masukkan panjang balok: "))
            l = float(input("Masukkan lebar balok: "))
            t = float(input("Masukkan tinggi balok: "))
            print("Nama Bangun : Balok")
            print("Luas Permukaan :", luas_permukaan_balok(p, l, t))
            print("Volume Bangun :", volume_balok(p, l, t))
        
        elif bangun_ruang == '2':
            r = float(input("Masukkan jari-jari kerucut: "))
            t = float(input("Masukkan tinggi kerucut: "))
            s = float(input("Masukkan panjang garis pelukis kerucut: "))
            print("Nama Bangun : Kerucut")
            print("Luas Permukaan :", luas_permukaan_kerucut(r, s))
            print("Volume Bangun :", volume_kerucut(r, t))

        elif bangun_ruang == '3':
            sisi = float(input("Masukkan panjang sisi alas prisma: "))
            tinggi = float(input("Masukkan tinggi prisma: "))
            jumlah_sisi = int(input("Masukkan jumlah sisi alas prisma (4/5/6): "))
            print("Nama Bangun : Prisma")
            print("Luas Permukaan :", luas_permukaan_prisma(sisi, tinggi, jumlah_sisi))
            print("Volume Bangun :", volume_prisma(sisi, tinggi, jumlah_sisi))
        
        else:
            print("Pilihan tidak valid.")

    else:
        print("Pilihan tidak valid.")
