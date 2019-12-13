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
    # no selb intersections
    board[point[0]][point[1]] = 1
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

def steps_to_point(intersection, path, start):
    distance = 0
    current_point = start[:]
    for step in path:


        direction = step[:1]
        step_length = int(step[1:])

        for s in range(step_length):
            if (current_point[0] == intersection[0]) and (current_point[1] == intersection[1]):
                # import pdb;pdb.set_trace()
                return distance

            if direction == 'R':
                current_point[0] += 1
            elif direction == 'L':
                current_point[0] -= 1
            elif direction == 'U':
                current_point[1] += 1
            elif direction == 'D':
                current_point[1] -= 1
            distance += 1
    return -1



def main():
    with open('./input.txt') as f:
        (path1, path2) = [l.rstrip('\n').split(',') for l in f.readlines()[:2]]

        # # find out extents of the board
        # he1 = get_horizontal_extent(path1)
        # he2 = get_horizontal_extent(path2)
        # max_left = max(he1[0], he2[0])
        # max_right = max(he1[1], he2[1])
        # ve1 = get_vertical_extent(path1)
        # ve2 = get_vertical_extent(path2)
        # max_down = max(ve1[0], ve2[0])
        # max_up = max(ve1[1], ve2[1])

        # import pdb;pdb.set_trace()

        # board = []
        # board1 = []
        # board2 = []
        # for i in range(max_left + max_right + 1):
        #     # print(i)
        #     board.append([])
        #     board1.append([])
        #     board2.append([])

        # for i in range(len(board1)):
        #     print('{}/{}'.format(i,len(board1)))
        #     for j in range(max_down + max_up + 1):
        #         # print(j)
        #         board[i].append(0)
        #         board1[i].append(0)
        #         board2[i].append(0)


        # print('boards initialized')
        # start = [max_left, max_down]
        start = [8412, 5080]
        # import pdb;pdb.set_trace()

        # board1 = wire(board1, start)
        # print('wire path1')
        # board1 = put_wire_on_board(board1, path1, start)
        # print('wire path2')
        # board2 = put_wire_on_board(board2, path2, start)

        # print('merge boards')
        # # merge boards
        # for x in range(len(board1)):
        #     for y in range(len(board1[0])):
        #         board[x][y] = (board1[x][y] + board2[x][y])


        # intersections = get_intersection(board)

        intersections=[[6016, 6091], [6016, 6117], [6113, 5674], [6121, 5674], [6148, 5578], [6578, 4467], [6638, 5564], [6688, 4393], [6734, 6930], [6803, 5521], [6843, 5564], [6843, 5769], [6885, 4091], [6885, 4123], [6990, 4091], [6990, 4123], [7107, 4179]]

        # closest_point = []
        # min_distance = max_down + max_up + max_left + max_right + 2
        min_distance = None

        for i in intersections:
            # distance = get_distance(start, i)
            distance1 = steps_to_point(i, path1, start)
            distance2 = steps_to_point(i, path2, start)
            distance = distance1 + distance2
            print(i)
            print(distance)
            if min_distance is None or distance < min_distance:
                min_distance = distance
                closest_point = i
        # print('intersections={}'.format(intersections))
        # print('start={}'.format(start))
        print('min_distance={}'.format(min_distance))
        # print('closest_point={}'.format(closest_point))
        # import pdb;pdb.set_trace()





if __name__ == '__main__':
    main()