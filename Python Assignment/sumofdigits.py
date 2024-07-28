def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))


def reverse_number(number):
    return int(str(number)[::-1])

number = int(input("Enter a four-digit number: "))

if 1000 <= number <= 9999:
    sum_digits = sum_of_digits(number)
    reversed_number = reverse_number(number)
    
    print(f"The sum of the digits is: {sum_digits}")
    print(f"The reversed number is: {reversed_number}")
else:
    print("Please enter a valid four-digit number.")
