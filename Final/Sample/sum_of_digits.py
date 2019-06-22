

n = input("Input a number that we will use as available digits: ")
desire_sum = int(input("Input a number that represents the desired sum: "))

l = [int(n[0]), 0]


for i in range(1, len(n)):
    for s in range(len(l)):
        l.append(l[s] + int(n[i]))

print(l.count(desire_sum))




