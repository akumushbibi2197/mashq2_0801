#1-misol
n = input("Son kiriting: ")
print("Raqamlar soni:", len(n))

#2-misol
n = int(input("n = "))
faktorial = 1

for i in range(1, n+1):
    faktorial *= i
    print(f"{i}! = {faktorial}")

#3-misol
n = input("Son kiriting: ")
kopaytma = 1

for d in n:
    kopaytma *= int(d)

print("Raqamlar ko‘paytmasi:", kopaytma)

#4-misol
n = int(input("n = "))
a, b = 0, 1

for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b

#5-misol
start = int(input("Boshlang'ich son: "))
end = int(input("Oxirgi son: "))

for num in range(start, end+1):
    if str(num) == str(num)[::-1]:
        print(num, end=" ")
