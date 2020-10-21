#Fibonacci

def fibonacci(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

data = list(fibonacci(6))
print(data)


# def fibonacci():
#     a, b = 1, 1
#     while True:
#         yield a
#         a, b = b, a + b

# gen = fibonacci()
# for i in range(5):
#     print(next(gen))

# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n

# print(fac(4))


##Пользователь вводит число. Вычислите факториал этого числа,
##факториалом называется произвидение всех чисел внутри числа который ввел пользователь,
##Пример: n = 4 , 1 * 2 * 3 * 4 = 24

# def fac(n):
#     if n == 0:
#         return 1
#     return fac(n-1) * n

# print(fac(4))


# for x in range (1, 15):
# 	if x % 3 == 0 and x % 5 == 0:
# 		print('SoloLearn')
# 	elif x % 2 == 0:
# 		continue
# 	elif x % 3 == 0:
# 		print('Solo')
# 	elif x % 5 == 0:
# 		print('Learn')
# 	else:
# 		print(x)
