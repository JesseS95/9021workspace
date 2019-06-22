

string = input("Please input a string of lowercase letters: ")

all_seq = []


visited = set()


for i in range(len(string)):
    if i in visited:
        continue
    else:
        one_string = string[i]
        visited.add(i)
        for j in range(i + 1, len(string)):
            if ord(string[j]) == ord(one_string[-1]) + 1:
                one_string += string[j]
                visited.add(j)
        all_seq.append(one_string)

print(max(all_seq, key = lambda x: len(x)))