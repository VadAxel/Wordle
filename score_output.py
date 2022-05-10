def score_output(game, score, values):
    guess = values['input_box']
    answer = game.Guess(guess)
    guess_split = guess.split()
    score = score + sum(answer)
    return answer,guess_split