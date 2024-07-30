n = 4
for i in range(n):
    for j in range(i + 1):
        print(chr(((ord("A") + n - 1) - (i - j))), end=" ")
    print()