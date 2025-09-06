class linkedlistNode:

    def __init__(self,value,nextNode = None):
        self.value=value
        self.nextNode=nextNode

#Create objects of the class linkedlist
node1= linkedlistNode("5")
node2= linkedlistNode("6")
node3= linkedlistNode("7")
node4=linkedlistNode("8")
node5= linkedlistNode("9")
node6= linkedlistNode("10")
node7= linkedlistNode("11")
node8= linkedlistNode("12")
node9= linkedlistNode("13")
node10= linkedlistNode("14")

node1.nextNode=node2
node2.nextNode=node3
node3.nextNode=node4
node4.nextNode=node5
node5.nextNode=node6
node6.nextNode=node7
node7.nextNode=node8
node8.nextNode=node9
node10.nextNode=None


currentNode=node1 #Sets node1 as the head node of our link list
while True:
    print(currentNode.value,">>> ",end='')

#.The condition only holds if: we have reached the end of the list or the link list only has one element
    if(currentNode.nextNode is None):
        print("None")
        break
    # Increments the currentNode to obtain the next node value
    currentNode =currentNode.nextNode