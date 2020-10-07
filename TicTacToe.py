from Game import Game, Text, Point
def main():
    TicTacToe = Game()
    
    menu_text = Text(
        Point(201, 201), """Hello!!! 
                            \nPress 0 to do simulation  
                            \nPress 1 to play the game. 
                            \nPress 2 to exit"""
    )
    menu_text.draw(TicTacToe)

    while True:
        key_check = TicTacToe.checkKey()

        if key_check == '0':
            TicTacToe.clear()
            TicTacToe.simulate(1000)
            TicTacToe.clear()
            menu_text.draw(TicTacToe)
            

        elif key_check == '1':
            TicTacToe.clear()
            TicTacToe.play_game()
            menu_text.draw(TicTacToe)

        elif key_check == '2':
            break

    TicTacToe.close()
    
if __name__ == '__main__':
    main()
