# Stack implementation in python 

# creating stack 
def create_stack():
    stack = []
    return stack 

#creating an empty stack check
def empty_stack(stack):
    return len(stack) == 0

#adding an item into a stack
def push(stack, item):
    stack.append(item)
    print("itme", item)

#remove an emlement 
def pop_(stack):
    if empty_stack(stack):
        return "empty"
    return stack.pop()

stack = create_stack()
push(stack, str(1))
push(stack, str(3))
push(stack, str(7))
pop_(stack)
push(stack, str(13))
print(stack)

    



