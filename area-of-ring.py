PI = 3.14

def areaOfDisk(r):
    return PI * r * r

def areaOfRing(outer, inner):
    return areaOfDisk(outer) - areaOfDisk(inner)

print(areaOfRing(5, 4))
