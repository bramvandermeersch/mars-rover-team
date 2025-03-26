import unittest
from src.move_forward import Rover


class MoveForwardTest(unittest.TestCase):
    def test_whilst_facing_north_and_we_call_forwards_we_move_north(self):
        initial_position = [1, 1]
        initial_orientation = "N"
        expected_new_position = [1, 2]
        rover = Rover(initial_position, initial_orientation)
        rover.forwards()
        assert expected_new_position == rover.current_position()
