number = int(input("Enter a four-digit number: "))

sum_of_digits = 0
reversed_number = 0

while number > 0:
  digit = number % 10
  sum_of_digits += digit
  reversed_number = reversed_number * 10 + digit
  number //= 10

print("Sum of digits:", sum_of_digits)
print("Reversed number:", reversed_number)
