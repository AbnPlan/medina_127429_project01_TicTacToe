import graphics

def main():
    window = graphics.GraphWin('Tic-Tac-Toe', 402, 402, autoflush=False)
    score = [0, 0]
    start_message(window)
    play_game(window, score)
    window.close()

#Creates the board
def set_board(window):
    #Set background to grey
    window.setBackground("grey")

    #The 4 lines that make up the board
    lines = [
        graphics.Line(graphics.Point(134, 0), graphics.Point(134, 402)),
        graphics.Line(graphics.Point(268, 0), graphics.Point(268, 402)),
        graphics.Line(graphics.Point(0, 134), graphics.Point(402, 134)),
        graphics.Line(graphics.Point(0, 268), graphics.Point(402, 268))
    ]

    #Draw all the lines in the list
    [i.draw(window) for i in lines]

#Prints the first messege to greet the user
def start_message(window):
    starting_messege = graphics.Text(graphics.Point(201,201), "Press any key to start...")
    starting_messege.draw(window)

    window.getKey()

    starting_messege.undraw()

#Prints goodby messege
def end_messege(window):
    end_messege = graphics.Text(graphics.Point(201,201), "Thanks for playing!!!")
    end_messege.draw(window)
    window.getMouse()

#Get working block
def getBlock(mouse_click):
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

#Print X
def drawX(window, block):

    if block == 0:
        lines = [
            graphics.Line(graphics.Point(0,0), graphics.Point(134,134)),
            graphics.Line(graphics.Point(0,134), graphics.Point(134,0))
        ]

    elif block == 1:
        lines = [
            graphics.Line(graphics.Point(134,0), graphics.Point(268,134)),
            graphics.Line(graphics.Point(134,134), graphics.Point(268,0))
        ]
        
    elif block == 2:
        lines = [
            graphics.Line(graphics.Point(268,0), graphics.Point(402,134)),
            graphics.Line(graphics.Point(268,134), graphics.Point(402,0))
        ]

    elif block == 3:
        lines = [
            graphics.Line(graphics.Point(0,134), graphics.Point(134,268)),
            graphics.Line(graphics.Point(0,268), graphics.Point(134,134))
        ]

    elif block == 4:
        lines = [
            graphics.Line(graphics.Point(134,134), graphics.Point(268,268)),
            graphics.Line(graphics.Point(134,268), graphics.Point(268,134))
        ]

    elif block == 5:
        lines = [
            graphics.Line(graphics.Point(268,134), graphics.Point(402,268)),
            graphics.Line(graphics.Point(268,268), graphics.Point(402,134))
        ]

    elif block == 6:
        lines = [
            graphics.Line(graphics.Point(0,268), graphics.Point(134,402)),
            graphics.Line(graphics.Point(0,402), graphics.Point(134,268))
        ]

    elif block == 7:
        lines = [
            graphics.Line(graphics.Point(134,268), graphics.Point(268,402)),
            graphics.Line(graphics.Point(134,402), graphics.Point(268,268))
        ]
    elif block == 8:
        lines = [
            graphics.Line(graphics.Point(268,268), graphics.Point(402,402)),
            graphics.Line(graphics.Point(268,402), graphics.Point(402,268))
        ]

    [i.draw(window) for i in lines]

#Print O
def drawO(window, block):
    if block == 0:
        block_center = graphics.Point(67, 67)
    elif block == 1:
        block_center = graphics.Point(201, 67)
    elif block == 2:
        block_center = graphics.Point(335, 67)
    elif block == 3:
        block_center = graphics.Point(67, 201)
    elif block == 4:
        block_center = graphics.Point(201, 201)
    elif block == 5:
        block_center = graphics.Point(335, 201)
    elif block == 6:
        block_center = graphics.Point(67, 335)
    elif block == 7:
        block_center = graphics.Point(201, 335)
    elif block == 8:
        block_center = graphics.Point(335, 335)

    circle = graphics.Circle(block_center , 65)
    circle.draw(window)
    


def cpu_move(master_board, boardX, boardO):
    possible_moves = [x for x, space in enumerate(master_board) if space == False]
    
    for i in possible_moves:
        board_copy = boardO[:]
        board_copy[i] = True
        if win_condition(board_copy):
            MOVE = i
            return MOVE

    for i in possible_moves:
        board_copy = boardX[:]
        board_copy[i] = True
        if win_condition(board_copy):
            MOVE = i
            return MOVE

    open_corners = []
    for i in possible_moves:
        if i in [0,2,6,8]:
            open_corners.append(i)
    if len(open_corners) > 0:
        MOVE = selectRandom(open_corners)
        return MOVE

    if 4 in possible_moves:
        MOVE = 4
        return MOVE

    open_edge = []
    for i in possible_moves:
        if i in [1,3,5,7]:
            open_edge.append(i)

    if len(open_edge) > 0:
        MOVE = selectRandom(open_edge)
        return MOVE

def selectRandom(open_spots):
    import random

    ln = len(open_spots)
    random_move = random.randrange(0 , ln)

    return open_spots[random_move]

#Check Win Condition
def win_condition(board):
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

def play_game(window, score):
    play_again = 'y'

    while play_again == 'y' or play_again == 'Y':
        set_board(window)
        game(window, score)

        clear(window)

        game_score = graphics.Text(graphics.Point(201,201), f'{score[0]} - {score[1]}')
        user_play_again = graphics.Text(graphics.Point(201,170), f'Press Y to play again, anything else to quit...')

        game_score.draw(window)
        user_play_again.draw(window)

        play_again = window.getKey()

        clear(window)

#Game Logic
def game(window, score):

    true_board = [
        True, True, True,
        True, True, True,
        True, True, True
    ]

    #Board checking for the X player moves
    boardX = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    #Board checking for the O player moves
    boardO = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    #Board marking all the spots already taken
    master_board = [
        False, False, False,
        False, False, False,
        False, False, False
    ]

    while True:
        user_click = window.getMouse()
        block = getBlock(user_click)

        if master_board[block] == False:
            master_board[block] = True

            drawX(window, block)
            boardX[block] = True

            if win_condition(boardX):
                Xwins = graphics.Text(graphics.Point(201,100), "X Wins!!!")
                Xwins.draw(window)
                end_messege(window)
                score[0] += 1
                return 0
            if master_board == true_board:
                is_draw = graphics.Text(graphics.Point(201,100), "It's a Draw")
                is_draw.draw(window)
                end_messege(window)
                return 0
            
            computer_move = cpu_move(master_board, boardX, boardO)
            drawO(window, computer_move)
            boardO[computer_move] = True
            master_board[computer_move] = True

            if win_condition(boardO):
                Owins = graphics.Text(graphics.Point(201,100), "O Wins!!!")
                Owins.draw(window)
                end_messege(window)
                score[1] += 1
                return 0
        #If the master board is full, the game ends in a draw
        if master_board == true_board:
            is_draw = graphics.Text(graphics.Point(201,100), "It's a Draw")
            is_draw.draw(window)
            end_messege(window)
            return 0

def clear(window):
    for item in window.items[:]:
        item.undraw()
    window.update()

if __name__ == '__main__':
    main()
