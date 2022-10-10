# a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())
# if a2 <= a1 <= b2:
#     print(a1)
# else:
#     if a2 <= b1 <= b2:
#         print(b1)

# print("Hello world")

num = int(input())
while num > 0:
    num = num % 10
    num = num // 10
    x = min(num)
    y = max(num)
print('Наименьшее число', '=', x)
print('Наибольшее число', '=', y)