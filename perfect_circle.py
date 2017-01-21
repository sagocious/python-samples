import math
import itertools


def get_center_and_radius(x1, y1, x2, y2, x3, y3):
    div_a = (x2 - x1) * y3 + (x1 - x3) * y2 + (x3 - x2) * y1
    if div_a == 0:
        return None
    A = ((y2 - y1) * y3 ** 2 + (-y2 ** 2 + y1 ** 2 - x2 ** 2 + x1 ** 2) * y3 + y1 * y2 ** 2 + (
    -y1 ** 2 + x3 ** 2 - x1 ** 2) * y2 + (x2 ** 2 - x3 ** 2) * y1) / div_a
    A *= -1

    div_b = (x2 - x1) * y3 + (x1 - x3) * y2 + (x3 - x2) * y1
    if div_b == 0:
        return None
    B = -((x2 - x1) * y3 ** 2 + (x1 - x3) * y2 ** 2 + (x3 - x2) * y1 ** 2 + (x2 - x1) * x3 ** 2 + (
    x1 ** 2 - x2 ** 2) * x3 + x1 * x2 ** 2 - x1 ** 2 * x2) / div_b
    B *= -1

    div_c = (x2 - x1) * y3 + (x1 - x3) * y2 + (x3 - x2) * y1
    if div_c == 0:
        return None
    C = -((x1 * y2 - x2 * y1) * y3 ** 2 + (
    -x1 * y2 ** 2 + x2 * y1 ** 2 - x1 * x2 ** 2 + x1 ** 2 * x2) * y3 + x3 * y1 * y2 ** 2 + (
          -x3 * y1 ** 2 + x1 * x3 ** 2 - x1 ** 2 * x3) * y2 + (x2 ** 2 * x3 - x2 * x3 ** 2) * y1) / div_c

    cent_x = A / 2.0
    cent_x = float("{0:.2f}".format(cent_x))
    cent_y = B / 2.0
    cent_y = float("{0:.2f}".format(cent_y))

    radius = math.sqrt((A ** 2) + (B ** 2) - (4 * C)) / 2.0
    radius = float("{0:.2f}".format(radius))

    return [[cent_x, cent_y], radius]


test_cases = input()

for i in range(test_cases):
    n = input()
    coordinates = []
    for j in range(n):
        coordinates.append(map(float, raw_input().split()))

    perfect_count = 0

    circles = []
    for point_set in itertools.combinations(coordinates, 3):
        # x^2 + y^2 + Ax + By + C = 0
        p1 = point_set[0]
        p2 = point_set[1]
        p3 = point_set[2]

        circle = get_center_and_radius(p1[0], p1[1], p2[0], p2[1], p3[0], p3[1])
        if circle is not None:
            circles.append(circle)

    for circle_pair in itertools.combinations(circles, 2):
        c1 = circle_pair[0]
        c2 = circle_pair[1]

        if c1[1] == c2[1]:
            dist = math.sqrt((c1[0][0] - c2[0][0]) ** 2 + (c1[0][1] - c2[0][1]) ** 2)
            dist = float("{0:.2f}".format(dist))

            perfect_dist = float("{0:.2f}".format(c1[1] * math.sqrt(2)))
            if dist == perfect_dist:
                perfect_count += 1

    print perfect_count

