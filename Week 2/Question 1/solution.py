
def Push(x, stack1, stack2):
    while stack1:
        stack2.append(stack1.pop())
    stack1.append(x)
    while stack2:
        stack1.append(stack2.pop())


# Function to pop an element from queue by using 2 stacks.
def Pop(stack1, stack2):
    if not stack1:
        return -1
    return stack1.pop()
    
