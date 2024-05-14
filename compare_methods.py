class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False

    def __lt__(self, other):
        if isinstance(other, Point):
            return (self.x, self.y) < (other.x, other.y)
        raise TypeError("Cannot compare Point with non-Point object.")

class Line:
    def __init__(self, start_point, end_point):
        self.start_point = start_point
        self.end_point = end_point

    def length(self):
        return ((self.end_point.x - self.start_point.x) ** 2 + (self.end_point.y - self.start_point.y) ** 2) ** 0.5

    def __eq__(self, other):
        if isinstance(other, Line):
            return self.length() == other.length()
        return False

    def __lt__(self, other):
        if isinstance(other, Line):
            return self.length() < other.length()
        raise TypeError("Cannot compare Line with non-Line object.")

# Example usage:
start_point1 = Point(1, 2)
end_point1 = Point(4, 6)
line1 = Line(start_point1, end_point1)

start_point2 = Point(1, 2)
end_point2 = Point(4, 6)
line2 = Line(start_point2, end_point2)

if line1 == line2:
    print("The lines are equal.")
elif line1 < line2:
    print("Line 1 is shorter than Line 2.")
else:
    print("Line 1 is longer than Line 2.")
