
class AlphaBeta:
    def __init__(self, game_state):
        self.game_state = game_state

    def is_terminal(self, state):
        win_conditions = [((0, 0), (0, 1), (0, 2)), 
                          ((1, 0), (1, 1), (1, 2)),
                          ((2, 0), (2, 1), (2, 2)),
                          ((0, 0), (1, 0), (2, 0)),  
                          ((0, 1), (1, 1), (2, 1)),
                          ((0, 2), (1, 2), (2, 2)),
                          ((0, 0), (1, 1), (2, 2)),  
                          ((0, 2), (1, 1), (2, 0))]
        for condition in win_conditions:
            if state[condition[0][0]][condition[0][1]] == state[condition[1][0]][condition[1][1]] == state[condition[2][0]][condition[2][1]] and state[condition[0][0]][condition[0][1]] != ' ':
                return True
        return not any(' ' in row for row in state)

    def utility(self, state):
        win_conditions = [((0, 0), (0, 1), (0, 2)),  
                          ((1, 0), (1, 1), (1, 2)),
                          ((2, 0), (2, 1), (2, 2)),
                          ((0, 0), (1, 0), (2, 0)),  
                          ((0, 1), (1, 1), (2, 1)),
                          ((0, 2), (1, 2), (2, 2)),
                          ((0, 0), (1, 1), (2, 2)),  
                          ((0, 2), (1, 1), (2, 0))]
        for condition in win_conditions:
            if state[condition[0][0]][condition[0][1]] == state[condition[1][0]][condition[1][1]] == state[condition[2][0]][condition[2][1]]:
                if state[condition[0][0]][condition[0][1]] == 'X':
                    return 1
                elif state[condition[0][0]][condition[0][1]] == 'O':
                    return -1
        return 0

    def alpha_beta(self, state, depth, alpha, beta, maximizing_player):
        if self.is_terminal(state):
            return self.utility(state)

        if maximizing_player:
            best_score = -float('inf')
            for row in range(3):
                for col in range(3):
                    if state[row][col] == ' ':
                        state[row][col] = 'X'
                        score = self.alpha_beta(state, depth + 1, alpha, beta, False)
                        state[row][col] = ' '
                        best_score = max(score, best_score)
                        alpha = max(alpha, best_score)
                        if beta <= alpha:
                            break
            return best_score
        else:
            best_score = float('inf')
            for row in range(3):
                for col in range(3):
                    if state[row][col] == ' ':
                        state[row][col] = 'O'
                        score = self.alpha_beta(state, depth + 1, alpha, beta, True)
                        state[row][col] = ' '
                        best_score = min(score, best_score)
                        beta = min(beta, best_score)
                        if beta <= alpha:
                            break
            return best_score

    def best_move(self, state):
        best_score = -float('inf')
        move = (-1, -1)
        alpha = -float('inf')
        beta = float('inf')
        for row in range(3):
            for col in range(3):
                if state[row][col] == ' ':
                    state[row][col] = 'X'
                    score = self.alpha_beta(state, 0, alpha, beta, False)
                    state[row][col] = ' '
                    if score > best_score:
                        best_score = score
                        move = (row, col)
        return move
