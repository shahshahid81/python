def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 401 | 403 | 404:
            return "Not allowed"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        # Note the last block: the “variable name” _ acts as a wildcard and never fails to match. If no case matches, none of the branches is executed.
        case _:
            return "Something's wrong with the internet"


point = (0, 0)
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    # Notice that we are storing the second item of tuple in y variable, change value of point to (0,1) and 1 is assigned to y
    case (0, y):
        print(f"Y={y}")
    # Notice that we are storing the first item of tuple in x variable, change value of point to (1,0) and 1 is assigned to x
    case (x, 0):
        print(f"X={x}")
    # Notice that we are storing the first item of tuple in x variable and second item of tuple in y variable, change value of point to (1,1) and 1 is assigned to x and y
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def where_is(point):
    match point:
        # Matching point variable with the constructor
        case Point(x=0, y=0):
            print("Origin")
        # Matching point variable with the constructor and storing the second parameter in y variable
        case Point(x=0, y=y):
            print(f"Y={y}")
        # Matching point variable with the constructor and storing the first parameter in x variable
        case Point(x=x, y=0):
            print(f"X={x}")
        # Matching point variable with any constructor
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")


point = Point(2, 2)
where_is(point)
