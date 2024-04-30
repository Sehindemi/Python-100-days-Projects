
def prime_checker(number):
    isprime = True
    for num in range(2, number):
        if number % num == 0:
            isprime = False
    if isprime:
        print("Prime number")
    else:
        print("Not prime number")


n = int(input())
prime_checker(number=n)