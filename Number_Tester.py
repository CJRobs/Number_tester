def prime_test(numb):
    dum = False
    for i in range(2, numb):
        prime = numb % i
        if prime == 0:
            dum = True
            break
    if dum:
        print(f"{numb} number is not a prime")
        main_menu()
    else:
        print("{numb} is a prime".format(numb=numb))
        main_menu()


def div_test(numb):
    div = int(input("Select to see if it is divisible by a certain number: "))
    if numb % div == 0:
        print("Divisible by {div}".format(div=div))
        main_menu()
    else:
        print("Number not divisible by {div}".format(div=div))
        main_menu()


def product_tester(numb):
    for i in range(1, numb):
        prod = numb % i
        prod1 = numb // i
        if prod == 0:
            print("{prod1} and {i} is a pair of {numb}".format(prod1=prod1, i=i, numb=numb))


def main_menu():
    numb = int(input("Please enter a number between 1 & Infinity: "))
    print("Now a number has been selected you may choose from the following categories ")
    print("1. Prime number tester")
    print("2. Divisibility tester")
    print("3. Product tester")
    opt = int(input("Please select an option "))
    if opt == 1:
        prime_test(numb)
    elif opt == 2:
        div_test(numb)
    elif opt == 3:
        product_tester(numb)
    else:
        print("please select an integer from the list")


print("Welcome to the number tester")
main_menu()
