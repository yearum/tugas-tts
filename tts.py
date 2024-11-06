while True:
    print("""
    Pilih Jenis Bangun:
    1. Bangun Datar
    2. Bangun Ruang
    """)
    jenis_bangun = input("Pilih (1/2) atau 'Next' untuk keluar: ")
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
            luas = alas * tinggi
            keliling = 2 * (alas + sisi_miring)
            print("Nama Bangun : Jajar Genjang")
            print("Luas :", luas)
            print("Keliling :", keliling)
        
        elif bangun_datar == '2a':
            alas_atas = float(input("Masukkan alas atas trapesium: "))
            alas_bawah = float(input("Masukkan alas bawah trapesium: "))
            tinggi = float(input("Masukkan tinggi trapesium: "))
            sisi_miring = float(input("Masukkan sisi miring trapesium: "))
            luas = (alas_atas + alas_bawah) * tinggi / 2
            keliling = alas_atas + alas_bawah + 2 * sisi_miring
            print("Nama Bangun : Trapesium Beraturan")
            print("Luas :", luas)
            print("Keliling :", keliling)
        
        elif bangun_datar == '2b':
            alas_atas = float(input("Masukkan alas atas trapesium: "))
            alas_bawah = float(input("Masukkan alas bawah trapesium: "))
            tinggi = float(input("Masukkan tinggi trapesium: "))
            sisi_miring = float(input("Masukkan sisi miring trapesium: "))
            sisi_tegak = float(input("Masukkan sisi tegak trapesium: "))
            luas = (alas_atas + alas_bawah) * tinggi / 2
            keliling = alas_atas + alas_bawah + sisi_miring + sisi_tegak
            print("Nama Bangun : Trapesium Tak Beraturan")
            print("Luas :", luas)
            print("Keliling :", keliling)

        elif bangun_datar == '3':
            sisi = float(input("Masukkan panjang sisi persegi lima: "))
            luas = 5 * sisi * (sisi / (2 * (3**0.5)))
            keliling = 5 * sisi
            print("Nama Bangun : Persegi Lima")
            print("Luas :", luas)
            print("Keliling :", keliling)

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
            luas_permukaan = 2 * (p * l + p * t + l * t)
            volume = p * l * t
            print("Nama Bangun : Balok")
            print("Luas Permukaan :", luas_permukaan)
            print("Volume Bangun :", volume)
        
        elif bangun_ruang == '2':
            r = float(input("Masukkan jari-jari kerucut: "))
            t = float(input("Masukkan tinggi kerucut: "))
            s = float(input("Masukkan panjang garis pelukis kerucut: "))
            luas_permukaan = 3.14 * r * (r + s)
            volume = (1/3) * 3.14 * r**2 * t
            print("Nama Bangun : Kerucut")
            print("Luas Permukaan :", luas_permukaan)
            print("Volume Bangun :", volume)

        elif bangun_ruang == '3':
            sisi = float(input("Masukkan panjang sisi alas prisma: "))
            tinggi = float(input("Masukkan tinggi prisma: "))
            jumlah_sisi = int(input("Masukkan jumlah sisi alas prisma (4/5/6): "))
            luas_alas = sisi**2 / (4 * (3**0.5) / 3)
            luas_permukaan = (jumlah_sisi * sisi * tinggi) + (2 * luas_alas)
            volume = luas_alas * tinggi
            print("Nama Bangun : Prisma")
            print("Luas Permukaan :", luas_permukaan)
            print("Volume Bangun :", volume)
        
        else:
            print("Pilihan tidak valid.")

    else:
        print("Pilihan tidak valid.")
