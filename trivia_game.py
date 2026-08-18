import random
questions = {
    "What is the keyword to define a function in Python?": "def",
    "Which data type is used to store True or False values?": "boolean",
    "What is the correct file extension for Python files?": ".py",
    "Which symbol is used to comment in Python?": "#",
    "What function is used to get input from the user?": "input",
    "How do you start a for loop in Python?": "for",
    "What is the output of 2 ** 3 in Python?": "8",
    "What keyword is used to import a module in Python?": "import",
    "What does the len() function return?": "length",
    "What is the result of 10 // 3 in Python?": "3"
}
def  trivia_game():
    score = 0 
    total_questions = 5
    available_questions = list(questions.keys())
    asked_questions = random.sample(available_questions, total_questions)
    for indx , question in enumerate(asked_questions):
        print(f'Question {indx + 1}: {question}')
        user_answer = input("Your answer: ").strip().lower()
        correct_answer = questions[question].lower()
        if user_answer == correct_answer:
            print('correct')
            score += 1
        else:
            print(f'Incorrect. The correct answer is: {questions[question]}')
    print(f'Your final score is: {score / total_questions * 100}%')

trivia_game()
