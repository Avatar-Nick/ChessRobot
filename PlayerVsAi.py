############################################################
###PlayerVsAI.py Player vs computer file                 ###   
###Written by Nicholas Maselli                           ###   
###                                                      ###  
###Purpose: Allows a player to play against a computer AI###
###                                                      ###
###Version: 1.0                                          ###
###Date: 6-30-17                                         ###
############################################################
from chess import Chess
from algorithm import Algorithm
import time
import serial

######################################################
#####Code for playing the game against a computer#####
######################################################
def PlayerVsAI(startState, robot=False):	
	chess = Chess()
	
	#Open Serial Port
	if (robot == True):
		port = open_port()
	
	while(True):
		player = input("Input Human Player's Color ('white' or 'black'): ")
	
		if (player == 'white'):	
			computer = 'black'
			break
		elif (player == 'black'): 
			computer = 'white'
			break
		else:
			print("Error incorrect color/n")
			print();

	#Send player color information to Arduino when it is ready to recieve
	if (robot == True):
		ready = ''
		while(ready != 'R'):
			ready = arduino_ready(port)
		send_input(port, player)
	
	#Allows play from a specific state
	if (startState != None):
		chess.input_state()
	chess.print_board()
		
	#Max Recommended Difficulty: 5 layers. Averages around 15 seconds per move.
	layers = 5
	algorithm = Algorithm(chess, computer, layers)
	
	#Play Chess!
	while(True):
		if (chess.state.turn == player):
			
			if (robot == True):
				serial_input = None
				move = recieve_input(port)
				move = chess.coordinate_to_notation(move)
				move = chess.convert_move(move)
			else:
				move = input('Input move: ')
				move = chess.convert_move(move)
			
		else:
			#Comments for move timing
			#start_time = time.time()		
			move = algorithm.best_move()			
			#end_time = time.time()		
			#print("Move time: {}".format(end_time - start_time))
		
			#If ChessBot is connected, send move via serial port
			if (robot == True):
				serial_input = chess.convert_serial_move(move)
		
		print_move = chess.convert_move(move)
		game = chess.move(move)
		
		if (robot == True and serial_input != None):
			send_input(port, serial_input)		
		
		#Ensure game has not ended before
		if (game == None):
			print(print_move)
			chess.print_board()
			return(chess)
		elif (game == False):
			continue
		else:
			print(print_move)
			chess.print_board()
			
	return(chess)

########################################
###### Robot Serial Port Functions #####
########################################
def open_port():
	#Open a serial port and test by writing a character
	ser = serial.Serial("COM3", 9600)
	return(ser)
	
def send_input(port, move):
	#For python 3, need to convert from unicode string to bytes
	port_input =  bytes(move, encoding="ascii")
	print(port_input)
	port.write(port_input)
	
def arduino_ready(port):
	value = port.read(size=1)
	value = value.decode("ascii")
	return(value)
	
def recieve_input(port):
	#Open a serial port and test by writing a character
	print("Starting Read")
	moves = 0
	moveDetection = False
	while(True):
		value = port.read(size=1)
		value = value.decode("ascii")
		
		if (value == "x"):
			moveLimit = 2
		
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int
			moveSquare = int(value)
			#print("Moving Square: ", end='')
			#print(value)
			
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int			
			landingSquare = int(value)
			#print("Landing Square: ", end='')
			#print(value)
			
			move = convert_move(moveSquare, landingSquare)
			return(move)
			
		if (value == 'y'):
			moveLimit = 2
		
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int
			moveSquare = int(value)
			print("Moving Square: ", end='')
			print(value)
			
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int			
			landingSquare = int(value)
			print("Landing Square: ", end='')
			print(value)
			
			move = convert_move(moveSquare, landingSquare)
			return(move)

		if (value == 'z'):
			moveLimit = 2
		
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int
			moveSquare = int(value)
			#print("Moving Square: ", end='')
			#print(value)
			
			value = port.read(size=1)
			value = int.from_bytes(value, byteorder='big') #Convert byte to int			
			landingSquare = int(value)
			#print("Landing Square: ", end='')
			#print(value)
			
			move = convert_move(moveSquare, landingSquare)
			return(move)	
			
		print(value, end='')

def convert_move(moveSquare, landingSquare):
	yCurrent = int(moveSquare/8)
	xCurrent = int(moveSquare - 8*yCurrent)
	yCurrent = 7-yCurrent
	current = (yCurrent, xCurrent)
	
	yNew = int(landingSquare/8)
	xNew = int(landingSquare - 8*yNew)
	yNew = 7-yNew
	new = (yNew, xNew)
	
	move = (current, new)
	print(move)
	
	return(move)

def main():

	#Set robot to True if playing against a physical chess robot
	PlayerVsAI(startState = None, robot = True)
	
main()

