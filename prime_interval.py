def prime_interval():

    print("Do you want know the prime numbers in an involve of numbers?")
    print("------------------------------------------------------------")
    
    
    usernum_1 = int(input("What number do you want to begin with?\n"))
    usernum_2 = int(input("What number do you want to end your interval with?\n"))

    numlist = [] 

    for i in range(usernum_1, (usernum_2)+1, 1):
        numlist.append(i)
    print(numlist)

    print("\n\nFrom the above list, these are the prime number in it:")

    prime_list = []
    othernum_list = []

    for number in numlist:
        if number == 2 or number == 3 or number == 5:
            prime_list.append(number)
        else:
            if number % 2 == 0 or number % 3 == 0 or number % 5 == 0 or number == 1 or number == 0:
                othernum_list.append(number)
            else:
                prime_list.append(number)
                
    print(prime_list)

prime_interval()