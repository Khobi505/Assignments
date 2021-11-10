
def prime_no():

    usernum = int(input("Please Type Your Number: "))


    if usernum == 2 or usernum == 3 or usernum == 5:
        print(usernum,"is a prime number.")
    else:
        if usernum % 2 == 0 or usernum % 3 == 0 or usernum % 5 == 0 or usernum == 1 or usernum == 0:
             print("{} is a not prime number.".format(usernum))
        else:
            print(usernum,"is a prime number.")
        
            

prime_no()



