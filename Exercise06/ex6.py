import math


def cal_shortest_dist(points):
    # Initialize the minimum distance to a large number
    min_distance = float('inf')

    # Loop through each pair of points
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            # Get the coordinates of the two points
            x1, y1 = points[i]
            x2, y2 = points[j]

            # Calculate the Euclidean distance
            distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

            # Update the minimum distance if the current distance is shorter
            if distance < min_distance:
                min_distance = distance

    return min_distance


# Example usage
points = [(0, 3), (0, 1), (5, 7)]
shortest_distance = cal_shortest_dist(points)
print("The shortest distance is:", shortest_distance)
