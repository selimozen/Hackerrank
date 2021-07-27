#ENG: if n is odd, print Weird , if n is even and in the inclusive range of 2 to 5, print Not Weird, 
#if n is even and in the inclusive range of 6 to 20, print Weird, if  is even and greater than 20, print Not Weird
#TR: Eğer n sayısı tekil ise, 'Weird' yazdır, eğer n sayısı 2 veya 5'e eşit veya arasında ise Not Weird yazdır, eğer n sayısı 6 ile 20'ye eşit veya arasında ise Weird yazdır.
#Eğer n sayısı 20'den büyük ise Not Weird yazdır.

if(n%2==1) or n in range (5,21):
    print("Weird")
else:
    print("Not Weird")
