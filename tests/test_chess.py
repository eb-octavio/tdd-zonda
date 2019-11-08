from chess.board import Board
from chess.board import Rook


class TestBoard:

    def test_it_can_settle_a_rook(self):

        board = Board()
        rook = Rook()

        board.settle(rook, x='a', y='1')

        assert board.squares['a']['1'] == rook
