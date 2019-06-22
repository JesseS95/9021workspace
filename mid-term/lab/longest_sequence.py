_str = 'abcefg'

_set = set()
target_list = []

for i in range(len(_str)):
    if i in _set:
        continue
    _set.add(i)
    one_str = _str[i]
    for j in range(i+1, len(_str)):
        if ord(_str[j]) == ord(one_str[-1]) + 1:
            one_str += _str[j]
            _set.add(j)
    target_list.append(one_str)
max_item = max(target_list, key = lambda x: len(x))
print(max_item)
    