############################################################
###Test.py Chess Test file                               ###   
###Written by Nicholas Maselli                           ###   
###                                                      ###  
###Purpose: Thoroughly tests the chess engine.           ###
###                                                      ###
###Version: 1.0                                          ###
###Date: 6-30-17                                         ###
############################################################
from chess import Chess

class Test():
	def test_Chess():
		chess = Chess()		
		correctCount = 0
		print('Testing the __init__() function')
		
		#Test 1
		correctOutput = 'Board size: 8'
		givenOutput = 'Board size: {}'.format(chess.size)
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 2
		correctOutput = ('rnbqkbnr\n'
						 'pppppppp\n'
						 '········\n'
						 '········\n'
						 '········\n'
						 '········\n'
						 'PPPPPPPP\n'
						 'RNBQKBNR\n')
		givenOutput = Test.boardString(chess)		
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	
		
		#Test 3
		correctOutput = 'P: ((-1, 0), (-2, 0), (-1, -1), (-1, 1))'
		givenOutput = 'P: {}'.format(chess.directions['P'])
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 4
		correctOutput = 'R: ((-1, 0), (0, 1), (1, 0), (0, -1))'
		givenOutput = 'R: {}'.format(chess.directions['R'])
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 5
		correctOutput = 'N: ((-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1))'
		givenOutput = 'N: {}'.format(chess.directions['N'])
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()			
			
		#Test 6
		correctOutput = 'B: ((-1, 1), (1, 1), (1, -1), (-1, -1))'
		givenOutput = 'B: {}'.format(chess.directions['B'])
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 7 
		correctOutput = 'Q: ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))'
		givenOutput = 'Q: {}'.format(chess.directions['Q'])
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 8
		correctOutput = 'K: ((-1, 0), (0, 1), (1, 0), (0, -1), (-1, 1), (1, 1), (1, -1), (-1, -1))'
		givenOutput = 'K: {}'.format(chess.directions['K'])
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print('{} correct tests out of 8'.format(correctCount))
		print()
		
	#Testing the move_piece() function
	def test_move_piece():
		chess = Chess()
		
		correctCount = 0
		print('Testing the move_piece() function')
		
		#Test 1
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)	
		
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkbnr\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 2
		move = 'b1c3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = ('r·bqkbnr\n'
						 'pppppppp\n'
						 '··n·····\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 'PPPP·PPP\n'
						 'RNBQKBNR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'd1d3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = ('RNB·KBNR\n'
						 'PPP··PPP\n'
						 '···Q····\n'
						 '···PP···\n'
						 '····p···\n'
						 '··n·····\n'
						 'pppp·ppp\n'
						 'r·bqkbnr\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4
		move = 'f1c4'
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		correctOutput = ('r·bqk·nr\n'
						 'pppp·ppp\n'
						 '··n·····\n'
						 '··b·p···\n'
						 '···PP···\n'
						 '···Q····\n'
						 'PPP··PPP\n'
						 'RNB·KBNR\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 5 Castle
		move = 'c1d2'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		move = 'g1h3'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		move = 'b1c3'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		#black castle
		move = 'e1g1'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		#white castle
		move = 'e1c1'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		correctOutput = ('··KR·BNR\n'
						 'PPPB·PPP\n'
						 '··NQ····\n'
						 '···PP···\n'
						 '··b·p···\n'
						 '··n····n\n'
						 'pppp·ppp\n'
						 'r·bq·rk·\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Reset Chess board
		chess = Chess()
		
		#Test 6 Pre Pawn promotion
		
		move = 'b2b4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'b2b7'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		move = 'b1a3'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)		 
	
		correctOutput = ('R·BQKBNR\n'
						 'PpPPPPPP\n'
						 'N·······\n'
						 '·P······\n'
						 '········\n'
						 '········\n'
						 'p·pppppp\n'
						 'rnbqkbnr\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 7: Pawn Promotion
		move = 'b7b8'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove) 
	
		correctOutput = ('rnbqkbnr\n'
						 'p·pppppp\n'
						 '········\n'
						 '········\n'
						 '·P······\n'
						 'N·······\n'
						 'P·PPPPPP\n'
						 'RqBQKBNR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Reset Chessboard
		chess = Chess()
		
		#Test 8: Castle Status
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove) 
	
		correctOutput = '[True, True], [True, True]'
		givenOutput = '{}, {}'.format(str(chess.state.white_castle), str(chess.state.black_castle))
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 9: En passant Status	
		correctOutput = '[(3, 3), (3, 5)]'
		givenOutput = '{}'.format(str(chess.state.en_passant))
		if (correctOutput == givenOutput):
			print('Test 9: Correct')
			correctCount += 1
		else:
			print('Test 9: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 10: Rotate board (now in move) ensuring checking status doesnt mess this up
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkbnr\n')
		
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 10: Correct')
			correctCount += 1
		else:
			print('Test 10: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 11: Move piece on rotated board
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove) 
		correctOutput = ('rnbqkbnr\n'
						 'pppp·ppp\n'
						 '········\n'
						 '····p···\n'
						 '····P···\n'
						 '········\n'
						 'PPPP·PPP\n'
						 'RNBQKBNR\n')
		
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 11: Correct')
			correctCount += 1
		else:
			print('Test 11: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 12: Move king, check castle criteria
		move = 'e1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = '[False, False], [True, True]'		
		givenOutput = '{}, {}'.format(chess.state.white_castle, chess.state.black_castle)
		if (correctOutput == givenOutput):
			print('Test 12: Correct')
			correctCount += 1
		else:
			print('Test 12: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Reset board
		chess = Chess()
		
		#Test 13: Move king on rest board, check castle criteria
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'e4d5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'e1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = '[True, True], [False, False]'		
		givenOutput = '{}, {}'.format(chess.state.white_castle, chess.state.black_castle)
		if (correctOutput == givenOutput):
			print('Test 13: Correct')
			correctCount += 1
		else:
			print('Test 13: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Reset board
		chess = Chess()
		
		#Test 14: Check turn		
		correctOutput = 'white'		
		givenOutput = '{}'.format(chess.state.turn)
		if (correctOutput == givenOutput):
			print('Test 14: Correct')
			correctCount += 1
		else:
			print('Test 14: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 15: rotate, move piece check turn
		move = 'b1c3'		
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		correctOutput = 'black'		
		givenOutput = '{}'.format(chess.state.turn)
		if (correctOutput == givenOutput):
			print('Test 15: Correct')
			correctCount += 1
		else:
			print('Test 15: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Reset board
		chess = Chess()
		
		#Test 16: En passant kept through rotate
		move = 'e2e5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		move = 'c1e3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		correctOutput = '[(3, 2), (3, 4)]'
		givenOutput = '{}'.format(str(chess.state.en_passant))
		if (correctOutput == givenOutput):
			print('Test 16: Correct')
			correctCount += 1
		else:
			print('Test 16: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 17: Make move, rotate, check enpassant		
		move = 'b1c3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)	
		
		correctOutput = '[]'
		givenOutput = '{}'.format(str(chess.state.en_passant))
		if (correctOutput == givenOutput):
			print('Test 17: Correct')
			correctCount += 1
		else:
			print('Test 17: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 18 actually perform the previous en passant
		chess = Chess()
		
		move = 'e2e5'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'e5d6'		
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '········\n'
						 '········\n'
						 '···P····\n'
						 'ppp·pppp\n'
						 'rnbqkbnr\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 18: Correct')
			correctCount += 1
		else:
			print('Test 18: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Reset Board
		chess = Chess()
		
		#Test 19: En passant next to a wall
		move = 'a2a5'
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)		
		
		move = 'b2b4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'a5b6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		correctOutput = ('RNBQKBNR\n'
						 '·PPPPPPP\n'
						 '········\n'
						 '········\n'
						 '········\n'
						 '·P······\n'
						 'p·pppppp\n'
						 'rnbqkbnr\n')
		
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 19: Correct')
			correctCount += 1
		else:
			print('Test 19: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()		
		
		#Test 20: Take opponents rook and check castle 
		chess = Chess()
		
		move = 'h2h3'		
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'd1h8'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = ('[True, False], [True, True]')
		givenOutput = '{}, {}'.format(chess.state.white_castle, chess.state.black_castle)		
		if (correctOutput == givenOutput):
			print('Test 20: Correct')
			correctCount += 1
		else:
			print('Test 20: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			
		#Test 21: Test castle if other rook moves
		move = 'a1a3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'a1h1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = ('[False, False], [False, True]')
		givenOutput = '{}, {}'.format(chess.state.white_castle, chess.state.black_castle)		
		if (correctOutput == givenOutput):
			print('Test 21: Correct')
			correctCount += 1
		else:
			print('Test 21: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
		
		print('{} correct tests out of 21'.format(correctCount))
		print()
		
	#Testing the value in the move_piece() function
	def test_value():
		chess = Chess()
		
		correctCount = 0
		print('Testing the value in the move_piece() function')
		
		#Test 1 starting board values
		correctOutput = (23905, 23905, 0)						 
		givenOutput = (chess.state.white_value, chess.state.black_value, chess.state.value)
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 2 starting board values
		chess = Chess()
		
		move = 'e2e4'		
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = (23945, 23905, 40)						 
		givenOutput = (chess.state.white_value, chess.state.black_value, chess.state.value)
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3 starting board values
		move = 'e2e4'		
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		correctOutput = (23945, 23945, 0)						 
		givenOutput = (chess.state.white_value, chess.state.black_value, chess.state.value)
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print('{} correct tests out of 3'.format(correctCount))
		print()
		
	#Testing gen_moves function
	def test_gen_moves():
		chess = Chess()
		
		correctCount = 0
		print('Testing the gen_moves() function')
		
		#Test 1
		correctOutput = ("((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 2), (5, 2))\n"
						 "((6, 2), (4, 2))\n"
						 "((6, 3), (5, 3))\n"
						 "((6, 3), (4, 3))\n"
						 "((6, 4), (5, 4))\n"
						 "((6, 4), (4, 4))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 1), (5, 2))\n"
						 "((7, 1), (5, 0))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (5, 5))\n")
						 
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 2		
		move = 'b1c3'		
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		
		correctOutput = ("((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 2), (5, 2))\n"
						 "((6, 2), (4, 2))\n"
						 "((6, 3), (5, 3))\n"
						 "((6, 3), (4, 3))\n"
						 "((6, 4), (5, 4))\n"
						 "((6, 4), (4, 4))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 1), (5, 2))\n"
						 "((7, 1), (5, 0))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (5, 5))\n")
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3:
		move = 'e2e4'		
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		
		correctOutput = ("((5, 2), (3, 3))\n"
						 "((5, 2), (4, 4))\n"
						 "((5, 2), (7, 1))\n"
						 "((5, 2), (4, 0))\n"
						 "((5, 2), (3, 1))\n"
						 "((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 3), (5, 3))\n"
						 "((6, 3), (4, 3))\n"
						 "((6, 4), (5, 4))\n"
						 "((6, 4), (4, 4))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 0), (7, 1))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (5, 5))\n")
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4:
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		correctOutput = ("((4, 4), (3, 4))\n"
						 "((4, 4), (3, 3))\n"
						 "((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 2), (5, 2))\n"
						 "((6, 2), (4, 2))\n"
						 "((6, 3), (5, 3))\n"
						 "((6, 3), (4, 3))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 1), (5, 2))\n"
						 "((7, 1), (5, 0))\n"
						 "((7, 3), (6, 4))\n"
						 "((7, 3), (5, 5))\n"
						 "((7, 3), (4, 6))\n"
						 "((7, 3), (3, 7))\n"
						 "((7, 4), (6, 4))\n"
						 "((7, 5), (6, 4))\n"
						 "((7, 5), (5, 3))\n"
						 "((7, 5), (4, 2))\n"
						 "((7, 5), (3, 1))\n"
						 "((7, 5), (2, 0))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (6, 4))\n"
						 "((7, 6), (5, 5))\n")
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 5:
		move = 'e4d5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		
		correctOutput = ("((5, 2), (3, 3))\n"
						 "((5, 2), (4, 4))\n"
						 "((5, 2), (7, 1))\n"
						 "((5, 2), (4, 0))\n"
						 "((5, 2), (3, 1))\n"
						 "((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 4), (5, 4))\n"
						 "((6, 4), (4, 4))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 0), (7, 1))\n"
						 "((7, 2), (6, 3))\n"
						 "((7, 2), (5, 4))\n"
						 "((7, 2), (4, 5))\n"
						 "((7, 2), (3, 6))\n"
						 "((7, 2), (2, 7))\n"
						 "((7, 3), (6, 3))\n"
						 "((7, 3), (5, 3))\n"
						 "((7, 3), (4, 3))\n"
						 "((7, 4), (6, 3))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (5, 5))\n")
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 6: Queen takes pawn d1d4
		move = 'd1d4'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.move_piece(coordinateMove)
		
		
		correctOutput = ("((6, 0), (5, 0))\n"
						 "((6, 0), (4, 0))\n"
						 "((6, 1), (5, 1))\n"
						 "((6, 1), (4, 1))\n"
						 "((6, 2), (5, 2))\n"
						 "((6, 2), (4, 2))\n"
						 "((6, 3), (5, 3))\n"
						 "((6, 3), (4, 3))\n"
						 "((6, 5), (5, 5))\n"
						 "((6, 5), (4, 5))\n"
						 "((6, 6), (5, 6))\n"
						 "((6, 6), (4, 6))\n"
						 "((6, 7), (5, 7))\n"
						 "((6, 7), (4, 7))\n"
						 "((7, 1), (5, 2))\n"
						 "((7, 1), (5, 0))\n"
						 "((7, 3), (6, 4))\n"
						 "((7, 3), (5, 5))\n"
						 "((7, 3), (4, 6))\n"
						 "((7, 3), (3, 7))\n"
						 "((7, 4), (6, 4))\n"
						 "((7, 5), (6, 4))\n"
						 "((7, 5), (5, 3))\n"
						 "((7, 5), (4, 2))\n"
						 "((7, 5), (3, 1))\n"
						 "((7, 5), (2, 0))\n"
						 "((7, 6), (5, 7))\n"
						 "((7, 6), (6, 4))\n"
						 "((7, 6), (5, 5))\n")
		givenOutput = ''
		for moves in chess.gen_moves():
			givenOutput += str(moves)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		print('{} correct tests out of 6'.format(correctCount))
		print()
		
	#Testing generating opponent's attaks
	def test_gen_check_attacks():
		chess = Chess()
		
		correctCount = 0
		print('Testing the gen_check_attacks() function')
		
		#Test 1
		correctOutput = ('(0, 1): [[((0, 0), (0, 1)), (0, 1), 0, None]]\n'
						 '(0, 2): [[((0, 3), (0, 2)), (0, -1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None]]\n'
						 '(0, 4): [[((0, 3), (0, 4)), (0, 1), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None]]\n'
						 '(0, 6): [[((0, 7), (0, 6)), (0, -1), 0, None]]\n'
						 '(1, 0): [[((0, 0), (1, 0)), (1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 2): [[((0, 3), (1, 2)), (1, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None], [((0, 3), (1, 3)), (1, 0), 0, None], [((0, 4), (1, 3)), (1, -1), 0, None]]\n'
						 '(1, 4): [[((0, 3), (1, 4)), (1, 1), 0, None], [((0, 4), (1, 4)), (1, 0), 0, None], [((0, 5), (1, 4)), (1, -1), 0, None], [((0, 6), (1, 4)), (1, -2), 0, None]]\n'
						 '(1, 5): [[((0, 4), (1, 5)), (1, 1), 0, None]]\n'
						 '(1, 6): [[((0, 5), (1, 6)), (1, 1), 0, None]]\n'
						 '(1, 7): [[((0, 7), (1, 7)), (1, 0), 0, None]]\n'
						 '(2, 0): [[((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 0), (2, 1)), (1, 1), 0, None], [((1, 2), (2, 1)), (1, -1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None], [((1, 3), (2, 2)), (1, -1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None], [((1, 4), (2, 3)), (1, -1), 0, None]]\n'
						 '(2, 4): [[((1, 3), (2, 4)), (1, 1), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None]]\n'
						 '(2, 5): [[((0, 6), (2, 5)), (2, -1), 0, None], [((1, 4), (2, 5)), (1, 1), 0, None], [((1, 6), (2, 5)), (1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None]]\n'
						 '(2, 7): [[((0, 6), (2, 7)), (2, 1), 0, None], [((1, 6), (2, 7)), (1, 1), 0, None]]\n')
		
		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
		
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 2
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2a4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'h2h3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		correctOutput = ('(0, 1): [[((0, 0), (0, 1)), (0, 1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None], [((1, 4), (0, 3)), (-1, -1), 0, None]]\n'
						 '(0, 4): [[((1, 4), (0, 4)), (-1, 0), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None], [((1, 4), (0, 5)), (-1, 1), 0, None]]\n'
						 '(0, 6): [[((0, 7), (0, 6)), (0, -1), 0, None]]\n'
						 '(1, 0): [[((0, 0), (1, 0)), (1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 2): [[((1, 4), (1, 2)), (0, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None], [((0, 4), (1, 3)), (1, -1), 0, None], [((1, 4), (1, 3)), (0, -1), 0, None]]\n'
						 '(1, 4): [[((0, 4), (1, 4)), (1, 0), 0, None], [((0, 5), (1, 4)), (1, -1), 0, None], [((0, 6), (1, 4)), (1, -2), 0, None]]\n'
						 '(1, 5): [[((0, 4), (1, 5)), (1, 1), 0, None], [((1, 4), (1, 5)), (0, 1), 0, None]]\n'
						 '(1, 6): [[((0, 5), (1, 6)), (1, 1), 0, None]]\n'
						 '(1, 7): [[((0, 7), (1, 7)), (1, 0), 0, None]]\n'
						 '(2, 0): [[((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 0), (2, 1)), (1, 1), 0, None], [((1, 2), (2, 1)), (1, -1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None], [((1, 4), (2, 3)), (1, -1), 0, None]]\n'
						 '(2, 4): [[((0, 2), (2, 4)), (1, 1), 0, None], [((1, 4), (2, 4)), (1, 0), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None]]\n'
						 '(2, 5): [[((0, 6), (2, 5)), (2, -1), 0, None], [((1, 4), (2, 5)), (1, 1), 0, None], [((1, 6), (2, 5)), (1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None]]\n'
						 '(2, 7): [[((0, 6), (2, 7)), (2, 1), 0, None], [((1, 6), (2, 7)), (1, 1), 0, None]]\n'
						 '(3, 2): [[((1, 4), (3, 2)), (1, -1), 0, None]]\n'
						 '(3, 4): [[((1, 4), (3, 4)), (1, 0), 0, None]]\n'
						 '(3, 5): [[((0, 2), (3, 5)), (1, 1), 0, None]]\n'
						 '(3, 6): [[((1, 4), (3, 6)), (1, 1), 0, None]]\n'
						 '(4, 1): [[((1, 4), (4, 1)), (1, -1), 0, None]]\n'
						 '(4, 2): [[((3, 3), (4, 2)), (1, -1), 0, None]]\n'
						 '(4, 3): [[((3, 4), (4, 3)), (1, -1), 0, None]]\n'
						 '(4, 4): [[((3, 3), (4, 4)), (1, 1), 0, None]]\n'
						 '(4, 5): [[((3, 4), (4, 5)), (1, 1), 0, None]]\n'
						 '(4, 6): [[((0, 2), (4, 6)), (1, 1), 0, None]]\n'
						 '(4, 7): [[((1, 4), (4, 7)), (1, 1), 0, None]]\n'
						 '(5, 0): [[((1, 4), (5, 0)), (1, -1), 0, None]]\n'
						 '(5, 7): [[((0, 2), (5, 7)), (1, 1), 1, (5, 7)]]\n')

		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
			
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 3
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e4d5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		correctOutput = ('(0, 1): [[((0, 0), (0, 1)), (0, 1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None], [((1, 4), (0, 3)), (-1, -1), 0, None]]\n'
						 '(0, 4): [[((1, 4), (0, 4)), (-1, 0), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None], [((1, 4), (0, 5)), (-1, 1), 0, None]]\n'
						 '(0, 6): [[((0, 7), (0, 6)), (0, -1), 0, None]]\n'
						 '(1, 0): [[((0, 0), (1, 0)), (1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 2): [[((1, 4), (1, 2)), (0, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None], [((0, 4), (1, 3)), (1, -1), 0, None], [((1, 4), (1, 3)), (0, -1), 0, None]]\n'
						 '(1, 4): [[((0, 4), (1, 4)), (1, 0), 0, None], [((0, 5), (1, 4)), (1, -1), 0, None], [((0, 6), (1, 4)), (1, -2), 0, None]]\n'
						 '(1, 5): [[((0, 4), (1, 5)), (1, 1), 0, None], [((1, 4), (1, 5)), (0, 1), 0, None]]\n'
						 '(1, 6): [[((0, 5), (1, 6)), (1, 1), 0, None]]\n'
						 '(1, 7): [[((0, 7), (1, 7)), (1, 0), 0, None]]\n'
						 '(2, 0): [[((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 0), (2, 1)), (1, 1), 0, None], [((1, 2), (2, 1)), (1, -1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None], [((1, 4), (2, 3)), (1, -1), 0, None]]\n'
						 '(2, 4): [[((0, 2), (2, 4)), (1, 1), 0, None], [((1, 4), (2, 4)), (1, 0), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None]]\n'
						 '(2, 5): [[((0, 6), (2, 5)), (2, -1), 0, None], [((1, 4), (2, 5)), (1, 1), 0, None], [((1, 6), (2, 5)), (1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None]]\n'
						 '(2, 7): [[((0, 6), (2, 7)), (2, 1), 0, None], [((1, 6), (2, 7)), (1, 1), 0, None]]\n'
						 '(3, 2): [[((1, 4), (3, 2)), (1, -1), 0, None]]\n'
						 '(3, 4): [[((1, 4), (3, 4)), (1, 0), 0, None]]\n'
						 '(3, 5): [[((0, 2), (3, 5)), (1, 1), 0, None]]\n'
						 '(3, 6): [[((1, 4), (3, 6)), (1, 1), 0, None]]\n'
						 '(4, 1): [[((1, 4), (4, 1)), (1, -1), 0, None]]\n'
						 '(4, 2): [[((3, 3), (4, 2)), (1, -1), 0, None]]\n'
						 '(4, 4): [[((1, 4), (4, 4)), (1, 0), 1, (4, 4)], [((3, 3), (4, 4)), (1, 1), 0, None]]\n'
						 '(4, 6): [[((0, 2), (4, 6)), (1, 1), 0, None]]\n'
						 '(4, 7): [[((1, 4), (4, 7)), (1, 1), 0, None]]\n'
						 '(5, 0): [[((1, 4), (5, 0)), (1, -1), 0, None]]\n'
						 '(5, 2): [[((4, 3), (5, 2)), (1, -1), 0, None]]\n'
						 '(5, 4): [[((1, 4), (5, 4)), (1, 0), 1, (4, 4)], [((4, 3), (5, 4)), (1, 1), 0, None]]\n'
						 '(5, 7): [[((0, 2), (5, 7)), (1, 1), 1, (5, 7)]]\n'
						 '(6, 4): [[((1, 4), (6, 4)), (1, 0), 1, (4, 4)]]\n'
						 '(7, 4): [[((1, 4), (7, 4)), (1, 0), 1, (4, 4)]]\n')

		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
			
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4
		move = 'd1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)

		move = 'a2a4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		correctOutput = ('(0, 1): [[((0, 0), (0, 1)), (0, 1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None], [((1, 4), (0, 3)), (-1, -1), 0, None]]\n'
						 '(0, 4): [[((1, 4), (0, 4)), (-1, 0), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None], [((1, 4), (0, 5)), (-1, 1), 0, None]]\n'
						 '(0, 6): [[((0, 7), (0, 6)), (0, -1), 0, None]]\n'
						 '(1, 0): [[((0, 0), (1, 0)), (1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 2): [[((1, 4), (1, 2)), (0, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None], [((0, 4), (1, 3)), (1, -1), 0, None], [((1, 4), (1, 3)), (0, -1), 0, None]]\n'
						 '(1, 4): [[((0, 4), (1, 4)), (1, 0), 0, None], [((0, 5), (1, 4)), (1, -1), 0, None], [((0, 6), (1, 4)), (1, -2), 0, None]]\n'
						 '(1, 5): [[((0, 4), (1, 5)), (1, 1), 0, None], [((1, 4), (1, 5)), (0, 1), 0, None]]\n'
						 '(1, 6): [[((0, 5), (1, 6)), (1, 1), 0, None]]\n'
						 '(1, 7): [[((0, 7), (1, 7)), (1, 0), 0, None]]\n'
						 '(2, 0): [[((0, 0), (2, 0)), (1, 0), 0, None], [((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 2), (2, 1)), (1, -1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None], [((1, 4), (2, 3)), (1, -1), 0, None]]\n'
						 '(2, 4): [[((0, 2), (2, 4)), (1, 1), 0, None], [((1, 4), (2, 4)), (1, 0), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None]]\n'
						 '(2, 5): [[((0, 6), (2, 5)), (2, -1), 0, None], [((1, 4), (2, 5)), (1, 1), 0, None], [((1, 6), (2, 5)), (1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None]]\n'
						 '(2, 7): [[((0, 6), (2, 7)), (2, 1), 0, None], [((1, 6), (2, 7)), (1, 1), 0, None]]\n'
						 '(3, 0): [[((0, 0), (3, 0)), (1, 0), 0, None]]\n'
						 '(3, 2): [[((1, 4), (3, 2)), (1, -1), 0, None]]\n'
						 '(3, 4): [[((1, 4), (3, 4)), (1, 0), 0, None]]\n'
						 '(3, 5): [[((0, 2), (3, 5)), (1, 1), 0, None]]\n'
						 '(3, 6): [[((1, 4), (3, 6)), (1, 1), 0, None]]\n'
						 '(4, 1): [[((1, 4), (4, 1)), (1, -1), 0, None], [((3, 0), (4, 1)), (1, 1), 0, None]]\n'
						 '(4, 2): [[((3, 3), (4, 2)), (1, -1), 0, None]]\n'
						 '(4, 4): [[((1, 4), (4, 4)), (1, 0), 1, (4, 4)], [((3, 3), (4, 4)), (1, 1), 0, None]]\n'
						 '(4, 6): [[((0, 2), (4, 6)), (1, 1), 0, None]]\n'
						 '(4, 7): [[((1, 4), (4, 7)), (1, 1), 0, None]]\n'
						 '(5, 0): [[((1, 4), (5, 0)), (1, -1), 0, None]]\n'
						 '(5, 2): [[((4, 3), (5, 2)), (1, -1), 0, None]]\n'
						 '(5, 4): [[((1, 4), (5, 4)), (1, 0), 1, (4, 4)], [((4, 3), (5, 4)), (1, 1), 0, None]]\n'
						 '(5, 7): [[((0, 2), (5, 7)), (1, 1), 1, (5, 7)]]\n'
						 '(6, 4): [[((1, 4), (6, 4)), (1, 0), 2, None]]\n'
						 '(7, 4): [[((1, 4), (7, 4)), (1, 0), 2, None]]\n')

		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
			
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 5
		move = 'e4d5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		

		move = 'e2e7'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a1a2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'g1h3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2a3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e1g1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a3b3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1e1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f2f3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e2h5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		correctOutput = ('(0, 1): [[((0, 0), (0, 1)), (0, 1), 0, None]]\n'
						 '(0, 2): [[((0, 4), (0, 2)), (0, -1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None], [((4, 7), (0, 3)), (-1, -1), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None], [((0, 6), (0, 5)), (0, -1), 0, None]]\n'
						 '(0, 6): [[((0, 4), (0, 6)), (0, 1), 0, None], [((2, 7), (0, 6)), (-2, -1), 0, None]]\n'
						 '(0, 7): [[((0, 6), (0, 7)), (0, 1), 0, None]]\n'
						 '(1, 0): [[((0, 0), (1, 0)), (1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None]]\n'
						 '(1, 4): [[((0, 4), (1, 4)), (1, 0), 0, None], [((4, 7), (1, 4)), (-1, -1), 0, None]]\n'
						 '(1, 5): [[((0, 6), (1, 5)), (1, -1), 0, None], [((2, 7), (1, 5)), (-1, -2), 0, None]]\n'
						 '(1, 6): [[((0, 6), (1, 6)), (1, 0), 0, None]]\n'
						 '(1, 7): [[((0, 6), (1, 7)), (1, 1), 0, None]]\n'
						 '(2, 0): [[((0, 0), (2, 0)), (1, 0), 0, None], [((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 2), (2, 1)), (1, -1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None]]\n'
						 '(2, 4): [[((0, 2), (2, 4)), (1, 1), 0, None], [((0, 4), (2, 4)), (1, 0), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None]]\n'
						 '(2, 5): [[((1, 6), (2, 5)), (1, -1), 0, None], [((4, 7), (2, 5)), (-1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None]]\n'
						 '(2, 7): [[((1, 6), (2, 7)), (1, 1), 0, None]]\n'
						 '(3, 0): [[((0, 0), (3, 0)), (1, 0), 0, None]]\n'
						 '(3, 4): [[((0, 4), (3, 4)), (1, 0), 0, None]]\n'
						 '(3, 5): [[((0, 2), (3, 5)), (1, 1), 0, None], [((2, 7), (3, 5)), (1, -2), 0, None]]\n'
						 '(3, 6): [[((4, 7), (3, 6)), (-1, -1), 0, None]]\n'
						 '(4, 1): [[((3, 0), (4, 1)), (1, 1), 0, None]]\n'
						 '(4, 4): [[((0, 4), (4, 4)), (1, 0), 0, None]]\n'
						 '(4, 6): [[((0, 2), (4, 6)), (1, 1), 0, None], [((2, 7), (4, 6)), (2, -1), 0, None]]\n'
						 '(5, 2): [[((4, 3), (5, 2)), (1, -1), 0, None]]\n'
						 '(5, 4): [[((0, 4), (5, 4)), (1, 0), 0, None], [((4, 3), (5, 4)), (1, 1), 0, None]]\n'
						 '(5, 6): [[((4, 7), (5, 6)), (1, -1), 0, None]]\n'
						 '(5, 7): [[((0, 2), (5, 7)), (1, 1), 1, (5, 7)]]\n'
						 '(6, 4): [[((0, 4), (6, 4)), (1, 0), 0, None]]\n'
						 '(6, 5): [[((4, 7), (6, 5)), (1, -1), 0, None]]\n'
						 '(7, 4): [[((0, 4), (7, 4)), (1, 0), 0, None], [((4, 7), (7, 4)), (1, -1), 0, None]]\n')

		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
			
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()			
			
		#Test 6
		move = 'c1e3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		

		move = 'h5e2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e2e1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		

		move = 'a1a3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e3c1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		

		move = 'e2h5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		correctOutput = ('(0, 0): [[((2, 0), (0, 0)), (-1, 0), 0, None]]\n'
						 '(0, 2): [[((0, 4), (0, 2)), (0, -1), 0, None]]\n'
						 '(0, 3): [[((0, 4), (0, 3)), (0, -1), 0, None], [((4, 7), (0, 3)), (-1, -1), 0, None]]\n'
						 '(0, 5): [[((0, 4), (0, 5)), (0, 1), 0, None], [((0, 6), (0, 5)), (0, -1), 0, None]]\n'
						 '(0, 6): [[((0, 4), (0, 6)), (0, 1), 0, None], [((2, 7), (0, 6)), (-2, -1), 0, None]]\n'
						 '(0, 7): [[((0, 6), (0, 7)), (0, 1), 0, None]]\n'
						 '(1, 0): [[((2, 0), (1, 0)), (-1, 0), 0, None]]\n'
						 '(1, 1): [[((0, 2), (1, 1)), (1, -1), 0, None]]\n'
						 '(1, 3): [[((0, 1), (1, 3)), (1, 2), 0, None], [((0, 2), (1, 3)), (1, 1), 0, None]]\n'
						 '(1, 4): [[((0, 4), (1, 4)), (1, 0), 0, None], [((4, 7), (1, 4)), (-1, -1), 0, None]]\n'
						 '(1, 5): [[((0, 6), (1, 5)), (1, -1), 0, None], [((2, 7), (1, 5)), (-1, -2), 0, None]]\n'
						 '(1, 6): [[((0, 6), (1, 6)), (1, 0), 0, None]]\n'
						 '(1, 7): [[((0, 6), (1, 7)), (1, 1), 0, None]]\n'
						 '(2, 0): [[((0, 1), (2, 0)), (2, -1), 0, None], [((1, 1), (2, 0)), (1, -1), 0, None]]\n'
						 '(2, 1): [[((1, 2), (2, 1)), (1, -1), 0, None], [((2, 0), (2, 1)), (0, 1), 0, None]]\n'
						 '(2, 2): [[((0, 1), (2, 2)), (2, 1), 0, None], [((1, 1), (2, 2)), (1, 1), 0, None], [((2, 0), (2, 2)), (0, 1), 0, None]]\n'
						 '(2, 3): [[((1, 2), (2, 3)), (1, 1), 0, None], [((2, 0), (2, 3)), (0, 1), 0, None]]\n'
						 '(2, 4): [[((0, 2), (2, 4)), (1, 1), 0, None], [((0, 4), (2, 4)), (1, 0), 0, None], [((1, 5), (2, 4)), (1, -1), 0, None], [((2, 0), (2, 4)), (0, 1), 0, None]]\n'
						 '(2, 5): [[((1, 6), (2, 5)), (1, -1), 0, None], [((2, 0), (2, 5)), (0, 1), 0, None], [((4, 7), (2, 5)), (-1, -1), 0, None]]\n'
						 '(2, 6): [[((1, 5), (2, 6)), (1, 1), 0, None], [((1, 7), (2, 6)), (1, -1), 0, None], [((2, 0), (2, 6)), (0, 1), 0, None]]\n'
						 '(2, 7): [[((1, 6), (2, 7)), (1, 1), 0, None], [((2, 0), (2, 7)), (0, 1), 0, None]]\n'
						 '(3, 0): [[((2, 0), (3, 0)), (1, 0), 0, None]]\n'
						 '(3, 4): [[((0, 4), (3, 4)), (1, 0), 0, None]]\n'
						 '(3, 5): [[((0, 2), (3, 5)), (1, 1), 0, None], [((2, 7), (3, 5)), (1, -2), 0, None]]\n'
						 '(3, 6): [[((4, 7), (3, 6)), (-1, -1), 0, None]]\n'
						 '(4, 1): [[((3, 0), (4, 1)), (1, 1), 0, None]]\n'
						 '(4, 4): [[((0, 4), (4, 4)), (1, 0), 0, None]]\n'
						 '(4, 6): [[((0, 2), (4, 6)), (1, 1), 0, None], [((2, 7), (4, 6)), (2, -1), 0, None]]\n'
						 '(5, 2): [[((4, 3), (5, 2)), (1, -1), 0, None]]\n'
						 '(5, 4): [[((0, 4), (5, 4)), (1, 0), 0, None], [((4, 3), (5, 4)), (1, 1), 0, None]]\n'
						 '(5, 6): [[((4, 7), (5, 6)), (1, -1), 0, None]]\n'
						 '(5, 7): [[((0, 2), (5, 7)), (1, 1), 1, (5, 7)]]\n'
						 '(6, 4): [[((0, 4), (6, 4)), (1, 0), 0, None]]\n'
						 '(6, 5): [[((4, 7), (6, 5)), (1, -1), 0, None]]\n'
						 '(7, 4): [[((0, 4), (7, 4)), (1, 0), 0, None], [((4, 7), (7, 4)), (1, -1), 0, None]]\n')

		input_dict = chess.gen_check_attacks()
		givenOutput = ''
		for key in sorted(input_dict):
			givenOutput += '{}: '.format(key)
			givenOutput += str(input_dict[key])
			givenOutput += '\n'
			
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	
			
		print('{} correct tests out of 6'.format(correctCount))
		print()
		
	#Testing king in check
	def test_king_in_check():
		chess = Chess()
		
		correctCount = 0
		print('Testing the king_in_check() function')
		
		#Test 1
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()		
		
		#Test 2
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 3
		move = 'f2f3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c1g5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'
		coordinateMove = chess.notation_to_coordinate(move)		
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4
		move = 'f3f2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'		
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 5
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'g5c1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c2c3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1b5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'g1h3'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 6
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 7
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1d2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 8
		move = 'g1h3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1b4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 9
		move = 'h3g1'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'b5f1'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		move = 'g1h3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'b4a4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		move = 'c3b4'
		chess.state.opponent_attack_dict = chess.gen_check_attacks()		
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 9: Correct')
			correctCount += 1
		else:
			print('Test 9: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 10
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'c3c4'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 10: Correct')
			correctCount += 1
		else:
			print('Test 10: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 11		
		move = 'c3b4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a4b5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'h3g1'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 11: Correct')
			correctCount += 1
		else:
			print('Test 11: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 12
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 12: Correct')
			correctCount += 1
		else:
			print('Test 12: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	
		
		#Test 13		
		move = 'f2f3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c1h4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 13: Correct')
			correctCount += 1
		else:
			print('Test 13: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()

		#Test 14		
		move = 'f3f2'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'b5a4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 14: Correct')
			correctCount += 1
		else:
			print('Test 14: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	
		
		#Test 15		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'b2b4'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 15: Correct')
			correctCount += 1
		else:
			print('Test 15: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()

		#Test 16		
		move = 'f2f3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'h4h5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'h3g1'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 16: Correct')
			correctCount += 1
		else:
			print('Test 16: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 17		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 17: Correct')
			correctCount += 1
		else:
			print('Test 17: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 18	
		move = 'h3g1'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1h4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1e2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 18: Correct')
			correctCount += 1
		else:
			print('Test 18: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 19		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		move = 'e1f2'	
		coordinateMove = chess.notation_to_coordinate(move)
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 19: Correct')
			correctCount += 1
		else:
			print('Test 19: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	

		#Test 20 Check en passant removing 2 pieces in a line with rook attacking king	
		chess = Chess()
		move = 'e1a5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'a1h4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e2e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e5d6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 20: Correct')
			correctCount += 1
		else:
			print('Test 20: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
	
		#Test 21 Check en passant not affecting king in check if pawn just moves up
		move = 'e5e6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
			
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 21: Correct')
			correctCount += 1
		else:
			print('Test 21: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 22 Check en passant removing 2 pieces in a line with rook attacking king, opponent's pawn closer
		chess = Chess()
		move = 'e1a5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'a1h4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd5e6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 22: Correct')
			correctCount += 1
		else:
			print('Test 22: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()

		#Test 23 Check en passant not affecting king in check if pawn just moves up
		move = 'd5d6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
			
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 23: Correct')
			correctCount += 1
		else:
			print('Test 23: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 24 Check en passant removing 2 pieces in a line with rook attacking king, opponent's pawn closer
		chess = Chess()
		move = 'a1a4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e1h5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'a2a3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e2e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e5d6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 24: Correct')
			correctCount += 1
		else:
			print('Test 24: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 25 pin_count = 0, black en passant				
		move = 'e5e6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 25: Correct')
			correctCount += 1
		else:
			print('Test 25: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 26 Check en passant removing 2 pieces in a line with rook attacking king, opponent's pawn closer
		chess = Chess()
		move = 'a1a4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e1h5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'a2a3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e2e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'f2f4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e5f6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 26: Correct')
			correctCount += 1
		else:
			print('Test 26: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 27 Check en passant removing 2 pieces in a line with rook attacking king, opponent's pawn closer
		chess = Chess()		
		move = 'e5e6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = False
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 27: Correct')
			correctCount += 1
		else:
			print('Test 27: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 28 Check en passant double check
		chess = Chess()
		
		move = 'e2e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd1e3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'a2a3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e5d6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 28: Correct')
			correctCount += 1
		else:
			print('Test 28: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 29 Check en passant double check
		chess = Chess()
		
		move = 'e2e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd1e3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e1e4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'e5d6'
		coordinateMove = chess.notation_to_coordinate(move)		
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 29: Correct')
			correctCount += 1
		else:
			print('Test 29: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 30: Using the new input state function, determine if checkmate from a blocking piece moving to block another piece
		chess = Chess()
		
		state_dict = {}		
		state_dict['board'] = [['r', '·', '·', '·', '·', '·', 'k', '·'],
							   ['p', 'p', 'p', '·', '·', 'p', '·', '·'],
							   ['·', '·', '·', '·', '·', '·', '·', 'p'],
							   ['·', '·', '·', '·', '·', 'P', 'p', '·'],
							   ['·', '·', 'q', 'B', 'K', '·', '·', '·'],
							   ['·', '·', 'P', '·', 'n', '·', 'r', 'P'],
							   ['·', '·', '·', '·', '·', 'R', '·', '·'],
							   ['·', '·', '·', '·', '·', '·', 'Q', '·']]
							
		state_dict['board'].reverse()
		state_dict['turn'] = 'black'
		state_dict['current_move'] = None
		state_dict['white_king_loc'] = (3, 4)
		state_dict['black_king_loc'] = (7, 6)
		state_dict['white_castle'] = [False, False]
		state_dict['black_castle'] = [False, False]
		state_dict['en_passant'] = []
		state_dict['en_passant_loc'] = []
		
		#Opponent attack dictionary and legal move list
		state_dict['opponent_attack_dict'] = {}
		state_dict['legal_move_list'] = {}
		
		#Value Hueristic
		state_dict['white_value'] = 0
		state_dict['black_value'] = 0
		state_dict['value'] = 0
		
		chess.input_state(state_dict)
		
		move = 'a1e1'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)		
		
		move = 'd4e5'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 30: Correct')
			correctCount += 1
		else:
			print('Test 30: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 31: En_passant revealing check
		chess = Chess()
		
		state_dict = {}		
		state_dict['board'] = [['r', '·', '·', '·', '·', '·', 'k', '·'],
							   ['p', 'q', 'p', '·', '·', 'p', '·', '·'],
							   ['·', '·', '·', '·', '·', '·', '·', 'p'],
							   ['·', 'P', '·', '·', '·', 'P', 'p', '·'],
							   ['·', 'K', 'P', 'B', '·', '·', '·', '·'],
							   ['·', '·', 'P', '·', '·', '·', 'r', 'P'],
							   ['·', '·', '·', '·', '·', 'R', '·', '·'],
							   ['·', '·', '·', '·', '·', '·', 'Q', '·']]
							
		state_dict['board'].reverse()
		state_dict['turn'] = 'black'
		state_dict['current_move'] = None
		state_dict['white_king_loc'] = (3, 1)
		state_dict['black_king_loc'] = (7, 6)
		state_dict['white_castle'] = [False, False]
		state_dict['black_castle'] = [False, False]
		state_dict['en_passant'] = []
		state_dict['en_passant_loc'] = []
		
		#Opponent attack dictionary and legal move list
		state_dict['opponent_attack_dict'] = {}
		state_dict['legal_move_list'] = {}
		
		#Value Hueristic
		state_dict['white_value'] = 0
		state_dict['black_value'] = 0
		state_dict['value'] = 0
		
		chess.input_state(state_dict)
		
		move = 'c2c4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)		
		
		move = 'b5c6'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.state.opponent_attack_dict = chess.gen_check_attacks()
		
		correctOutput = True
		givenOutput = chess.king_in_check(coordinateMove)			
		if (correctOutput == givenOutput):
			print('Test 31: Correct')
			correctCount += 1
		else:
			print('Test 31: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print('{} correct tests out of 31'.format(correctCount))
		print()		
	
	#Testing the legal_moves() function
	def test_legal_moves():
		chess = Chess()
		
		correctCount = 0
		print('Testing the legal_moves() function')
		
		#Test 1
		legal_moves = chess.legal_moves()
		correctOutput = ('((6, 0), (5, 0))\n'
						 '((6, 0), (4, 0))\n'
						 '((6, 1), (5, 1))\n'
						 '((6, 1), (4, 1))\n'
						 '((6, 2), (5, 2))\n'
						 '((6, 2), (4, 2))\n'
						 '((6, 3), (5, 3))\n'
						 '((6, 3), (4, 3))\n'
						 '((6, 4), (5, 4))\n'
						 '((6, 4), (4, 4))\n'
						 '((6, 5), (5, 5))\n'
						 '((6, 5), (4, 5))\n'
						 '((6, 6), (5, 6))\n'
						 '((6, 6), (4, 6))\n'
						 '((6, 7), (5, 7))\n'
						 '((6, 7), (4, 7))\n'
						 '((7, 1), (5, 2))\n'
						 '((7, 1), (5, 0))\n'
						 '((7, 6), (5, 7))\n'
						 '((7, 6), (5, 5))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
			
		#Test 2
		move = 'e2e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((4, 4), (3, 4))\n'
						 '((4, 4), (3, 3))\n'
						 '((6, 0), (5, 0))\n'
						 '((6, 0), (4, 0))\n'
						 '((6, 1), (5, 1))\n'
						 '((6, 1), (4, 1))\n'
						 '((6, 2), (5, 2))\n'
						 '((6, 2), (4, 2))\n'
						 '((6, 3), (5, 3))\n'
						 '((6, 3), (4, 3))\n'
						 '((6, 5), (5, 5))\n'
						 '((6, 5), (4, 5))\n'
						 '((6, 6), (5, 6))\n'
						 '((6, 6), (4, 6))\n'
						 '((6, 7), (5, 7))\n'
						 '((6, 7), (4, 7))\n'
						 '((7, 1), (5, 2))\n'
						 '((7, 1), (5, 0))\n'
						 '((7, 3), (6, 4))\n'
						 '((7, 3), (5, 5))\n'
						 '((7, 3), (4, 6))\n'
						 '((7, 3), (3, 7))\n'
						 '((7, 4), (6, 4))\n'
						 '((7, 5), (6, 4))\n'
						 '((7, 5), (5, 3))\n'
						 '((7, 5), (4, 2))\n'
						 '((7, 5), (3, 1))\n'
						 '((7, 5), (2, 0))\n'
						 '((7, 6), (5, 7))\n'
						 '((7, 6), (6, 4))\n'
						 '((7, 6), (5, 5))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3
		move = 'e4d5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd4e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((7, 2), (5, 4))\n'
						 '((7, 3), (6, 4))\n'
						 '((7, 4), (6, 3))\n'
						 '((7, 5), (6, 4))\n'
						 '((7, 6), (6, 4))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4
		move = 'e1d2'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e4e7'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((6, 3), (6, 4))\n'
						 '((6, 3), (5, 2))\n'						 
						 '((7, 3), (6, 4))\n'
						 '((7, 5), (6, 4))\n'
						 '((7, 6), (6, 4))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 5
		chess = Chess()
		
		move = 'b1a3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a1e4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c1a4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'h1d4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1a5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c2c3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'g1h3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f2f3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1h4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2a3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((3, 0), (2, 0))\n'
						 '((3, 0), (3, 1))\n'
						 '((3, 0), (3, 2))\n'
						 '((3, 0), (3, 3))\n'
						 '((3, 0), (2, 1))\n'
						 '((3, 0), (1, 2))\n'
						 '((3, 0), (0, 3))\n'
						 '((3, 0), (4, 1))\n'
						 '((3, 0), (5, 2))\n'
						 '((4, 0), (3, 1))\n'
						 '((4, 0), (2, 2))\n'
						 '((4, 0), (5, 1))\n'
						 '((4, 7), (5, 6))\n'
						 '((4, 7), (3, 6))\n'
						 '((4, 7), (2, 5))\n'
						 '((5, 0), (3, 1))\n'
						 '((5, 0), (4, 2))\n'
						 '((5, 0), (7, 1))\n'
						 '((5, 7), (7, 6))\n'
						 '((5, 7), (4, 5))\n'
						 '((5, 7), (3, 6))\n'
						 '((6, 1), (5, 1))\n'
						 '((6, 1), (4, 1))\n'
						 '((6, 2), (5, 2))\n'
						 '((6, 2), (4, 2))\n'
						 '((6, 3), (5, 3))\n'
						 '((6, 3), (4, 3))\n'
						 '((6, 4), (5, 4))\n'
						 '((6, 4), (4, 4))\n'
						 '((6, 5), (5, 5))\n'
						 '((6, 5), (4, 5))\n'
						 '((6, 6), (5, 6))\n'
						 '((6, 6), (4, 6))\n'
						 '((7, 0), (7, 1))\n'
						 '((7, 0), (7, 2))\n'
						 '((7, 0), (7, 3))\n'
						 '((7, 4), (7, 2))\n'
						 '((7, 4), (7, 5))\n'
						 '((7, 4), (7, 3))\n'
						 '((7, 7), (7, 6))\n'
						 '((7, 7), (7, 5))\n'
						 '((7, 4), (7, 6))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()

		#Test 6		
		move = 'e2h5'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'b2b3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((7, 4), (7, 5))\n'
						 '((7, 4), (7, 3))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 7		
		move = 'd2h6'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e4f4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
				
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((2, 7), (1, 6))\n'
						 '((3, 0), (2, 0))\n'
						 '((3, 0), (3, 1))\n'
						 '((3, 0), (3, 2))\n'
						 '((3, 0), (3, 3))\n'
						 '((3, 0), (2, 1))\n'
						 '((3, 0), (4, 1))\n'
						 '((3, 0), (5, 2))\n'
						 '((3, 0), (6, 3))\n'
						 '((4, 0), (3, 1))\n'
						 '((4, 0), (2, 2))\n'
						 '((4, 0), (5, 1))\n'
						 '((4, 7), (5, 6))\n'
						 '((4, 7), (3, 6))\n'
						 '((4, 7), (2, 5))\n'
						 '((5, 0), (3, 1))\n'
						 '((5, 0), (4, 2))\n'
						 '((5, 0), (7, 1))\n'
						 '((5, 7), (7, 6))\n'
						 '((5, 7), (4, 5))\n'
						 '((5, 7), (3, 6))\n'
						 '((6, 1), (5, 1))\n'
						 '((6, 1), (4, 1))\n'
						 '((6, 2), (5, 2))\n'
						 '((6, 2), (4, 2))\n'
						 '((6, 5), (5, 5))\n'
						 '((6, 5), (4, 5))\n'
						 '((6, 6), (5, 6))\n'
						 '((6, 6), (4, 6))\n'
						 '((7, 0), (7, 1))\n'
						 '((7, 0), (7, 2))\n'
						 '((7, 0), (7, 3))\n'
						 '((7, 4), (6, 4))\n'
						 '((7, 4), (7, 5))\n'
						 '((7, 7), (7, 6))\n'
						 '((7, 7), (7, 5))\n'
						 '((7, 4), (7, 6))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 8		
		move = 'f2a7'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd4c4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		

		move = 'g2a8'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'g2g3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c2h8'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((0, 0), (0, 1))\n'
						 '((0, 0), (1, 1))\n'
						 '((0, 0), (2, 2))\n'
						 '((0, 7), (1, 7))\n'
						 '((0, 7), (0, 6))\n'
						 '((0, 7), (1, 6))\n'
						 '((0, 7), (2, 5))\n'
						 '((1, 0), (0, 1))\n'
						 '((3, 0), (2, 0))\n'
						 '((3, 0), (3, 1))\n'
						 '((3, 0), (3, 2))\n'
						 '((3, 0), (2, 1))\n'
						 '((3, 0), (4, 1))\n'
						 '((3, 0), (5, 2))\n'
						 '((3, 0), (6, 3))\n'
						 '((3, 7), (2, 6))\n'
						 '((4, 0), (3, 1))\n'
						 '((4, 0), (2, 2))\n'
						 '((4, 0), (5, 1))\n'
						 '((4, 0), (6, 2))\n'
						 '((4, 0), (7, 3))\n'
						 '((4, 7), (5, 6))\n'
						 '((4, 7), (6, 5))\n'
						 '((4, 7), (3, 6))\n'
						 '((4, 7), (2, 5))\n'
						 '((5, 0), (3, 1))\n'
						 '((5, 0), (4, 2))\n'
						 '((5, 0), (6, 2))\n'
						 '((5, 0), (7, 1))\n'
						 '((5, 7), (7, 6))\n'
						 '((5, 7), (6, 5))\n'
						 '((5, 7), (4, 5))\n'
						 '((5, 7), (3, 6))\n'
						 '((6, 1), (5, 1))\n'
						 '((6, 1), (4, 1))\n'
						 '((7, 0), (7, 1))\n'
						 '((7, 0), (7, 2))\n'
						 '((7, 0), (7, 3))\n'
						 '((7, 4), (6, 4))\n'
						 '((7, 4), (7, 3))\n'
						 '((7, 4), (6, 3))\n'
						 '((7, 7), (7, 6))\n'
						 '((7, 7), (7, 5))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 9		
		move = 'b2b3'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f4g4'
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ('((0, 0), (0, 1))\n'
						 '((0, 0), (1, 1))\n'
						 '((0, 0), (2, 2))\n'
						 '((0, 7), (1, 7))\n'
						 '((0, 7), (0, 6))\n'
						 '((0, 7), (1, 6))\n'
						 '((0, 7), (2, 5))\n'
						 '((1, 0), (0, 1))\n'
						 '((3, 0), (2, 0))\n'
						 '((3, 0), (3, 1))\n'
						 '((3, 0), (3, 2))\n'
						 '((3, 0), (2, 1))\n'
						 '((3, 0), (4, 1))\n'
						 '((3, 0), (5, 2))\n'
						 '((3, 0), (6, 3))\n'
						 '((3, 7), (2, 6))\n'
						 '((4, 0), (3, 1))\n'
						 '((4, 0), (2, 2))\n'
						 '((4, 7), (5, 6))\n'
						 '((4, 7), (6, 5))\n'
						 '((4, 7), (3, 6))\n'
						 '((5, 0), (3, 1))\n'
						 '((5, 0), (4, 2))\n'
						 '((5, 0), (6, 2))\n'
						 '((5, 0), (7, 1))\n'
						 '((5, 1), (4, 1))\n'
						 '((5, 7), (7, 6))\n'
						 '((5, 7), (6, 5))\n'
						 '((5, 7), (4, 5))\n'
						 '((5, 7), (3, 6))\n'
						 '((7, 0), (7, 1))\n'
						 '((7, 0), (7, 2))\n'
						 '((7, 0), (7, 3))\n'
						 '((7, 4), (6, 4))\n'
						 '((7, 4), (7, 5))\n'
						 '((7, 4), (7, 3))\n'
						 '((7, 4), (6, 5))\n'
						 '((7, 4), (6, 3))\n'
						 '((7, 7), (7, 6))\n'
						 '((7, 7), (7, 5))\n')
						 
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'
		if (correctOutput == givenOutput):
			print('Test 9: Correct')
			correctCount += 1
		else:
			print('Test 9: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 10 Checkmate
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2a4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f1c4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'h2h4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1f3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a4a5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f3f7'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		legal_moves = chess.legal_moves()
		correctOutput = ''
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'			
		if (correctOutput == givenOutput):
			print('Test 10: Correct')
			correctCount += 1
		else:
			print('Test 10: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()		
		
		#Test 11 Bug response: Take knight while knight is checking king
		chess = Chess()
		
		move = 'b1c3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)			
		
		move = 'b1c3'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)

		move = 'c3d5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)

		move = 'c3b1'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
		
		move = 'd5f6'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)
				
		legal_moves = chess.legal_moves()
		correctOutput = ('((6, 4), (5, 5))\n'
						 '((6, 6), (5, 5))\n'
						 '((7, 6), (5, 5))\n')
		givenOutput = ''
		for move in legal_moves:
			givenOutput += str(move)
			givenOutput += '\n'			
		if (correctOutput == givenOutput):
			print('Test 11: Correct')
			correctCount += 1
		else:
			print('Test 11: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	

		print('{} correct tests out of 11'.format(correctCount))
		print()
		
	#Testing king in check after a move
	def test_king_ray_check():
		chess = Chess()
		
		correctCount = 0
		print('Testing the king_ray_check() function')		
		
		#Test 1	
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		givenOutput = chess.king_ray_check()
		correctOutput = False
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
	
		#Test 2
		chess = Chess()
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a1e5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'c1a4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 4		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f2f4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd1h5'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 5	
		chess = Chess()
		
		move = 'g1f6'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 6		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f2f4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e4f7'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 7		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2d7'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = True
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 8		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'd2d4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'a2c6'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = False
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 9		
		chess = Chess()
		
		move = 'e2e4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'f2f4'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		move = 'e4g6'	
		coordinateMove = chess.notation_to_coordinate(move)	
		chess.move_piece(coordinateMove)		
		
		
		givenOutput = chess.king_ray_check()
		correctOutput = False
		if (correctOutput == givenOutput):
			print('Test 9: Correct')
			correctCount += 1
		else:
			print('Test 9: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 10		
		chess = Chess()
		
		state_dict = {}		
		state_dict['board'] = [['r', '·', 'b', '·', '·', '·', '·', 'Q'],
							   ['p', 'p', 'p', 'k', 'P', '·', '·', 'p'],
							   ['q', '·', 'n', '·', '·', '·', '·', '·'],
							   ['·', '·', '·', '·', '·', 'r', '·', '·'],
							   ['·', '·', 'P', '·', '·', '·', '·', '·'],
							   ['·', 'P', '·', '·', 'R', '·', '·', '·'],
							   ['·', 'P', '·', 'N', 'K', '·', 'N', '·'],
							   ['·', '·', '·', '·', '·', '·', '·', '·']]
							
		state_dict['board']
		state_dict['turn'] = 'white'
		state_dict['current_move'] = None
		state_dict['white_king_loc'] = (6, 4)
		state_dict['black_king_loc'] = (1, 3)
		state_dict['white_castle'] = [False, False]
		state_dict['black_castle'] = [False, False]
		state_dict['en_passant'] = []
		state_dict['en_passant_loc'] = []
		
		#Opponent attack dictionary and legal move list
		state_dict['opponent_attack_dict'] = {}
		state_dict['legal_move_list'] = {}
		
		#Value Hueristic
		state_dict['white_value'] = 0
		state_dict['black_value'] = 0
		state_dict['value'] = 0
		
		chess.input_state(state_dict)
		
		move = 'e7e8'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2d3'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		move = 'd2e4'	
		coordinateMove = chess.notation_to_coordinate(move)
		chess.move_piece(coordinateMove)
		
		correctOutput = True
		givenOutput = chess.king_ray_check()		
		if (correctOutput == givenOutput):
			print('Test 10: Correct')
			correctCount += 1
		else:
			print('Test 10: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print('{} correct tests out of 10'.format(correctCount))
		print()	
	
	
	#Test the formatting of moves
	def test_format_move():
		chess = Chess()
		
		correctCount = 0
		print('Testing the format_move() function')
		
		#Test 1
		move = 'e2e45'
		print('Test 1 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.format_move(move)
		
		print()
		
		#Test 2
		move = 'k2e4'
		print('Test 2 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.format_move(move)
		
		print()
		
		#Test 3
		move = 'e2z4'
		print('Test 3 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.format_move(move)
		
		print()
		
		#Test 4
		move = 'e9e4'
		print('Test 4 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.format_move(move)
		
		print()
		
		#Test 5
		move = 'e2e9'
		print('Test 5 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.format_move(move)
		
		print()
		
		#Test 6
		move = 'e2e4'
		correctOutput = '((6, 4), (4, 4))'
		givenOutput = str(chess.format_move(move))
		
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print()
		
	#Testing the move function
	def test_move():
		chess = Chess()
		
		correctCount = 0
		print('Testing the move() function')
		
		#Test 1
		move = 'e2e4'
		chess.move(move)
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkbnr\n')
		givenOutput = Test.boardString(chess)		
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print()

		#Test 2
		move = 'e2e45'
		print('Test 2 Correct output:')
		print('Input move in the form such as: e2e4')
		print('Given output:')
		chess.move(move)
		
		print()
		
		#Test 3
		move = 'e2e5'
		print('Test 3 Correct output:')
		print('Not a valid move')
		print('Given output:')
		chess.move(move)

		print()
		
		#Test 4
		move = 'e2e4'
		chess.move(move)
		correctOutput = ('rnbqkbnr\n'
						 'pppp·ppp\n'
						 '········\n'
						 '····p···\n'
						 '····P···\n'
						 '········\n'
						 'PPPP·PPP\n'
						 'RNBQKBNR\n')
		givenOutput = Test.boardString(chess)		
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		print()
			
		#Test 5
		move = 'f1c4'
		chess.move(move)
		
		move = 'b1c3'
		chess.move(move)
		
		move = 'd1f3'
		chess.move(move)
		
		move = 'd2d3'
		chess.move(move)
		
		move = 'f3f7'
		chess.move(move)		
		correctOutput = ('RNB·K·NR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '··B·P···\n'
						 '····p···\n'
						 '··np····\n'
						 'ppp··Qpp\n'
						 'r·bqkbnr\n')
		givenOutput = Test.boardString(chess)		
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		print()		

		#Test 6
		move = 'e1e2'
		print('Test 6 Correct output:')
		print('Not a valid move')
		print('Given output:')
		chess.move(move)

		print()
		
	#Testing the undo function
	def test_undo_move():
		chess = Chess()
		
		correctCount = 0
		print('Testing the undo_move() function')
		
		#Test 1
		move = 'e2e4'	
		chess.move(move)			
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkbnr\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 1: Correct')
			correctCount += 1
		else:
			print('Test 1: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 2
		move = 'e2e4'	
		chess.move(move)
		chess.undo_move()
		correctOutput = ('RNBQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····P···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkbnr\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 2: Correct')
			correctCount += 1
		else:
			print('Test 2: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 3
		move = 'c2c4'	
		chess.move(move)
		correctOutput = ('rnbqkbnr\n'
						 'pp·ppppp\n'
						 '········\n'
						 '··p·····\n'
						 '····P···\n'
						 '········\n'
						 'PPPP·PPP\n'
						 'RNBQKBNR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 3: Correct')
			correctCount += 1
		else:
			print('Test 3: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()			
			
		#Test 4
		previous_state = chess.states[len(chess.states)-2]
		correctOutput = str(previous_state.en_passant)
		chess.undo_move()
		givenOutput = str(chess.state.en_passant)
		if (correctOutput == givenOutput):
			print('Test 4: Correct')
			correctCount += 1
		else:
			print('Test 4: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 5		
		move = 'g1f3'	
		chess.move(move)
		move = 'b1c3'	
		chess.move(move)
		move = 'f3e5'	
		chess.move(move)
		move = 'c3e4'	
		chess.move(move)
		correctOutput = ('R·BQKBNR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '····N···\n'
						 '········\n'
						 '········\n'
						 'pppppppp\n'
						 'rnbqkb·r\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 5: Correct')
			correctCount += 1
		else:
			print('Test 5: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()	
			
		#Test 6		
		chess.undo_move()
		correctOutput = ('rnbqkb·r\n'
						 'pppppppp\n'
						 '········\n'
						 '········\n'
						 '····n···\n'
						 '··N·····\n'
						 'PPPP·PPP\n'
						 'R·BQKBNR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 6: Correct')
			correctCount += 1
		else:
			print('Test 6: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 7		
		chess.undo_move()
		correctOutput = ('R·BQKBNR\n'
						 'PPPP·PPP\n'
						 '··N·····\n'
						 '····P···\n'
						 '········\n'
						 '·····n··\n'
						 'pppppppp\n'
						 'rnbqkb·r\n')
						 
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 7: Correct')
			correctCount += 1
		else:
			print('Test 7: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
				
		#Test 8
		chess = Chess()
		
		move = 'e2e4'	
		chess.move(move)
		move = 'e2e4'	
		chess.move(move)
		move = 'f1c4'	
		chess.move(move)
		move = 'b1c3'	
		chess.move(move)
		move = 'd1f3'	
		chess.move(move)
		move = 'd2d3'	
		chess.move(move)
		move = 'f3f7'	
		chess.move(move)
		
		
		correctOutput = ('RNB·K·NR\n'
						 'PPPP·PPP\n'
						 '········\n'
						 '··B·P···\n'
						 '····p···\n'
						 '··np····\n'
						 'ppp··Qpp\n'
						 'r·bqkbnr\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 8: Correct')
			correctCount += 1
		else:
			print('Test 8: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 9
		chess.undo_move()
		correctOutput = ('r·bqkbnr\n'
						 'ppp··ppp\n'
						 '··np····\n'
						 '····p···\n'
						 '··B·P···\n'
						 '·····Q··\n'
						 'PPPP·PPP\n'
						 'RNB·K·NR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 9: Correct')
			correctCount += 1
		else:
			print('Test 9: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 10
		move = 'h2h4'
		chess.move(move)
		move = 'd1d2'
		chess.move(move)
		correctOutput = ('r·b·kbnr\n'
						 'pppq·ppp\n'
						 '··np····\n'
						 '····p···\n'
						 '··B·P··P\n'
						 '·····Q··\n'
						 'PPPP·PP·\n'
						 'RNB·K·NR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 10: Correct')
			correctCount += 1
		else:
			print('Test 10: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 11
		move = 'f3f7'
		chess.move(move)
		move = 'd2f2'
		chess.move(move)
		correctOutput = ('r·b·kbnr\n'
						 'ppp··qpp\n'
						 '··np····\n'
						 '····p···\n'
						 '··B·P··P\n'
						 '········\n'
						 'PPPP·PP·\n'
						 'RNB·K·NR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 11: Correct')
			correctCount += 1
		else:
			print('Test 11: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
		
		#Test 12
		chess.undo_move()
		correctOutput = ('RNB·K·NR\n'
						 'PPPP·PP·\n'
						 '········\n'
						 '··B·P··P\n'
						 '····p···\n'
						 '··np····\n'
						 'pppq·Qpp\n'
						 'r·b·kbnr\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 12: Correct')
			correctCount += 1
		else:
			print('Test 12: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 13
		chess.undo_move()
		chess.undo_move()
		chess.undo_move()
		correctOutput = ('r·bqkbnr\n'
						 'ppp··ppp\n'
						 '··np····\n'
						 '····p···\n'
						 '··B·P···\n'
						 '·····Q··\n'
						 'PPPP·PPP\n'
						 'RNB·K·NR\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 13: Correct')
			correctCount += 1
		else:
			print('Test 13: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		#Test 14
		move = 'g1h3'
		chess.move(move)
		correctOutput = ('RNB·K··R\n'
						 'PPPP·PPP\n'
						 '·····Q·N\n'
						 '··B·P···\n'
						 '····p···\n'
						 '··np····\n'
						 'ppp··ppp\n'
						 'r·bqkbnr\n')
		givenOutput = Test.boardString(chess)
		if (correctOutput == givenOutput):
			print('Test 14: Correct')
			correctCount += 1
		else:
			print('Test 14: Incorrect')
			print('Correct output:\n{}'.format(correctOutput))
			print('Given output:\n{}'.format(givenOutput))
			print()
			
		print('{} correct tests out of 14'.format(correctCount))
		print()		
	
	#Creates a simple representation of the given chess board
	def boardString(chess):
		correctOutput = ''
		for row in chess.state.board:
			for tile in row:
				correctOutput += tile
			correctOutput += '\n'
			
		return(correctOutput)
		
def main():

	#Testing setup and move calculation	
	test = Test

	test.test_Chess()	
	test.test_move_piece()
	test.test_value()
	test.test_gen_moves()
	test.test_gen_check_attacks()	
	
	#Testing check detection
	test.test_king_in_check()
	test.test_legal_moves()
	test.test_king_ray_check()
	
	#Testing gameplay
	test.test_format_move()
	test.test_move()
	test.test_undo_move()	
	
main()
		