class Node:

    def __init__(self,data):
        self.data=data #Assigns the given data to the node
        self.next=None #sets the attribute pointer to none, however, it will be updated to point to the subsequent node

class linkedlist: #This class holds the linked list that will contain all values
    def __init__(self):
        self.head=None


    def insertatthebeginning(self,new_data):
        #Inheritance
        #Create a parameter called new_node then call the class and pass the  parameter new_data
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    # Every time you call this method , a new node is created with the new data
    # The pointer of the new_node is set to be the head
    # This places it at the front of the list,making it the head


    def printlinkedlist(self):
        temporary= self.head #Start from the head of the list
        while temporary:
            print( temporary.data, end=' ')#Prints the data in the current node
            temporary = temporary.next #This moves to the next node
        print()

    def insertattheend(self, new_data):
        new_node = Node(new_data)  # Create a new node
      #If you have nothing at the link list i'm creating a new node
        if self.head is None:
            self.head=new_node  # If the list is empty, make the new node the head
            return None

        tail=self.head
        while tail.next:  # Otherwise, traverse the list to find the last node
            tail=tail.next
        tail.next=new_node # Make the new node the next node of the last node

    def deletefromthebeginning(self):
         if self.head is None:
           return "The list is empty" #if the list is empy that is
         self.head = self.head.next   #If not empty ,remove the head by making the next node the new  head

    def deletefromtheEnd(self):
         if self.head is None:
             return "List is empty"
         if self.head.next is None:
            self.head=None   #if there's only one node, remove the head by making it none
            return

         temp =self.head
         while temp.next.next: # Otherwise, go to the second-last node
          temp=temp.next

         temp.next=None #Removes the last node by setting the next pointer of the second last node to none

    #Searching the linked list for a specific value
    def search(self,value):

        current= self.head#Starts with the head of the list
        position =0 #Keeps the track of the list
        while current:
            if current.data == value:
                return f"Value '{value}' found at the position {position}"
            current=current.next
            position += 1
        return f"Value '{value}' not found in the list "



if __name__== '__main__':
    linkedlist=linkedlist()
    linkedlist.insertatthebeginning("fox")
    linkedlist.insertatthebeginning("brown")
    linkedlist.insertatthebeginning("quick")
    linkedlist.insertatthebeginning("The")

    linkedlist.printlinkedlist()

    linkedlist.insertattheend("jumps")
    linkedlist.printlinkedlist()

    linkedlist.deletefromthebeginning()
    print("List after deletion:")
    linkedlist.printlinkedlist()
    print("")

    print(linkedlist.search('quick'))
    print(linkedlist.search('lazy'))