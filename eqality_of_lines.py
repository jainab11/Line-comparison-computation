'''

@Author: sheikh jainab

@Date: 2024-05-14

@Last Modified by: sheikh jainab


@Title : I want to
check equality of two lines based on the end points, So that I know when two lines are the equal. 

'''
class Point:
    def __init__(self, x, y):
        """
        Initializes a Point object with given x and y coordinates.

        Parameters:
        - x (float): The x-coordinate of the point.
        - y (float): The y-coordinate of the point.
        """
        self.x = x
        self.y = y

class Line:
    """
    Represents a line segment connecting two points in 2D space.
    """
    def __init__(self, start_point, end_point):
        """
        Initializes a Line object with given start and end points.

        Parameters:
        - start_point (Point): The starting point of the line segment.
        - end_point (Point): The ending point of the line segment.
        """
        self.start_point = start_point
        self.end_point = end_point

    def __eq__(self, other):
        """
        Checks if two Line objects are equal based on their start and end points.

        Two lines are considered equal if they have the same start and end points, 
        regardless of the order in which the points are specified.

        Parameters:
        - other (Line): The Line object to compare with.

        Returns:
        - bool: True if the lines are equal, False otherwise.
        """
        if isinstance(other, self.__class__):
            # Convert start and end points into tuples for comparison
            self_points = (self.start_point.x, self.start_point.y, self.end_point.x, self.end_point.y)
            other_points = (other.start_point.x, other.start_point.y, other.end_point.x, other.end_point.y)
            # Check if both tuples are equal or reversed tuple is equal
            return self_points == other_points or self_points[::-1] == other_points
        return False

def main():
  
    start_point1 = Point(1, 2)
    end_point1 = Point(4, 6)
    line1 = Line(start_point1, end_point1)

    start_point2 = Point(1, 2)
    end_point2 = Point(4, 6)
    line2 = Line(start_point2, end_point2)

    if line1 == line2:
        print("The lines are equal.")
    else:
        print("The lines are not equal.")

if __name__ == "__main__":
    main()
