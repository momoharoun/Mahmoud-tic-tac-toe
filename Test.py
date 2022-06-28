import mvc_final
import random
import unittest


class TestModel(unittest.TestCase):

    def test_spot_available(self):
        model = mvc_final.Model()
        for row in range(mvc_final.internal_board_rows):
            for col in range(mvc_final.internal_board_colm):
                number = random.randint(1, 2)
                self.assertTrue(model.is_square_available(row, col), "There is no square available to be claim.")
                model.highlight_board(row, col, number)
                self.assertFalse(model.is_square_available(row, col), "The square was not claimed.")

    def test_board_full(self):
        model = mvc_final.Model()
        for row in range(mvc_final.internal_board_rows):
            for col in range(mvc_final.internal_board_colm):
                number = random.randint(1, 2)
                self.assertFalse(model.is_my_board_full(), "The board is already full")
                model.highlight_board(row, col, number)
            self.assertTrue(model.is_my_board_full(), "The board is not yet filled")


if __name__ == '__main__':
    unittest.main()

"PLease check README file for sources used throughout the project !!!"
"However I learned how this is done by using Jannatul example as a reference and then implementing it on my own !"