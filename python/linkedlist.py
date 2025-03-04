class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class link:
    def __init__(self):
        self.head=None
    def beg(self,data):
        newnode=Node(data)
        if self.head is None: 
            self.head=newnode
            return
        else:
            newnode.next=self.head
            self.head=newnode
    def end(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
            return
        else:
            l=self.head
            while l.next is not None:
                l=l.next
            l.next=newnode
    def pos(self,data,index):
        newnode=Node(data)
        temp=self.head
        pos=0
        if pos == index:
            self.beg(data)
            return
        else:
            while (temp != None and pos+1 != index):
                pos=pos+1
                temp=temp.next
            if temp != None:
                newnode.next=temp.next
                temp.next=newnode
            else:
                print("none")
    def print(self):
        temp=self.head
        while temp:
            print(temp.data,end = " ") 
            temp=temp.next
    def reverse_linked_list(head: Node) -> Node:
        prev = None
        curr = head
    
        while curr:
            next_node = curr.next  
            curr.next = prev       
            prev = curr            
            curr = next_node      
    
        return prev  
    
l=link()
l.beg(1)
l.pos(2,1)               
l.end(3)
l.reverse_linked_list()
l.print()
