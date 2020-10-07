from Game import Game, Text, Point
def main():
    TicTacToe = Game()

    Text(Point(201, 201), 'Hello!!! \nPress any key to play the game.').draw(TicTacToe)
    TicTacToe.getKey()
    TicTacToe.clear()

    TicTacToe.play_game()

    Text(Point(201, 201), 'Thanks for playing!!!!  \nPress any key to play the game.').draw(TicTacToe)
    TicTacToe.getKey()
    
    TicTacToe.close()


    
    

if __name__ == '__main__':
    main()
