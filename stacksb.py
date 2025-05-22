from inspect import stack

stack=[]
stack.append(10)
stack.append(20)
stack.append(30)

print("Stack after the pushes or appending",stack)

top_element=stack[-1]
print("\nThe top elememt is: ",top_element)

#Checks if the stack is empty
if len(stack)==0:
    print("\nStack is empty")
else:
    print("\nStack has values")


class SimpleStack:
    def __init__(self):
#initializes an empty list without elements
       self.items=[]

    def is_empty(self):
        return len(self.items)==0


    def push(self,item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise Exception("Cannot pop an empty stack")
        return  self.items.pop()

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is empty")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def print_stack(self):

        print("Stack from bottom to top is :",self.items)
        return

if __name__ == "__main__":

    stack1=SimpleStack()

    stack1.push(20000)
    stack1.push(10000)
    stack1.push(30000)
    stack1.push(56000)


    stack1.print_stack()

    print("Top Elements: ",stack1.peek())

    print("Popped: ",stack1.pop())
    stack1.print_stack()

    print("Is the stack emptyy?", stack1.is_empty())


    stack1.pop()
    stack1.pop()
    stack1.pop()
    print("Is the stack emptyyy",stack1.is_empty())


