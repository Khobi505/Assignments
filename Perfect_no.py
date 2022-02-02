def perfect_no(num):
    
    factors = []
    for i in range(1, (num + 1), 1):
        if num % i == 0:
            factors.append(i)
    print("These are the factors of",num,":" ,factors)
    
    sum = 0
    if num == 1:
        print("\n{} is a perfect number.".format(num))
    else:
        for x in range(0, (len(factors) - 1), 1):
            Addition = sum + factors[x]
            if Addition > sum:
                sum = Addition
        print(Addition, "is the sum all of the factors of" , num)
        
        if Addition == num:
            print("\n{} is a perfect number.".format(num))
        else:
            print("\n{} is not a perfect number.".format(num))
perfect_no(496)