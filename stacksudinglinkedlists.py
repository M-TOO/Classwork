#This creates a class for the list
class StackNode:
    def __init__(self,value):
        self.value=value
        self.next=None #Pointing towards the next node(Downwards)

#The stack implements the link list in this class
class LinkedListStack:
    def __init__(self):
      #Points to the top element in the stack
        self.top=None

    def is_empty(self):
        return self.top is None


    def push(self,value):
        #Adds values to the stack
        new_node=StackNode(value)
        #The new nodes pointer should be the current top node

        new_node.next=self.top
        #Updates the top node header every time we add a new element to the top of the stack
        self.top=new_node

    def pop(self):
        #If the stack is empty we raise an error to show an Underflow error
        if self.is_empty():
         raise Exception("Cannot pop an empty stack!")

        #Gets the value in the top node
        popped_value=self.top.value

        #The pointer is then directed to the nes=xt value in the stack
        self.top= self.top.next

        return popped_value

    def peek(self):
        #Checks the top value alone doesn't affect it
        if self.is_empty():
            raise Exception("Unable to peek an empty stack")
        return self.top.value

    def display(self):
        current=self.top
        values=[]
        while current:
            values.append(str(current.value))
            current=current.next

        print("Stack from the to the bottom: ","->" .join(values))


    #Make instances of the class stackusinglinkedlist

if __name__=="__main__":
        stackll=LinkedListStack()
        stackll.push(5)
        stackll.push(10)
        stackll.push(15)

        stackll.display()

        print("Peeking from the top: ", stackll.peek())

        print("Pop:", stackll.pop())
        stackll.display()










