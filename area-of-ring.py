def areaOfDisk(r):
    return 3.14 * r * r

def areaOfRing(outer, inner):
    return areaOfDisk(outer) - areaOfDisk(inner)

print(areaOfRing(5, 4))
