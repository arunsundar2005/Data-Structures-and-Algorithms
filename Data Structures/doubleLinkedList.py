class Node:
    def __init__(self, data, prev, next):
        self.data = data
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_at_head(self, data):
        node = Node(data,None,self.head)
        if self.head:
            self.head.prev = node
            self.head = node
        else:
            self.head = node
            self.tail = node
        

    def insert_at_end(self, data):
        if self.tail:
            node = Node(data, self.tail, None)
            self.tail.next = node
            self.tail = node
        else:
            node = Node(data, None, None)
            self.head = node
            self.tail = node
        

        # if self.head is None:
        #     self.insert_at_head(data)
        #     return 
        # else:
        #     node = Node(data, None)
        #     current = self.head
        #     while current.next:
        #         current = current.next
        #     current.next = node



    def multiple_insert(self, data_list):
        self.head = None
        self.tail = None
        for data in data_list:
            self.insert_at_end(data)
            print(f"Inserted : {data}")

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
            self.head.prev = None
        else:
            c = 0
            itr = self.head
            val = ''
            while itr.next:
                if c == index-1:
                    val = str(itr.next.data)
                    itr.next.next.prev = itr
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
                    node = Node(data, itr, itr.next)
                    itr.next.prev = node
                    itr.next = node
                    break
                itr = itr.next
                c+=1


    def insert_after(self, after_data, data):
        itr = self.head
        found = False
        while itr.next:
            if itr.data == after_data:
                node = Node(data, itr ,itr.next)
                itr.next.prev = node
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
                itr.next.next.prev = iter
                itr.next = itr.next.next
                remove = True
                break
            itr = itr.next
        if not remove:
            raise Exception("Value not found")

    
    def print_forward(self):
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

    def print_backward(self):
        if self.tail is None:
            print("Linked List is Empty")
            return -1
        else:
            itr = self.tail
            ll = ''
            while itr:
                ll += str(itr.data) + "<-"
                itr = itr.prev
            print(ll)



if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.insert_at_head(8)
    dll.insert_at_end(89)
    dll.multiple_insert(['Apple', 'Orange', 'Bananan', 'Pine Apple', 'Mango'])
    dll.print_forward()
    dll.insert_after("Orange", "Watermelon")
    dll.print_forward()
    dll.print_backward()