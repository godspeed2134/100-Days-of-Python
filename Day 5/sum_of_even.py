target = int(input())
sum = 0
for target in range(0,target + 1):
    if target % 2 == 0:
        sum += target
print("Sum : ",sum)