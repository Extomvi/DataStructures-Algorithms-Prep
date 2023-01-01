"""
Implementing a queue (FIFO) with linked list
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class Queue:
    def __init__(self):
        self.first = Node("first")
        self.last = Node("last")
        self.size = 0

    def __str__(self):
        cur = self.first.next
        out = ""
        while cur:
            out += str(cur.value) + " -> "
            cur = cur.next
        return out[:-3]

    def add(self, value):
        node = Node(value)
        if self.last.next != None:
            self.last.next.next = node
        self.last.next = node
        if self.first.next == None:
            self.first.next = self.last.next
        self.size += 1

    def remove(self):
        if self.first == None:
            raise Exception("No such element")
        remove = self.first.next.value
        self.first.next = self.first.next.next
        if self.first.next == None:
            self.last.next == None
        self.size -= 1
        return remove

if __name__ == "__main__":
    stack = Queue()
    for i in range(1,11):
        print(i)
        stack.add(i)
    print(f"After adding to the queue: {stack}")
    if stack.size != 0:
        stack.remove()
    print(f"After popping: {stack}") 
        