# Pattern 11: Increasing and Decreasing Number Pyramid

print("by sanskriti saxena ")

n = 5

for i in range(1, 2 * n):
    
    if i <= n:
        num = i
    else:
        num = 2 * n - i
    
    for j in range(1, num + 1):
        print(j, end=" ")
    
    print(end="\n")

print("saxenasanskriti")