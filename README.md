### Hector A. Medina Torres  127429  
# TicTacToe
Personal TicTacToe project  
  
This is a TicTacToe game that opens a Gui and allows the user to pick a space to put a X on and then lets a Computer algorithm pick a space for O. 
The program starts by creating a list of the scores of both the computer player and the user, used to keep track of the wins. It then proceds to 
create the windows that will display the game. The window is 402x402 pixels and it has a tittle of 'Tic-Tac-Toe'. After the window is created, it 
displays a messege for the user to welcome it. When the user clicks on any spot on the window, it will start a loop of the game that ends whnever 
the user click any other key besides 'y' or 'Y' at the end of the loop. The loop starts by seting the board and waiting for user input to let the 
user pick his play. After the user plays, the computer proceeds to generate a play.   

The algorith for the computer to pick ist play goes as follow:  
1- If the computer can win this turn by using a move, play that move.  
2- If the user can win next turn by using a move, play that move.  
3- If any of the corner are available, play one of them. If more than one is open, pick at random.  
4- If the center is open, play the center  
5- If any  of the edges are available, play one of them. If more than one is open, pick at random.  
6- If nothing is available, return 0  

This loop of the user and the CPU is going to keep going until one of three conditions are met:  
1- The user meets the win condition  
2- The cpu meets the win condition  
3- The master board is filled with all true, meaning that all the posiible moves have been made, but neither player met the win condition.  

Whenever one of the conditions are met, a messege will display, telling the user who won or it was a draw. When the user clicks on the screen, 
board is cleared and a messege is displayed showing the current scores and asking the user if he wants to continue playing. If the user press
'y' or 'Y' the board clears and the user can play again, otherwise, the game closes.  
  
  
  Referencias:  
  https://www.youtube.com/watch?v=jAaJZLqryTI&t=836s - Idea para hacer el CPU
