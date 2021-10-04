def is_palindrome(n):
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




a=int(input("Introdu numarul tau:"))
print(is_palindrome(a))

