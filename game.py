import random as r

class TicTacToe:
    def __init__(self):
        # self.board = ["  " for _ in range(3)]
        # self.current_winner = None

        self.board = {'7': ' ', '8': ' ', '9': ' ',
                    '4': ' ', '5': ' ', '6': ' ',
                    '1': ' ', '2': ' ', '3': ' '}

    def print_board(self):
        print(self.board['7'] + ' | ' + self.board['8'] + ' | ' + self.board['9'])
        print('--+---+--')
        print(self.board['4'] + ' | ' + self.board['5'] + ' | ' + self.board['6'])
        print('--+---+--')
        print(self.board['1'] + ' | ' + self.board['2'] + ' | ' + self.board['3'])


class human_player(TicTacToe):

    def __init__(self):
        super().__init__()

    def get_user_input(self):
        entry = input("Where do you want to mark?")
        return entry

    def get_computer_input(self):
        r1 = r.randint(1, 9)
        for i in range(10):
            if r1 not in comp_inp_list:
                break
            else:
                r1 = r.randint(1, 9)

        comp_inp_list.append(r1)
        return str(r1)

    def human_player_turn(self, user_input):

        end_loop = True

        while end_loop:

            if self.board[user_input] == ' ':
                end_loop = False
                self.board[user_input] = "X"
                self.print_board()

            else:
                user_input = input("Already filled, use a different place to mark?")
                # print("Already filled, use a different place to mark")


    def computer_turn(self, user_input):
        end_loop = True

        while end_loop:

            if self.board[user_input] == ' ':
                end_loop = False
                self.board[user_input] = "O"
                self.print_board()

            else:
                print("Looks like its already filled, I am choosing a different place to mark")
                user_input = self.get_computer_input()



tk = TicTacToe()
hp = human_player()

comp_inp_list = []
# def get_user_input():
#     entry = input("Where do you want to mark?")
#     return entry
#
# def get_computer_input():
#     r1 = r.randint(1,9)
#     for i in range(10):
#         if r1 not in comp_inp_list:
#             break
#         else:
#             r1 = r.randint(1,9)
#
#     comp_inp_list.append(r1)
#     return str(r1)

print("Assume you are X, O is played by the computer")
starter = ""

while starter != "X" or starter != "O":
    starter = str(input("Who wants to start X or O?"))
    if starter == "X" or starter == "O":
        break

turns = 1

while turns<10:
    if starter == "X":
        if turns%2 != 0:
            print("Xs turn")
            inp = hp.get_user_input()
            hp.human_player_turn(inp)
            turns = turns + 1
        else:
            print("Os turn")
            cp_inp = hp.get_computer_input()
            hp.computer_turn(cp_inp)
            turns = turns+1


    else:
        if turns % 2 != 0:
            print("Os turn")
            turns = turns + 1
        else:
            print("Xs turn")
            turns = turns + 1