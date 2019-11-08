from chess.board import Board
from chess.board import Rook


class TestBoard:

    def test_it_should_be_instantiated(self):

        board = Board()

    def test_it_can_settle_a_rook(self):

        board = Board()
        rook = Rook()

        board.settle(rook, x='a', y='1')

        assert board.squares['a']['1'] == rook

    def xtest_it_shold_move_the_rook_to_a_position(self):

        board = Board()
        rook = Rook()
        board.settle(rook, x='a', y='1')

        board.move(from_x, from_y, to_x, to_y)
