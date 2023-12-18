def prints(stack):
    for i in stack[::-1]:
        
        print(i, end="\n")
    
def peek(stack):
    return stack[-1]


stack = []

# small demonstration

# this also works with multi dimenstional arrays
stack.append(4)
stack.append(2)
stack.append(3)

prints(stack)


print(stack.pop())
print("------")
prints(stack)

print(peek(stack))