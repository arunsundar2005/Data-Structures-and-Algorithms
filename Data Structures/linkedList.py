
class Node:
    def __init__(self, data=None, head=None):
        self.data = data
        self.next = head

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, data):
        node = Node(data, self.head)
        self.head = node

    def insert_at_end(self, data):
        if self.head is None:
            self.insert_at_head(data)
            return 
        else:
            node = Node(data, None)
            current = self.head
            while current.next:
                current = current.next
            current.next = node

    def multiple_insert(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def length(self):
        c = 0
        itr = self.head
        while itr.next:
            c +=1
            itr = itr.next
        return c
    

    def remove(self, index):
        if index < 0 or index>=self.length():
            raise Exception("Linekd List out of bound")
        elif index == 0:
            self.head = self.head.next.next
        else:
            c = 0
            itr = self.head
            val = ''
            while itr.next:
                if c == index-1:
                    val = str(itr.next.data)
                    itr.next = itr.next.next
                    break
                itr = itr.next
                c+=1
            print(f"Removed '{val}'")

    def insert(self, index, data):
        if index < 0 or index>=self.length():
            raise Exception("Linekd List out of bound")
        elif index == 0:
            self.insert_at_head(data)
        else:
            c = 0
            itr = self.head
            while itr.next:
                if c == index-1:
                    node = Node(data, itr.next)
                    itr.next = node
                    break
                itr = itr.next
                c+=1


    def insert_after(self, after_data, data):
        itr = self.head
        found = False
        while itr.next:
            if itr.data == after_data:
                node = Node(data, itr.next)
                itr.next = node
                found = True
                break
            itr = itr.next
        if not found:
            raise Exception("Value not found")

    def remove_by_value(self, byvalue):
        itr = self.head
        remove = False
        while itr.next:
            if itr.data == byvalue:
                itr.next = itr.next.next
                remove = True
                break
            itr = itr.next
        if not remove:
            raise Exception("Value not found")

    
    def print(self):
        if self.head is None:
            print("The Linekd List is empty")
            return -1
        else:
            itr = self.head
            ll = ''
            while itr:
                ll += str(itr.data) + '->'
                itr = itr.next
            print(ll)
        

if __name__ == '__main__':
    ll = LinkedList()
    ll.insert_at_end(85)
    ll.insert_at_head(10)
    ll.insert_at_head(20)
    ll.insert(1, 6584)
    ll.print()
    ll.insert_after(6584, 666);ll.print(); ll.remove_by_value(6584)
    ll.print()