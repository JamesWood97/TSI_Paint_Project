import unittest
from main import *


class WallTests(unittest.TestCase):
    def create_wall(self):
        wall = Wall(2, 10, (), None, 1)
        self.assertIsInstance(wall, Wall)

    def get_wall_area(self):
        wall = Wall(2, 10, (), None, 1)
        self.assertEqual(wall.get_area(), 20)

    def set_wall_paint(self):
        wall = Wall(2, 10, (), None, 1)
        paint = Paint("bob", 10)
        wall.set_paint(paint)
        self.assertEqual(paint, wall.get_paint())

    def wall_get_length(self):
        wall = Wall(2, 10, (), None, 1)
        self.assertEqual(wall.get_length(), 10)

    def wall_get_height(self):
        wall = Wall(2, 10, (), None, 1)
        self.assertEqual(wall.get_length(), 2)













if __name__ == '__main__':
    unittest.main()
