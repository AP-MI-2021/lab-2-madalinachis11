import math
'''
Problema 12
Returneaza toate numerele din intervalul [start,stop] care sunt patrate perfecte.
Start reprezinta capatul din stanga al intervalului.
Stop reprezinta capatul din dreapta al intervalului.
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
Problema 10
Returneaza combinari de n luate cate k.
'''
def get_n_choose_k(n,k):
    n_factorial=1
    for i in range(1,n+1):
        n_factorial=n_factorial*i
    k_factorial=1
    for i in range(1,k+1):
        k_factorial=k_factorial*i
    nk_factorial=1
    for i in range(1,n-k+1):
        nk_factorial=nk_factorial*i
    result=n_factorial/(k_factorial*nk_factorial)
    return result
'''
Problema 5
Functa returneaza daca numarul introdus de utilizator este palindrom sau nu.
"n" este numarul care trebuie studiat.
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
Problema 5
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
Functia testeaza combinarile de n luate cate k.
'''
def test_get_n_choose_k():
    assert(get_n_choose_k(5,4))
    assert(get_n_choose_k(10,3))
    assert(get_n_choose_k(9,5))

'''
Functia principala pentru interfata consolei.
'''

def main():
    while True:
            print('1.   Verifica daca un numar este palindrom.')
            print('2.   Toate pătratele perfecte dintr-un interval închis dat.')
            print('3.   Combinari de n luate cate k.')
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
                st = int(input('Introduceti capatul din stanga al intervalului:'))
                fn = int(input('Introduceti capatul din dreapta al intervalului:'))
                print(f'Patratele perfecte din intervalul [{st},{fn}] sunt: {get_perfect_squares(st,fn)}')
                test_get_perfect_squares()
            elif optiune == '3':
                a = int(input('Introduceti numarul n:'))
                b = int(input('Introduceti numarul k:'))
                print(f'Combinari de {a} luate cate {b} sunt:{int(get_n_choose_k(a,b))}')
                test_get_n_choose_k()
            elif optiune == 'x':
                break
            else:
                print('Optiune invalida.')

if __name__ == '__main__':
   main()

