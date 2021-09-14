import random


# read questions from the file
def question():
    questions = []
    with open("trivia.csv", "r") as f:
        file = f.readlines()
        for item in file:
            if item[0].isdigit():
                item = item.strip("\n")
                new_q = [item]
                questions.append(new_q)
        return random.choice(questions)

# check if question was already asked
def is_asked(quest):
    asked = []
    if question in asked:
        return False
    else:
        asked.append(quest)
        return quest


def ask(quest):
    for item in quest:
        new_item = list(item.split(","))
        print(new_item[4])
        answers = new_item[5:]
        random.shuffle(answers)

        print(f'A: {answers[0]}   B: {answers[1]}   C: {answers[2]}   D: {answers[3]}')
        return new_item[5]



def main():
    score = 0
    turns = 10
    print("Welcome to our TRIVIA game.\nAnswer questions in full, don\'t use a, b, c, d.\nDon\'t be lazy.\nHave fun!!!\n")
    while turns > 0:
        try:
            quest = question()
            if is_asked(quest) != False:
                x = ask(quest)
                answer = input("Answer: ")
                if answer.isalpha():
                    answer = answer.capitalize()
                
                if answer == x:
                    score += 1
                    print("That\'s right.\n")
                else:
                    print("Wrong answer.\n")
                turns -= 1
        finally:
            pass
    
    print(f'Correct answers: {score}')

main()