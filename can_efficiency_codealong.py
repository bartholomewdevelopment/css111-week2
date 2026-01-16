import math

def main():
    can_efficiency("#1 Picnic", 6.83, 10.16)
    can_efficiency("#1 Tall", 7.78, 11.91)
    can_efficiency("#2", 8.73, 11.59)
    can_efficiency("#2.5", 10.32, 11.91)
    can_efficiency("#3 Cylinder", 10.79, 17.78)
    can_efficiency("#5", 13.02, 14.29)
    can_efficiency("#6Z", 5.40, 8.89)
    can_efficiency("#8Z short", 6.83, 7.62)
    can_efficiency("#10", 15.72, 17.78)
    can_efficiency("#211", 6.83, 12.83)
    can_efficiency("#300", 7.62, 11.27)
    can_efficiency("#303", 8.10, 11.11)


def compute_surface_area(radius,height):
    surface_area = 2 * math.pi * radius * (radius + height)
    return surface_area

def compute_volume(radius,height):
    volume = math.pi * radius**2 * height
    return volume

def can_efficiency(name,radius,height):
    volume = compute_volume(radius,height)
    area = compute_surface_area(radius,height)
    efficiency = volume / area
    print(f"{name} volume = {volume:.2f} area= {area:.2f} efficiency= {efficiency:.2f}")

main()
