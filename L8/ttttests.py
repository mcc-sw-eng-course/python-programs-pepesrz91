import unittest
from unittest.mock import patch
import random

class Board:
    def __init__(self):
        self.board = [['','',''],['','',''],['','','']]


    def print_board(self):
        print(' ------------- ')
        for i in self.board:
            board_string = ''
            for index, j in enumerate(i):
                if index != 1:
                    if j == '':
                        board_string += ' |   | '
                    else:
                        board_string += ' | ' + j + ' | '
                else:
                    if j == '':
                        board_string += ' '
                    else:
                        board_string += '' + j + ''
            print(board_string)
            print(' ------------- ')

    def available_moves(self): #TODO: Check if there are still avialable moves.
        available_moves = []
        for row, i in enumerate(self.board):
            for column, j in enumerate(i):
                if row == 0 and j == '':
                    available_moves.append(column)
                elif row == 1 and j == '':
                    available_moves.append(column + 3)
                elif row == 2 and j == '':
                    available_moves.append(column + 6)
                else:
                    continue
        return available_moves

    def player_move(self,index,string):
        if string != 'X' and string != 'O':
            raise Exception('Move must be X or O only.')
        while True:
            if index > 0 and index <= 3 and (index - 1) in self.available_moves():
                self.board[0][index -1] = string
                break
            elif index > 3 and index <= 6 and (index - 1) in self.available_moves():
                self.board[1][index - 4] = string
                break
            elif index > 6 and index <= 9 and (index - 1) in self.available_moves():
                self.board[2][index - 7] = string
                break
            else:
                print("Invalid move! Try again")
                index = int(input("> "))
                continue


class TicTacToe:
    def __init__(self):
        count = 0
        while True:
            print("Please choose a X or O")
            self.player_char = input('> ').upper()
            if self.player_char == 'X':
                self.ai_char = 'O'
                break
            elif self.player_char == 'O':
                self.ai_char = 'X'
                break
            else:
                print("invalid input!, please try again")
                entered_loop()
        self.board = Board()
        self.game_won = False

    def player_won(self, letter, board):

        if board[0][0] == letter and board[0][1] == letter and board[0][2] == letter:
            return True
        elif board[1][0] == letter and board[1][1] == letter and board[1][2] == letter:
            return True
        elif board[2][0] == letter and board[2][1] == letter and board[2][2] == letter:
            return True
        elif board[0][0] == letter and board[1][0] == letter and board[2][0] == letter:
            return True
        elif board[0][1] == letter and board[1][1] == letter and board[2][1] == letter:
            return True
        elif board[0][2] == letter and board[1][2] == letter and board[2][2] == letter:
            return True
        elif board[0][0] == letter and board[1][1] == letter and board[2][2] == letter:
            return True
        elif board[0][2] == letter and board[1][1] == letter and board[2][0] == letter:
            return True
        else:
            return False

    def game_start(self):
        # Get the first player move
        if self.ai_char == 'X':
            ai_move = random.choice(self.board.available_moves()) + 1
            self.board.player_move(ai_move, self.ai_char)
            player_turn = 'O'

        else:
            self.board.print_board()
            player_move = int(input("Choose Your move"))
            self.board.player_move(player_move,self.player_char)
            player_turn = 'O'

        while self.game_won == False and len(self.board.available_moves()) > 0:

            if self.player_char == 'O' and player_turn == 'O':
                self.board.print_board()
                player_move = int(input("Choose Your move"))
                self.board.player_move(player_move, self.player_char)
                player_turn = 'X'
                if self.player_won(self.player_char, self.board.board):
                    print("You won!")
                    break
            elif self.player_char == 'X' and player_turn == 'X':
                self.board.print_board()
                player_move = int(input("Choose Your move"))
                self.board.player_move(player_move, self.player_char)
                player_turn = 'O'
                game_won = self.player_won(self.player_char, self.board.board)
                if game_won:
                    print("You won!")
                    break
            elif self.ai_char == 'O' and player_turn == 'O':
                print(self.board.available_moves())
                ai_move = random.choice(self.board.available_moves()) + 1
                self.board.player_move(ai_move, self.ai_char)
                player_turn = 'X'
                if self.player_won(self.ai_char,  self.board.board):
                    print("You Lost!")
                    break
            elif self.ai_char == 'X' and player_turn == 'X':
                print(self.board.available_moves())
                ai_move = random.choice(self.board.available_moves()) + 1
                self.board.player_move(ai_move, self.ai_char)
                player_turn = 'O'
                if self.player_won(self.ai_charr, self.board.board):
                    print("You Lost!")
                    break
            else:
                print("Something went wrong")


def entered_loop():
    return True


class Board_Tests(unittest.TestCase):
    def test_correct(self):
        new_board = Board()
        another_board = [['','',''],['','',''],['','','']]
        self.assertEqual(new_board.board == another_board, True)

    def test_print_board(self):
        new_board = Board()
        new_board.board = [['','X',''],['','','X'],['','','X']]


    def test_available_moves(self):
        new_board = Board()
        new_board.board = [['', '', ''], ['', '', ''], ['', '', '']]
        available_moves = new_board.available_moves()
        print(available_moves)
        self.assertEqual(available_moves == [0,1,2,3,4,5,6,7,8],True)

    def test_player_move(self):
        new_board = Board()
        new_board.player_move(1,'X')
        another_board = [['X', '', ''], ['', '', ''], ['', '', '']]
        self.assertEquals(new_board.board == another_board, True)
        another_board = [['X', '', 'O'], ['', '', ''], ['', '', '']]
        new_board.player_move(3, 'O')
        self.assertEquals(new_board.board == another_board, True)
        another_board = [['X', '', 'O'], ['', 'X', ''], ['', '', '']]
        new_board.player_move(5, 'X')
        self.assertEquals(new_board.board == another_board, True)
        another_board = [['X', '', 'O'], ['', 'X', ''], ['', '', 'O']]
        new_board.player_move(9, 'O')
        self.assertEquals(new_board.board == another_board, True)

    @patch('builtins.input', return_value='X')
    def test_player_char_x(self, input):
        new_ttt = TicTacToe() ## Input X
        self.assertEqual(new_ttt.ai_char == 'O', True)

    @patch('builtins.input', return_value='O')
    def test_player_char_o(self, input):
        new_ttt = TicTacToe()  ## Input X
        self.assertEqual(new_ttt.ai_char == 'X', True)

    @patch('builtins.input', return_value=1)
    def test_player_char_loop(self, input):
        loop = entered_loop()
        self.assertEqual(loop, True)
    def test_game_star(self):
        new_ttt = TicTacToe()
        new_ttt.game_start()


if __name__ == "__main__":

    unittest.main()