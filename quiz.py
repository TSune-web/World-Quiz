questions = {
    "What is the highest mountain in the world?": "Mount Everest",
    "What is the largest national park?": "Northeast Greenland National Park",
    "What is the deepest point in the sea?": "Challenger Deep"
}
quiz_length = len(questions)

## Starting the game
def play_quiz():
    print(f"There are {quiz_length} questions in total.\n")
    print("Let's play!\n")
    print("================================\n")

    score = 0
    question_num = 1
    ## Asking each question at a time =================
    for question in questions:
        current_question = f"{question_num}. {question}"
        print(current_question)
        user_input = input("What is your answer?: ")
        answer = user_input.title()

        if answer != questions.get(question):
            print("Close! Think it again!\n")
        else:
            print("That's correct!\n")
            score += 1
        
        question_num += 1


    ## Show the user's total score
    message = f"Your final score is {score}/ 3!\nThank you for playing!\n"

    print("*********************\n")
    print(message)
    print("*********************\n")


    ## Ask the user whether playing the quiz again or not
    play_again = input("Do you want to play the quiz again?(Y/y for yes, or N/n for no): ")

    if play_again != "Y" and play_again != "y":
        quit()
    else:
        play_quiz()


## Starting the game
print("\n")
print("World Record Quiz!\n")
start = input("Do you want to play quiz? (Y/y for yes, or N/n for no): ")


## Check if the user wants to play
if start != "Y" and start != "y":
    quit()
else:
    play_quiz()
