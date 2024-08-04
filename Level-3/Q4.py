class Shape:
    def __init__(self):
        pass
    
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    
    def area(self):
        return self.length ** 2

# Example usage
shape = Shape()
print(f"Shape area: {shape.area()}")  # Default area: 0

square = Square(4)
print(f"Square area: {square.area()}")  # Area of square with side length 4
