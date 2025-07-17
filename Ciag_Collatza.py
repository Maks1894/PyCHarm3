# Ciąg Collatza zdefiniowany jest następująco:
# Rozpoczynamy od podanej ze standardowego wejścia liczby x (od 1 do 100).
# Jeśli x jest liczbą parzystą, to kolejny wyraz ciągu będzie obliczony jako x/2.
# W przeciwnym przypadku kolejny wyraz ciągu będzie równy 3x+1.
# W ten sam sposób obliczamy kolejne wyrazy ciągu, aż pojawi się liczba 1.
#
# Napisz program, który wypisze długość ciągu Collatza dla podanego ze standardowego wejścia x.
# X może przyjmować wartości od 1 do 100.
x = int(input("Podaj x (od 1 do 100): "))
if x < 1 or x > 100:
     print ('Nie prawidlo wartos x, wpisz ilosc od 1 do 100')
else :
     dlugosc = 1

while True :
     if x == 1 :
          break
     elif x % 2:
          x= 3*x + 1
          print (x)

     else :
          x = x//2
          print (x)

     dlugosc += 1
print(f'Dlugos ciagu Collatza dla x jest: {dlugosc}')