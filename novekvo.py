#Órai munka

print("Kérj be 3 számot és a program növekvő sorrendbe helyezi őke.t")
a = float(input("Első szám: "))
b = float(input("Második szám: "))
c = float(input("Haramadik szám: "))

if a > b > c:
    print(c,b,a)
elif a > c > b:
    print(a,c,b)
elif b > a > c:
    print(b,a,c)
elif b > c > a:
    print(b,c,a)
elif c > a > b:
    print(c,a,b)
else:
    print(c,b,a)