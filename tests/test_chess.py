import pytest

from chess.board import (
    Board,
    ImpossibleSettleException,
    Rook,
)


class TestBoard:

    class TestSettle:

        def test_it_should_settle_the_rook_in_a_square(self):

            board = Board()
            rook = Rook()

            board.settle(rook, x='a', y='1')

            assert board.squares['a']['1'] == rook

        def test_it_raise_an_exception_if_a_piece_already_settled(self):

            board = Board()
            board.squares = {
                'a': {
                    '1': Rook()
                }
            }

            with pytest.raises(ImpossibleSettleException):

                board.settle(Rook(), x='a', y='1')
