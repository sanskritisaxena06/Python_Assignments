
# Exercise 6: Find the sum of odd numbers from 1 to 100.

sum = 0

for i in range(1, 101):
    if i % 2 != 0:
        sum = sum + i

print("Sum of odd numbers =", sum)


