############################################################
###algorithm.py Chess Algorithm Engine                   ###   
###Written by Nicholas Maselli                           ###   
###                                                      ###  
###Purpose: The Algorithm class creates a minimax tree   ###
###that utilizies alpha beta pruning and iterative       ###
###deepening to search through the tree quickly. Piece   ###
###square tables are used to obtain good value functions ### 
###for chess board evaluation.                           ###
###                                                      ###
###Version: 1.0                                          ###
###Date: 6-30-17                                         ###
############################################################
from chess import Chess
import random
import collections
import time
	
###############################
#####MinimaxGameTree Class#####
###############################
class MinimaxGameTree():
	def __init__(self, chess, color, depth):
		self.chess = chess
		self.player = color
		self.depth = depth
		
		#Time
		self.fulltime = 0
		
	#Continuously Iterate search depth to obtain better move ordering
	def iterativeDeepening(self):
		alpha = -40000
		beta = 40000
		pv = []		
		for depth in range(1, self.depth+1):
			data = self.dfsMax(alpha, beta, depth, pv)
			pv = data[1]
		
		best_value = data[0]
		move_list = data[1]
		best_move = move_list[self.depth-1]
		return(best_move)
	
	#Minimax algorithm with alpha-beta pruning, max function
	def dfsMax(self, alpha, beta, depth, pv):
	
		if (depth == 0):
			value = self.evaluate_board(self.player)
			return((value, []))
		
		#Start with the principal value move
		move_list = []
		best_move = None
		if (pv != []):
			move = pv.pop()
			self.next_position(move)			
			data = self.dfsMin(alpha, beta, depth-1, pv)
			self.previous_position()			
			value = data[0]
			
			if (value >= beta):				
				move_list = data[1]
				move_list.append(best_move)
				return((beta, move_list))			
			if (value > alpha):					
				alpha = value
				best_move = move
				move_list = data[1]
		
		for move in self.chess.legal_moves():
			self.next_position(move)			
			data = self.dfsMin(alpha, beta, depth-1, pv)
			self.previous_position()			
			value = data[0]
			
			if (value >= beta):				
				move_list = data[1]
				move_list.append(best_move)
				return((beta, move_list))			
			if (value > alpha):					
				alpha = value
				best_move = move
				move_list = data[1]
					
		#If you are in checkmate		
		if (best_move == None):
			alpha = -20000
		
		move_list.append(best_move)
		return((alpha, move_list))
	
	#Minimax algorithm with alpha-beta pruning, min function
	def dfsMin(self, alpha, beta, depth, pv):
	
		if (depth == 0):
			value = self.evaluate_board(self.player)
			return((value, []))
		
		#Start with the principal value move		
		move_list = []
		best_move = None
		if (pv != []):
			move = pv.pop()
			self.next_position(move)			
			data = self.dfsMax(alpha, beta, depth-1, pv)
			self.previous_position()
			value = data[0]
			
			if (value <= alpha):
				move_list = data[1]
				move_list.append(best_move)
				return((alpha, move_list))			
			if (value < beta):
				beta = value
				best_move = move
				move_list = data[1]
		
		for move in self.chess.legal_moves():
			self.next_position(move)			
			data = self.dfsMax(alpha, beta, depth-1, pv)
			self.previous_position()			
			value = data[0]
			
			if (value <= alpha):
				move_list = data[1]
				move_list.append(best_move)
				return((alpha, move_list))			
			if (value < beta):
				beta = value
				best_move = move
				move_list = data[1]
					
		#If opponent is in checkmate		
		if (best_move == None):
			beta = 20000
		
		move_list.append(best_move)
		return((beta, move_list))
		
	#Evaluate the current board and state from color's perspective
	def evaluate_board(self, color):	
		if (color == 'white'):
			value = self.chess.state.value 
		if (color == 'black'):
			value = -self.chess.state.value
		
		return(value)
		
	#Move to the next position in the chess board
	def next_position(self, move):			
		self.chess.move_piece(move)
	
	#Move to previous position in the chessboard
	def previous_position(self):
		self.chess.undo_move()

#########################
#####Algorithm Class#####
#########################
class Algorithm():
	
	#Initialize values
	def __init__(self, chess, player, depth):
		self.chess = chess
		self.player = player
		self.depth = depth
		self.fulltime = 0
		
	#Choose next move using algorithm
	def best_move(self):	
		self.tree = MinimaxGameTree(self.chess, self.player, self.depth)
		
		#Comments here for timing purposes
		#start_time = time.time()
		move = self.tree.iterativeDeepening()
		#end_time = time.time()		
		#print("Searching the tree: {}".format(end_time - start_time))		
		
		notation = self.chess.coordinate_to_notation(move)
		return(notation)