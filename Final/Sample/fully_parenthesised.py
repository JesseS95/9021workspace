

brackets = {
    ")": "(",
    "]": "[",
    "}": "{"
}

f_brackets = {"{", "[", "("}

operators = {"+", "-", "*", "/"}
def transfer(a):
    try:
        a = int(a)
    except ValueError:
        a = float(a)
    return a

def calculator(a, b, op):
    if op == "+":
        return transfer(a) + transfer(b)
    if op == "-":
        return transfer(a) - transfer(b)
    if op == "*":
        return transfer(a) * transfer(b)
    if op == "/":
        return transfer(a) / transfer(b)



def evaluate(expression):
    brackets_stack = []
    number_stack = []
    Not_Digit = False
    for e in expression:
        print(number_stack)
        print(brackets_stack)
        if e == ' ':
            Not_Digit = False
            continue
        if e in f_brackets:
            Not_Digit = False
            brackets_stack.append(e)
            continue
        if e in operators:
            Not_Digit = False
            number_stack.append(e)
            continue
        if e in brackets:
            Not_Digit = False
            fb = brackets_stack.pop()
            if brackets[e] != fb:
                return
            try:
                last_num = number_stack.pop()
                operator = number_stack.pop()
                first_num = number_stack.pop()
            except:
                return
            number_stack.append(str(calculator(first_num, last_num, operator)))
            continue
        if e.isdigit():
            if not Not_Digit:
                number_stack.append(e)
                Not_Digit = True
                continue
            if Not_Digit:
                number_stack.append(number_stack.pop() + e)
                continue
    if brackets_stack:
        return
    if len(number_stack) != 1:
        return
    return number_stack.pop()

