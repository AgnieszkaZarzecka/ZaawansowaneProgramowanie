#Zad2

#a)

#przeniesienie parametrów do listy
def zwracanie_imion1(imie_1, imie_2, imie_3, imie_4, imie_5): 
   imiona = [imie_1, imie_2, imie_3, imie_4, imie_5]
   for i in imiona:
      print(i)

zwracanie_imion1('Agnieszka','Ania','Jakub','Dominika','Kacper')


def zwracanie_imion2(imiona):
   for i in imiona:
       print (i)

zwracanie_imion2(['Agnieszka','Ania','Jakub','Dominika','Kacper'])

#b)


def zwracanie_liczb(listofnumbers):
    result = []
    for number in listofnumbers:
      result.append(number*2)
    return result

print(zwracanie_liczb([1,2,3,4,5]))

#ii

def zwracanie_liczb2(listofnumbers):
   return [number * 2 for number in listofnumbers]


print(zwracanie_liczb2([1,2,3,4,5]))


for number in range(10):
    if number%2 != 1:
        print(number)


#c) 

for number in range(10):
    if number%2 != 1:
        print(number)

 #d)
list =list(range(0,10,2))
for i in list:
   print(i)
    