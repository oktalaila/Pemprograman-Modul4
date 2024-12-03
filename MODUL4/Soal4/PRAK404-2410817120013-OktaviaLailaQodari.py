while True:
    print("\nPilih program")
    print("1. Penjumlahan")
    print("2. Pengurangan")
    print("3. Perkalian")
    print("4. Pembagian")
    print("5. Exit")
        
    pilihan = input("Masukkan Pilihan : ")
        
    if pilihan == '5':
        print("Terimakasih, telah menggunakan kalkulator Oktavia")
        break
        
    if pilihan in ['1', '2', '3', '4']:
        try:
            nilai1 = float(input("Masukkan nilai pertama : "))
            nilai2 = float(input("Masukkan nilai kedua : "))
        except ValueError:
            print("Input tidak valid, silakan masukkan angka.")
            continue
            
        if pilihan == '1':
            hasil = nilai1 + nilai2
            operasi = "Penjumlahan"
        elif pilihan == '2':
            hasil = nilai1 - nilai2
            operasi = "Pengurangan"
        elif pilihan == '3':
            hasil = nilai1 * nilai2
            operasi = "Perkalian"
        elif pilihan == '4':
            if nilai2 == 0:
                print("Error: Pembagian dengan nol tidak diperbolehkan.")
                continue
            hasil = nilai1 / nilai2
            operasi = "Pembagian"

        print(f"Hasil {operasi} antara {nilai1:.2f} dan {nilai2:.2f} adalah {hasil:.2f}")
    else:
        print("Input anda salah, silahkan coba lagi")