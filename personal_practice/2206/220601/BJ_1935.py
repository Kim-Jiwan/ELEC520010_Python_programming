N = int(input())
equation = input()

operands = []
stack = []
# result = 0

for _ in range(N):
    operands.append(int(input()))

for x in equation:
    if x == "+":
        op1 = stack.pop()
        op2 = stack.pop()
        result = op2 + op1
        stack.append(result)
        print(stack)
    elif x == "-":
        op1 = stack.pop()
        op2 = stack.pop()
        result = op2 - op1
        stack.append(result)
        print(stack)
    elif x == "*":
        op1 = stack.pop()
        op2 = stack.pop()
        result = op2 * op1
        stack.append(result)
        print(stack)
    elif x == "/":
        op1 = stack.pop()
        op2 = stack.pop()
        result = op2 / op1
        stack.append(result)
        print(stack)
    else:
        index = ord(x) - ord("A")
        stack.append(operands[index])
        print(stack)

print(f"{stack[0]:.2f}")