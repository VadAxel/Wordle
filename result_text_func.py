def result_text_func(result):
    result_text = []
    for i in range(len(result)):
        if result[i] == 0:
            result_text.append("rätt")
        elif result[i] == 1:
            result_text.append("rätt ish")
        else:
            result_text.append("fel")
    return result_text