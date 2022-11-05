def ordinal():
    print("Ordinal Number")
    print("ketik 0 untuk menghentikan program")
    while True:
        num = int(input("Masukan sebuah ankga: "))
        if num in [10, 11, 12, 13]:
            print("(", num, "'th'", ")")
        else:
            ka = num % 10
            if ka == 1:
                print("(", num, "'st", ")")
            elif ka == 2:
                print("(", num, "'nd'", ")")
            elif ka == 3:
                print("(", num, "'rd'", ")")
            else:
                print("(", num, "'th'", ")")
        if num == 0:
            print("Terima kasih sudah menggunakan program")
            print("Andri Martin - 046002200010")
            break
a = ordinal()
print(a)