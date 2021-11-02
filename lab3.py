#Zad1
def zwracam_stringa(name: str, surname: str) -> str:
     return (f'Hi {name} {surname}!')

x = zwracam_stringa('Julia','Nowak')
print(x)

#Zad2
def zwracam_iloczyn(number1: int, number2: int) -> int:
    return (number1 * number2)
   

print(zwracam_iloczyn(5,4))

#Zad3
def spr_czy_parzysta(number3: int) -> bool:
    if number3%2 == 0:
        return True
    else:
        return False

result = spr_czy_parzysta(5)

if result == True:
    print("Liczba parzysta")
elif result == False:
    print("Liczba nieparzysta")

#Zad4
def spr_sumy(num_1: int, num_2: int, num_3: int) -> bool:
    if num_1+num_2 >= num_3:
        return True
    else:
        return False
   
print(spr_sumy(1,2,4))



#Zad5
def sprawdzam_liste(arg1: list, arg2: int) -> bool:
    if arg2 in arg1:
        return True
    else:
        return False

print(sprawdzam_liste([1,2,3],2))



#Zad6
def operacje_na_listach(list1: list, list2: list) -> list:
   temporary_list=list1 + list2 
   temporary_list=list(set(temporary_list))
   final_list= [i**3 for i in temporary_list]
  
   return (final_list)

print(operacje_na_listach([1,2,3],[1,2,4]))
#operacje_na_listach([1,2,3],[1,2,4])