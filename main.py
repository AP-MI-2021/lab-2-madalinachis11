import math
'''
Returneaza toate numere din intervalul [start,stop] care sunt patrate perfecte.
'''
def get_perfect_squares(start,stop):
    lista=[]
    for i in range(start,stop+1):
        #j=2
        #while j*j<i
            #j++
        #if j*j==i:
        #lista.append(i)
        if math.sqrt(i)==int(math.sqrt(i)):
            lista.append(i)
    return lista
'''
Functa returneaza daca numarul introdus de utilizator este palindrom sau nu.
'''
def is_palindrome(n) ->bool:
    palindrom=0
    palindromcopie=n
    while n!=0:
        ultima=int(n%10)
        palindrom=palindrom*10+ultima
        n=int(n/10)
    if palindrom==palindromcopie:
        return 1
    else:
        return 0
'''
Functia testeaza daca un numar este palindrom utilizand functia is_palindrome.
'''
def test_is_palindrome():
    assert (is_palindrome(515)==True)
    assert (is_palindrome(11)==True)
    assert (is_palindrome(13)==False)

'''
Functia testeaza daca intre doua numere se afla anumite patrate perfecte.
'''
def test_get_perfect_squares():
    lst = get_perfect_squares(2,10)
    assert (lst[0] == 4)
    assert (lst[1] == 9)
    lst = get_perfect_squares(10,17)
    assert (lst[0] == 16)

'''
Functia principala pentru interfata consolei.
'''
def main():
    while True:
            print('1.   Verifica daca un numar este palindrom.')
            print('2.   Toate pătratele perfecte dintr-un interval închis dat.')
            print('x    Exit. ')
            optiune = input('Optiune:')
            if optiune == '1':
                x = int(input('Introduceti numarul:'))
                if is_palindrome(x):
                    print(f'Numarul {x} este palindrom.')
                else:
                    print(f'Numarul {x} nu este palindrom.')
                test_is_palindrome()
            elif optiune == '2':
                st = int(input('Introduceti marginea inferioara a intervalului:'))
                fn = int(input('Introduceti marginea superioara a intervalului:'))
                print(f'Patratele perfecte din intervalul [{st},{fn}] sunt: {get_perfect_squares(st,fn)}')
                test_get_perfect_squares()
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')


main()

