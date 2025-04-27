from typing import ByteString
import math

class TicTacToe:
  def __init__(self):
    self.board = [' ' for _ in range(9)]
    self.current_winner = None

  def print_board(self):
    for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
      print('| ' + ' | '.join(row) + ' |')
    
  def empty_squares(self):
    return ' ' in self.board
  
  def available_moves(self):
    return [i for i, spot in enumerate(self.board) if spot == ' ']
  
  def make_move(self, square, letter):
    if self.board[square] == ' ':
      self.board[square] = letter
      if self.winner(square, letter):
        self.current_winner = letter
      return True
    return False
  
  def winner(self, square, letter):
    row_index = square // 3;
    row = self.board[row_index*3: (row_index + 1)*3]
    if all([spot == letter for spot in row]):
      return True

    col_index = square % 3;
    col = [self.board[col_index + i*3] for i in range(3)]
    if all([spot == letter for spot in col]):
      return True
    
    if square %2 == 0:
      diagonal1 = [self.board[i] for i in [0,4,8]]
      if all([spot == letter for spot in diagonal1]):
        return True
      
      diagonal2 = [self.board[i] for i in [2,4,6]]
      if all([spot == letter for spot in diagonal2]):
        return True
      
    return False

def minimax(state, player):
  max_player = 'O'
  other = 'X' if player == 'O' else 'O'

  if state.current_winner == other:
    return {'position': None, 'score': 1*(len(state.available_moves())+ 1) if other == 'O' else -1*(len(state.available_moves()) + 1)}
  elif not state.empty_squares():
    return {'position': None, 'score': 0}
  
  if player == max_player:
    best = {'position': None, 'score': -math.inf}
  else:
    best = {'position': None, 'score': math.inf}
  
  for possible_move in state.available_moves():
    state.make_move(possible_move, player)
    sim_score = minimax(state, other)

    state.board[possible_move] = ' '
    state.current_winner = None
    sim_score['position'] = possible_move
    
    if player == max_player:
      if sim_score['score'] > best['score']:
        best = sim_score
    else:
      if sim_score['score'] < best['score']:
                best = sim_score
  
  return best

def play():
  game = TicTacToe()
  human = 'X'
  computer = 'O'
  turn = 'X'

  while game.empty_squares():
    if turn == human: 
      game.print_board()
      square = int(input("Enter your move (0-8): "))
      if square not in game.available_moves():
        print("Invalid move.")
        continue
      game.make_move(square, human)
      if game.current_winner:
        game.print_board()
        print("You win!")
        return
      turn = computer
    
    else:
      move = minimax(game, computer)['position']
      game.make_move(move, computer)
      print(f"Computer made the move {move}")
      if game.current_winner:
        game.print_board()
        print("You lose!")
        return

      turn = human
  
  game.print_board()
  print("Game Tied")

if __name__ == "__main__":
  play()