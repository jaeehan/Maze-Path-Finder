import queue


# map of the maze
def createMaze():
    maze = []
    maze.append(["#", "O", "#", "#", "#", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", " ", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", " ", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", "#", "#", "#", "#", "#", "#", "X", "#"])

    return maze


# loop over the maze and enumerate through them, starting at index 0
def printMaze(maze, path=""):
    # x is the index, pos is the value
    for x, pos in enumerate(maze[0]):
        # find the O for pos
        if pos == "O":
            # set the index to start position
            start = x

    # c is the column position
    c = start
    # r is the row position
    r = 0

    # let pos be a new empty set object
    pos = set()
    for move in path:
        if move == "L":
            c -= 1

        elif move == "R":
            c += 1

        elif move == "U":
            r -= 1

        elif move == "D":
            r += 1

        # add movement to position
        pos.add((r, c))

    # for row position and value, enumerate over the maze
    for r, row in enumerate(maze):
        # for column position and vlue, enumerate over the maze
        for c, col in enumerate(row):
            # if current pos, set to +
            if (r, c) in pos:
                print("+ ", end="")
            # if not current pos, leave it as is
            else:
                print(col + " ", end="")
        print()


def valid(maze, moves):
    # x (index) and pos (value) will enumerate over the maze starting at index 0
    for x, pos in enumerate(maze[0]):
        # find the O for pos
        if pos == "O":
            # set the index to start position
            start = x

    # c is the column position
    c = start
    # r is the row position
    r = 0

    for move in moves:
        if move == "L":
            c -= 1

        elif move == "R":
            c += 1

        elif move == "U":
            r -= 1

        elif move == "D":
            r += 1

        # if c (column) and r (row) are NOT more than or equal to 0 and less than the column or row position,
        # it is an invalid position
        if not (0 <= c < len(maze[0]) and 0 <= r < len(maze)):
            return False
        # if the position has #, it is an invalid position
        elif maze[r][c] == "#":
            return False
    # otherwise, return true for valid position
    return True


def findEnd(maze, moves):
    # x (index) and pos (value) will enumerate over the maze starting at index 0
    for x, pos in enumerate(maze[0]):
        # find O for pos
        if pos == "O":
            # set index to start position
            start = x

    # c is the column position
    c = start
    # r is the row position
    r = 0
    for move in moves:
        if move == "L":
            c -= 1

        elif move == "R":
            c += 1

        elif move == "U":
            r -= 1

        elif move == "D":
            r += 1

    # if pos has an X
    if maze[r][c] == "X":
        # print the moves
        print("Found: " + moves)
        # print the maze with moves
        printMaze(maze, moves)
        return True

    return False


# Breadth First Search algorithm

# set nums to create queue
nums = queue.Queue()
# start by putting blank string into the queue
nums.put("")
# add is the first path that we have, initialize here
add = ""
# create maze
maze = createMaze()

# while the end of the maze is not found, continue updating the path
while not findEnd(maze, add):
    # get and dequeue first element of queue
    add = nums.get()
    # print(add)
    for j in ["L", "R", "U", "D"]:
        # create new queue (updt) and add the first element we get, then add either L,R,U, or D
        updt = add + j
        # make sure it is a valid path
        if valid(maze, updt):
            # if valid, add to queue
            nums.put(updt)
