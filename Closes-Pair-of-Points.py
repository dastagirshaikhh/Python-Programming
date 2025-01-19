from math import sqrt


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p, q):
    return sqrt((p.x - q.x) * (p.x - q.x) + (p.y - q.y) * (p.y - q.y))


def bruteforce(subarray):
    min_distance = float("inf")
    for i in range(len(subarray) - 1):
        for j in range(i + 1, len(subarray)):
            actual_distance = distance(subarray[i], subarray[j])
            if actual_distance < min_distance:
                min_distance = actual_distance
    return min_distance


def getstripdelta(strippoints, delta):
    min_distance = delta
    n = len(strippoints)
    for i in range(n):
        j = i + 1
        while j < n and (strippoints[j].y - strippoints[i].y) < min_distance:
            min_distance = distance(strippoints[i], strippoints[j])
            j += 1
    return min_distance


def ClosestPairs(listx, listy, items):
    if items <= 3:
        return bruteforce(listx)

    middleindex = items // 2
    middleitem = listx[middleindex]
    deltaleft = ClosestPairs(listx[:middleindex], listy, middleindex)
    deltaright = ClosestPairs(listx[middleindex:], listy, items - middleindex)

    delta = min(deltaleft, deltaright)

    strip_points = []

    for i in range(items):
        if abs(listy[i].x - middleitem.x) < delta:
            strip_points.append(listy[i])
    stripdelta = getstripdelta(strip_points, delta)

    return min(stripdelta, delta)


def run(list1, list2):
    list1.sort(key=lambda point: point.x)
    list2.sort(key=lambda point: point.y)
    return ClosestPairs(list1, list2, len(list1))


if __name__ == "__main__":
    points = [Point(1, 1), Point(4, 2), Point(10, 10), Point(0, 0), Point(3, 5)]
    l1 = list(points)
    l2 = list(points)
    print(run(l1, l2))
