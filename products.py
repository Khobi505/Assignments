def product(numbers):

    max1 = max2 = max3 = 0
    min1 = min2 = 0
    for number in numbers:
        if number > max1: 
            max3, max2, max1 = max2, max1, number
        elif number > max2:
            max3, max2 = max2, number
        elif number > max3:
            max3 = number
        elif number < min1:
            min2, min1 = min1, numbers
        elif number < min2:
            min2 = number
    product1 = max1 * max2 * max3
    product2 = max1 * min1 * min2

    highest = max(product1, product2)

    print(highest)

product([2, -10, - 5 , -10])
            