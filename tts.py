import math

print("SELAMAT DATANG DI PROGRAM HITUNG BANGUN")

while True:
    print("\nMenu Bangun Datar:")
    print("1. Jajar Genjang")
    print("2. Trapesium")
    bangun_datar = input("Pilih nomor bangun datar yang diinginkan atau ketik 'exit' untuk keluar: ")
    
    if bangun_datar.lower() == 'exit':
        break

    print("\nMenu Bangun Ruang:")
    print("1. Balok")
    print("2. Kerucut")
    print("3. Prisma")
    bangun_ruang = input("Pilih nomor bangun ruang yang diinginkan atau ketik 'exit' untuk keluar: ")

    if bangun_ruang.lower() == 'exit':
        break

    if bangun_datar == '1':
        print("\nAnda memilih Jajar Genjang.")
        alas = float(input("Masukkan panjang alas: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_miring = float(input("Masukkan panjang sisi miring: "))
        luas_datar = alas * tinggi
        keliling_datar = 2 * (alas + sisi_miring)
        print("Luas Jajar Genjang:", luas_datar)
        print("Keliling Jajar Genjang:", keliling_datar)

    elif bangun_datar == '2':
        print("\nAnda memilih Trapesium.")
        alas_atas = float(input("Masukkan panjang alas atas: "))
        alas_bawah = float(input("Masukkan panjang alas bawah: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_miring1 = float(input("Masukkan panjang sisi miring 1: "))
        sisi_miring2 = float(input("Masukkan panjang sisi miring 2: "))
        luas_datar = 0.5 * (alas_atas + alas_bawah) * tinggi
        keliling_datar = alas_atas + alas_bawah + sisi_miring1 + sisi_miring2
        print("Luas Trapesium:", luas_datar)
        print("Keliling Trapesium:", keliling_datar)

    else:
        print("Pilihan bangun datar tidak valid.")

    if bangun_ruang == '1':
        print("\nAnda memilih Balok.")
        panjang = float(input("Masukkan panjang: "))
        lebar = float(input("Masukkan lebar: "))
        tinggi = float(input("Masukkan tinggi: "))
        luas_permukaan = 2 * (panjang * lebar + panjang * tinggi + lebar * tinggi)
        volume = panjang * lebar * tinggi
        print("Luas Permukaan Balok:", luas_permukaan)
        print("Volume Balok:", volume)

    elif bangun_ruang == '2':
        print("\nAnda memilih Kerucut.")
        radius = float(input("Masukkan jari-jari: "))
        tinggi = float(input("Masukkan tinggi: "))
        sisi_miring = math.sqrt(radius ** 2 + tinggi ** 2)
        luas_permukaan = math.pi * radius * (radius + sisi_miring)
        volume = (1/3) * math.pi * radius ** 2 * tinggi
        print("Luas Permukaan Kerucut:", luas_permukaan)
        print("Volume Kerucut:", volume)

    elif bangun_ruang == '3':
        print("\nAnda memilih Prisma.")
        sisi_alas = float(input("Masukkan panjang sisi alas segi empat: "))
        tinggi_prisma = float(input("Masukkan tinggi prisma: "))
        luas_permukaan = 2 * sisi_alas**2 + 4 * sisi_alas * tinggi_prisma
        volume = sisi_alas**2 * tinggi_prisma
        print("Luas Permukaan Prisma:", luas_permukaan)
        print("Volume Prisma:", volume)

    else:
        print("Pilihan bangun ruang tidak valid.")

    print("\n---- Penghitungan selesai ----\n")