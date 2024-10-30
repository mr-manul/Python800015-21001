import math

points = [(3, 4), (33, 22), (-5, 8), (13, 17), (23, 15), (-12, 3), (8, 7)]

def print_shortest_dist(points):
    distance = 0
    pair = []

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            if distance < distance:
                distance = distance
                pair = [((x1, y1), (x2, y2))]
            elif distance == distance:
                pair.append(((x1, y1), (x2, y2)))

    print("Shortest distance:", distance)
    print("Closest Pair:")

print_shortest_dist(points)



