number = str(input("Enter Number "))
baseA = int(input("Enter Number base "))
baseB = int(input("Convert it to base "))

number = int(number, baseA)
result = ""

while number > 0:
    digit = number % baseB
    result = str(digit) + result
    number = int(number/baseB)

print(result)
