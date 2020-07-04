print("Inputkan Umur : ")
umur = input()
umur = int(umur)

#conditions if else
if umur <= 1 :
    print("Bayi")
elif umur <= 10 :
    print("Anak-anak")
elif umur <= 19 :
    print("Remaja")
elif umur <= 60 :
    print("Dewasa")
else :
    print("Lanjut Usia")