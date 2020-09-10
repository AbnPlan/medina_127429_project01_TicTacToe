import graphics

def main():
    window = set_board()
    first_message(window)
    game(window)
    

#Creates the board
def set_board():
    #Create the window
    window = graphics.GraphWin('Tic-Tac-Toe', 402, 402)

    #The 4 lines that make up the board
    line1 = graphics.Line(graphics.Point(134, 0), graphics.Point(134, 402))
    line2 = graphics.Line(graphics.Point(268, 0), graphics.Point(268, 402))
    line3 = graphics.Line(graphics.Point(0, 134), graphics.Point(402, 134))
    line4 = graphics.Line(graphics.Point(0, 268), graphics.Point(402, 268))

    #Draws the board on a grey background
    window.setBackground("grey")
    line1.draw(window)
    line2.draw(window)
    line3.draw(window)
    line4.draw(window)

    return window

#Prints the first messege to greet the user
def first_message(window):
    starting_messege = graphics.Text(graphics.Point(201,201), "Hello, click anywhere to start.")
    starting_messege.draw(window)
    window.getMouse()
    starting_messege.undraw()

#Prints goodby messege
def end_messege(window):
    end_messege = graphics.Text(graphics.Point(201,201), "Thanks for playing!!!")
    end_messege.draw(window)
    window.getMouse()


#Print X
def drawX(window, block):

    if block == 0:
        line1 = graphics.Line(graphics.Point(0,0), graphics.Point(134,134))
        line2 = graphics.Line(graphics.Point(0,134), graphics.Point(134,0))
    elif block == 1:
        line1 = graphics.Line(graphics.Point(134,0), graphics.Point(268,134))
        line2 = graphics.Line(graphics.Point(134,134), graphics.Point(268,0))
    elif block == 2:
        line1 = graphics.Line(graphics.Point(268,0), graphics.Point(402,134))
        line2 = graphics.Line(graphics.Point(268,134), graphics.Point(402,0))
    elif block == 3:
        line1 = graphics.Line(graphics.Point(0,134), graphics.Point(134,268))
        line2 = graphics.Line(graphics.Point(0,268), graphics.Point(134,134))
    elif block == 4:
        line1 = graphics.Line(graphics.Point(134,134), graphics.Point(268,268))
        line2 = graphics.Line(graphics.Point(134,268), graphics.Point(268,134))
    elif block == 5:
        line1 = graphics.Line(graphics.Point(268,134), graphics.Point(402,268))
        line2 = graphics.Line(graphics.Point(268,268), graphics.Point(402,134))
    elif block == 6:
        line1 = graphics.Line(graphics.Point(0,268), graphics.Point(134,402))
        line2 = graphics.Line(graphics.Point(0,402), graphics.Point(134,268))
    elif block == 7:
        line1 = graphics.Line(graphics.Point(134,268), graphics.Point(268,402))
        line2 = graphics.Line(graphics.Point(134,402), graphics.Point(268,268))
    elif block == 8:
        line1 = graphics.Line(graphics.Point(268,268), graphics.Point(402,402))
        line2 = graphics.Line(graphics.Point(268,402), graphics.Point(402,268))

    line1.draw(window)
    line2.draw(window)

#Print O
def drawO(window, block):
    block_center = graphics.Point(0,0)

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
    
#Get working block
def getBlock(mouse_click):
    if mouse_click.getX() < 134 and mouse_click.getY() < 134:
        return 0
    elif mouse_click.getX() < 268 and mouse_click.getY() < 134:
        return 1
    elif mouse_click.getX() < 402 and mouse_click.getY() < 134:
        return 2
    if mouse_click.getX() < 134 and mouse_click.getY() < 268:
        return 3
    elif mouse_click.getX() < 268 and mouse_click.getY() < 268:
        return 4
    elif mouse_click.getX() < 402 and mouse_click.getY() < 268:
        return 5
    if mouse_click.getX() < 134 and mouse_click.getY() < 402:
        return 6
    elif mouse_click.getX() < 268 and mouse_click.getY() < 402:
        return 7
    elif mouse_click.getX() < 402 and mouse_click.getY() < 402:
        return 8

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

#Game Logic
def game(window):
    i = True

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

        #This has 2 functions, check if the spot the player is clicking is taken
        #and to mark the taken spots for the draw condition
        if master_board[block] == False:
            master_board[block] = True

            #Variable i starts as true so that the X player plays first
            #and at the end, if player X does not meet the win condition
            #i changes to false to let the O player play
            if i:
                drawX(window, block)
                boardX[block] = True

                if win_condition(boardX):
                    Xwins = graphics.Text(graphics.Point(201,100), "X Wins!!!")
                    Xwins.draw(window)
                    end_messege(window)
                    return 0
                i = False

            #Same as the X player, and at the end, if the O player does not meet the win condition
            #i changes to True to let the X player play
            else:
                drawO(window, block)
                boardO[block] = True

                if win_condition(boardO):
                    Owins = graphics.Text(graphics.Point(201,100), "O Wins!!!")
                    Owins.draw(window)
                    end_messege(window)
                    return 0
                i = True

        #If the master board is full, the game ends in a draw
        if master_board == true_board:
            is_draw = graphics.Text(graphics.Point(201,100), "It's a Draw")
            is_draw.draw(window)
            end_messege(window)
            return 0


main()