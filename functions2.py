import math

def main():
    print("This program computes the volume of a right circular cone.")
    print("For example, if the radius of a cone is 2.8 and")
    print("the height is 3.2, then the volume is 26.3")

    radius = float(input("Please enter the radius of the cone: "))
    height = float(input("Please enter the height of the cone: "))

    volume = cone_volume(radius, height)
    print(f"Radius: {radius}")
    print(f"Height: {height}")
    print(f"Volume: {volume:.1f}")

def cone_volume(radius, height):
    volume = math.pi * radius**2 * height / 3
    return volume

main()
