from collections import defaultdict

1, 2, 5, 10, 20, 50, 100.

amount = int(input("Input the desired amount: "))

dic = defaultdict(int)


while amount:
    if amount >= 100:
        dic[100] += 1
        amount -= 100
        continue
    if amount >= 50:
        dic[50] += 1
        amount -= 50
        continue
    if amount >= 20:
        dic[20] += 1
        amount -= 20
        continue
    if amount >= 10:
        dic[10] += 1
        amount -= 10
        continue
    if amount >= 5:
        dic[5] += 1
        amount -= 5
        continue
    if amount >= 2:
        dic[2] += 1
        amount -= 2
        continue
    if amount >= 1:
        dic[1] += 1
        amount -= 1
        continue
    
print(dic)
for key in reversed(sorted(dic)):
    _key = '$' + str(key)
    print(f"{' ' * (4 - len(_key)) + _key}: {dic[key]}")
    
    
