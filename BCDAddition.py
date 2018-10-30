# Manual way to BCD
# def to_bcd(number):
#      number = str(number)
#      result = 0
#      for digit in number:
#         result = (result << 4) + int(digit)
#      return "{0:b}".format(result)
def add_binary(bin_num1, bin_num2):
    result = ''
    carry = 0
    i=3 
    while i >= 0:
        temp = carry 
        temp += 1 if bin_num1[i]=='1' else 0
        temp += 1 if bin_num2[i]=='1' else 0
        result = ('1' if temp%2 == 1 else '0') + result
        carry = 1 if temp > 1 else 0
        i-=1
    if carry == 1:
        result = '1' + result
    return result

class BCDNumber():
    
    def __init__(self, number1):
        self.num = []
        temp = '{0:b}'.format(int(str(number1), 16))
        off = len(temp)%4
        if(off > 0):
            off = 4-off
        temp = ('0')*off + temp
        num_size =  len(temp)
        i=0
        while i < num_size:
            self.num.append(temp[i:i+4])
            i+=4
    
    def make_zero(self):
        self.num = '0000'

    def make_one(self):
        self.num = '0001'

    def append_digits(self, digits):
        for i in range(digits):
            self.num.insert(0, '0000')

    def get_decimal(self):
        return ''.join(str(int(x, 2)) for x in self.num)

    def add(self, num2):
        result = BCDNumber(self.get_decimal())
        self_size = len(result.num)
        num2_size = len(num2.num)
        if self_size > num2_size:
            num2.append_digits(self_size - num2_size)
        elif num2_size > self_size:
            self.append_digits(num2_size - self_size)
        i = len(result.num)-1
        digit = ''
        while i > 0:
            digit = add_binary(result.num[i], num2.num[i])
            print(digit)
            if int(digit, 2) > 9:
                if len(digit) > 4:
                    result.num[i] = add_binary('0110', digit[1:5])
                else:
                    result.num[i] = add_binary('0110', digit)[1:5]
                result.num[i-1] = add_binary('0001', result.num[i-1])
            else:
                result.num[i] = digit
            i-=1
        digit = add_binary(result.num[0], num2.num[0])
        if int(digit, 2) > 9:
            if len(digit) > 4:
                result.num[0] = add_binary('0110', digit[1:5])
            else:
                result.num[0] = add_binary('0110', digit)[1:5]
            result.num.insert(0, '0001')
        else:
            result.num[0] = digit
        result.show()
        return result

    def show(self):
        print(self.num)
        print(''.join(self.num))
        

# def add(num1, num2):
#     result = ''
#     carry = ''
#     tempCarry = 0
#     i=3 
#     while i >= 0:
#         temp = tempCarry 
#         temp += 1 if num1[i]=='1' else 0
#         temp += 1 if num2[i]=='1' else 0
#         result = ('1' if temp%2 == 1 else 0) + result
#         tempCarry = 1 if temp > 1 else 0
#         i-=1
#     if tempCarry == 1:
#         result = '1' + result
#     return result , carry

# def add_bcd(num1, num2):
#     result = ''
#     size = max(len(num1), len(num2))
#     num1 = num1.zfill(size)
#     num2 = num2.zfill(size)
#     c = '' # carry
#     i = size
#     while i >= 4:
#         temp , c = add(num1[i-4:i], num2[i-4:i])
#         i-=4
#     return result

# x = input()
# y = input()
# # Easy way to BCD
# number1 = '{0:b}'.format(int(x, 16))
# number2 = '{0:b}'.format(int(y, 16))
# off = len(number1)%4
# if(off > 0):
#     off = 4-off
# number1 = number1[::-1] + ('0')*off
# off = len(number2)%4
# if(off > 0):
#     off = 4-off
# number2 = number2[::-1] + ('0')*off
# print(number1)
# print(number2)

bcd1 = BCDNumber(input())
bcd2 = BCDNumber(input())

# bcd1.show()
# bcd2.show()
# print(bcd1.get_decimal())
print(bcd1.add(bcd2).get_decimal())
