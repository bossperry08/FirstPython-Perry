# -*- coding: utf-8 -*-
#Phần import module
import decimal
import fractions #load module fractions
import math
#Phần khai báo biến
a = decimal.Decimal(10) / decimal.Decimal(3)
b = decimal.Decimal(100) / decimal.Decimal(3)
m = fractions.Fraction('1.67') 
n = fractions.Fraction(5) 
o = fractions.Fraction(1,3) 
'''
print(0.1) #Output: 0.1
print(decimal.Decimal(0.1)) #Output: Decimal 0.1000000000000000055511151231257827021181583404541015625
from decimal import Decimal as D #from module decimal import package Decimal as D (prefix)
#output: Decimal('3.3')
print(D('1.1') + D('2.2'))
#output: Decimal('3.000')
print(D('1.2') * D('2.50'))
getcontext().prec = 8 #Lấy 8 chữ số tính cả phần nguyên và phần thập phân
print(a)
print(b)
print(m) #in dạng phân số 1.5, output: 3/2
print(n) #in dạng phân số của 5, output: 5
print(o) #in 1 phân số có tử là 1, mẫu là 3
print(fractions.Fraction(1.1))
print(fractions.Fraction('1.1'))
from fractions import Fraction as F
print(F(3.5))
#Phân biệt giữa phép chia bình thường và phép chia lấy phần thương nguyên:
print(7/5)
print(7//5)
print(8/5)
print(8//5)
#Hằng số toán học
print(math.pi)
print(math.e)
'''
#Hàm tính toán
print(abs(-28))
print(math.ceil(8.7))
print((a > b) - (a < b))
print(math.exp(5))
print(math.fabs(-12.24))
print(math.floor(45.1))
print(math.gcd(144, 96))
print(math.hypot(3,4))
print(math.lcm(4,6))
print(max(45,293,1827,3726,2,34,19))
print(min(1627,342,61,82,28382))
print(math.modf(a))
print(math.pow(5,7))
print(round(a, 2))
print(math.sqrt(144))
print(math.trunc(48.9))