
def fibo(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    ff = 0
    f = 1
    result = ff + f
    while n - 2:
        ff = f
        f = result
        result = ff + f
        n -= 1
    return result


# for i in range(100):
#     print(fibo(i))

def encode(n):
    # establish dic
    dic_of_fibo = {}
    for i in range(2, n + 3):
        if fibo(i) > n:
            break
        else:
            dic_of_fibo[fibo(i)] = i
    # encode
    list_ = []
    output = ''
    print(dic_of_fibo)
    for key in reversed(sorted(dic_of_fibo)):
        if key <= n:
            list_.append(dic_of_fibo[key])
            n -= key
    for i in range(2, max(list_) + 1):
        if i in list_:
            output += '1'
        else:
            output += '0'
    print(list_)
    output += '1'
    return output


print(encode(8))

def decode(n):
    if len(n) < 2:
        return 0
    if n[-2: ] != '11':
        return 0
    code = n[: -1]
    result = 0
    # check if has two consecutive '1'
    for i in range(len(code) - 1):
        if code[i] == code[i+1] == '1':
            return 0
        else:
            if code[i] == '1':
                result += fibo(int(i) + 2)
    if code[i+1] == '1':
        result += fibo(int(i+1) + 2)
    return result

print(decode('001011'))