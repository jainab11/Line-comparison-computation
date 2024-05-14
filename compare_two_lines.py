import math

def calculate_length(start_point, end_point):
    """
    Calculate the length of a line segment given its start and end points.
    """
    return math.sqrt((end_point[0] - start_point[0]) ** 2 + (end_point[1] - start_point[1]) ** 2)

def compare_lines(line1, line2):
    """
    Compare two line segments based on their lengths.
    """
    length1 = calculate_length(line1[0], line1[1])
    length2 = calculate_length(line2[0], line2[1])

    if length1 == length2:
        return "The lines are equal."
    elif length1 < length2:
        return "Line 1 is shorter than Line 2."
    else:
        return "Line 1 is longer than Line 2."

# Example usage:
start_point1 = (1, 2)
end_point1 = (5, 6)
line1 = (start_point1, end_point1)

start_point2 = (1, 2)
end_point2 = (4, 6)
line2 = (start_point2, end_point2)

print(compare_lines(line1, line2))
