def score_output(game, score, guess):
    answer = game.Guess(guess)
    guess_split = guess.split()
    score = score + sum(answer)
    return answer,guess_split