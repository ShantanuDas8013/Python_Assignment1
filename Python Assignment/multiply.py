def multiply_list(lst):
    result = 1
    for num in lst:
        result *= num
    return result


numbers = [1, 2, 3, 4, 5]
product = multiply_list(numbers)
print("The product of all the items in the list is:", product)
