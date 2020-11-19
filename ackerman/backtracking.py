def spring(point, N, reeks):
    if point in reeks:
        print(reeks)

    for i in (point.x, N):
        point.x = + 1
        if point.x <= N and (point.y + 1) <= N:
            spring(Point(point.x + 2, point.y + 1), N, reeks)
        point.x -= 1
    reeks.append(point)


class Point:
    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def __eq__(self, o: object) -> bool:
        return self.x == o.x and self.y == o.y


if __name__ == '__main__':
    spring(0, 0, 8, [])
