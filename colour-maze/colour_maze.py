class Queue(object):

    def __init__(self, sequence):

        if len(sequence) == 0:
            raise IndexError('Zero length sequences are disallowed.')

        self.sequence = sequence
        self.reset()

    def reset(self):
        self.queue = [x for x in self.sequence[::-1]]

    def next(self):
        try:
            return self.queue.pop()
        except IndexError:
            self.reset()
            return self.next()

def parse_maze(unparsed_maze):
    """
    Pass the maze into something usable
    :param unparsed_maze: The maze to be parsed
    :return: The parsed maze
    :type: str -> list[list]
    """
    maze = [x.split() for x in [y for y in unparsed_maze.split('\n')]]

    return maze

def is_valid(maze, position, next_sequence):
    """
    Is there a valid next sequence in the position provided
    :param maze: The maze
    :param position: A tuple giving the position in the maze
    :param sequence: Possible valid values
    :return: Bool
    :type: (list[list], tuple[int, int], str) -> Bool
    """

    row, col = position

    return maze[row][col] == next_sequence

def find_nearby(maze, position):
    """
    Find legal, potentially valid, future positions
    :param maze: The maze
    :param position: The current position within the maze
    :return: The legal next positions
    :type: (list[list], tuple[int, int]) -> list[tuple[int, int]]
    """
    def position_exists(row, col):

        if row < 0:
            return
        elif col < 0:
            return

        try:
            if maze[row][col]:
                return (row, col)
        except IndexError:
            pass

    row, col = position

    nearby = []

    nearby.append(position_exists(row + 1, col))
    nearby.append(position_exists(row, col + 1))
    nearby.append(position_exists(row - 1, col))
    nearby.append(position_exists(row, col - 1))

    return [x for x in nearby if x is not None]

def starting_point(maze, starting_character):
    """
    Find the starting point, always on the last row of the maze
    :param maze: The maze
    :param sequence: Possible valid values
    :return: All valid starting points
    :type: (list[list], str) -> list[tuple[int, int]]
    """

    last_row = len(maze) - 1
    positions = []

    for column, character in enumerate(maze[last_row]):

        if maze[last_row][column] == starting_character:
            positions.append((last_row, column))

    return positions


def solve(maze, position, next_sequence, path):
    """
    Given a position and sequence within the maze determine the next step to make
    :param maze: The maze
    :param position: Current position within the maze
    :param next_sequence: The next valid step to be made
    :param path: All steps made so far
    :return: The path with the new step appended
    :type: (list[list], tuple[int, int], str, list[tuple[int, int]]) -> list[tuple[int, int]]
    """
    nearby_positions = find_nearby(maze, position)

    # Try to find a unique path
    for position in nearby_positions:
        if position in path:
            continue
        if is_valid(maze, position, next_sequence):
            path.append(position)
            return path

    # If there is no unique path pick anything that keeps us moving.
    for position in nearby_positions:
        if is_valid(maze, position, next_sequence):
            path.append(position)

    return path


def run(unparsed_maze, sequence):
    """
    Run the entire solution.
    :param unparsed_maze: A string representing the maze to be run
    :param sequence: The sequence of events that need to be looked out for
    :return: The list of steps that are to be taken
    :type: (str, str) -> list[tuple[int, int]]
    """

    maze = parse_maze(unparsed_maze)
    queue = Queue(sequence)
    queue.reset()
    starting_positions = starting_point(maze, queue.next())
    for position in starting_positions:
        path = [position]
        while True:
            path = solve(maze, path[-1:][0], queue.next(), path)

            if not path:
                queue.reset()
                queue.next()
                break

            if path[-1:][0][0] == 0:
                break

    return path


def print_path(maze, path):
    """
    Prints the maze with the path highlighted
    :param maze: The parsed maze
    :param path: The path taken through the parsed maze
    :return: Nothing
    :type: (list[list], list[tuple[int, int]]) -> None
    """

    maze_size = len(maze)

    for i in range(maze_size):
        for j in range(maze_size):
            if (i, j) in path:
                continue
            maze[i][j] = '\\'

    rows = []
    for row in maze:
        rows.append(' '.join(x for x in row))

    printable_maze = '\n'.join(x for x in rows)

    print(printable_maze)