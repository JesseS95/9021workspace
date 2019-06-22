str1 = input("Please input the first string: ")
str2 = input("Please input the second string: ")
str3 = input("Please input the third string: ")

def merge_string(s1, s2, s3):
    if not s1:
        if not s2 and not s3:
            return True
        print("hhh")

        print("No solution")
    elif not s2:
        if s1 == s3:
            return True
        print("No solution")
    elif not s3:
        if s1 == s2:
            return True
        print("No solution")
    else:
        if s2[0] == s3[0] and s2[0] + s3[0] == s1[: 2]:
            return merge_string(s1[2: ], s2[1: ], s3[1: ])
        elif s2[0] == s1[0] and s3[0] != s1[0]:
            return merge_string(s1[1: ], s2[1: ], s3)
        elif s3[0] == s1[0] and s2[0] != s1[0]:
            return merge_string(s1[1: ], s2, s3[1: ])
        

if len(str1) == len(str2) + len(str3):
    if merge_string(str1, str2, str3):
        print("first")
    else:
        print("No solution")
elif len(str2) == len(str1) + len(str3):
    if merge_string(str2, str1, str3):
        print("second")
    else:
        print("No solution")
elif len(str3) == len(str1) + len(str2):
    if merge_string(str3, str1, str2):
        print("third")
    else:
        print("No solution")
else:
    print("No")