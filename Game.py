from graphics import GraphWin, Line, Circle, Text, Point
from random import randrange

class Game():
    
    def __init__(self):
        self.window = GraphWin('Tic-Tac-Toe', 402, 402, autoflush=False)

        self.score = [0,0]

        self.true_board = [True] * 9
        self.boardX = [False] * 9
        self.boardO = [False] * 9
        self.master_board = [False] * 9

    def start_message(self):
        starting_messege = Text(Point(201,201), "Press any key to start...")
        starting_messege.draw(self.window)

        self.window.getKey()

        starting_messege.undraw()

    #Prints goodby messege
    def end_messege(self):
        end_messege = Text(Point(201,201), "Thanks for playing!!!")
        end_messege.draw(self.window)
        self.window.getMouse()

    def clear(self):
        for item in self.window.items[:]:
            item.undraw()

        self.window.update()
    
    def board(self):
        #Set background to grey
        self.window.setBackground("grey")

        #The 4 lines that make up the board
        lines = [
            Line(Point(134, 0), Point(134, 402)),
            Line(Point(268, 0), Point(268, 402)),
            Line(Point(0, 134), Point(402, 134)),
            Line(Point(0, 268), Point(402, 268))
        ]

        #Draw all the lines in the list
        [i.draw(self.window) for i in lines]

    #Print X
    def drawX(self, block):

        if block == 0:
            lines = [
                Line(Point(0,0), Point(134,134)),
                Line(Point(0,134), Point(134,0))
            ]

        elif block == 1:
            lines = [
                Line(Point(134,0), Point(268,134)),
                Line(Point(134,134), Point(268,0))
            ]
            
        elif block == 2:
            lines = [
                Line(Point(268,0), Point(402,134)),
                Line(Point(268,134), Point(402,0))
            ]

        elif block == 3:
            lines = [
                Line(Point(0,134), Point(134,268)),
                Line(Point(0,268), Point(134,134))
            ]

        elif block == 4:
            lines = [
                Line(Point(134,134), Point(268,268)),
                Line(Point(134,268), Point(268,134))
            ]

        elif block == 5:
            lines = [
                Line(Point(268,134), Point(402,268)),
                Line(Point(268,268), Point(402,134))
            ]

        elif block == 6:
            lines = [
                Line(Point(0,268), Point(134,402)),
                Line(Point(0,402), Point(134,268))
            ]

        elif block == 7:
            lines = [
                Line(Point(134,268), Point(268,402)),
                Line(Point(134,402), Point(268,268))
            ]
        elif block == 8:
            lines = [
                Line(Point(268,268), Point(402,402)),
                Line(Point(268,402), Point(402,268))
            ]

        [i.draw(self.window) for i in lines]

    def drawO(self, block):
        if block == 0:
            block_center = Point(67, 67)
        elif block == 1:
            block_center = Point(201, 67)
        elif block == 2:
            block_center = Point(335, 67)
        elif block == 3:
            block_center = Point(67, 201)
        elif block == 4:
            block_center = Point(201, 201)
        elif block == 5:
            block_center = Point(335, 201)
        elif block == 6:
            block_center = Point(67, 335)
        elif block == 7:
            block_center = Point(201, 335)
        elif block == 8:
            block_center = Point(335, 335)

        Circle(block_center , 65).draw(self.window)
    
    def getBlock(self):
        mouse_click = self.window.getMouse()

        if mouse_click.getX() < 134 and mouse_click.getY() < 134:
            return 0
        elif mouse_click.getX() < 268 and mouse_click.getY() < 134:
            return 1
        elif mouse_click.getX() < 402 and mouse_click.getY() < 134:
            return 2
        elif mouse_click.getX() < 134 and mouse_click.getY() < 268:
            return 3
        elif mouse_click.getX() < 268 and mouse_click.getY() < 268:
            return 4
        elif mouse_click.getX() < 402 and mouse_click.getY() < 268:
            return 5
        elif mouse_click.getX() < 134 and mouse_click.getY() < 402:
            return 6
        elif mouse_click.getX() < 268 and mouse_click.getY() < 402:
            return 7
        elif mouse_click.getX() < 402 and mouse_click.getY() < 402:
            return 8

    def cpu_move(self):
        possible_moves = [x for x, space in enumerate(self.master_board) if space == False]
        
        for i in possible_moves:
            board_copy = self.boardO[:]
            board_copy[i] = True
            if self.win_condition(board_copy):
                MOVE = i
                return MOVE

        for i in possible_moves:
            board_copy = self.boardX[:]
            board_copy[i] = True
            if self.win_condition(board_copy):
                MOVE = i
                return MOVE

        open_corners = []
        for i in possible_moves:
            if i in [0,2,6,8]:
                open_corners.append(i)
        if len(open_corners) > 0:
            MOVE = self.selectRandom(open_corners)
            return MOVE

        if 4 in possible_moves:
            MOVE = 4
            return MOVE

        open_edge = []
        for i in possible_moves:
            if i in [1,3,5,7]:
                open_edge.append(i)

        if len(open_edge) > 0:
            MOVE = self.selectRandom(open_edge)
            return MOVE

    def selectRandom(self, open_spots):
        ln = len(open_spots)
        random_move = randrange(0 , ln)
        return open_spots[random_move]
    
    def win_condition(self, board):
        if (
        (board[0] == True and board[1] == True and board[2] == True) or
        (board[3] == True and board[4] == True and board[5] == True) or
        (board[6] == True and board[7] == True and board[8] == True) or
        (board[0] == True and board[3] == True and board[6] == True) or
        (board[1] == True and board[4] == True and board[7] == True) or
        (board[2] == True and board[5] == True and board[8] == True) or
        (board[0] == True and board[4] == True and board[8] == True) or
        (board[6] == True and board[4] == True and board[2] == True)):
            return True
        else:
            return False

    def game(self):
        while True:
            block = self.getBlock()

            if self.master_board[block] == False:
                self.master_board[block] = True
                self.boardX[block] = True
                self.drawX(block)
                

                if self.win_condition(self.boardX):
                    Text(Point(201,100), "X Wins!!!").draw(self.window)
                    self.end_messege()
                    self.score[0] += 1
                    return 0
                if self.master_board == self.true_board:
                    Text(Point(201,100), "It's a Draw").draw(self.window)
                    self.end_messege()
                    return 0
                
                computer_move = self.cpu_move()
                self.drawO(computer_move)
                self.boardO[computer_move] = True
                self.master_board[computer_move] = True

                if self.win_condition(self.boardO):
                    Text(Point(201,100), "O Wins!!!").draw(self.window)
                    self.end_messege()
                    self.score[1] += 1
                    return 0
            #If the master board is full, the game ends in a draw
            if self.master_board == self.true_board:
                Text(Point(201,100), "It's a Draw")
                self.end_messege()
                return 0

    def play_game(self):
        play_again = 'y'

        while play_again == 'y' or play_again == 'Y':
            self.board()
            self.game()
            self.clear()
            Text(Point(201,201), f'{self.score[0]} - {self.score[1]}').draw(self.window)
            Text(Point(201,170), f'Press Y to play again, anything else to quit...').draw(self.window)

            play_again = self.window.getKey()
            
            self.clear()
            self.true_board = [True] * 9
            self.boardX = [False] * 9
            self.boardO = [False] * 9
            self.master_board = [False] * 9

        