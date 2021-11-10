


def largest(numbers):
    # for i in range(len(numbers) - 1):
    #     new = str(numbers[i])
    #     numbers = []
    #     numbers.append(new)
    # print(numbers)
    # print(type(numbers[0]))
    numbers.sort(key = custom_compare)
    numbers = [str(i) for i in numbers]
    for i in numbers:


largest([1,2])