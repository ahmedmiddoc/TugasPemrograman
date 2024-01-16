def main_menu():
    print("\nMENU UTAMA")
    print("1. Transaksi Debet")
    print("2. Transaksi Kredit")
    print("3. Info Saldo")
    print("4. Keluar")
    return int(input("Masukkan pilihan: "))

def info_saldo(saldo):
    print("\nINFO SALDO")
    print(f"Saldo anda: Rp. {saldo}")

def masukkan_pin():
    pin = input("Masukkan PIN Anda: ")
    return pin

def cek_pin(pin_awal):
    pin = masukkan_pin()
    if pin == pin_awal:
        return True
    else:
        print("Maaf, PIN yang Anda masukkan salah.")
        return False

def transaksi_debet(saldo):
    print("\nTRANSAKSI DEBET")
    nominal = int(input("Masukkan nominal: "))
    if nominal > saldo:
        print("Maaf, saldo anda tidak mencukupi untuk transaksi ini.")
    else:
        saldo -= nominal
        print(f"Transaksi debet sebesar Rp. {nominal} berhasil.")
        return saldo

def transaksi_kredit(saldo):
    print("\nTRANSAKSI KREDIT")
    nominal = int(input("Masukkan nominal: "))
    saldo += nominal
    print(f"Transaksi kredit sebesar Rp. {nominal} berhasil.")
    return saldo

def exit_program():
    print("\nTERIMA KASIH TELAH MELAKUKAN TRANSAKSI DI ATM KAMI SEMOGA HARI MU MENYANGKAN !")

saldo_awal = 5000000
pin_awal = "1234"

while True:
    if cek_pin(pin_awal):
        menu_pilihan = main_menu()

        if menu_pilihan == 1:
            saldo_awal = transaksi_debet(saldo_awal)
            info_saldo(saldo_awal)
        elif menu_pilihan == 2:
            saldo_awal = transaksi_kredit(saldo_awal)
            info_saldo(saldo_awal)
        elif menu_pilihan == 3:
            info_saldo(saldo_awal)
        elif menu_pilihan == 4:
            exit_program()
            break
        else:
            print("Maaf, pilihan yang Anda masukkan tidak valid.")
    else:
        continue