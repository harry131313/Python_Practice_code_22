
n = 4
for i in range(n):
    for j in range(0, 4-i+1):
        print(" ", end="")
        
    for j in range(0, i+1):
        print("*", end=" ")
    print()
print("-----------------------------------------")
# Daimond Pattern 

c = 4
for i in range(4):
    for j in range(c, 0, -1):
        print(" ", end="")
    for j in range(i+1):
        print("*", end="")
    for j in range(i):
        print("*", end="")
    c -=1
    print()

k = 4
for i in range(4):
    for j in range(i+1):
        print(" ", end="")
    for j in range(k,0, -1):
        print("*", end="")
    for j in range(k, 1, -1):
        print("*", end="")
    k -=1
    print()

#Daimond Patterns

print()
print("-----------------------------------------")
for i in range(4):
    print(" "*(4-i-1) + "* "*(i+1))
for j in range(4, 0, -1):
    print(" "*(4-j)+ "* "*(j))

print()
print("-----------------------------------------")
for i in range(7):
    for j in range(4):
        if (j== 0 and (i!=0 and i!=6)) or ((i==0 or i==6) and (j>0)):
            print("*", end=" ")
        else:
            print(end=" ")
 

    print()