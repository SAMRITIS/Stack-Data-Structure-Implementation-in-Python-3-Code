class stack:
    def __init__(self):
        self.stck = []
    def push(self, x):
        self.stck.append(x)
    def pop(self):
        if len(self.stck) == 0:
            print("No Element to Pop")
        else:
            self.stck.pop()
    def show(self):
        print(self.stck)
print("Stack Created")
s = stack()
print("Element 10 Pushed into Stack")
s.push(10)
s.show()
print("Element 20 Pushed into Stack")
s.push(20)
s.show()
print("Element 30 Pushed into Stack")
s.push(30)
s.show()
print("Element 40 Pushed into Stack")
s.push(40)
s.show()
print("Element Poped from Stack")
s.pop()
s.show()
print("Element Poped from Stack")
s.pop()
s.show()
print("Element Poped from Stack")
s.pop()
s.show()
print("Element Poped from Stack")
s.pop()
s.show()
print("Again performing pop from Stack")
s.pop()
