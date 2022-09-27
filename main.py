"""Created by bar1k4real on 24.09.2022."""


class NumberNotInRangeError(Exception):
    """MyException NumberNotInRangeError"""


class CellOverflowError(Exception):
    """MyException CellOverflowError"""


class TicTacGame:
    """Tic-Tac-Toe Game"""

    def __init__(self):
        self.board = list(range(1, 10))

    def show_board(self):
        """Show board"""
        print('┌───┬───┬───┐')
        print(f'│ {self.board[0]} │ {self.board[1]} │ {self.board[2]} │')
        print('├───┼───┼───┤')
        print(f'│ {self.board[3]} │ {self.board[4]} │ {self.board[5]} │')
        print('├───┼───┼───┤')
        print(f'│ {self.board[6]} │ {self.board[7]} │ {self.board[8]} │')
        print('└───┴───┴───┘')

    def validate_input(self):
        """All checks for validate input"""
        while True:
            try:
                value = input()
                value = self.check_input(value)
                break
            except ValueError:
                print('Invalid value, enter a number: ')
            except NumberNotInRangeError:
                print('Invalid range, enter a number from 1 to 9: ')
            except CellOverflowError:
                print('This cell is already occupied, enter another number: ')
        return value

    def check_input(self, value):
        """Check Exceptions"""
        value = int(value)
        if value < 1 or value > 9:
            raise NumberNotInRangeError()
        if self.board[value - 1] != ' ':
            raise CellOverflowError()
        return value

    def start_game(self):
        """Start Game"""
        print('Welcome to the Tic-Tac-Toe Game!')
        print('Choose the cell number to put a cross or a zero.')
        self.show_board()
        self.board = list(' ' * 9)
        move_number = 0
        while True:
            move_number += 1
            self.show_board()
            print(f'{move_number} move')
            print('Enter the cell number: ')
            value = self.validate_input()
            if move_number % 2 == 0:
                self.board[value - 1] = 'O'
            else:
                self.board[value - 1] = 'X'
            if self.check_winner():
                print(f'Player {(move_number + 1) % 2 + 1} wins!')
                break
            if move_number == 9:
                print('Draw!')
                break
        self.show_board()

    def check_winner(self):
        """Check winner"""
        winning_combinations = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
                                (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
        for combination in winning_combinations:
            if self.board[combination[0]] == self.board[combination[1]] == \
                    self.board[combination[2]] != ' ':
                return True
        return False


if __name__ == '__main__':
    game = TicTacGame()
    game.start_game()
