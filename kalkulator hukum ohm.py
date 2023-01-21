print("   SELAMAT DATANG DI KALKULATOR HUKUM OHM")
while (True):
    print("                 MENU                       ")
    print("1. MENGHITUNG R(Pengganti) pararel")
    print("2. MENGHITUNG R(Pengganti) seri")
    print("3. MENGHITUNG VOLT")
    print("4. MENGHITUNG HAMBATAN (R)")
    print("5. MENGHITUNG AMPERE")
    pilihan = int(input("pilih menu : "))
    if pilihan == 1:
        print("PILIH OPTION")
        print("1. 2 RESISTOR")
        print("2. 3 RESISTOR")
        print("3. 4 RESISTOR")
        pilih = int(input(""))
        if pilih == 1:
            # Mendefinisikan variabel hambatan
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))

            # menghitung hambatan pengganti secara paralel
            R_pengganti = 1 / (1/R1 + 1/R2)

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti, "ohm")

        elif pilih == 2:
            # Mendefinisikan variabel hambatan1
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))
            R3 = float(input("Masukkan hambatan 3 (dalam ohm): "))

            # menghitung hambatan pengganti secara paralel
            R_pengganti2 = 1 / (1/R1 + 1/R2 + 1/R3)

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti2, "ohm")

        elif pilih == 3:
            # Mendefinisikan variabel hambatan
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))
            R3 = float(input("Masukkan hambatan 3 (dalam ohm): "))
            R4 = float(input("Masukkan hambatan 4 (dalam ohm): "))

            # menghitung hambatan pengganti secara paralel
            R_pengganti3 = 1 / (1/R1 + 1/R2 + 1/R3 + 1/R4)

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti3, "ohm")

    elif pilihan == 2:
        print("PILIH OPTION")
        print("1. 2 RESISTOR")
        print("2. 3 RESISTOR")
        print("3. 4 RESISTOR")
        pilih = int(input(""))
        if pilih == 1:
            # Mendefinisikan variabel hambatan
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))

            # menghitung hambatan pengganti secara seri
            R_pengganti = R1 + R2

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti, "ohm")

        elif pilih == 2:
            # Mendefinisikan variabel hambatan1
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))
            R3 = float(input("Masukkan hambatan 3 (dalam ohm): "))

            # menghitung hambatan pengganti secara seri
            R_pengganti2 = R1 + R2 + R3

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti2, "ohm")

        elif pilih == 3:
            # Mendefinisikan variabel hambatan
            R1 = float(input("Masukkan hambatan 1 (dalam ohm): "))
            R2 = float(input("Masukkan hambatan 2 (dalam ohm): "))
            R3 = float(input("Masukkan hambatan 3 (dalam ohm): "))
            R4 = float(input("Masukkan hambatan 4 (dalam ohm): "))

            # menghitung hambatan pengganti secara seri
            R_pengganti3 = R1 + R2 + R3 + R4

            # menampilkan hasil hambatan pengganti ke layar
            print("Hambatan pengganti adalah: ", R_pengganti3, "ohm")

    elif pilihan == 3:
        # mendefinisikan variabel tegangan, arus, dan hambatan
        I = float(input("Masukkan arus (dalam ampere): "))
        R = float(input("Masukkan hambatan (dalam ohm): "))

        # menghitung arus menggunakan rumus V = IR
        V = I / R

        # menampilkan hasil arus ke layar
        print("tegangan adalah: ", V, "volt")

    elif pilihan == 4:
        # mendefinisikan variabel tegangan dan arus
        V = float(input("Masukkan tegangan (dalam volt): "))
        I = float(input("Masukkan arus (dalam ampere): "))

        # menghitung hambatan menggunakan rumus R = V / I
        R = V / I

        # menampilkan hasil hambatan ke layar
        print("Hambatan adalah: ", R, "ohm")

    elif pilihan == 5:
        # mendefinisikan variabel tegangan dan arus
        V = float(input("Masukkan tegangan (dalam volt): "))
        R = float(input("Masukkan hambatan (dalam ohm): "))

        # menghitung hambatan menggunakan rumus I = V / R
        I = V / R

        # menampilkan hasil hambatan ke layar
        print("arus adalah: ", I, "ampere")

    else:
        print("mohon ulangi lagi")
