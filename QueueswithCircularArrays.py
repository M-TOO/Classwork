class Circulararrayqueue:
    #1.Queue works in a first in first out principles
#We first decide the maximum size of the queue

    default_capacity=10

    def __init__(self):
        #We create an empty queue by initializing three important things:
        #data-which is a list with none values,array
        #size how many elements are in the list,we start from 0
        #front:The position of the first element.We also initialise to 0

         #Create an empty list,with the default capacity of 10(10 empty spaces in a list-booking)
        self._data=[None]*Circulararrayqueue.default_capacity

        #Then we keep track of the elements in the list
        self._size=0

        #This is to know the first element in the list
        self._front=0



    def __len__(self):
        #inbuilt constructor or dunder method
        #returns the size of the attribute  created in the constructor< i.e ELEMENTS IN THE QUEUES >--How many cars in the circular lot
        return self._size

    def is_Empty(self):

        #it returns a boolean,denoted by (==),comparison
        #It returns True if empy,False if it has elements
        return  self._size==0


    def first(self):
        #It does the same as peek() in the stack method...to look at the top elemnt in the queue
        #It will raise an Empty Exception if the queue is empty


        if self.is_Empty():
            raise Empty('The queue is currently empty')

        return  self._data[self._front]


    def dequeue(self):
        #TThis removes the element at the front of the list
        #It implements ...the mvmt in a circular linked list by pointing the front pointer to the next position
        if self.is_Empty():
            raise Empty('The queue is currently empty')
        #Then after,we get the element at the front of the queue and save it
        item_to_dequeue=self._data[self._front]

        #Clear the old front position to help with garbage collection??


#GARBAGE COLLECTION:It's a technique/process manual or autonomous,that handles memory allocation and dea-location,ensuring efficient use of memory


        self._data[self._front]=None

        #Move the front pointer to the next position
        #The modulo(%) makes it wrap around,if we are at the last position add 1,which will go pstn 0
        self._front=(self._front +1) %len(self._data)

        self._size-=1

        return  item_to_dequeue

    def enqueue(self,element):
        #We check if the list has reached its maximum capacity stated as 10

        if self._size==len(self._data):
            self._resize(2*len(self._data))#Double the capacity

        back_of_the_queue=(self._front+self._size)%len(self._data)

        #Place the element in the back position
        self._data[back_of_the_queue]=element

        #Since we have a new element in the queue we increase the size of the list
        self._size+=1


    #I'M SURE YOU WERE CONFUSED AS ME WITH WHAT IF THE DEFAULT CAPACITY
    # IS ALREADY REACHED BUT WE STILL NEED TO ENQUEUE THE DATA

    def _resize(self,new_capacity):
        #We also need to know that we removed the circular motion of the
        # list in order to increase the size of the list

        #Create a bigger array
        old_data=self._data#it will the data of the list
        self._data=[None] *new_capacity #Resizing has occurred


        #We the copy all the elements in the array and past them in the new array..from the front to the back

        current_index=self._front
        for item in range(self._size):
            #Copy them in order
            self._data[item]=old_data[current_index]
            #Moe to the next element
            current_index=(current_index+1)%len(old_data)

        #Reset the front to 0
        self._front=0


class Empty(Exception):
        def __init__(self,message='The queue is currently empty'):
            self.message=message
            super().__init__(self.message)








if __name__== '__main__':
    queue=Circulararrayqueue()

    print("Queues using circular array")
    print(f"The initial size is :{len(queue)}")
    print(f"Is the queue empty? {queue.is_Empty()} ")

    print("\nEnqueueing the queue")
    elements_to_queue=['Alice','Bob','William','Dorothy','Jessica']

    for person in elements_to_queue:
        queue.enqueue(person)
        print(f"Added {person}. Queue size now: {len(queue)}" )


    print(f"\n Person at the front of the queue: {queue.first()}")


    print("\n Serving people from the front of the queue:")
    for i in range(3):
        served_person=queue.dequeue()
        print(f"Served: {served_person}. Queue size now is : {len(queue)}")


    print("\n Adding more people to induce the wrap around in the array")
    more_people=['Frank','Linda','Ford']

    for person in more_people:
        queue.enqueue(person)
        print(f"Added {person}.Queue size now: {len(queue)}")


    print(f"\n Person currently at the front: {queue.first()}")
    print(f"Total people still in the queue: {len(queue)}")


    print(f"\n Internal details:")
    print(f"Front index: {queue._front}")
    print(f"Array  contents: {queue._data}")













