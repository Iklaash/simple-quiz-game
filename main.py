import questions
import random

user_answer = None
correct_answer = 0
wrong_answer = 0
random.shuffle(questions.question_bank)

for element in questions.question_bank:
    print(element["Question"])
    print(element["Choices"])
    user_answer = input().lower()
    if user_answer == element["Answer"]:
        correct_answer +=1
        print("Correct!")
    else:
        wrong_answer +=1
        print("Incorrect")
print(f"You got {correct_answer} right and {wrong_answer} wrong")
