def calculate_circumference(radius):

    """
    Calculate the circumference of a circle given its radius.
    Formula: Circumference = 2 * π * radius
    """

    pi = 3.14159 # Approximation of π

    circumference = 2 * pi * radius

    return circumference

# Example usage:

radius = float(input("Enter the radius of the circle: "))

circumference = calculate_circumference(radius)

print(f"The circumference of the circle with radius {radius} is {circumference:.2f}")