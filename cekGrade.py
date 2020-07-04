def cekGrade(nilai):
    if nilai >= 80:
        return "A"
    elif nilai >= 70:
        return "B"
    else :
        return "C"

print("Masukkan Nilai Anda : ")
nilaiAnda = input()
nilaiAnda = int(nilaiAnda)

grade = cekGrade(nilaiAnda)

print("Grade anda adalah", grade)