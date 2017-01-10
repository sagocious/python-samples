def areaOfDisk(radius):
    return 3.14 * radius**2

def areaOfRect(width, height):
    return width * height

def areaOfCylinder(radius, height):
    return areaOfDisk(radius) + areaOfRect(2*3.14*radius, height)

print(areaOfCylinder(3, 5))
