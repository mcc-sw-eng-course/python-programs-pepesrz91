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

    def available_moves(self):
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
            player_move = int(input("Choose Your move, only numbers!"))
            self.board.player_move(player_move,self.player_char)
            player_turn = 'O'

        while self.game_won == False and len(self.board.available_moves()) > 0:

            if self.player_char == 'O' and player_turn == 'O':
                self.board.print_board()
                player_move = int(input("Choose Your move, only numbers!"))
                self.board.player_move(player_move, self.player_char)
                player_turn = 'X'
                if self.player_won(self.player_char, self.board.board):
                    print("You won!")
                    self.board.print_board()
                    return
            elif self.player_char == 'X' and player_turn == 'X':
                self.board.print_board()
                player_move = int(input("Choose Your move"))
                self.board.player_move(player_move, self.player_char)
                player_turn = 'O'
                game_won = self.player_won(self.player_char, self.board.board)
                if game_won:
                    print("You won!")
                    self.board.print_board()
                    return
            elif self.ai_char == 'O' and player_turn == 'O':
                print(self.board.available_moves())
                ai_move = random.choice(self.board.available_moves()) + 1
                self.board.player_move(ai_move, self.ai_char)
                player_turn = 'X'
                if self.player_won(self.ai_char,  self.board.board):
                    print("You Lost!")
                    self.board.print_board()
                    return
            elif self.ai_char == 'X' and player_turn == 'X':
                print(self.board.available_moves())
                ai_move = random.choice(self.board.available_moves()) + 1
                self.board.player_move(ai_move, self.ai_char)
                player_turn = 'O'
                if self.player_won(self.ai_char, self.board.board):
                    print("You Lost!")
                    self.board.print_board()
                    return
            else:
                print("Something went wrong")

        print("It was a tie!!")


def entered_loop():
    return True

new_board = Board()
tictactoe = TicTacToe()

tictactoe.game_start()