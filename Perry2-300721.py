
print("Python"[-2])

print("Perry"[1:4])

#Ex1:

a = "Học Python"
b = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit.
Sed tristique odio eget elit dapibus, ultricies congue ante viverra.
Nulla facilisi.'''
print(len(a))
print(len(b))


#Ex2: 
n = "Nimbus Computer School"
print(len(n))
print(n[2], n[-6])
print(n[0:6])
print(n[-6:])
print(n[-15:-7])

h = "abc {} def"
m = 40
print(h.format(m))

#Ex1.2.8
a = 3
b = "Nimbus"
print(b, b, b)
print(b*3)
print(b*a)
print(b, str(a))

#Ex2.2.8
retained = 100
interest = 0.15
result = 100 * (1 + interest)**7
print(result)
r = '''I have {} in my saving account
After 7 years, I will have {}
    '''
print(r.format(retained, result))
#Ex3.2.8
sales_jul, sales_aug, sales_sep = 1532, 2020, 1876
maxsales = max(sales_jul, sales_aug, sales_sep)
minsales = min(sales_jul, sales_aug, sales_sep)
print(maxsales, minsales)
print("Maximum value of sales transactions in quarter 3 is {}".format(maxsales))
print("The value of sales transactions in Jul, Aug and Sep were {}, {} and {}, respectively.".format(sales_jul, sales_aug, sales_sep))
print("The maximum value of sales transaction was {1}, then {2} and the minimum value was {0}".format(sales_jul, sales_aug, sales_sep))
