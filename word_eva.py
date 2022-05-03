def word_paint():
    for i, letter in enumerate(guess):
        if letter == answer2[i]:
            window[(cur_row, i)].update(text_color='green')
            answer2 = answer2.replace(letter, '*')
        elif letter in answer2:
                    window[(cur_row, i)].update(text_color='#C9B359')
                    answer2 = answer2.replace(letter, '*')
        else:
            window[(cur_row, i)].update(text_color='gray')