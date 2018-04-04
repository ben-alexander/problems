import unittest
import colour_maze


class TestQueue(unittest.TestCase):

    @classmethod
    def setUp(self):
        self.sequence = 'OG'
        self.queue = colour_maze.Queue(self.sequence)

    def test_reset(self):
        self.queue.reset()

        self.assertEqual(self.queue.queue, ['G', 'O'])

    def test_queue_exhaustion(self):
        self.assertEqual(self.queue.next(), 'O')
        self.assertEqual(self.queue.next(), 'G')
        self.assertEqual(self.queue.next(), 'O')


class TestColourMaze(unittest.TestCase):

    @classmethod
    def setUp(self):

        self.sequence = 'OG'
        self.maze = """B O R O Y\nO R B G R\nB O G O Y\nY G B Y G\nR O R B R"""

    def test_parse_maze(self):
        """
        The maze as a string is parsed into a list of lists.
        """

        maze = colour_maze.parse_maze(self.maze)

        self.assertEqual(maze, [['B', 'O', 'R', 'O', 'Y']
                                , ['O', 'R', 'B', 'G', 'R']
                                , ['B', 'O', 'G', 'O', 'Y']
                                , ['Y', 'G', 'B', 'Y', 'G']
                                , ['R', 'O', 'R', 'B', 'R']
                                ])

    def test_is_valid(self):
        """
        Given a position within the maze a valid sequence is returned.
        """

        maze = colour_maze.parse_maze(self.maze)

        self.assertEqual(colour_maze.is_valid(maze, (0, 1), 'O'), True)
        self.assertEqual(colour_maze.is_valid(maze, (1, 2), 'G'), False)

    def test_find_nearby(self):
        """
        Legal valid positions.
        """

        maze = colour_maze.parse_maze(self.maze)

        self.assertItemsEqual(colour_maze.find_nearby(maze, (0, 0)), [(0, 1), (1, 0)])
        self.assertItemsEqual(colour_maze.find_nearby(maze, (4, 1)), [(4, 0), (4, 2), (3, 1)])
        self.assertItemsEqual(colour_maze.find_nearby(maze, (3, 1)), [(3, 0), (3, 2), (2, 1), (4, 1)])


    def test_starting_point(self):
        """
        Find all possble starting points.
        """

        maze = colour_maze.parse_maze(self.maze)

        self.assertItemsEqual(colour_maze.starting_point(maze, 'O'), [(4, 1)])
        self.assertItemsEqual(colour_maze.starting_point(maze, 'R'), [(4, 0), (4, 2), (4, 4)])

    def test_solve(self):
        """
        Iterate over the maze and find the path through
        """

        maze = colour_maze.parse_maze(self.maze)
        queue = colour_maze.Queue('OG')
        queue.reset()
        queue.next()
        self.assertEqual(colour_maze.solve(maze, (4, 1), queue.next(), [(4, 1)])
                         , [(4, 1), (3, 1)])

        self.assertEqual(colour_maze.solve(maze, (3, 1), queue.next(), [(4, 1), (3, 1)])
                         , [(4, 1), (3, 1), (2, 1)])


    def test_run(self):
        """
        End to end integration test
        """

        self.assertEqual(colour_maze.run(self.maze, self.sequence), [(4, 1), (3, 1), (2, 1), (2, 2), (2, 3), (1, 3), (0, 3)])