from binary_tree_adt import *

def parse_tree(expression):
    if expression.isdigit():
        return BinaryTree(int(expression))
    Not_Digit = False
    Bracket_Stack = []
    Stack = []
    bracket_map = {']': '[', ')': '(', '}': '{'}
    f_brackets = {"{", "[", "("}
    operators = {"+", "-", "*", "/"}
    for i in range(len(expression)):
        if expression[i] in f_brackets:
            Bracket_Stack.append(expression[i])
            Not_Digit = False
            continue
        if expression[i] in operators:
            Stack.append(expression[i])
            Not_Digit = False
            continue
        if expression[i].isdigit():
            if not Not_Digit:
                Not_Digit = True
                Stack.append(expression[i])
            else:
                added_digit = Stack.pop() + expression[i]
                Stack.append(added_digit)
            continue
        if expression[i] in bracket_map:
            formal_bracket = Bracket_Stack.pop()
            if formal_bracket != bracket_map[expression[i]]:
                return
            _right = Stack.pop()
            operater = Stack.pop()
            _left = Stack.pop()
            sub_Tree = BinaryTree(operater)
            if str(_left).isdigit():
                sub_Tree.left_node = BinaryTree(int(_left))
            else:
                sub_Tree.left_node = _left
            if str(_right).isdigit():
                sub_Tree.right_node = BinaryTree(int(_right))
            else:
                sub_Tree.right_node = _right
            Stack.append(sub_Tree)
    return Stack.pop()

