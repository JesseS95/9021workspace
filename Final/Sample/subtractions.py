


def subtractions(tup, target_sum):
    all_list = _subtractions(tup)
    for exp in all_list:
        if eval(exp) == target_sum:
            print(exp[1:-1])


def _subtractions(tup):
    if len(tup) == 1:
        return [str(tup[0])]
    if len(tup) == 2:
        return [f'({tup[0]} - {tup[1]})']
    output_list = []
    for i in range(1, len(tup)):
        left = _subtractions(tup[: i])
        right = _subtractions(tup[i: ])
        for expl in left:
            for expr in right:
                output_list.append(f'({expl} - {expr})')
    return output_list

        