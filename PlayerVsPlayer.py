############################################################
###PlayerVsPlayer.py Player vs player file               ###   
###Written by Nicholas Maselli                           ###   
###                                                      ###  
###Purpose: Allows a player to play against another      ###
###human player.                                         ###
###                                                      ###
###Version: 1.0                                          ###
###Date: 6-30-17                                         ###
############################################################
from chess import Chess

#########################################################################
##########    Code for playing the game against a human player   ########
#########################################################################	
def PlayerVsPlayer(startState = None):
	chess = Chess()
	chess.print_board()
	
	#Allows play from a specific state
	if (startState != None):
		chess.input_state()
		chess.print_board()
	
	#Play Chess!
	while(True):
		move = input('Input move: ')
		move = chess.convert_move(move)
		game = chess.move(move)
		
		if (game == None
			print(print_move)
			chess.print_board()
			return(chess)
		elif (game == False):
			continue
		else:
			chess.print_board()	
	return(chess)
	
def main():
	PlayerVsPlayer()	
main()