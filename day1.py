#Store apple's stock price for 5 days and answer,
#What is is the prince on day one?
#What is the price on day 3?
#stock_prices = [298, 305, 320,301, 292]
#stock_prices[0]
#stock_prices[2] #address + 2 +sizeof(integer)

class Array:
    def __init__(self):
        self.array = []
        #initializes the array class

    def insert(self, element):
        self.array.append(element)
        #adds an elements

    def remove(self,element):
        self.array.remove(element)
        #removes an element

    def get(self, index):
        if index < len (self.array):
            return self.array[index]
        else:
            return None
        
    def size(self):
        return len(self.array)
    #returns number of element

    def display(self):
        print(self.array)
        #print current elements present in array

  
    

#example usage
stock_prices = Array()
stock_prices.insert(298)
stock_prices.insert(305)
stock_prices.insert(320)
stock_prices.insert(301)
stock_prices.insert(292)

stock_prices.display()#displays full array
print(stock_prices.get(0)) #price on day one
print(stock_prices.get(2))#price on day 3
print(stock_prices.get(6))#returns None since it doeesnt have a sixth index

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0
    
    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("peek at empty stack")
        
    def size(self):
        return len(self.items)

#example usage
stack = Stack()
stack.push(1)
stack.push(4)
stack.push(9)
stack.push(3)
stack.push(8)

print("Stack size:", stack.size())
print("Top element:", stack.peek())

popped_element = stack.pop()
print("Popped element:", popped_element)
print("Stack size after popping:", stack.size())


class Queue:
    def __init__(self):
        self.items = []  # Correct initialization

    def enqueue(self, item):
        self.items.append(item)

    def is_empty(self):
        return len(self.items) == 0

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("dequeue from empty queue")
        
    def peek(self):
        if not self.is_empty():
            return self.items[0]
        else:
            raise IndexError("peek at empty queue")
        
    def size(self):
        return len(self.items)

#Example usage
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Queue size:", queue.size())
print("Front element:", queue.peek())