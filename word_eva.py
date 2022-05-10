""""
import colorama
from colorama import Fore


def answer_list_converter(answer):
    for i,c in enumerate(answer):
        if i == 2:
            answer[i] = (Fore.GREEN ")
        elif i == 1:
                answer[i].update(text_color='#C9B359')
        else:
            answer[i].update(text_color='gray')





def guess_split(guess,answer):
    guess_split = list(guess.split(""))
    return guess_split

def answer_list_converter(guess_split,answer):
    new_list = []
    for i in len(range(answer)):
        if answer[i] == "1":
            new_list.append(guess_split[i].update(text_color='#C9B359'))
        elif answer[i] == "2":
            new_list.append(guess_split[i].update(text_color='green'))
        elif answer[i] == "0":
            new_list.append(guess_split[i].update(text_color='gray'))
    return new_list

            
"""
"""
from SwedishWordle import result
import colorama
from colorama import Fore

for i in range(len(result)):
    if result[i] == 2:
        result[i] = Fore.GREEN + str(result[i]) + Fore.RESET
    elif result[i] == 1:
        result[i] = Fore.YELLOW + str(result[i]) + Fore.RESET
    elif result[i] == 0:
        result[i] = Fore.RED + str(result[i]) + Fore.RESET
    """