"""
Given a stack, remove its middle element using recursion
"""


def helper(stack, index, stack_len):
    if index == stack_len // 2:
        stack.pop()
        return

    num = stack[-1]
    stack.pop()
    helper(stack, index + 1, stack_len)
    stack.append(num)

def delete_middle(stack):
    n = len(stack)
    middle_index = n // 2

    helper(stack, 0, len(stack))
    return stack

st = [1, 2, 3, 4, 5, 6]
print("delete middle", delete_middle(st))