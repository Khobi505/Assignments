def factorial(num):
    
    factorial_list = []
    
    for i in range(1, (num + 1), 1):
        factorial_list.append(i)
    print(factorial_list)
    
    factorial_num = 1
    for x in factorial_list:
        factorial_num = factorial_num * x
    print(factorial_num)
        
        
          
    
factorial(20)