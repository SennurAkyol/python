#kullanıcıdan girdi almak
#karar blokları
#döngüler

#print('2. gün başlangıc')

#kullanıcıdan girdi almak

#userInput=input()
#print(f'Girilen deger:{userInput}')

#type conversion

#numberStr='10'
#print(type(numberStr))
#number=int(numberStr)
#print(number)
#print(type(number))

#userInput=input() #kullanıcıdan ınput alma
#lessonNote=int(userInput)
#print(f'ders notunuz: {lessonNote}')

#indent
#n adet conditiona baglı karar bloğu
#if lessonNote > 50:
    #print('Geçtiniz')
#elif lessonNote == 50:
    #print('sınırda geçtiniz')
#else:
    #print('kaldınız')

#kullanıcıdan vize ve final notları alacak
# vize %40 final %60 etkili olacak
#vize ve final notları 50.5 gibi ondalıklı sayılar olabilir
#uygulama ortalamayı hesaplayacak ve ortalamaya göre
#0-49 FF
#50-60 DD
#60-70 CC
#70-80 BB
#80-100 AA
#not ortalamasını ve not harfini kullanıcıya gösterecek program kodlayınız


vize=float (input('vize notu giriniz'))
final=float (input('final notu giriniz'))

ortalama = vize*0.4 + final*0.6
print(f'ortalama:{ortalama}')

if ortalama >=0 and ortalama <50:
    print('FF')
elif ortalama >=50 and ortalama <60:
    print('DD')
elif ortalama >=60 and ortalama <70:
    print('CC')
elif ortalama >=70 and ortalama <80:
    print('BB')
else:
    print('AA')
















