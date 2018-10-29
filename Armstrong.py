def armstrong (number):
    sum = 0
    for j in str(number):
        slice = int(j) % 10
        sum += slice ** len(str(number))
        j = int(j) / 10
    if sum == i:
        return True
    return False

start = int(input("Enter the start number"))
end = int(input("Enter the end number"))

for i in range(start, end+1):
    if armstrong(i):
        print(i)
