import math
def cartesian_system(x1,y1,x2,y2):
    length_of_line = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return length_of_line
def main():
    print("Welcome to Line Comparison Computation Program")
    x1, y1 = 2, 6
    x2, y2 = 9, 6
    length = cartesian_system(x1,y1,x2,y2)
    print("Length of the line:", length)

if __name__ == "__main__":
    main()