#-*- coding=utf-8 -*-
import random
import os

N = 10

nums = []

for i in range(N):
    nums.append(random.randint(0, 99))

print("Запомните числа")
print(nums)
input("нажмите enter для продолжения")

os.system("cls")

i = random.randint(1, len(nums))

n = input(f"какое число было {i} ")

try_amount = 1
try:
    while try_amount < 3:
        n = int(n)
        if n == nums[i-1]:
            print("правильно")
            break
        else:
            print("неправильно")
            try_amount += 1
            n = int(input(f"еще одна попытка\nпопытка {try_amount} "))
except:
    print("произошла ошибка")
        

