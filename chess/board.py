class ImpossibleSettleException(Exception):
    pass


class Board:

    def __init__(self):
        self.squares = {
            'a': {'1': {}},
        }

    def settle(self, rook, x, y):

        if self.squares[x][y]:
            raise ImpossibleSettleException

        self.squares = {
            x: {
                y: rook
            }
        }


class Rook:
    pass
