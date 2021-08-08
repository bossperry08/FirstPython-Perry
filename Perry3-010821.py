#Khai bao bien o duoi day:
a = "I am just a little girl named BP"
b = "2008"
c = "Perry"
d = u"Boss Perry"
e = u"2021"
f = u"minhtam"
g = "PEZ"
h = "My name is Pez. People usually call me Pez. And I'd love to be called Pez more than Pez."
i = "   BPDA   "
k = ".....TĐN....."

#Phần thực thi lệnh
print(a.capitalize())
print(a.swapcase())
print(a.upper())
print(a.lower())
print(a.casefold())
print(a.count('l'))
print(a.index('l'))
print(a.rindex('l'))
print(b.isalnum()) #True
print(c.isalnum()) #True
print(a.isalnum()) #False vi co khoang trang
print(a.isalpha())
print(b.isalpha())
print(c.isalpha())
print(a.isnumeric())
print(b.isnumeric())
print(c.isnumeric())
print(d.isnumeric())
print(e.isnumeric())
print(f.isnumeric())
print(a.isupper())
print(f.isupper())
print(g.isupper())
print(a.islower())
print(f.islower())
print(g.islower())
print(h.replace("Pez", c))
print(h.replace("Pez", c, 3))
print(len(a))
print(len(h))
print(h.find("Pez"))
print(h.rfind("Pez"))
print(a.find("Pez"))
print(i.strip())
print(k.strip('.'))
print(max(c))
print(max(28,119,3462))
print(max("Boss Perry", "PEZ", "BPDA cua Perry", key=len))
print(min(c))
print(min(28,119,3462))
print(min("Boss Perry", "PEZ", "BPDA cua Perry", key = len))
print(b + c)
print(c*3)
print(c in d)
print(b in a)
print(c not in d)
print(b not in a)
print(b < e)
print(b >= e)
print('s' != 'S')
print('A' == 'a')
print('A' == "65")

