import random

def guess_number():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed = False

    print("selamat datang di permainan Tebak Angka")
    print("Saya telah memilih sebuah angka antara 1 dan 100.")
    
    while not guessed:
        guess = int(input("Tebakan Anda: "))
        attempts += 1
        
        if guess < number_to_guess:
            print("terlalu rendah. coba lagi!")
        elif guess > number_to_guess:
            print("terlalu tinggi. coba lagi!")
        else:
            guessed = True
            print(f"Slamat Anda menebak angka dengan benar dalam {attempts} percobaan.")
    
    print("terima kasih telah bermain!")

# Jalankan permainan
guess_number()