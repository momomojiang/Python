class Node:
    def __init__(self,value):
	    self.value=value
	    self.next=None
class Slist:
    def __init__(self,value):
	    node=Node(value)
	    self.head=node
    def addValue(self,value):
	    node=Node(value)    	
	    runner=self.head
	    while(runner.next!=None):
		    runner = runner.next
	    runner.next=node
    def printAllValues(self):
	    runner=self.head
	    while(runner.next!=None):
		    print(runner.value)
		    runner=runner.next
	    print(runner.value)
    def remove_front_Node(self):
    	runner=self.head
    	self.head= self.head.next
    	return runner.value
    def remove_middle_Node(self):
	    runner=self.head
	    while(runner.next!=None):
		    if(runner.next.value==9):
			    runner.next=runner.next.next
		    else:
			    runner=runner.next
	    return runner.value
 #    def remove_last_Node(self):
	# 	runner=self.head
	#     while(runner.next!=None):
	# 	    if(runner.next.next== None):
	# 		    runner.next=None
	# 	    else:
	# 		    runner=runner.next
	#     return runner
    def addFrontNode(self,value):
	    new_node=Node(value)
	    new_node.next=self.head
	    self.head=new_node
	    return self





slist1=Slist(5)
slist1.addValue(7)
slist1.addValue(9)
slist1.addValue(1)
# # slist1.remove_front_Node()
# slist1.remove_last_Node()
# slist1.remove_middle_Node()
slist1.addFrontNode(3)
slist1.addFrontNode(20)
slist1.printAllValues()


