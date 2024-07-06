def prime_checker(number):
    is_prime = True
    for i in range(2, number):
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("Prime Number")
    else:
        print("Not Prime")


n = int(input("Enter number : "))
prime_checker(number=n)
