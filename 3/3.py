def get_horizontal_extent(path):
    left = 0
    right = 0
    counter = 0
    for step in path:
        direction = step[:1]
        step_length = int(step[1:])
        if direction == 'L':
            counter -= step_length
            if left < -counter:
                left = -counter
        if direction == 'R':
            counter += step_length
            if counter > right:
                right = counter
    return (left, right)


def get_vertical_extent(path):
    down = 0
    up = 0
    counter = 0
    for step in path:
        direction = step[:1]
        step_length = int(step[1:])
        if direction == 'D':
            counter -= step_length
            if down < -counter:
                down = -counter
        if direction == 'U':
            counter += step_length
            if counter > up:
                up = counter
    return (down, up)


def put_wire_on_board(board, path, start):
    if len(path) == 0:
        return board

    step = path[0]
    direction = step[:1]
    step_length = int(step[1:])
    # print(step)
    coordinate = start[:]
    for i in range(0, step_length):
        if direction == 'R':
            coordinate[0] += 1
        elif direction == 'L':
            coordinate[0] -= 1
        elif direction == 'U':
            coordinate[1] += 1
        elif direction == 'D':
            coordinate[1] -= 1
        else:
            import pdb;pdb.set_trace()
        board = wire(board, coordinate)

    return put_wire_on_board(board, path[1:], coordinate)


def wire(board, point):
    # print(point)
    board[point[0]][point[1]] += 1
    return board

def get_intersection(board):
    intersections = []
    for x in range(len(board)):
        for y in range(len(board[0])):
            if board[x][y] == 2:
                intersections.append([x,y])
    return intersections

def get_distance(point, start):
    return abs(point[0] - start[0]) + abs(point[1] - start[1])


def main():
    with open('./input.txt') as f:
        (path1, path2) = [l.rstrip('\n').split(',') for l in f.readlines()[:2]]

        # find out extents of the board
        he1 = get_horizontal_extent(path1)
        he2 = get_horizontal_extent(path2)
        max_left = max(he1[0], he2[0])
        max_right = max(he1[1], he2[1])
        ve1 = get_vertical_extent(path1)
        ve2 = get_vertical_extent(path2)
        max_down = max(ve1[0], ve2[0])
        max_up = max(ve1[1], ve2[1])

        board = []
        for _ in range(max_left + max_right + 1):
            board.append([])

        for i in range(len(board)):
            for _ in range(max_down + max_up + 1):
                board[i].append(0)

        start = [max_left, max_down]

        board = wire(board, start)
        board = put_wire_on_board(board, path1, start)

        board = put_wire_on_board(board, path2, start)

        intersections = get_intersection(board)

        closest_point = []
        min_distance = max_down + max_up + max_left + max_right + 2

        for i in intersections:
            distance = get_distance(start, i)
            if distance < min_distance:
                min_distance = distance
                closest_point = i

        print(min_distance)
        print(closest_point)
        # import pdb;pdb.set_trace()





if __name__ == '__main__':
    main()