def armstrong (number):
    sum = 0
    for j in str(i):
        slice = int(j) % 10
        sum += slice ** len(str(i))
        j = int(j) / 10
    if sum == i:
        return True
    return False

start = int(input())
end = int(input())

for i in range(start, end+1):
    if armstrong(i):
        print(i)
