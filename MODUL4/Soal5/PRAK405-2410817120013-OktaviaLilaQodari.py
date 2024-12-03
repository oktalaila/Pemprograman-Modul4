a, b = map(int, input().split()) 
c = 0

for i in range (1, a +1):
    hasil = 0
    for j in range (i, 0, -1):
        print(f"({j} * {b})", end=" ")
        hasil += j*b 
        c += j*b
        if j>1:
            print("+", end="")
        else:
            print("=", hasil)
print(c) 