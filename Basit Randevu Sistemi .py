

_author_ = "güneş"


print("Pazartesi (1)")
print("Salı (2)")
print("Çarşamba (3)")
print("Perşembe  (4)")
print("Cuma (5)")
print()
secim = input("Randevu almak istediğiniz günü seçin :")
isim = input("ADINIZ SOYADINIZ :")
# noinspection PyUnreachableCode
if secim == "1":
    print("Randevunuz Pazartesi Gününe Alınmıştır ")
    print()

elif secim == "2":
    print("Randevunuz Salı Gününe Alınmıştır ")
    print()
elif secim == "3":
    print("Randevunuz Çarşamba Gününe Alınmıştır ")
elif secim == "4":
    print("Randevunuz Perşembe Gününe Alınmıştır ")
elif secim == "5":
    print("Randevunuz Cuma Gününe Alınmıştır ")
    print()
else:
    print("Gün Aralığı geçersiz Randevu Oluşturulamamıştır.")




