import json
import random
madlibs = []

# read json file
def read_json(filename):
    with open(filename) as data_file:
        data = json.load(data_file)
    return data

# return colored string
def color_string(string, color):
    if color == "red":
        return "\033[31m" + string + "\033[0m"
    elif color == "green":
        return "\033[32m" + string + "\033[0m"
    elif color == "yellow":
        return "\033[33m" + string + "\033[0m"
    elif color == "blue":
        return "\033[34m" + string + "\033[0m"
    elif color == "magenta":
        return "\033[35m" + string + "\033[0m"
    elif color == "cyan":
        return "\033[36m" + string + "\033[0m"
    elif color == "white":
        return "\033[37m" + string + "\033[0m"
    else:
        return string

def random_item(list):
    return list[random.randint(0, len(list) - 1)]

def start_game():
    # clear console
    print("\033[2J")
    madlib = random_item(madlibs)
    inputs = []
    output = madlib["text"]
    print(color_string(f'Name: {madlib["name"]}', "magenta"))
    print(color_string(f'Description: {madlib["description"]}', "magenta"))
    for index,current_input in enumerate(madlib["inputs"]):
        answer = input(color_string(f'{index+1}/{len(madlib["inputs"])}. {current_input["question"]} ', "yellow"))
        inputs.append({"id":current_input["id"],"answer":answer})

    for input_ in inputs:
        output = output.replace("{" + input_["id"] + "}", color_string(input_["answer"], "green"))

    print(color_string("-"*60, "blue"))
    print(output)
    print(color_string("-"*60, "blue"))


def main():
    global madlibs
    madlibs = read_json("madlibs.json")
    while True:
        start_game()
        play = input(color_string("Do you want to play again? (y/n) ","red"))
        if play == "y":
            continue
        else:
            print(color_string("Bye!", "cyan"))
            break

main()

