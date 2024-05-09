number = int(input("Enter your number:"))

b = ''

while number > 0:
    b = str(number % 2) + b
    number = number // 2

print(b)
