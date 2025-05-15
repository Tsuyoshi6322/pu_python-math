'''''''''''''''''''''''''''''''''''''''''''''''''''''''''
    Pythagorean triple and right triangle check
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''

### HELPING FUNCTIONS ###
def is_valid_triangle(a: int, b: int, c: int) -> bool:
    # Check if all input numbers are positive integers
    if not all(isinstance(x, int) and x > 0 for x in [a, b, c]):
        return False
    
    # Sort the values in ascending order
    sides = sorted([a, b, c])

    # Return sides inequality
    return sides[0] + sides[1] > sides[2]


def is_pythagorean_triple(a: int, b: int, c: int) -> bool:
    # Sort the values in ascending order
    sides = sorted([a, b, c])

    # Return a Pythagorean triple
    return sides[0]**2 + sides[1]**2 == sides[2]**2


### MAIN FUNCTIONALITY ###
def right_triangle_checker(a: int, b: int, c: int) -> str:
    # Should the sides be of negative length or c > a+b
    if not is_valid_triangle(a, b, c):
        return "Not a triangle at all."
    
    if is_pythagorean_triple(a, b, c):
        return "Yes, it's a right triangle (Pythagorean Triple)."
    else:
        return "It forms a triangle, but not a right one."
