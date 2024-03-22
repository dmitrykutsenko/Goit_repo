'''
In Python, create a Point class that will be responsible for displaying a geometric point on a plane.

Use the __init__ constructor to initialize two attributes: x-coordinates and y-coordinates.

Example:

point = Point(5, 10)

print(point.x) # 5
print(point.y) # 10
'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

# Example usage:

# Create an instance of the Point class
point = Point(5, 10)

# Access the x and y attributes
print(point.x)  # Output: 5
print(point.y)  # Output: 10
