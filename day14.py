n = 5
for r in range(1, n+1):
    for c in range(1, r+1):
        print(c,end=" ")
    print()

for i in range(1, 6):
    for j in range(i):
        print(i, end=" ")
    print()

n = 5
for i in range(1, n+1):
    for j in range(i):
        print(1, end=" ")
    print()

n = 5
for i in range(1, n+1):
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()

n = 5
for r in range(1, n+1):
    for c in range(n-r):
        print(" ", end="")
    for c in range(1, r+1):
        print(c, end=" ")
    print()